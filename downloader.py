import conversor
from pytube import YouTube

def subStr(txt = ""):
    txt = txt.replace("|", "").replace("#", "")
    return txt

class Video:
    
    def __init__(self, url = "") -> None:
        self.yt = YouTube(url)
        self.title = subStr(self.yt.title) or 'Untitled'

    def get_streams(self):
            return self.yt.streams.filter(file_extension='mp4')
    
    def download(self, local, mp4 = True):
        if mp4 ==True:
            d = self.yt.streams.get_highest_resolution()
            d.download(local)
        else:
            d = self.yt.streams.get_highest_resolution()
            d.download()
            conversor.convert(local)
