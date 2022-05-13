import os
import glob
import shutil
from moviepy.video.io.VideoFileClip import VideoFileClip


def convert(local):
    lista_mp4 = glob.glob('*.mp4')

    for video in lista_mp4:
        mp4 = VideoFileClip(os.path.join(video))
        nome_mp3 = video[:-4] + '.mp3'
        mp4.audio.write_audiofile(os.path.join(nome_mp3))
        mp4.close()
        os.remove(video)

        shutil.move(nome_mp3, local)
