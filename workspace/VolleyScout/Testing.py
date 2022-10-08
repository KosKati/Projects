import os
#import xpath
import xml.etree.ElementTree as ET
from xml.dom import minidom

from imageio.plugins import ffmpeg
from lxml import etree
import datetime
from moviepy.editor import *
import re
# Python code t get difference of two lists
# Not using set()

#clip = VideoFileClip('C:/videos/BSO-STU.mp4')
#clip = clip.cutout(3, 7)
#Angriff Video : 0:1:8 (neu), 0:08:21, 9:48, 22:12, 24:02, 43:22, 47:47, 49:37, 55:12, 1:06:04, 1:40:7, 1:42:57, 1:46:54, 1:53:26, 2:09:42, 2:25:00
#Aufschlag 10:33,12:47, 12:17, 36:02, 1:11:27 Block: 1:37:43 Annahme 1:41:27
#from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.ffmpeg_tools import *
# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")

    # s = 1000
    # m = 60000
    # h = 3600000
s = 4197.345

m, s = divmod(s, 60)
h, m = divmod(m, 60)
result = ("%d:%02d:%02d" % (h, m, s)) if h else ("%d:%02d" % (m, s))

print(result)
