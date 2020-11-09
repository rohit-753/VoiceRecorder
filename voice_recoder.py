import sounddevice as sd        
import soundfile as sf          
from tkinter import *           
import numpy                    
bg='#f1c159'
fg='#2b2b2b'


def Voice_rec():
    fs=48000        

    
    duration=5         
    myrecording=sd.rec(int(duration * fs),samplerate=fs, channels=2)
    sd.wait()

    
    return sf.write('my_Audio_file.flac',myrecording,fs)


master=Tk()
master.geometry("250x100")
master.configure(bg = bg)

Label(master,text="Voice Recorder By Rohit",fg=fg,bg=bg).place(x=60,y=10)

b=Button(master,text="Start", command=Voice_rec).place(x=100,y=50)

mainloop()