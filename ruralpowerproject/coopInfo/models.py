from django.db import models
from django_resized import ResizedImageField
from dateutil.relativedelta import relativedelta
from django.utils import timezone

class State(models.Model):
    name = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Cooperative(models.Model):
    stateId = models.ForeignKey(State)
    name = models.CharField(max_length=50)
    acronym = models.CharField(max_length=6, blank=True)
    streetAddress = models.CharField(max_length=150, verbose_name='street address', blank=True)
    website = models.CharField(max_length=255, unique=True, blank=True)
    mailAddress = models.CharField(max_length=80, verbose_name='mail address', blank=True)
    email = models.CharField(max_length=60, blank=True)
    phone = models.CharField(max_length=70, blank=True)
    countiesServed =  models.CharField(max_length=500, verbose_name='counties served', blank=True)
    consumers = models.IntegerField(default=0, null=True, verbose_name='number of consumers', blank=True)
    montlyMeeting = models.CharField(max_length=500, verbose_name='info about montly meeting', blank=True)
    annualMeeting = models.CharField(max_length=500, verbose_name='info about annual meeting', blank=True)
    numberOfEmployees = models.IntegerField(default=0, null=True, verbose_name='number of employees', blank=True)
    milesOfLines = models.IntegerField(default=0, null=True, verbose_name='miles of electric lines', blank=True)
    nextElectionTerms = models.CharField(max_length=60, verbose_name='next election', blank=True)
    servingTime = models.CharField(max_length=50, verbose_name='serving time', blank=True)
    bylaws = models.CharField(max_length=255, blank=True)
    is990present = models.BooleanField(default=False, blank=True)

    def __unicode__(self):
        return self.name


def content_file_name(instance, filename):
    return '/'.join(['persons', ''.join(e for e in instance.name if e.isalnum()) + "-" + str(instance.coopId.id) + ".jpg"])

class Person(models.Model):

    coopId = models.ForeignKey(Cooperative)
    name = models.CharField(max_length=50)
    ethnicity = models.CharField(max_length=10, blank=True)
    distric = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=20, blank=True)
    inBoardSince = models.DateTimeField(null=True, verbose_name='in board since', blank=True)
    picture = ResizedImageField(size=[120, 150],upload_to=content_file_name, default='/media/persons/default.jpg')
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))

    def numberOfYearsInBoard(self):
        return relativedelta(timezone.now(), self.inBoardSince).years

    def __unicode__(self):
        return self.name