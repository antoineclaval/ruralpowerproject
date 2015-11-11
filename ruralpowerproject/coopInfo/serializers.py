from django.forms import widgets
from rest_framework import serializers
from coopInfo.models import Person, State, Cooperative

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'coopId', 'name', 'ethnicity', 'distric', 'title', 'inBoardSince', 'picture', 'numberOfYearsInBoard')

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name')

class CooperativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cooperative
        fields = ('id', 'stateId', 'name', 'acronym', 'streetAddress', 'website', 'mailAddress', 
            'email', 'phone', 'countiesServed', 'consumers', 'montlyMeeting', 'annualMeeting', 
        	'numberOfEmployees', 'milesOfLines', 'nextElectionTerms', 'servingTime', 'bylaws', 'is990present')

