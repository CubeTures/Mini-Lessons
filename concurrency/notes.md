# What is Concurrency?

Concurrency, otherwise known as multithreading or parallel processing, is the act of running multiple tasks simultaneously, typically by creating multiple processes or threads. There's a long history behind it, but essentially threads are lightweight tasks that can be spun up and handled by your kernel.

Concurrency is useful when you want to complete a large task that can be split up into multiple parts: calculating some metric on a large dataset or sorting using merge sort. It's also useful when you have blocking calls to an API, meaning your code has to wait for a response before continuing. Concurrency is nice because it can make otherwise slow to complete tasks quick by dividing up the workload.

# Concurrency Pitfalls

Ok, so you get what concurrency is and why it is useful. How do you get started? Well, there's a bit you need to understand before you can jump right in. Consider [the code in version 1](v1/v1.go). What does it output? You'd be inclined to say 1,000,000, since 1,000 threads \* 1,000 counts = 1,000,000, but that's actually incorrect. Threads run independent of each other, meaning the print statement will occur before any of the threads have a chance to even run; the output will be 0.

Obviously, this behavior is undesired. So, how do we counter it?

# Wait Group

Go's `sync` package has a structure called the `WaitGroup`. It is used to count the number of operations occurring and then wait for them all to finish before going on. In other programming languages, it may look something like this:

```c++
// c++
int numThreads = 1000;
std::thread *threads = new std::thread[numThreads];

// create all the threads
for (int i = 0; i < numThreads; i++) {
    threads[i] = std::thread([]{ worker(&data); });
}

// wait for threads to complete
for (int i = 0; i < numThreads; i++) {
    threads[i].join();
}
```

```java
// java
int numThreads = 1000;
Thread[] threads = new Thread[numThreads];

// create all the threads
for (int i = 0; i < numThreads; i++) {
    threads[i] = new Thread(() -> {
        worker(data);
    });
    threads[i].start();
}

// wait for all threads to complete
for (int i = 0; i < numThreads; i++) {
    threads[i].join();
    // ignoring possible errors for brevity
}
```

In these languages, threads themselves hold the ability to the "joined" upon, essentially waiting for the thread to stop running of its own accord before continuing. In Go, since threads are started using a keyword and aren't stored in a variable, the `WaitGroup` is how it handles synchronization.

Knowing this, read [version 2 of the code](v2/v2.go). It utilizes a `WaitGroup` to first wait for all the threads to finish running before printing the output. So now, surely, the output must be 1,000,000, right? Unfortunately, no.

# Race Conditions

The next pitfall of concurrency is the race condition. If you ran the code, did you notice that the output was always inconsistent? It swung wildly between 2 (the absolute lower bound) and 1,000,000 (the upper bound). Threads are non-deterministic and will always run in a different order, causing this behavior. But why is the number not 1,000,000 in the first place?

This is the race condition. To be as brief as possible, the operations we see on the screen aren't actually what occurs on your computer; `data.counter++` isn't what happens, instead it'll run some assembly along the lines of

```asm
movq counter %rax
addq 1 %rax
movq %rax counter
```

Now it's a bit more obvious why this discrepancy is occurring. What happens if a thread is running and moves the variable int `%rax`, then stops executing and another thread starts running? When the initial thread is restarted again, it'll still have the old value of the counter in `%rax`, add to it, then overwrite whatever value is stored in counter, erasing any progress made by other threads. Again, this sucks. So, what do we do now?

# The Mutex

The mutex is like the bathroom key owned by an urban coffee shop. Imagine this: if you get the key from the store owner, enter the bathroom, then lock the door, nobody else will be able to enter. Instead, the will need to wait for you to finish, then return the key to store owner before going through the same process you did. The mutex is the exactly the same.

Read [version 3 of the code](v3/v3.go). Notice how it uses a mutex around where it is incrementing count? `data.mu.Lock()` will offer the mutex's key to the first thread that wants it, then prevent anyone else from passing into the section. In this time, the thread that owns the key can safely mutate the variable and then release the key with `data.mu.Unlock()`. Now, after all of this, our program will output 1,000,000 as desired.

# Conclusion

In conclusion, while multithreading offers many benefits, it also creates a lot of problems that can be hard to debug if you're not careful. As they say: "With great power comes great responsibility." Knowing when to use multithreading and when not to is also important; some tasks would work better on a single thread or the overhead of creating and maintaining multiple threads does not offset the time saved from multithreading. That being said, practically everything in your computer is optimized to utilize the CPU as efficiently as possible with multithreading, so learning how to do so effectively will be a big boon.
