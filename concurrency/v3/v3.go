package v3 // added mutex

import (
	"sync"
	"time"
)

type data struct {
	counter int
	mu      sync.Mutex
}

// 1. what is a mutex
// 2. what will this program output?
// 3. difference in the two mutex placements
// 4. do you want to see more mini-lessons on various topics?
func Run() {
	data := new(data)

	var wg sync.WaitGroup
	for range 1000 {
		wg.Add(1)
		go func() {
			worker(data)
			wg.Done()
		}()
	}
	wg.Wait()

	println(data.counter)
}

func worker(data *data) {
	time.Sleep(time.Millisecond * 10)

	data.mu.Lock()
	for range 1000 {
		// data.mu.Lock()
		data.counter++
		// data.mu.Unlock()
	}
	data.mu.Unlock()
}
