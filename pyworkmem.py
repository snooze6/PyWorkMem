import logging
import os
import random
import webbrowser
from abc import abstractmethod
from time import sleep

import speech_recognition as sr
from gtts import gTTS


def gen_vector(length):
    if length >= 10:
        raise Exception('El límite es 10')
    else:
        arr = list(range(1, 10))
        err = []
        for i in range(0, length):
            n = random.choice(arr)
            err.append(n)
            arr.remove(n)
        return err


def recognize_audio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Di algo!")
        audio = r.listen(source)

    string = None

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        string = r.recognize_google(audio, language='es-ES')
        print("Has dicho: " + string)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return string


def play(file):
    webbrowser.open(file)


def play_str(string):
    tts = gTTS(text=string, lang='es')
    tts.save('temp.mp3')
    play('temp.mp3')


def introduction():
    string = """
    Hola, y bienvenido a PyWorkMem
    """
    play_str(string)


def test_repeat():
    play_str("Porfavor repita los siguientes vectores en el mismo orden")
    for j in range(3, 8):
        arr = gen_vector(j)
        sleep(5)
        play_str(' '.join(map(str, arr)))
        sleep(j-1)
        # play_str('Ahora usted')
        # sleep(j-1)
        # string = recognize_audio()
        # play_str('Ha dicho: '+string)
        print(' '.join(map(str, arr)))


if __name__ == '__main__':
    # introduction()
    test_repeat()
    os.remove('temp.mp3')
