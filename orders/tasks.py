from orders.models import Order
from robots.models import Robot
from celery import shared_task
import smtplib


@shared_task
def notify_customer_on_robot_availability():
  orders = Order.objects.filter(is_available=False)
  print(orders)
  for order in orders:
    robot = Robot.objects.filter(serial=order.robot_serial)
    if robot.exists():
      order.is_available = True
      order.save()
      password = "dyppgtsddlebavaa"
      sender_email = "serfikhad333@gmail.com"
      receiver = order.customer.email
      body = f"Добрый день! Недавно вы интересовались нашим роботом модели {robot[0].model}, версии {robot[0].version}. Этот робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами"

      smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
      smtpObj.starttls()
      smtpObj.login(sender_email, password)
      smtpObj.sendmail(sender_email, receiver, body.encode('utf-8'))
      smtpObj.quit()
  else:
    print("ammamama")