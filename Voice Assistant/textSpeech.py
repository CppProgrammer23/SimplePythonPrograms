from gtts import gTTS
import playsound
import speech_recognition as sr

def talk(txt):
    tts=gTTS(text=txt,lang='en')
    tts.save('test.mp3')
    playsound.playsound('test.mp3')

def getAudio():
    a=sr.Recognizer()
    with sr.Microphone() as s:
        audio = a.listen(s)
        said=''
        try:
            said=a.recognize_google(audio)
            print(said)
        except Exception as e:
            print(e)
    return said

t=getAudio()
if 'hello' in t:
    talk('hello idris')
