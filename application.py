from tkinter import *
from panhandler import *

root = Tk()
root.configure(background='#404040', padx=10, pady=10)
root.title("Panhandler")

title = Label(root, text="That Panhandlin' Bitch")
title.configure(background='#404040', fg='#FFFFFF')
title.grid(row=0, column=0)

streamerLabel = Label(root, text="Enter a streamer's username", pady=10)
streamerLabel.configure(background='#404040', fg='#FFFFFF')
streamerLabel.grid(row=1, column=0)

streamer = Entry(root, width=40)
streamer.grid(row=2, column=0)
streamer.insert(0, "")

def startScrape():
    streamerName = streamer.get()
    scrape(streamerName)

bitchBtn = Button(root, text="Start Scraping!", command=startScrape, padx=30,\
                    relief=RAISED, cursor="hand2")
bitchBtn.grid(row=2, column=1)

root.mainloop()
