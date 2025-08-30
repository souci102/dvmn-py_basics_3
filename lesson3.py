import smtplib
import os
from dotenv import load_dotenv


load_dotenv()


addres_sender="Souci2003@yandex.ru"
addres_receiver="dima.909.dima@gmail.com"
subject="Приглашение!"

PASSWORD=os.getenv('PASSWORD')
LOGGIN=os.getenv('LOGGIN')

#pasword="mkseenhyhbxqqwtj"
#loggin="Souci2003"

letter = """From: {0}
To: {1}
Subject: {2}
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

letter=letter.replace("%website%", "https://dvmn.org/profession-ref-program/zerg____rush/13JQf/").replace("%friend_name%", "СТЕПАШКА-КАКАШКА").replace("%my_name%", "СТЕПАНИДЗЕ")
letter=letter.format(addres_sender,addres_receiver, subject)
letter=letter.encode("UTF-8")

#print(letter)
server=smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(LOGGIN, PASSWORD)
server.sendmail(addres_sender, addres_receiver, letter)
server.quit()

