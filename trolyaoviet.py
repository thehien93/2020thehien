import speech_recognition
import playsound
import webbrowser

may_nghe = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	
	print("Sen: tớ đang nghe nè")
	audio = may_nghe.record(mic, duration=3)
	may_nghe.adjust_for_ambient_noise(mic) 
	print("Sen:tớ đang suy nghĩ nha ...")
try:
	you = may_nghe.recognize_google(audio,language="vi-VI")

except:
	you == ""
	
print("Bạn: " + you)

if you == "":
	nao_may = "tôi không nghe"
elif "chào" in you:
	nao_may = "Xin chào cậu chủ, chúc cậu chủ một ngày tốt đẹp nha"

elif "Google" in you:
	nao_may = " Đơn giản"	
	url = 'https://www.google.com/'
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	webbrowser.get(chrome_path).open(url)

elif "YouTube" in you:
	nao_may = "Được thôi"	
	url = 'https://www.youtube.com/'
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	webbrowser.get(chrome_path).open(url)
	
elif "Facebook" in you:
	nao_may = "Dễ mà"	
	url = 'https://www.facebook.com/'
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	webbrowser.get(chrome_path).open(url)

elif "tin" in you:
	nao_may = "Dễ mà"	
	url = 'https://thanhnien.vn/'
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	webbrowser.get(chrome_path).open(url)

elif "dịch" in you:
	nao_may = "Dễ ợt"	
	url = 'https://translate.google.com/?hl=vi#view=home&op=translate&sl=en&tl=vi'
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	webbrowser.get(chrome_path).open(url)

else: 
	nao_may = "tớ còn nhỏ nên tớ chưa biết"


print("Sen: " + nao_may)

from gtts import gTTS


output = gTTS(nao_may,lang="vi", slow=False)
output.save("output.mp3")
playsound.playsound('output.mp3', True)
