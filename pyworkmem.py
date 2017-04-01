import logging
import os
import random
import webbrowser
from abc import abstractmethod
from time import sleep

import speech_recognition as sr
from gtts import gTTS
from mutagen.mp3 import MP3


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
        print("[Sig]: Di algo!")
        audio = r.listen(source)

    string = None

    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        string = r.recognize_google(audio, language='es-ES')
        print("[You]: " + string)
    except sr.UnknownValueError:
        print("[Err]: Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("[Err]: Could not request results from Google Speech Recognition service; {0}".format(e))
    return string


def play(file):
    audio = MP3(file)
    webbrowser.open(file)
    sleep(audio.info.length)


def play_str(string):
    tts = gTTS(text=string, lang='es')
    print('[Bot]: ' + string)
    tts.save('temp.mp3')
    play('temp.mp3')


def introduction():
    string = """
    Hola, y bienvenido a PyWorkMem
    """
    play_str(string)


def test_repeat():
    play_str("Porfavor repita los siguientes vectores en el mismo orden")
    for j in range(3, 9):
        arr = gen_vector(j)
        play_str(' '.join(map(str, arr)))
        play_str('Ahora usted')

        # Listen
        string = recognize_audio()
        if string:
            string.strip().replace(' ', '')
            string = ' '.join(string)
            if string == ' '.join(map(str, arr)):
                play_str('Ha dicho: ' + string + ' y es correcto')
            else:
                play_str('Ha dicho: ' + string + ' y es incorrecto')
        else:
            play_str('No he podido entender lo que ha dicho')


if __name__ == '__main__':
    # introduction()
    test_repeat()

    # play_str('Ahora usted')
    # sleep(2)
    # string = recognize_audio()
    # play_str('Ha dicho: '+string)

    os.remove('temp.mp3')
