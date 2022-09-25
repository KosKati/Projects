import os
#import xpath
import xml.etree.ElementTree as ET
from xml.dom import minidom
import ffmpeg

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
test = 'test'
print(test[-1])


"""
stamps = [19.456, 34.678, 56.987]
import subprocess
# Code to join different mp4 video files
import glob
import os

dir = os.path.dirname(__file__) + "/FFMPEG static/ffmpeg.exe"
#dir = dir + "/FFMPEG static/ffmpeg.exe"
#cmd = "-ss 00:01:00 -i C:/videos/TG-Planegg.mp4 -to 00:02:00 -c copy C:/videos/TG-Planegg-out.mp4"
# ffmpeg -i "concat:C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp1.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp2.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp3.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp4.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp5.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp6.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp7.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp8.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp9.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp10.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp11.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp12.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp13.ts|C:\Users\Vergil\PycharmProjects\VideoScout/Videofiles/temp14.ts" -c copy  -bsf:a aac_adtstoasc C:/videos/HureAufs.mp4
cmd = ['C:\\Users\\Vergil\\PycharmProjects\\VideoScout/FFMPEG static/ffmpeg.exe', '-i', '"concat:C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp1.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp2.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp3.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp4.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp5.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp6.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp7.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp8.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp9.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp10.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp11.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp12.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp13.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp14.ts"', '-c', 'copy', '-bsf:a', 'aac_adtstoasc', 'C:/videos/HurAUfs.mp4']
cmd2 = ['C:\\Users\\Vergil\\PycharmProjects\\VideoScout/FFMPEG static/ffmpeg.exe', '-i', '"concat:C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp1.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp2.ts"', '-c', 'copy', '-bsf:a', 'aac_adtstoasc', 'C:/videos/HurAUfs.mp4']
cmd3 = 'C:\\Users\\Vergil\\PycharmProjects\\VideoScout/FFMPEG static/ffmpeg.exe -i "concat:C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp1.ts|C:\\Users\\Vergil\\PycharmProjects\\VideoScout/Videofiles/temp2.ts" -c copy C:/videos/HurAUfs.mp4'
for i in cmd:
    if '\\' in i:
        i = i.replace('\\', '/')
print(cmd3)
#subprocess.run([dir, "-ss", "00:01:00", "-i", "C:/videos/TG-Planegg.mp4", "-to", "00:02:00", "-c", "copy", "C:/videos/TG-Planegg-out5.mp4"], shell=False)
subprocess.call(cmd3, shell=False)

dir = os.path.dirname(__file__)
dir = dir + "/Videofiles/"
files_to_delete = []

for i in range(len(stamps)):
    cliptmp = ffmpeg_extract_subclip("C:/videos/TG-Planegg.mp4", stamps[i] - 4, stamps[i] + 4, targetname=dir + "cutfinal"+ str(i) + ".mp4")
    files_to_delete.append(dir + "cutfinal"+ str(i) + ".mp4")


def concatenate():
    stringa = "ffmpeg -i \"concat:"
    elenco_video = glob.glob(dir + "*.mp4")
    elenco_file_temp = []
    for f in elenco_video:
        file = dir + "temp" + str(elenco_video.index(f) + 1) + ".ts"
        files_to_delete.append(dir + "temp" + str(elenco_video.index(f) + 1) + ".ts")
        os.system("ffmpeg -i " + f + " -c copy -bsf:v h264_mp4toannexb -f mpegts " + file)
        elenco_file_temp.append(file)
    print(elenco_file_temp)
    for f in elenco_file_temp:
        stringa += f
        if elenco_file_temp.index(f) != len(elenco_file_temp) - 1:
            stringa += "|"
        else:
            stringa += "\" -c copy  -bsf:a aac_adtstoasc "+ dir + "output.mp4"
    print(stringa)
    os.system(stringa)
    for i in files_to_delete:
        os.remove(i)

concatenate()

clips = []
path = "C:/videos/Paula_Angriff_final.mp4"
path_tmp = path.replace(".mp4", "tmp.mp4")
cliptmp = ffmpeg_extract_subclip("C:/videos/TG-Planegg.mp4", stamps[0] - 4, stamps[0] + 4, targetname="C:/videos/cutfinal.mp4")
clip_tmp = VideoFileClip("C:/videos/cuttmp.mp4")
clips.append(clip_tmp)
for time in stamps[1:]:
    clip2 = ffmpeg_extract_subclip("C:/videos/TG-Planegg.mp4", time - 4, time + 4, targetname="C:/videos/cuttmp.mp4")
    clip2_vid = VideoFileClip("C:/videos/cuttmp.mp4")
    clips.append(clip2_vid)
    #clipfinal = concatenate_videoclips(clips)
    clipfinal = CompositeVideoClip(clips)
    clipfinal.write_videofile("C:/videos/cutfinal.mp4")
    clips = clips[:1]
    print(len(clips))
    #cliptmp = ffmpeg.concat(cliptmp, clip2, v=1, a=1).output("C:/videos/cutfinal.mp4").run()
    #os.system("ffmpeg -i concat 'C:/videos/cutfinal.mp4' | 'C:/videos/cuttmp.mp4' -map 0 -vcodec copy -aprofile aac_low -acodec aac -strict experimental -cutoff 15000 -vbsf aac_adtstoasc -b:a 32k 'C:/videos/cutfinal.mp4'")
    #os.system(
    #    "ffmpeg -i concat 'C:/videos/cutfinal.mp4|C:/videos/cuttmp.mp4' -map 0 -vcodec copy -aprofile aac_low -acodec aac -strict experimental -cutoff 15000 -vbsf aac_adtstoasc -b:a 32k 'C:/videos/cutfinal.mp4'")

#s = 'Jenny&12-B+, 1-D+, 3-Z0, 4-A+,'

s = '4&5&10&34#B++, '
if re.fullmatch(
        r"[0-9A-Za-z]+((&([0-9A-Za-z]+)){0,2})#[SRDABZ]([+0E/-]|(--)|(\+\+)),?\s?( [0-9A-Za-z]+#[SRDABZ]([+0E/-]|(--)|(\+\+)),\s?)*",
        s):
    print('Treffer')
else:
    print('Niete')

if re.fullmatch(
        r"[0-9A-Za-z]+((&([0-9A-Za-z]+)){0,2})#[SRDABZ]([+0E/-]|(--)|(\+\+)),?\s?( [0-9A-Za-z]+#[SRDABZ]([+0E/-]|(--)|(\+\+)),\s?)*",
        s):


path = 'C:/videos/vids/output.'

h = 1
min = 26
sec = 6

import xml.etree.cElementTree as ET
player = '4'
aktion = 'Angriff'
firstball = ''
rating = ''

if rating != '':
    rating = "[@rating='" + rating + "']"
if firstball != '':
    firstball = "[@Laufer='" + firstball + "']"
if player != '':
    player = "[.='" + player + "']"

dir = os.path.dirname(__file__)
dir = dir + "/Games/" + 'lollipopo.xml'
tree = ET.parse(dir)
for i in tree.findall(".//Timestamp//" + aktion + rating + firstball + player +"/.."):
    print(i.get('time'))


#time = sec + (min * 60) + (h * 3600) + 0.76

stamps = [19, 34, 56]
clips = []
path = "C:/videos/Paula_Angriff_final.mp4"
path_tmp = path.replace(".mp4", "tmp.mp4")
for time in stamps:
    clip2 = VideoFileClip("C:/videos/TG-Planegg.mp4").subclip(time - 4 , time + 4)

    #clip2.to_videofile('C:/videos/Paula_Angriff_Planegg_' + str(time) + '.mp4', codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
    clip2.to_videofile(path_tmp, codec="libx264",
                       temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
    clips.append(clip2)

clipfinal = concatenate_videoclips(clips)
clipfinal.write_videofile("C:/videos/Paula_Angriff_final.mp4")

os.remove(path_tmp)




s = '3-Z/, '
if re.fullmatch(r"[0-9A-Za-z]+(&([0-9A-Za-z]+))?-[SRDABS][0+/-],?\s?( [0-9A-Za-z]+-[SRDABZ][0+/-],\s?)*", s):
#if re.fullmatch(r"( [0-9A-Za-z]+-[SRDABS][0+/-])*,", s):
#if re.fullmatch(r"[0-9A-Za-z]+(&([0-9A-Za-z]+))?-[SRDABS][0+/-](, [0-9A-Za-z]+-[SRDABS][0+/-],?)*", s):
    print('Treffer')


    s_l = s.split(',')
    print(s_l)
    for i in s_l:
        if i.strip() != '':
            i = i.strip()
            i_list = i.split('-')
            for j in i_list:
                if '&' in j:
                    players = j.split('&')
                    for p in players:
                        if i_list[1][0] == 'B':
                            print(p + ' Block ' + i_list[1][1])
                else:

                    if i_list[1][0] == 'D':
                        print(i_list[0] + ' Verteidigung ' + i_list[1][1])
                    elif i_list[1][0] == 'Z':
                        print(i_list[0] + ' Zuspiel ' + i_list[1][1])
                    elif i_list[1][0] == 'A':
                        print(i_list[0] + ' Angriff ' + i_list[1][1])
                    elif i_list[1][0] == 'B':
                        print(i_list[0] + ' Block ' + i_list[1][1])
                    elif i_list[1][0] == 'S':
                        print(i_list[0] + ' Aufschlag ' + i_list[1][1])
                    elif i_list[1][0] == 'R':
                        print(i_list[0] + ' Annahme ' + i_list[1][1])

else:
    print('Niete')



h = 1
min = 26
sec = 6

time = sec + (min * 60) + (h * 3600)


clip = VideoFileClip("C:/videos/TG-Planegg.mp4").subclip(time - 4, time + 3)
clip.to_videofile('C:/videos/Paula_Angriff_Planegg_8.mp4', codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif


# Driver Code
li1 = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '12', '13', '14']
li2 = ['2', '3', '5', '9', '10', '4', '1']
#li1 = [10, 15, 20, 25, 30, 35, 40]
#li2 = [25, 40, 35]
li3 = Diff(li1, li2)




dir = os.path.dirname(__file__)
dir = dir + "/Games/kiki.xml"
dir2 = os.path.dirname(__file__)
dir2 = dir2 + "/Games/kiki2.xml"
id = '3'

def delete_node(id, file):
    tree = ET.parse(file)
    xml = tree.getroot()
    iterator = xml.findall("Timestamp")
    for item in iterator:
        f = item
        text = item.attrib["id"]
        if text == id:
            xml.remove(f)
            tree.write(file)

deleted_residue(id, dir2)




for x in xml:
            for y in x:
                if y.attrib["title"] == titem:
                    x.remove(y)
                    self.xml.write("output.xml")
                    return
tree = ET.parse(dir)
root = tree.getroot()
root = etree.parse(dir).getroot()

xmldoc = minidom.parse(dir)

nodes = xmldoc.getElementsByTagName("Timestamp")
for node in nodes:
    if node.attributes['id'].value == '3':
        print(node.attributes['time'].value)
        parent = node.parentNode
        parent.removeChild(node)



#save_xml_document(dir2, root)

print('Ende')

with open(dir2,"w") as fs:
    fs.write(xmldoc.toxml())
    fs.close()



#tree = ET.parse(dir)
#root = tree.getroot()

mydoc = minidom.parse(dir)

items = mydoc.getElementsByTagName('Timestamp')


label_string = ''
for elem in items:
    print(elem.tagName)


    var = int(elem.attributes['time'].value)
    temp = datetime.datetime.fromtimestamp(var / 1000).strftime('%H:%M:%S')
    label_string = 'id : ' + elem.attributes['id'].value + ' Zeit : ' + str(temp)
    print(label_string)
    for sub_elem in elem.childNodes:
        if sub_elem.nodeType == sub_elem.ELEMENT_NODE:
            print(str(sub_elem.nodeName))
            print(str(sub_elem.firstChild.nodeValue))



try:
    for elem in tree.iter():
        #print(elem.attrib.get('id'))
        if id == (elem.attrib.get('id')):
            print('elem' + elem.tag)
            root.remove(elem)
            print('treffer')
            for child in elem.iter():
                print('child' + child.getchildren()[0])
                elem.remove(child)

                #print(child.tag)

except:
    lastid = 1

    """
