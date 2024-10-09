export:
	ffmpeg -f concat -safe 0 -y -i fileList.txt -c copy output.mp4

.phony: export