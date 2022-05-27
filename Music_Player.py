from pygame import mixer
import pygame
import os
import random


cursor = 0
mixer.init()
def inputManager():
	tempp = input("Drag and Drop a Folder or a Song\n>>> ")
	tempp = tempp.replace("\"","")
	global songsList
	global shuffleList
	# if not os.path.exists(temp) and len(temp) > 1:
	# 	print("invalid directory\n")
	# 	inputManager()
	# elif os.path.isfile(temp) and not temp.endswith(".mp3") and len(temp) > 1:
	# 	print("file type is not supported\n")
	# 	inputManager()


	if os.path.isfile(tempp) and tempp.endswith(".mp3") and len(tempp) > 1: #if input is a song
		temp = tempp
		directory = temp[:-(len(temp) - temp.rfind("\\"))]	# find the song's location so we add it's directory to find other songs in same folder

		songsList = []
		shuffleList = []

		# songsList.append([temp,directory[(directory.rfind("\\") - len(directory)+1):]])
		cursor = 0
		print("Loading...")
		for thePath, folderName, songName in os.walk(directory): # find all the songs with mp3 format in both directorys and suub-directorys
			for songName in [s for s in songName if s.endswith(".mp3")]:
				songsList.append([os.path.join(thePath, songName),songName])

		randomNumber = random.sample(range(0,len(songsList)),len(songsList))
		for i in range(len(songsList)):
			shuffleList.append(randomNumber[i])

		n = songsList.index([temp,temp[(temp.rfind("\\") - len(temp)+1):]]) # to play the Entered song first so it puts it at the begining of the list 
		index0temp = shuffleList[0]
		index0 = shuffleList.index(index0temp)
		indexN = shuffleList.index(n)
		if not index0 == indexN:
			shuffleList[index0],shuffleList[indexN] = shuffleList[indexN], shuffleList[index0]
		mixer.music.stop()
		mixer.music.load(songsList[shuffleList[cursor]][0])
		mixer.music.set_volume(1)
		mixer.music.play()

		return temp


	elif not os.path.isfile(tempp) and os.path.exists and len(tempp) > 1:    # if input is a folder
		temp = tempp
		directory = temp
		songsList = []
		shuffleList = []
		print("Loading...")
		for thePath, folderName, songName in os.walk(directory):
			for songName in [s for s in songName if s.endswith(".mp3")]:
				songsList.append([os.path.join(thePath, songName),songName])

		randomNumber = random.sample(range(0,len(songsList)),len(songsList))
		for i in range(len(songsList)):
			shuffleList.append(randomNumber[i])
		if len(songsList) > 0:
			return directory
		else:
			print("No songs were found\n")
			return inputManager()


	elif tempp == 'r' or tempp == 'R':
		return 'r'
	elif tempp == 'p' or tempp == 'P':
		return 'p'
	elif tempp == 'n' or tempp == 'N' or tempp == "":
		return 'n'
	elif tempp == 'b' or tempp == 'B':
		return 'b'
	elif tempp == 'e' or tempp == 'E':
		return 'e'
	else:# this doesn't work for some reason
		print("Invalid input")
		return inputManager()

directory = inputManager()
if not os.path.isfile(directory) and os.path.exists(directory):# if the first input is folder
	print(str(len(shuffleList)) + " Songs Found")
	mixer.music.stop()
	mixer.music.load(songsList[shuffleList[cursor]][0])
	mixer.music.set_volume(1)
	mixer.music.play()


while mixer.music.get_busy():# this obviesly saying if the player is playing a song then:...
	
	os.system('CLS')
	print("******MENUE********\nP to pause\nR to resume\nE to exit \nN or just press Enter to next\nB to back\n*******************")
	if not len(songsList) == 0:
		print(str(songsList[shuffleList[cursor]][1]) + " is playing")
		control = inputManager()
	else:
		inputManager()

	if os.path.isfile(control) and control.endswith(".mp3"): # if the second input is song
		print("New directory from song registered\n")
		print(str(len(shuffleList)) + " Songs Found")
		cursor = 0
		mixer.music.stop()
		mixer.music.load(songsList[shuffleList[cursor]][0])
		mixer.music.set_volume(1)
		mixer.music.play()

	elif os.path.isfile(control) and not control.endswith(".mp3"):# this is a unsucsessful attempt of mine trying to make a smart move so that when user inputs a valid but epty from mp3 files it says this
		print("Can\'t play this file format")
		inputManager()

	elif os.path.exists(control) and not os.path.isfile(control): # if the second input is folder
		print("\nNew directory from folder registered")
		songsList = []
		shuffleList = []
		print("Loading...")
		for thePath, folderName, songName in os.walk(control):#same shit again
			for songName in [s for s in songName if s.endswith(".mp3")]:
				songsList.append([os.path.join(thePath, songName),songName])

		randomNumber = random.sample(range(0,len(songsList)),len(songsList))
		for i in range(len(songsList)):
			shuffleList.append(randomNumber[i])
		print(str(len(shuffleList)) + " Songs Found")

		if len(songsList) > 0:
			cursor = 0
			mixer.music.stop()
			mixer.music.load(songsList[shuffleList[cursor]][0])
			mixer.music.set_volume(1)
			mixer.music.play()
		else:
			print("no songs were found\n")
			pass


	elif control == 'p':
		mixer.music.pause()

	elif control == 'r':
		mixer.music.unpause()

	elif control == 'n':
		cursor += 1
		if cursor < len(shuffleList)-1:
			if not len(songsList) == 0:
				mixer.music.stop()
				mixer.music.load(songsList[shuffleList[cursor]][0])
				mixer.music.set_volume(1)
				mixer.music.play()
			else :
				pass
		else:
			if not len(songsList) == 0:
				cursor = 0
				mixer.music.stop()
				mixer.music.load(songsList[shuffleList[cursor]][0])
				mixer.music.set_volume(1)
				mixer.music.play()
			else :
				pass

	elif control == 'b':
		cursor -= 1
		if cursor > 0:
			if not len(songsList) == 0:
				mixer.music.stop()
				mixer.music.load(songsList[shuffleList[cursor]][0])
				mixer.music.set_volume(1)
				mixer.music.play()
			else :
				pass
		else:
			if not len(songsList) == 0:
				cursor = len(shuffleList)-1
				mixer.music.stop()
				mixer.music.load(songsList[shuffleList[cursor]][0])
				mixer.music.set_volume(1)
				mixer.music.play()
			else :
				pass

	elif control == 'e':
		mixer.music.stop()
		break
	else :
		inputManager()