from gtts import gTTS

testfile = "/tmp/temp.mp3"

blabla = ("аксес грантэд, Дэвид!")
tts = gTTS(text=blabla, lang='ru')
tts.save(testfile)