all:
	manim -aql scene.py

clean:
	rm -rf ./media/

export:
	ffmpeg -f concat -safe 0 -y -i sceneList.txt -c copy output.mp4

.phony: all clean export
