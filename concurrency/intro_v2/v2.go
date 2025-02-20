package intro_v2 // added wait group

import (
	"sync"
	"time"
)

type data struct {
	counter int
}

// 1. what is a wait group
// 2. what is an anonymous function
// 3. what will this program output?
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
	time.Sleep(time.Millisecond * 100)

	for range 1000 {
		data.counter++
	}
}
