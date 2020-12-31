import vk_api #Либа вк апи
import random #Название за себя говорит
import time #Библиотека для задержек
import datetime # Включение времени
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
	if nowtime == "00:00" and stop == 0: #Если на часах уже новый год и есть разрешение цикла
		vk = vk_api.VkApi(token="ur token")#Подключение вк
		json = vk.method("friends.get",{"user_id":199776748,"order":"id","count":5000,"offset":5,"fields":"name,sex","name_case":"nom"})#Запрос JSON на список друзей и их инфу
		i = 0 # Число цикла
		while i != 89: # Выполняться, пока число цикла не будет равно 89, моё кол-во друзей
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