"""
    def keyPressEvent(self, event):
        keys = keyFunktionen(self.current_game + '.xml', self.label_last, self.label_last_but_one, self.label_third_last)

        modifiers = QApplication.keyboardModifiers()
        if event.key() == Qt.Key_R:
            self.rotieren(self.pos1, self.pos2, self.pos3, self.pos4, self.pos5, self.pos6)
            self.showCurrentLineup(self.currentLineUp)

        # ALle Abwehrpostionen

        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_A):
            keys.abwehr4(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif event.key() == Qt.Key_A:
            keys.abwehr5(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_S):
            keys.abwehr3(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif event.key() == Qt.Key_S:
            keys.abwehr6(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_D):
            keys.abwehr2(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)

        elif event.key() == Qt.Key_D:
            # keys.abwehr1(self.currentLineUp)
            keys.abwehr1(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)

        # Zuspiel

        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_H):
            keys.liberoZuspiel(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif event.key() == Qt.Key_H:
            keys.zuspiel(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)

        # Aufschlag

        elif event.key() == Qt.Key_F:
            keys.aufschlag(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)

        # Annahme

        # elif (modifiers & Qt.ShiftModifier) and (event.key() == 0x45):

        elif event.key() == Qt.Key_E:
            keys.annahme(self.currentLineUp, '2', '1', '1', '2', '1', '1', str(self.mediaPlayer.position()),
                         self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif event.key() == Qt.Key_W:
            keys.annahme(self.currentLineUp, '6', '5', '6', '6', '5', '6', str(self.mediaPlayer.position()),
                         self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif event.key() == Qt.Key_Q:
            keys.annahme(self.currentLineUp, '5', '4', '3', '5', '4', '3', str(self.mediaPlayer.position()),
                         self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)

        # Angriff

        elif event.key() == Qt.Key_J:
            keys.angriff4(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_K):
            keys.angriff6(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif event.key() == Qt.Key_K:
            keys.angriff3(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_L):
            keys.angriff1(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif event.key() == Qt.Key_L:
            keys.angriff2(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)

        # Block

        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_U):
            keys.doppelblock4(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif event.key() == Qt.Key_U:
            keys.einblock4(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_I):
            keys.dreierblock(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif event.key() == Qt.Key_I:
            keys.einerblock3(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif (modifiers & Qt.ShiftModifier) and (event.key() == Qt.Key_O):
            keys.doppelblock2(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)
        elif event.key() == Qt.Key_O:
            keys.einervblock2(self.currentLineUp, str(self.mediaPlayer.position()), self.key_counter)
            self.key_counter = self.increase_counter(self.key_counter)

        # Sonstiges

        elif event.key() == Qt.Key_P:
            print('Pause/Play')
        elif event.key() == Qt.Key_C:
            self.liberoInOut(self.currentLineUp)
        elif event.key() == Qt.Key_T:
            print('Anderer Libero')

        elif (modifiers & Qt.ShiftModifier):
            None
        else:
            None
    

"""