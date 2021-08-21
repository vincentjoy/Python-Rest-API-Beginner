from rest_framework import serializers

class HelloSerailizer(serializers.Serializer):
    """Serailizers a name field for testing our API view"""
    name = serializers.CharField(max_length=10)