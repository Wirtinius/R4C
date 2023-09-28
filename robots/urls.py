from django.urls import path
from .views import RobotView
urlpatterns = [
  path('', RobotView.as_view())
]