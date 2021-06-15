from tkinter import *
import time
import pyttsx3
import os
import datetime
import pyautogui
import tkinter as tk
from tkinter import filedialog
import webbrowser
import psutil
import subprocess

# Functions Defines here
# Speak Engine.

def myScreenshot():
        myScreenshot = pyautogui.screenshot()
        file_path = filedialog.asksaveasfilename(defaultextension = '.png')
        myScreenshot.save(file_path)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Time():
	now = datetime.datetime.now()
	chat_window.insert(END, "Current Time is : " + now.strftime("%H:%M:%S") + '\n\n')

def Date():
	now = datetime.datetime.now()
	chat_window.insert(END, "Current Date is : " + now.strftime("%d-%m-%y") + '\n\n')

def BatteryInfo():
	def convertTime(seconds):
	    minutes, seconds = divmod(seconds, 60)
	    hours, minutes = divmod(minutes, 60)
	    return "%d:%02d:%02d"% (hours, minutes, seconds)

	battery = psutil.sensors_battery()
	percent = battery.percent
	time = convertTime(battery.secsleft)

	chat_window.insert(END, "Battery percentage : "  + str(percent)+'%'+ '\n')
	chat_window.insert(END, "Power plugged in : "  + str(battery.power_plugged) + '\n')
	chat_window.insert(END, "Battery left : " + str(time) + '\n\n')

def OpenCamera():
	subprocess.run('start microsoft.windows.camera:', shell=True)
	chat_window.insert(END, "Camera is Opening!" + '\n\n')

def OpenControlPAnel():
	os.system("cmd /c control")
	chat_window.insert(END, "Control Panel is Opening!" + '\n\n')

def OpenSetting():
	subprocess.run('start ms-settings:', shell=True)
	chat_window.insert(END, "Setting is Opening!" + '\n\n')

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir! I Am Your Assistent Root, How May I Help you")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir! I Am Your Assistent Root, How May I Help you!")
    else:
        speak("Good Evening Sir! I Am Your Assistent Root, How May I Help you!")

def reply():
	question = message_window.get()
	question = question.capitalize()
	chat_window.tag_config('justified', justify = RIGHT)
	chat_window.tag_add("right", 1.0, "end")
	chat_window.insert(END, question + "   " + '\n\n', 'justified')
	message_window.delete(0, END)
	func(question)
	chat_window.yview_pickplace("end")


def Quit():
	global root
	root.quit()

def clear():
	chat_window.delete("1.0", "end")

