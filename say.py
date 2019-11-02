from gtts import gTTS



def sayV(message):
    f = open("text.txt", "w")
    f.write(message)
    f.close()

    mp3_name = "1.ogg"

    f = open("text.txt", "r")
    ss = f.readline()

    tts = gTTS(text=ss, lang='ru')
    tts.save(mp3_name)
