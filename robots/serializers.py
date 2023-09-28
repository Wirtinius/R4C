from rest_framework.serializers import ModelSerializer
from .models import Robot
from rest_framework import serializers

class RobotSerializer(ModelSerializer):
  class Meta:
    model = Robot
    fields = '__all__'

  def validate(self, data):
    allowed_models = ["R2", "13", "X5"]
    if data['model'] not in allowed_models:
      raise serializers.ValidationError("Недопустимая модель")
    return data