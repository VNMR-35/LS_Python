from gtts import gTTS

text_open = open('task1.4.txt')
text = text_open.read()
text_open.close()

speechObj = gTTS(text=text)

speechObj.save("task1.4.mp3")