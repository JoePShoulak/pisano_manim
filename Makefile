fib:
	./.venv/bin/manim -pql scene.py Fibonacci

pisano:
	./.venv/bin/manim -pql scene.py Pisano

test:
	./.venv/bin/manim -pql scene.py Test

clean:
	rm -rf ./media/

.PHONY: fib pisano test clean
