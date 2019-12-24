from pytube import YouTube
import getpass

class downloader_class():
    def __init__(self, url, save_path='C:\\Users\\' + getpass.getuser() +'\\Downloads\\Video'):
        self.url = url
        self.save_path = save_path

    def download(self):
        try:
            yt = YouTube(self.url)
        except:
            print('Connection error')