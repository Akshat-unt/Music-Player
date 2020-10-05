from tkinter import *
from tkinter import filedialog
from pygame import mixer
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

class MusicPlayer:
	def __init__(self, window ):
		window.geometry('325x100'); window.title('Music Player'); window.resizable(0,0)
		Load = Button(window, text = 'LOAD', width = 10, font = ('Orbitron', 10), command = self.load)
		Play = Button(window, text = 'PLAY', width = 10, font = ('Orbitron', 10), command = self.play)
		Pause= Button(window, text = 'PAUSE', width = 10, font = ('Orbitron', 10), command = self.pause)
		Stop = Button(window, text = 'STOP', width = 10, font = ('Orbitron', 10), command = self.stop)
		Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=110,y=60)
		self.music_file = False
		self.playing_state = False
	def load(self):
		speak("please select a music to play")
		self.music_file = filedialog.askopenfilename()

	def play(self):
		speak("playing")
		if self.music_file:
			mixer.init()
			mixer.music.load(self.music_file)
			mixer.music.play()
	def pause(self):
		speak("pausing")
		if not self.playing_state:
			mixer.music.pause()
			self.playing_state=True
		else:
			mixer.music.unpause()
			self.playing_state=False
	def stop(self):
		speak("see you next time")
		mixer.music.stop()

root=Tk()
app=MusicPlayer(root)
root.mainloop()