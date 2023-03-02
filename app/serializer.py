from rest_framework import serializers
from .models import Requestcallback


class StockDataSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()



class CallbackRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requestcallback
        fields = ('id','full_name','phone_number','email')   