package main

import (
	"concurrency/intro_v0"
	"concurrency/intro_v1"
	"concurrency/intro_v2"
	"concurrency/intro_v3"
)

func main() {
	intro()
}

func intro() {
	version := 0

	switch version {
	case 0:
		intro_v0.Run()
	case 1:
		intro_v1.Run()
	case 2:
		intro_v2.Run()
	case 3:
		intro_v3.Run()
	default:
		println("Invalid version for intro")
	}
}
