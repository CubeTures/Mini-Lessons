package v1 // added concurrency

import (
	"time"
)

type data struct {
	counter int
}

// 1. what is a thread
// 2. anatomy of a process
// 3. the "go" keyword
// 4. what will program this output?
func Run() {
	data := new(data)

	for range 1000 {
		go worker(data)
	}

	println(data.counter)
}

func worker(data *data) {
	time.Sleep(time.Millisecond * 10)

	for range 1000 {
		data.counter++
	}
}
