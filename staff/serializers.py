from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    employee_id = serializers.CharField()
    name = serializers.CharField()
    department = serializers.CharField()
    salary = serializers.IntegerField()
    joining_date = serializers.DateField()
    skills = serializers.ListField(child=serializers.CharField())
