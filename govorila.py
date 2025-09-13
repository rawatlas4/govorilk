import speech_recognition as sr#імпортуємо бібліотеку#розпізнавання мови
import subprocess#відкриття програм
import webbrowser#відкриття сайтів
import pyowm#погода
owm = pyowm.OWM('5817d6a145c443107efc34417e35c2ac')#створюємо апі ключ
end_program = True
raspoznovatel = sr.Recognizer()#створюємо об'єкт який відповідає за розпізнавання мови
def vvod_golosa():#запис аудио
    with sr.Microphone() as source:# используем микрофон как источник звука
        print("слухаю")
        audio = raspoznovatel.listen(source)#слушаем звук с микро
    return audio#возвращаем аудио запись
def iz_golosa_v_tekst(audio):#розпізнаввая мови
    try:
        #преобразуем речь в текст с помощью google speach recognition language какой язик будет розпозновать
        text = raspoznovatel.recognize_google(audio,language = 'uk-UK')
        print("Ви сказали" + text)
    except:
        text = ""
        print("моя твоя не понимать")
    return text#возвращаем текст
def golosova_comanda(text):
    global end_program
    if "привіт" in text.lower():
        print("хелоу")
    elif "как дела" in text.lower():
        print("cупер,а у тебя?")
    elif "пока" in text.lower():
        end_program=False
    elif "калькулятор" in text.lower():
        subprocess.call(['calc'])
    elif "roblox" in text.lower() or "роблокс" in text.lower():
        subprocess.call(["C:/Users/krom/AppData/Local/Roblox/Versions/version-8afc5a7d5e894d22/RobloxPlayerBeta.exe"])
    elif "steam" in text.lower():
        subprocess.call(["C:/Program Files (x86)/Steam/steam.exe"])
    elif "google" in text.lower():
        webbrowser.open(f"https://www.google.com/search?q={text.lower()[7:]}&oq=&gs_lcrp=EgZjaHJvbWUqDwgCECMYJxjqAhiABBiKBTIPCAAQIxgnGOoCGIAEGIoFMg8IARAjGCcY6gIYgAQYigUyDwgCECMYJxjqAhiABBiKBTIPCAMQIxgnGOoCGIAEGIoFMg8IBBAjGCcY6gIYgAQYigUyDwgFECMYJxjqAhiABBiKBTIJCAYQIxgnGOoCMg8IBxAjGCcY6gIYgAQYigXSAQkyMzE1OWowajeoAgiwAgHxBUL8YBI5bo9y&sourceid=chrome&ie=UTF-8")
    elif "telegram" in text.lower():
        subprocess.call(["C:/Users/krom/AppData/Roaming/Telegram Desktop/Telegram.exe"])
    elif "щоденник" in text.lower():
        webbrowser.open("https://nz.ua/dashboard/news")
    elif "macro" in text.lower() or "макро" in text.lower():
        subprocess.call(["C:/Users/krom/Desktop/ДЗ/tinytask.exe"])
    elif "youtube" in text.lower():
        webbrowser.open(f"https://www.youtube.com/results?search_query={text.lower()[7:]}")

    elif "погода" in text.lower():
        place = text.lower()[7:]#беремо назву міста
        observation = owm.weather_manager().weather_at_place(place)
        location = observation.location
        weather = observation.weather
        weather = "Температура" + str(int(weather.temperature('celsius')['temp']))#отримаємо температуру в градусах цельсія
        print(weather)
    else:
        print("моя втоя не понимать")
def main():#функція main, щоб запустити створені раніше функції.
    while end_program:
        audio = vvod_golosa()
        text = iz_golosa_v_tekst(audio)
        text = golosova_comanda(text)
if __name__ == "__main__":#точка входа в програму
    main()