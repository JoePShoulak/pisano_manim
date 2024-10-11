export:
	ffmpeg -f concat -safe 0 -y -i sceneList.txt -c copy output.mp4

.phony: export