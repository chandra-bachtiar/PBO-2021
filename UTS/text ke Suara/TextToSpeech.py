#import
#Sebelum dijalankan pastikan sudah install module gttsnya
# command -> pip install gTTS
from gtts import gTTS
import os

print("===== Program Text to Speech =====")
text = input("Masukan text : ")
bahasa = 'id'
hasil = gTTS(text=text,lang=bahasa,slow='false')

hasil.save('suara.mp3')
os.system('start suara.mp3')