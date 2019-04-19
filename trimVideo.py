from moviepy.editor import *
import sys

# video work
video = VideoFileClip('vid/sample.mp4')
clip = video.subclip(1, 5)
clip.write_videofile('out/trimmed.mp4', fps=20)
