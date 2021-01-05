import natsort
import os

import shutil
import pydub
import subprocess

from natsort import natsorted
from pydub import AudioSegment
AudioSegment.converter = "C:\\ffmpeg\\bin\\ffmpeg.exe"
path = 'D:\Working\Audiobooks\\'



def CombinedMp3(files,path,folder):
    combined = AudioSegment.empty()
    sf = natsorted(files)
    filestxt = path+"\\files.txt"
    txtFile = open(filestxt, 'w')
    i=0
    last=""
    for f in sf:
        print("file "+"'"+f.replace(path+"\\","")+"'")
        txtFile.write("file "+"'"+f.replace(path+"\\","")+"'\n")
        last=f.replace(path+"\\","")
        i+=1
    txtFile.close()
    '''
    #count files
    if str(i) not in last:
        counttxt = path + "\\"+str(i)+" - "+last+".txt"
        txtCount = open(counttxt, 'w')
        txtCount.close()

    '''
    print(filestxt)
    file1 = '"'+filestxt+'"'
    print("folder ",folder)

    text = "ffmpeg -f concat -vn -safe 0 -analyzeduration 5000000000 -probesize 5000000000 -i " + file1.replace("\\", "/") + " -c:a copy D:/A/Done/"+'"'+folder+'"'+".mp3"
    print("text ", text)
    subprocess.call(text, shell=True)
    shutil.move(path, 'D:\Working\\Done\\' + folder)

    print("Done***********************")

def fileperfolder(path):
    # r=root, d=directories, f = files
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            if '.mp3' in file:
                files.append(os.path.join(r, file))
    return files
for r, d, f in os.walk(path):
    for folder in d:
        path = os.path.join(r, folder)
        CombinedMp3(fileperfolder(path),path,folder)


'''

combined = AudioSegment.empty()
for song in playlist_songs:
    combined += song

combined.export("/path/to/output.mp3", format="mp3")
'''
