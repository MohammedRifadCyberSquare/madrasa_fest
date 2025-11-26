from django.db import models
from django.utils import timezone

class MadrasaAdmin(models.Model):
    user_name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 100)
    class Meta:
        db_table = "db_admin"


# models.py
from django.db import models

class Participant(models.Model):
    madrasa_name = models.CharField(max_length=30)
    cls_madrasa = models.IntegerField()
    student_name = models.CharField(max_length=40)
    father_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=20)
    dob = models.CharField(max_length=50)  # keep as string for now
    gender = models.CharField(max_length=15)
    category = models.CharField(max_length=80)
    chest_no = models.IntegerField()
    house_name = models.CharField(max_length=20)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student_name} ({self.madrasa_name})"


class ParticipantItem(models.Model):
    participant = models.ForeignKey(Participant, related_name='items', on_delete=models.CASCADE)
    item = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.item} for {self.participant.student_name}"
