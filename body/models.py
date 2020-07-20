from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField(default=0)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    user_type = models.IntegerField(choices=((1, ("Member")),(2, ("Trainer"))),default=1)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    trainer= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name="trainers")
    name = models.CharField(max_length=20,default=True)
    phone = models.IntegerField(default=0)
    age= models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(default=1,max_length=1, choices=GENDER_CHOICES)
    experience=models.IntegerField()
    skills=models.TextField(max_length=150)
    def __str__(self):
        return self.name

class Member(models.Model):
    member= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="member")
    trainer= models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True, related_name="trainers")
    name = models.CharField(max_length=20,default=True)
    phone = models.IntegerField(default=0)
    age= models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(default=1,max_length=1, choices=GENDER_CHOICES)
    height=models.IntegerField()
    weight=models.IntegerField()
    def __str__(self):
        return self.gender

class Workout(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="pics/", null=True, blank=True)
    def __str__(self):
        return self.name

class Session(models.Model):
    member= models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    trainer= models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)
    name = models.ForeignKey(Workout, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(default=1)
    time= models.TimeField(default=1)
    duration = models.IntegerField()
    def __str__(self):
        return self.name.name
