from gtts import gTTS
import os

text = 'Press 1'
language = 'en'
speech = gTTS(text=text, lang=language, slow=False)
speech.save('text.mp3')

# os.system('start text.mp3')
