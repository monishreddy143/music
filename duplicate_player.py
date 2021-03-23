from tkinter import *
from pygame import mixer
from tkinter import messagebox
from tkinter import filedialog
root= Tk()
mixer.init()


Menubar=Menu(root)
root.config(menu=Menubar)


def Browesing():
    global filename
    filename=filedialog.askopenfilename()

file_open=Menu(Menubar)
Menubar.add_cascade(label="File",menu=file_open)
file_open.add_command(label="open" ,command=Browesing)
file_open.add_command(label="exit",command=root.destroy)





root.geometry("500x500")

root.title("dup_player")
root.iconbitmap(r"melody.ico")


play_btn=PhotoImage(file="play.png")
stop_btn=PhotoImage(file="stop.png")

def play_it():
    try:
        mixer.music.load(filename)
        mixer.music.play()
    except:
        messagebox.showerror("opening song","song not uploaded correctly")
def stop_it():
    mixer.music.stop()

def volume(val):
    vol=int(val)/100
    mixer.music.set_volume(vol)



but1=Button(root, image=play_btn ,command=play_it).pack()

but2=Button(root, image=stop_btn ,command=stop_it).pack()


scale=Scale(root,from_=0 ,to=100 , command=volume)
scale.set(30)
mixer.music.set_volume(0.3)
scale.pack()




root.mainloop()