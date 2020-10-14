from gtts import gTTS
import librosa
import soundfile as sf
import os

print("TTS starting!")

SAMPLE_RATE = 44100
LOW_FACTOR = 1.42

text = 'Press 1'
language = 'en'
speech = gTTS(text=text, lang=language, slow=False)
speech.save('text.mp3')
# os.system('start text.mp3')

# y, sr = librosa.load("text.mp3")
# data = librosa.resample(y, sr, SAMPLE_RATE)
# librosa.output.write_wav('placeholder.wav', data, SAMPLE_RATE)
# d, sr = sf.read('placeholder.wav')
# sf.write('placeholder.wav', d, sr)

y, sr = librosa.load("text.mp3")
lowData = librosa.resample(y, sr, SAMPLE_RATE * LOW_FACTOR)
librosa.output.write_wav('lowPlaceholder.wav', lowData, SAMPLE_RATE)
d, sr = sf.read('lowPlaceholder.wav')
sf.write('lowPlaceholder.wav', d, sr)
