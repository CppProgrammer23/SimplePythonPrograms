# -*- coding: utf-8 -*-
"""convertToGIF.ipynb

Automatically generated by Colaboratory.

"""

from moviepy.editor import VideoFileClip

clp=VideoFileClip('yourVideoHere.mp4')
clp.write_gif('myvideo.gif')
