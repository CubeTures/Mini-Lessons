package main

import (
	v0 "concurrency/v0"
	v1 "concurrency/v1"
	v2 "concurrency/v2"
	v3 "concurrency/v3"
)

func main() {
	version := 3

	switch version {
	case 0:
		v0.Run()
	case 1:
		v1.Run()
	case 2:
		v2.Run()
	case 3:
		v3.Run()
	default:
		println("Invalid version", version)
	}
}
