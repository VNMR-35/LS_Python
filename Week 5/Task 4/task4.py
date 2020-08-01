from tkinter import *
import pygame
import os

window = Tk()
window.geometry("400x150")
li = Label(window, text = 'Music Player', font = 'times 20')
li.grid(row = 1, column = 1)

pygame.mixer.init()

n = 0

def start_stop():
    global n
    n += 1
    if n==1:
        global song = songs_listbar.get()
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(0)
    elif n%2==0:
        pygame.mixer_music.pause()
    elif n%2!=0:
        pygame.mixer_music.unpause()

def stop():
    global n
    n = 0

def previous():
    global n
    if n==0:
        song = 
    else:

def next():
    song = 

b2 = Button(window, text = 'Pause/Play', width = 20, command = start_stop)
b2.grid(row = 4, column = 1)

b3 = Button(window, text = 'Stop', width = 20, command = stop)
b3.grid(row = 5, column = 1)

b4 = Button(window, text = '<<', width = 10, command = previous)
b4.grid(row = 6, column = 1)

b5 = Button(window, text = '>>', width = 10, command = next)
b5.grid(row = 6, column = 3)

songs_list = os.listdir()
songs_listbar = StringVar(window)
songs_listbar.set("Select Songs")
menu = OptionMenu(window, songs_listbar, *songs_list)
menu.grid(row = 4, column = 4)

window.mainloop()