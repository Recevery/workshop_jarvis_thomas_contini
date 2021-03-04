#!/usr/bin/env python3

# from gtts import gTTS
# import datetime
# import pyaudio
# import wave
# import sys

# CHUNK = 1024


# def talk(str):
#     tts = gTTS(str, lang='fr')
#     return tts


# talk(datetime.datetime.today().strftime('%Y-%m-%d')).save('yo.mp3')

# wf = wave.open('yo.mp3', 'rb')
# p = pyaudio.PyAudio()
# stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
#                 channels=wf.getnchannels(),
#                 rate=wf.getframerate(),
#                 output=True)
# data = wf.readframes(CHUNK)
# while len(data) > 0:
#     stream.write(data)
#     data = wf.readframes(CHUNK)
# stream.stop_stream()
# stream.close()
# p.terminate()

import playsound, tempfile, gtts
import datetime, time
import speech_recognition, locale
import wikipedia

Ai_name = "Jarvis"

def say(audio):
    speech = gtts.gTTS(audio, lang="zh-CN")
    tmp = tempfile.NamedTemporaryFile()
    speech.write_to_fp(tmp.file)
    playsound.playsound(tmp.name)
    tmp.close()

def rec_voice():
    say("Je vous ecoute ...")
    rec = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Recording")
        rec.pause_threshold = 1
        rec.energy_threshold = 5400
        voice = rec.listen(source)
        try:
            result = rec.recognize_google(voice, language='fr_FR')
        except:
            say("Je n'ai pas compris Idiot")
            print("No result")
            result = None
        return result

def rec_loop():
    result = None
    while result == None:
        result = rec_voice()
        time.sleep(1)
    return result.lower()

def say_date():
    locale.setlocale(locale.LC_TIME, "fr_FR")
    current_date = datetime.datetime.now().strftime("%A %d %B %Y %H:%M")
    say(current_date)

if __name__ == "__main__":
    say("la pi niche haut loi ninche bas ou libou niche libou niche ni haut ni bas !")
    # while True:
    #     result = rec_loop()
    #     word_array = result.split()
    #     print(word_array)
    #     if (word_array[0] == "fermer"):
    #         exit(0)
    #     elif (word_array[0] == "date"):
    #         say_date()