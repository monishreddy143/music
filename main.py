from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter import messagebox
import os

from tkinter import ttk
from ttkthemes import themed_tk as tk


from mutagen.mp3 import MP3
import threading
import time

root = tk.ThemedTk()
root.get_themes()                 
root.set_theme("radiance") 


Statusbar=ttk.Label(root , text="Munny melody",relief=SUNKEN, anchor=W,background="lightgreen")
Statusbar.pack(side=BOTTOM , fill=X)

menubar=Menu(root ,bg="#20232A")
root.config(menu=menubar)


def about_it():
    messagebox.showerror("About music","Nothing right now")


play_list=[]

def browse_file():
    global filename_path
    filename_path=filedialog.askopenfilename()
    add_to_playlist(filename_path)

def add_to_playlist(filename):
    filename=os.path.basename(filename)
    index=0
    playlistbox.insert(index , filename)
    play_list.insert(index,filename_path)
    index+=1


sub_menu=Menu(menubar ,tearoff=0,background='#90EE90')
menubar.add_cascade(label='File',menu=sub_menu)
sub_menu.add_command(label="open", command=browse_file)
sub_menu.add_command(label="close",underline=1)
sub_menu.add_command(label="exit",command=root.destroy)


About=Menu(menubar ,background="#90EE90")
menubar.add_cascade(label="About",menu=About)
About.add_command(label="About player",command=about_it)


leftframe=Frame(root)
leftframe.pack(side=LEFT,padx=30)

playlistbox=Listbox(leftframe)
playlistbox.pack()


add_btn=ttk.Button(leftframe , text="+Add",command=browse_file)
add_btn.pack(side=LEFT)

def del_song():
    selected_song=playlistbox.curselection()
    selected_song=int(selected_song[0])
    playlistbox.delete(selected_song)
    play_list.pop(selected_song)
    print(play_list)



del_btn=ttk.Button(leftframe,text="-Del",command=del_song)
del_btn.pack(side=LEFT)

#root window -statusbar , left , rightframe
#leftframe-listbox , del , add
#rightframe-topframe , bottom , middlframe

rightframe=Frame(root)
rightframe.pack()



topframe=Frame(rightframe)
topframe.pack()

top_label=ttk.Label(topframe , text ="Lets make some noise......!@").pack(pady=5)

song_length_label=ttk.Label(topframe , text="length:--:--")
song_length_label.pack(pady=5)





mixer.init()


root.title("Munny melody la la la l all aaa")
root.iconbitmap(r"images/melody2.ico")



play_photo=PhotoImage( file="images/play.png")

stop_photo=PhotoImage( file="images/stopbtn.png")

pause_photo=PhotoImage(file="images/pause.png")

rewind_photo=PhotoImage(file="images/rewind.png")

def showdetails(play_this_song):
    filedata=os.path.splitext(play_this_song)

    if filedata[1]=='.mp3':
        audio=MP3(play_this_song)
        total_length=audio.info.length
    else:
        a=mixer.Sound(play_this_song)
        total_length=a.get_length()

    min,sec=divmod(total_length,60)
    min=round(min)
    sec=round(sec)
    time_format ='{:02d}:{:02d}'.format(min,sec)
    song_length_label["text"]="Total length"+"-"+time_format
  



def play_it():
    
    global paused

    if paused:
        mixer.music.unpause()
        Statusbar['text']="song resumed"
        paused=FALSE
    else:
        try:
            #this is for listbox curser function in listbox 
            #play_list=[song path , song path]
            #playlistbox=[song filenmae , song filename2]
            selected_song=playlistbox.curselection()
            selected_song=int(selected_song[0])
            play_this_song=play_list[selected_song]
            mixer.music.load(play_this_song)
            mixer.music.play()
            Statusbar['text']="song playing"+" "+os.path.basename(play_this_song)
            showdetails(play_this_song)
        except:
            messagebox.showerror("file loding","file not loded correctly")



def stop_it():
    mixer.music.stop()
    Statusbar['text']="song stoped"


def set_vol(val):
    volume=float(val)/100
    mixer.music.set_volume(volume)

paused=FALSE
def pause_it():
    global paused
    paused=TRUE
    mixer.music.pause()
    Statusbar["text"]="Song paused"

def rewind_it():
    play_it()
    Statusbar["text"]="Song rewinded"

middle_Frame=Frame(rightframe)
middle_Frame.pack(padx=30,pady=30)

bottom_frame=Frame(rightframe)
bottom_frame.pack(padx=30 ,pady=30)

button1=ttk.Button(middle_Frame , image=play_photo,command=play_it)
button2=ttk.Button(middle_Frame, image=stop_photo,command=stop_it)
button3=ttk.Button(middle_Frame , image=pause_photo , command=pause_it)
button4=ttk.Button(bottom_frame ,image=rewind_photo , command=rewind_it )

button1.grid(row=0,column=0,padx=10)
button2.grid(row=0,column=1,padx=10)
button3.grid(row=0,column=3,padx=10)
button4.grid(row=0 ,column=0,padx=30)

#volume scale
scale =ttk.Scale (bottom_frame , from_=0 , to =100 , command=set_vol,orient=HORIZONTAL)
scale.set(30)  
mixer.music.set_volume(0.3)
scale.grid(row=0 ,column=3,padx=30)
#volume scale end

#mute unmute start
muted=False
def mute_it():
    global muted
    if muted:
        mixer.music.set_volume(0.4)
        scale.set(40)
        mute_unmute_volume.configure(image=unmute_photo)
        muted=False
        Statusbar['text']="Song UN_Muted"

    else:
        mixer.music.set_volume(0)
        scale.set(0)
        mute_unmute_volume.configure(image=mute_photo)
        muted=True
        Statusbar['text']="Song Muted"


mute_photo =PhotoImage(file="images/mute.png")
unmute_photo =PhotoImage(file="images/audio.png")
mute_unmute_volume=ttk.Button(bottom_frame , image=unmute_photo , command=mute_it)
mute_unmute_volume.grid(row=0 , column=2)

#mute unmute end





def on_close():
    stop_it()
    root.destroy()

root.protocol("WM_DELETE_WINDOW",on_close)
root.mainloop()