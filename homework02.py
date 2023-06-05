#Напишите программу, которая позволяет считывать из файла вопрос, отвечать на него и отправлять ответ обратно пользователю.
import telebot


# создаем бота
bot = telebot.TeleBot('TOKEN')

#открытие файла с сообщениями
def open_file(path):
    file=open(path, 'r', encoding='utf-8')
    messages=file.readlines()
    file.close()
    return messages

#отправка ответа
def send_message(user_name, chat_id, date, message):
    bot.send_message(chat_id, f" {user_name} на Ваш запрос от {date} отвечаем:\n\n{message}" )

#работа с сообщениями
def work_with_appeals(messages):
    array=messages
    #разбиваем список на отдельные списки содержащие в себе
    #все данные по каждому запросу(по 4 строки)
    #0 user_name
    #1 дата в строчном виде
    #2 chat_id
    #3 текст сообщения
    #это формат сохранения из предыдущего проекта "Support_telebot"
    new_list = []
    for i in range(0, len(array), 4):
        new_list.append(array[i:i+4])
    #работа оператора с обращениями
    for user in new_list:
        print(f"Имя: {user[0]}\nДата обращения: {user[1]}\n Chat Id пользователя: {user[2]}\nВопрос : {user[3]}\nЖду ответа :\n")
        length=0
        response=""
        while length==0:
            response=input()
            length=len(response)
        send_message(user[0],user[2],user[1],response)
    print("Больше запросов нет.Спасибо.")

work_with_appeals(open_file("support.log"))
