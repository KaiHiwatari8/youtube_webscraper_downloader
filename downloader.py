from pytube import YouTube
import getpass

class downloader_class():
    def __init__(self, url, save_path='C:\\Users\\' + getpass.getuser() +'\\Downloads\\Video'):
        self.url = url
        self.save_path = save_path

    def download(self, quality, extension):
        try:
            yt = YouTube(self.url)
        except:
            print('Connection error')
        self.all_streams = yt.streams.all()[0]
        print(self.all_streams.parse_codecs())

d = downloader_class('https://www.youtube.com/watch?v=9bZkp7q19f0')
d.download()