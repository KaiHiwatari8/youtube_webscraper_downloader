import tkinter as tk
import WebScraper as ws

class index(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.run()

    def run(self):
        tk.Label(self, text='Enter Youtube URL:').grid(row=0, column=0, pady=20, stick='E')
        self.url = tk.Entry(self, width=50)
        self.url.grid(row=0, column=1, pady=20, stick='W', columnspan=3)
        self.go = tk.Button(self, text='Scrap!', command=self.scrap)
        self.go.grid(row=1, column=1, pady=5, stick='E', padx=10)
        self.go_download = tk.Button(self, text='Download!', command=self.download)
        self.go_download.grid(row=1, column=2, pady=5, stick='W', padx=10)

    def scrap(self):
        url = self.url.get()
        self.scrapped = ws.scraper(url)
        self.scrapped.scrap()
        details = self.scrapped.__str__()
        self.text = tk.Message(self, text=details)
        self.text.grid(row=3, column=0, columnspan=2, pady=10, ipady=5)

    def download(self):
        url = self.url.get()
        self.quality_label = tk.Label(self, text='Choose quality:')
        self.quality_label.grid(row=3, column=0, pady=10)
        self.p480 = tk.Checkbutton(self, text='480p')
        self.p480.grid(row=3, column=1)
        self.p720 = tk.Checkbutton(self, text='720p')
        self.p720.grid(row=3, column=2)
        self.p1080 = tk.Checkbutton(self, text='1080p')
        self.p1080.grid(row=3, column=3)

        self.extension_label = tk.Label(self, text='Choose extension:')
        self.extension_label.grid(row=4, column=0)
        self.mp4 = tk.Checkbutton(self, text='mp4')
        self.mp4.grid(row=4, column=1)
        self.webm = tk.Checkbutton(self, text='webm')
        self.webm.grid(row=4, column=2)
        self.flv = tk.Checkbutton(self, text='flv')
        self.flv.grid(row=4, column=3)

        self.download_selection = tk.Button(self, text='Download Selected', command=self.download_selected)
        self.download_selection.grid(row=5, column=0, columnspan=4)

    def download_selected(self):
        quality = []
        extenson = []

root = tk.Tk()
root.title('Youtube Scraper and Downloader')
ind = index(master=root)
frame = tk.Frame(root, width=500)
frame.pack()
ind.mainloop()