def func(question):
	if(question == 'Hi' or question == 'Hello' or question == 'Hy' or question == 
		'Hey'):
		chat_window.insert(END, "Root : Hello" + '\n\n')

	elif(question == 'Camera' or question == 'Open camera'):
		OpenCamera()

	elif(question == 'Open control panel' or question == 'Control panel'):
		OpenControlPAnel()

	elif(question == 'Open setting' or question == 'Setting'):
		OpenSetting()

	elif(question == 'Time' or question =='What is the time' or question == 
		'Current time' or question == 'Time please'):
		Time()

	elif(question == 'Date' or question == 'What is the date' or question == 
		'Current date' or question == 'Date please'):
		Date()

	elif(question == 'Time and date' or question == 'Date and time' or question ==
		'Time & date' or question == 'Date & time' or question == 
		'What is the date and time' or question == 'What is the time and date'):
		Time()
		Date()

	elif(question == 'Battery info' or question == 'Battery' or question == 
		'Battery details' or question == 'Battery percentage' or question ==
		'Battery percent' or question == 'Battery life' or question == 
		'What is the percentage of battery'):
		BatteryInfo()

	elif(question == 'Who create you'or question == 'Who made you' or question 
		== 'Who built you'):
		chat_window.insert(END, "Root : Amresh Ranjan built me!" + '\n\n')

	elif(question == 'How are you'):
		chat_window.insert(END, "Root : I am Good!" + '\n\n')
		
	elif(question == 'Tell me about yourself'):
		chat_window.insert(END, "Root : I am System Assistent which work on your system functions" + '\n\n')
	
	elif(question == 'Take screenshot' or question == 'Took screenshot' or question ==
		'Screenshot' or question == 'Capture screen' or question == 'Screenshot take'
		or question == 'Save image' or question == 'Save photo' or question == 
		'Take photo' or question == 'Photo save'):
		chat_window.insert(END, "Root : Ok! Please Wait" + '\n\n')
		myScreenshot()
		    
	elif(question == 'Who are you' or question == 'who are you' or question ==
		'whats your name' or question == 'your name' or question == 'what is your name'
		or question == 'What is your name'):
		chat_window.insert(END, "Root : I am Virtual ChatBot Assistance, My Name is Root" 
			+ '\n\n')

	elif(question == 'End' or question == 'Destroy' or question == 'Quit'or 
		question == 'Abourt' or question == 'Bye' or question == 'Good bye' or question 
		== 'Exit' or question == 'By'):
		chat_window.insert(END, "Root : END ALL!" + '\n\n')
		speak("Ok by sir Take care")
		Quit()

	elif(question == 'Open wikipedia' or question == 'Open Wikipedia' or question ==
		'Wikipedia' or question == 'Www.wikipedia.com' or question == 'Wiki' or question
		== 'Open wiki'):
		chat_window.insert(END, "Root : Ok! Opening Wikipedia Please wait" + '\n\n')
		webbrowser.open("www.wikipedia.com")
		speak("Opening Wikipedia Please wait!")

	elif(question == 'Open Google' or question == 'Open google' or question ==
		'google' or question == 'Www.google.com' or question == 'Google' or question
		== 'Open search engine'):
		chat_window.insert(END, "Root : Ok! Opening Google Please wait" + '\n\n')
		webbrowser.open("www.google.com")
		speak("Opening Google Please wait!")

	elif(question == 'Open YouTube' or question == 'Open youtube' or question ==
		'Youtube' or question == 'Www.youtube.com' or question == 'Online vedio'):
		chat_window.insert(END, "Root : Ok! Opening YouTube Please wait" + '\n\n')
		webbrowser.open("www.youtube.com")
		speak("Opening YouTube Please wait")

	elif(question == 'Open Gmail' or question == 'Open gmail' or question ==
		'Gmail' or question == 'Www.gmail.com' or question == 'Mail'):
		chat_window.insert(END, "Root : Ok! Opening Gmail Please wait" + '\n\n')
		webbrowser.open("www.gmail.com")
		speak("Opening Gmail Please wait")

	elif(question == 'Open Github' or question == 'Open github' or question ==
		'Github' or question == 'Www.github.com' or question == 'Open source code'):
		chat_window.insert(END, "Root : Ok! Opening Github Please wait" + '\n\n')
		webbrowser.open("www.github.com")
		speak("Opening Github Please wait")

	else:
		chat_window.insert(END, "Root : Sorry! I can't get it" + '\n\n')


###################################################################################


root = Tk() 	# Object of TK class
root.configure(bg = 'green')
root.title('Advance Chat Bot Application')
root.geometry('400x550') 	# size of window
root.resizable(False, False)

main_menu = Menu(root) 		# Main Menu

main_menu.add_command(label = 'Quit', command = Quit)
main_menu.add_command(label = 'Clear Screen', command = clear)
root.config(menu = main_menu)

scroll_bar = Scrollbar(root)
scroll_bar.place(x = 375, y = 5, height = 385)

chat_window = Text(root, bd = 1, bg = 'black', fg = 'orange',
	font = ('Helvetica 14', 15),
			  width = 50, height = 8, wrap = 'word', yscrollcommand = scroll_bar.set)
chat_window.place(x = 6, y = 6, height = 385, width = 370)

scroll_bar.config(command = chat_window.yview)

message_window = Entry(root, font = ('Helvetica 14', 20,'bold'), bg = 'purple', 
	fg = 'yellow')
message_window.place(x = 10, y = 405, height = 50, width = 380)

src = PhotoImage(file = 'image.png')
button = Button(root, image = src,
				   width = 12, height = 5, font = ('Arial', 20), fg = 'white', 
				   command = reply)
button.place(x = 150, y = 470, height = 70, width = 90)


def click(event):
	button.invoke()

root.bind('<Return>', click)

wish()

root.mainloop()