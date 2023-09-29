from rest_framework import generics
from .models import Robot
from .serializers import RobotSerializer
from .excel import create_excel
from django.http import FileResponse, HttpResponse

class RobotView(generics.CreateAPIView):
  queryset = Robot.objects.all()
  serializer_class = RobotSerializer


def download_excel(request):
  file_path = create_excel()
  if file_path:
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    response['Content-Disposition'] = f'attachment; filename="robot_production_report.xlsx"'
    # os.remove(file_path)
    return response
