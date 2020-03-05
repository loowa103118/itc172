

from django.db import models
from django.contrib.auth.models import User

class Meeting (models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    meetinglocation=models.CharField(max_length=255)
    meetingagenda=models.TextField()

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'  

class MeetingMinutes(models.Model):
    MeetingMinutesTitle=models.CharField(max_length=255)
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    meetingattendance=models.ManyToManyField(User)

    def __str__(self):
        return self.MeetingMinutesTitle

    class meta:
        db_table='minutes'   

class Resource(models.Model):
    ResourceName=models.CharField(max_length=255)  
    resourcetype=models.CharField(max_length=255)
    resourceurl=models.URLField()
    resourcedateentered=models.DateField()  
    resourceid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)  

    def __str__(self):
        return self.ResourceName 
    class meta:
        db_table='minutes' 

class Event(models.Model):
     EventTitle=models.CharField(max_length=255)
     eventlocation=models.CharField(max_length=255) 
     eventdate=models.DateField()  
     eventtime=models.TimeField()
     eventdescription=models.TextField()
     eventuserid=models.ForeignKey(User, on_delete=models.DO_NOTHING)  


     def __str__(self): 
        return self.EventTitle

     class meta:
         db_table='minutes'                
