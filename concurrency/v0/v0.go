package v0 // no concurrency

import (
	"time"
)

type data struct {
	counter int
}

// 0. intro to golang
// 1. what is concurrency?
// 2. why use concurrency?
func Run() {
	data := new(data)

	for range 1000 {
		worker(data)
	}

	print(data.counter)
}

// a function that does some work
// takes a long time to do that work
func worker(data *data) {
	// sleep to simulate some other miscellaneous work
	time.Sleep(time.Millisecond * 10)

	for range 1000 {
		data.counter++
	}
}
