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
        self.url.grid(row=0, column=1, pady=20, stick='W')
        self.go = tk.Button(self, text='Scrap!', command=self.scrap)
        self.go.grid(row=1, column=0, pady=5, stick='E', padx=10)
        self.go_download = tk.Button(self, text='Download!', command=self.download)
        self.go_download.grid(row=1, column=1, pady=5, stick='W', padx=10)

    def scrap(self):
        url = self.url.get()
        self.scrapped = ws.scraper(url)
        self.scrapped.scrap()
        details = self.scrapped.__str__()
        self.text = tk.Message(self, text=details)
        self.text.grid(row=3, column=0, columnspan=2, pady=10, ipady=5)

    def download(self, url):
        pass

root = tk.Tk()
root.title('Youtube Scraper and Downloader')
ind = index(master=root)
frame = tk.Frame(root, width=500)
frame.pack()
ind.mainloop()