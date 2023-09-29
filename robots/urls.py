from django.urls import path
from .views import RobotView, download_excel
urlpatterns = [
  path('', RobotView.as_view()),
  path('download_excel/', download_excel, name='download_excel'),

]