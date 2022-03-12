import requests
import os
import time
import json
import urllib
import sys
print("IAP - Info About People")
def loading():
	time.sleep(5)
	os.system("cls")
	print("Loading...")
	time.sleep(0.5)
	os.system("cls")
	print("Loading/..")
	time.sleep(0.5)
	os.system("cls")
	print("Loading|..")
	time.sleep(0.5)
	os.system("cls")
	print("Loading\..")
	time.sleep(0.5)
	os.system("cls")
	print("Loading./.")
	time.sleep(0.5)
	os.system("cls")
	print("Loading.|.")
	time.sleep(0.5)
	os.system("cls")
	print("Loading.\.")
	time.sleep(0.5)
	os.system("cls")
	print("Loading../")
	time.sleep(0.5)
	os.system("cls")
	print("Loading..|")
	time.sleep(1)
	os.system("cls")
	print("Upload Successful")
	os.system("cls")

loading()

def menu():
	print("1.Информация по номеру\n2.Информация по фото\n3.Виртуальный номер\n4.Звонок с номера ")
	select_menu = int(input("Выберите пункт: "))
	if select_menu == 1:
		#http://phoneradar.ru/phone/
		key = "6b3fbb3a6920b208b3a32140a0f5392e"
		inumber = str(input("Введите номер: +7"))
		number = inumber
		api = "http://apilayer.net/api/validate?access_key=" + key + "&number=" + number + "&country_code=RU&format=1"
		output = requests.get(api)
		content = output.text
		obj = json.loads(content)
		country_name = obj['country_name']
		location = obj['location']
		carrier = obj['carrier']
		print("Страна:", country_name)
		print("Область:", location)
		print("Оператор:", carrier)

	elif select_menu == 2:
		print("https://search4faces.com/")

	elif select_menu == 3:
		vnumber = int(input("Введите желаемый номер: "))
		vfamily = str(input("Введите фамилию для данного номера: "))
		vname = str(input("Введите имя для данного номера: "))
		votchestvo = str(input("Введите отчество для данного номера: "))

	elif select_menu == 4:
		cnumber = int(input("Введите номер с которого будет звонок: "))
		numbercall = int(input("Введите номер на который будет совершён звонок: "))

	else:
		print("Вы выбрали неверный пункт!")
menu()
