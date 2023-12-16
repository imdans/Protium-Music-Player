import sys, math, wave, numpy, pygame
from pygame.locals import *
from scipy.fftpack import dct
from pathlib import Path
import pygame 
import os 
import tkinter as tk
from tkinter import *
from tkinter import filedialog , Entry , Button , messagebox
from youtube_dl import YoutubeDL
from os import path
from pydub import AudioSegment
import soundfile as sf 
import pyrubberband 




OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/home/dhanush/Downloads/python shit/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = tk.Tk()

window.title("Atom Music Player")
window.geometry("892x528")
window.configure(bg = "#173F5F")

pygame.mixer.pre_init(44100,-16,2,1024)
pygame.mixer.init()
songs=[]
current_song=""
paused= False


def visualing():
    global num 
    Number = 30 
    HEIGHT = 600 
    WIDTH = 40 
    FPS = 10

    file_name = sys.argv[0]
    status = 'stopped'
    fpsclock = pygame.time.Clock()

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode([Number * WIDTH, 50 + HEIGHT])
    pygame.display.set_caption('Audio Visualizer')
    my_font = pygame.font.SysFont('consolas', 16)
    pygame.mixer.music.load(entryv.get())
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent()
    pygame.mixer.music.set_volume(0.2)
    status = "Playing"

    #process wave data

    f = wave.open(entryv.get(), 'rb')
    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    str_data = f.readframes(nframes)
    f.close()
    wave_data = numpy.fromstring(str_data, dtype = numpy.short)
    wave_data.shape = -1, 2
    wave_data = wave_data.T

    num = nframes

    def Visualizer(nums):
        num = int(nums)
        h = abs(dct(wave_data[0][nframes - num:nframes - num + Number]))
        h = [min(HEIGHT, int(i**(1 / 2.5) * HEIGHT / 100)) for i in h]
        draw_bars(h)

    def vis(status):
        global num
        if status == "stopped":
            num = nframes
            return
        elif status == "paused":
            Visualizer(num)
        else:
            num -= framerate / FPS
            if num > 0:
                Visualizer(num)

    def get_time():
        seconds = max(0, pygame.mixer.music.get_pos() / 1000)
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        hms = ("%02d:%02d:%02d" % (h, m, s))
        return hms

    def controller(key):
        global status
        if status == "stopped":
            if key == K_RETURN:
                pygame.mixer_music.play()
                status = "playing"
        elif status == "paused":
            if key == K_RETURN:
                pygame.mixer_music.stop()
                status = "stopped"
            elif key == K_SPACE:
                pygame.mixer.music.unpause()
                status = "playing"
        elif status == "playing":
            if key == K_RETURN:
                pygame.mixer.music.stop()
                status = "stopped"
            elif key == K_SPACE:
                pygame.mixer.music.pause()
                status = "paused"

    def draw_bars(h):
        bars = []
        for i in h:
            bars.append([len(bars) * WIDTH , 50 + HEIGHT - i, WIDTH - 1, i])
        for i in bars:
            pygame.draw.rect(screen, [255,255,255], i, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                controller(event.key)

        if num <= 0:
            status = "stopped"

        name = my_font.render(file_name, True, (255,255,255))
        info = my_font.render(status.upper() + "" + get_time(), True, (255,255,255))
        screen.fill((0,0,0))
        screen.blit(name,(0,0))
        screen.blit(info,(0, 18))
        fpsclock.tick(FPS)
        vis(status)
        pygame.display.update()

def visuall():
    global entryv
    window5=tk.Tk()
    window5.title("Visualiser")
    window5.geometry("800x500")
    window5.configure(bg="#173F5F")

    entryv=tk.Entry(window5,width=30)
    entryv.place(
        x=270,
        y=100
    )
    inputv=tk.Button(window5,text="Enter the name of the file",command=visualing,width=20)
    inputv.place(
        x=300,
        y=130
    )
def loud():
    filenameloud=entryloud.get()
    vol=entryvol.get()
    audio=AudioSegment.from_file(filenameloud)
    newaud=audio+vol
    newaud.export("volchange"+filenameloud,format="wav")
def louding():
    global entryloud , entryvol
    window2=tk.Tk()
    window2.title("Loudness of Audio")
    window2.geometry("800x500")
    window2.configure(bg="#173F5F")

    entryloud=tk.Entry(window2,width=30)
    entryloud.place(
        x=270,
        y=100
    )
    inputloud=tk.Button(window2,text="Enter File Name", width=20)
    inputloud.place(
        x=300,
        y=130
    )
    entryvol=tk.Entry(window2,width=30)
    entryvol.place(
        x=270,
        y=300
    )
    inputvol=tk.Button(window2,text="Enter Vol Value",width=20,command=loud)
    inputvol.place(
        x=300,
        y=330
    )
    
def speedy():  
    spfile=entrysp.get()
    audio, sr = sf.read(spfile)
    slowed_audio = pyrubberband.time_stretch(audio, sr, 1.5)
    sf.write("newspeed"+spfile, slowed_audio, sr)
    messagebox.showinfo("Result","File saved!")

def slowy():
    slfile=entrysl.get()
    audio, sr = sf.read(slfile)
    slowed_audio = pyrubberband.time_stretch(audio, sr, 0.5)
    sf.write("newslow"+slfile, slowed_audio, sr)
    messagebox.showinfo("Result","File saved!")

def speed_slow():
    global entrysp , entrysl , spfile , slfile
    window2=tk.Tk()
    window2.title("Speed up / Slow down")
    window2.geometry("800x500")
    window2.configure(bg="#173F5F")

    entrysl=tk.Entry(window2,width=30)
    entrysl.place(
        x=270,
        y=100
    )
    inputsl=tk.Button(window2,text="slow down(only wav)", width=20,command=slowy)
    inputsl.place(
        x=300,
        y=130
    )
    entrysp=tk.Entry(window2,width=30)
    entrysp.place(
        x=270,
        y=300
    )
    inputsp=tk.Button(window2,text="speedup(only wav)",width=20,command=speedy)
    inputsp.place(
        x=300,
        y=330
    )
    
def converfile():
        
    filename=entry2.get()
    filename2=os.path.splitext(filename)
    inputextension=filename2[1]
    inext=inputextension.replace(".","")

    outfile=entry3.get()
    outfile2=os.path.splitext(outfile)
    outextension=outfile2[1]
    outext=outextension.replace(".",'')
    
    raw_audio= AudioSegment.from_file(filename,format=inext)
    raw_audio.export(outfile,format=outext)
    messagebox.showinfo("Result","File converted!")

def file_conversion():
    global entry2 , entry3
    window2=tk.Tk()
    window2.title("File converter")
    window2.geometry("800x500")
    window2.configure(bg="#173F5F")

    entry2=tk.Entry(window2,width=30)
    entry2.place(
        x=270,
        y=100
    )
    inputf=tk.Button(window2,text="Enter the name of the file", width=20)
    inputf.place(
        x=300,
        y=130
    )
    entry3=tk.Entry(window2,width=30)
    entry3.place(
        x=270,
        y=300
    )
    outputf=tk.Button(window2,text="Enter the name of output file",width=20,command=converfile)
    outputf.place(
        x=300,
        y=330
    )
    

def youtube_download():
    global download_music
    new_window = tk.Tk()
    new_window.title("Youtube Downloader")
    new_window.geometry("800x500")
    new_window.configure(bg="#173F5F")

    entry_box = tk.Entry(new_window, width=30)
    entry_box.place(
        x=260,
        y=264)
    
    def download_music():
        url = entry_box.get()
             # make command that will be later executed
        command = 'youtube-dl --verbose --embed-thumbnail --no-warnings --extract-audio --audio-format mp3 -o "%(title)s.%(ext)s" ' + url[url.find("=")+1:]

        try: 
            print('Downloading %s' % url)
            os.system(command)
            messagebox.showinfo("Result","Command Accepted")
        except:
            print("Unable to fetch video information. Please check the video URL or your network connection.")
            messagebox.showinfo("Result","Download could not complete:Error")

    my_button = tk.Button(new_window, text="Enter URL",command=download_music,width=20)
    my_button.place(
        x=290, 
        y=364)
    
    
def load_music():
    global paths , song2
    song=filedialog.askopenfilename(title="Select song", filetypes=(("mp3 Files","*.mp3"),))
    paths=os.path.dirname(song)
    song=song.replace(paths,"")
    song=song.replace("/","")
    songlist.insert(END,song)


def play_music():
    global song
    song=songlist.get(ACTIVE)
    song=os.path.abspath(song)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

global pausing
pausing=False
def pause_music(is_paused):
    global pausing
    pausing=is_paused
    if pausing:
        pygame.mixer.music.unpause()
        pausing=False
    else:
        pygame.mixer.music.pause()
        pausing=True

def next_music():
    next_one=songlist.curselection()
    next_one=next_one[0]+1
    song=songlist.get(next_one)
    song=os.path.abspath(song)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songlist.selection_clear(0,END)
    songlist.activate(next_one)
    songlist.selection_set(next_one,last=None)

def prev_music():
    prev_one=songlist.curselection()
    prev_one=prev_one[0]-1
    song=songlist.get(prev_one)
    song=os.path.abspath(song)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    songlist.selection_clear(0,END)
    songlist.activate(prev_one)
    songlist.selection_set(prev_one,last=None)


canvas = Canvas(
    window,
    bg = "#173F5F",
    height = 528,
    width = 892,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    205.0,
    528.0,
    fill="#141414",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=play_music,
    relief="flat"
)
button_1.place(
    x=527.0,
    y=292.0,
    width=57.0,
    height=62.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda:pause_music(pausing),
    relief="flat"
)
button_2.place(
    x=482.0,
    y=296.0,
    width=46.0,
    height=56.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=prev_music,
    relief="flat"
)
button_3.place(
    x=421.0,
    y=295.0,
    width=44.0,
    height=57.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=next_music,
    relief="flat"
)
button_4.place(
    x=592.0,
    y=293.0,
    width=44.0,
    height=57.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=speed_slow,
    relief="flat"
)
button_6.place(
    x=9.0,
    y=262.0,
    width=187.0,
    height=56.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=load_music,
    relief="flat"
)
button_7.place(
    x=9.0,
    y=85.0,
    width=187.0,
    height=56.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=file_conversion,
    relief="flat"
)
button_8.place(
    x=421.0,
    y=465.0,
    width=197.0,
    height=34.0
)

canvas.create_rectangle(
    349.0,
    69.0,
    702.0,
    284.0,
    #fill="#071E22",
    outline="")

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=visuall,
    relief="flat"
)
button_9.place(
    x=438.0,
    y=398.0,
    width=164.0,
    height=47.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=louding,
    relief="flat"
)
button_10.place(
    x=9.0,
    y=171.0,
    width=187.0,
    height=61.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=youtube_download,
    relief="flat"
)
button_11.place(
    x=8.0,
    y=348.0,
    width=189.0,
    height=61.0
)
#songlist = Listbox(window ,bg="#071E22",width=50,height=14)
songlist = Listbox(window ,bg="#262455",width=50,height=13)
songlist.place(
    x=315,
    y=14
)
window.resizable(False, False)
window.mainloop()
