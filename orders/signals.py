from django.db.models.signals import post_save
from django.dispatch import receiver
from robots.models import Robot
from .models import Order
from django.core.mail import send_mail

@receiver(post_save, sender=Order)
def update_order_availability(sender, instance, **kwargs):
    robot_exists = Robot.objects.filter(serial=instance.robot_serial).exists()
    instance.is_available = robot_exists
    Order.objects.filter(pk=instance.pk).update(is_available=robot_exists)

