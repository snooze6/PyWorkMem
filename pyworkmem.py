import random

import logging
from time import sleep

import speech_recognition as sr
from gtts import gTTS
from tempfile import TemporaryFile
import pyglet


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


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.CRITICAL)

    print(gen_vector(5))

    tts = gTTS(text='Hello', lang='en')
    f = TemporaryFile()
    tts.write_to_fp(f)
    f.close()

    music = pyglet.media.load(f, streaming=False)
    sleep(music.duration)
    music.play()
