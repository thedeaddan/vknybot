import vk_api
import time

vk = vk_api.VkApi(token="Token")

FriendsList = vk.method("friends.get")["items"]
for Friend in FriendsList:
	FriendName = vk.method("users.get",{"user_ids":Friend})[0]["first_name"]
	vk.method("messages.send",{"message":"С Новым Годом,"+str(FriendName)+"!🎄\n ВАШЕ ПОЗДРАВЛЕНИЕ","random_id":0,"user_id":Friend})
	print(FriendName+" Поздравлен")
	time.sleep(3)
