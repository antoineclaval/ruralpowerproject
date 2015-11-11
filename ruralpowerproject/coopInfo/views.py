from django.shortcuts import render
from django.views.generic import ListView
from coopInfo.models import Person, State, Cooperative
from coopInfo.serializers import PersonSerializer, StateSerializer, CooperativeSerializer
from rest_framework import generics


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CooperativeList(generics.ListCreateAPIView):
    queryset = Cooperative.objects.all()
    serializer_class = CooperativeSerializer

class CooperativeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cooperative.objects.all()
    serializer_class = CooperativeSerializer

class CooperativeListWeb(ListView):
    model = Cooperative

class PersonListWeb(ListView):
    model = Person