# Protium-Music-Player
![Screenshot_20231217_024722](https://github.com/imdans/Protium-Music-Player/assets/150439350/1aa3a8ef-7c6a-4edb-afe5-83b3747866ed)

This is the first python project ive ever made dont be too harsh plis :') </br>
Using this app you can:
* Increase/Decrease the base volume of an audio file
* Speedup/Slowdown an audiofile (currently values are default and cannot be changed , custom values option will be provided soon)
* Download Music from Youtube by providing the url in the entry box.
* play .mp3 songs (slider will be implemented soon)
* convert audio files from one type to the other
* A visualiser that i casually ripped off from [This repo](https://github.com/pureforwhite/AudioVisualizer)
* I had some help creating the GUI using [this designer (very cool)](https://github.com/ParthJadhav/Tkinter-Designer) but i had to rewrite the gui in the end to make everything fit in well.

# REQUIREMENTS:
* Python3.10 is a hard requirement sadly. i HIGHLY reccomend creating a 3.10 venv and running the app there.
* Well how do i create a venv?
  * venv's are virtual environments. this helps you run and install python modules isolated from the host system (kind of like a container)
  * to create venv of a particular python version it needs to be installed on your system.
  * then to create venv open terminal (or cringe powershell) and type in "python3.10 -m venv venv_name"
  * enter the venv (the process differs based on OS)
  * you can replace 3.10 with any version you want (but this project will strictly need 3.10)
*  as soon as the "pyrubberband" module moves to 3.12 this wont be required
* Once you create a venv install the following modules using pip:
  * scipy
  * pygame
  * tkinter(pip install may not work so you may need to install this manually or use your OS package manager specifically for tkinter-python3.10)
  * youtube_dl
  * pydub
  * soundfile
  * pyrubberband
  * math
  * wave
  * numpy
  * os , path (preinstalled)
 # How to run:
 * Just download the "protiumplayer.zip" from the repo and unpack it. then run the python file.
# How to Use:
Basic Usage Guide
* It is required that the file you need to work on should be in the same directory as the protium app.
* i'll implement the option to selection using a dialogbox soon as my dumbass wasn't aware of the existence of os.path() commands until after i finished half of the work.
## Audio Loudness ##
* Enter the name of the file in the first entry box
* Enter the volume by which you need to increase/decrease the file. i'll consider adding a slider instead for the volume value later.
* a new file will be generated in the same directory. for now the file will have the same name followed by the prefix "changevol" but i'll implement custom output names later.
* This uses the "pydub" module
* .mp3 and .wav both work.
## Speedup/Slow down ##
* For now the speedup and slowdown values are default and cant be changed (1.5x and 0.8x)
* As ive realised its actually pretty simple to have custom values but im lazy and hopefully will get to it. maybe.
* Enter the name of the audio file WITH the extension and click on the button to either speedup/slowdown file.
* This uses the "pyrubberband" module which i prefer because it conserves the audio pitch
* only .wav files will work (working on mp3 is not reccomended anyways as it may nuke the audio quality)
## Youtube Downloader ##
* Enter the URL in the entry box and download the audio in mp3!
* uses good-ol youtube-dl
* KNOWN ISSUE WITH YOUTUBE DOWNLOADER:
    * youtube downloader gives out some error when you use it (uploader id error)
    * this is sadly an upstream bug and i cant do anything to fix it , however there is a workaround by disabling the uploader id , which we dont need anyways
    * if you are in a venv go to (venv_name)>lib64>youtube_dl>extractor>youtube.py (this is the location of the youtube_dl module and specifically the .py file that handles youtube downloads)
    * '#' out line 1794 (this is the line related to uploader id)
## Audio converter ##
* This converts audio from one format to another
* Enter the names of both the input and output file in the boxes WITH the extensions in the name
* This has little to no effect on conversion of files from high compression -> low compression formats
* This uses the "pydub" module as well
## Visualiser ##
* As i mentioned before the visualiser is a blatant , shameless ripoff , and can be better explained by the repo i linked above.
* note that only .wav audio files work for the visualiser

# Plans for the Future (if life dosent exhaust me):
* Add custom theming
* Move away (As far as i can) from tkinter and use Qt instead
* add sliders (which i can even now but im lazy)
* add better dialog boxes and not so ugly entry boxes
* write my own visualiser
  
