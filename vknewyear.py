##### Бот написан @thedeaddan за 20 минут |v2.3
import vk_api #Либа вк апи
import random #Название за себя говорит
import time #Библиотека для задержек
import datetime # Включение времени
import telebot #Бот тг
bot = telebot.TeleBot("токен тг") # Подключение ТГ бота для ошибок
vk = vk_api.VkApi(token="токен вк")#Подключение вк
bot.send_message(895942747,"Бот начал работу!") # Оповещаем создателя о начале работы.
while True: #Проверка времени каждую секунду
	time.sleep(1) #Задержка
	delta = datetime.timedelta(hours=3, minutes=0)# Учёт часового пояса
	t = (datetime.datetime.now(datetime.timezone.utc) + delta)# Создание функции времени
	sec = str(t.strftime("%S"))#Секунды
	nowdata = t.strftime("%d.%m.%Y")#ДМГ
	nowtime = t.strftime("%H:%M")#Время
	hour = t.strftime("%H") # Часы
	minutes = t.strftime("%M") # Минуты
	ostm = 60 - int(minutes)
	osth = 24 - int(hour)
	print("Сейчас "+str(nowtime)+" до нового года "+str(osth)+" ч. "+ str(ostm) +" мин.")
	stop = 0
	#КУСОК КОДА КОТОРЫЙ НУЖЕН ПО ПРИКОЛУ!!! Каждые пол часа присылать сообщение о том сколько осталось до нг времени
	if minutes == "00" and seconds == "00":
		rand = int(random.randint(1,1000)) # Рандомное число для сообщения ( надо )
		vk.method("messages.send",{"random_id":rand,"peer_id":2000000178,"message":"До нового года "+ osth +" ч. !"}) #отправляем сообщение
	if minutes == "30" and seconds == "00":
		rand = int(random.randint(1,1000)) # Рандомное число для сообщения ( надо )
		vk.method("messages.send",{"random_id":rand,"peer_id":2000000178,"message":"До нового года "+ osth +" ч." + ostm + " мин. !"}) #отправляем сообщение
	################################################################################################################
	if nowtime == "00:00" and stop == 0: #Если на часах уже новый год и есть разрешение цикла
		print("Поздравление началось!")
		rand = int(random.randint(1,1000)) # Рандомное число для сообщения ( надо )
		bot.send_message(895942747,"Сообщения начали отправку!") # Оповещаем создателя о начала отправки
		json = vk.method("friends.get",{"user_id":199776748,"order":"id","count":5000,"offset":5,"fields":"name,sex","name_case":"nom"})#Запрос JSON на список друзей и их инфу
		i = 0 # Число цикла
		while i != 89: # Выполняться, пока число цикла не будет равно 89, моё кол-во друзей
			try: #Защита от падений
				response = json.get("items")[i] # Вытаскиваем каждого пользователя из запроса под номером i
				first_name = response.get("first_name") # Вытаскиваем имя пользователя
				ed = response.get("id") # Вытаскиваем ID пользователя
				sex = response.get("sex") # Вытаскиываем пол пользователя, чтоб нормально с ним общаться
				rand = int(random.randint(1,1000)) # Рандомное число для сообщения ( надо )
				if sex == 1: # Если пол женский
					vk.method("messages.send",{"random_id":rand,"peer_id":ed,"message":"🎄Добрый вечер "+first_name+" с Новым Годом! Желаю тебе всего, что тебе желается и всего наилучшего в твоей жизни!🎄"}) #отправляем сообщение
				else:# И если пол мужской
					vk.method("messages.send",{"random_id":rand,"peer_id":ed,"message":"🎄Привет "+first_name+" с Новым Годом! Желаю тебе всего, что тебе желается и всего наилучшего в твоей жизни!🎄"}) # Отправляем сообщение
				i = i+1 # Переход к следующему по списку
				stop = 1 # прекращаем работу цикла
				time.sleep(15) # Ждём 10 сек
			except Exception:
				bot.send_message(895942747,traceback.format_exc())
