import gtts

def say(speech):
    tts = gtts.gTTS(speech)
    tts.save("audio.mp3")

say("Hello")