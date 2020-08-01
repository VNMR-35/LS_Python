import speech_recognition as sr
#import pyttsx3

r = sr.Recognizer()

def recognize(src):
    try:
        with sr.AudioFile(src) as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source = source)
            text = r.recognize_google(audio)
            doc = open('task1.3.txt', 'a')
            doc.write(text + '\n')
            doc.close()
    
    except sr.RequestError as e: 
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured")

recognize('BarneyStinson.wav')
recognize('task1.3.wav')