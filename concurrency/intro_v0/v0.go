package intro_v0 // no concurrency

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
// theoretically takes a long time
// for the purposes of now, just a simple loop
func worker(data *data) {
	for range 1000 {
		data.counter++
	}
}
