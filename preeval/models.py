from django.db import models
from django.contrib.auth.models import User

class Level(models.Model):
    description = models.CharField(max_length=60)
    
    def __str__(self):
        return self.description

class Group(models.Model):
    description = models.CharField(max_length=60)
    level = models.ForeignKey(Level)
    
    def __str__(self):
        return self.description

class Student(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=100)
    group = models.ForeignKey(Group)
    
    def __str__(self):
        return ' '.join((self.first_name, self.last_name))

class Teacher(models.Model):
    user = models.ForeignKey(User)
    
    def __str__(self):
        return ' '.join((self.user.first_name, self.user.last_name))
    
class Subject(models.Model):
    description = models.CharField(max_length=60)
    group = models.ForeignKey(Group)
    teacher = models.ForeignKey(Teacher)
    
    def __str__(self):
        return '{} ({})'.format(self.description, self.group)

TERMS = (
    ('1', '1er trimestre'),
    ('2', '2o trimestre'),
    ('3', '3er trimestre')
    )

MARKS = (
    ('1', 'Malo'),
    ('2', 'Regular'),
    ('3', 'Bueno')
    )
    
class Mark(models.Model):
    student = models.ForeignKey(Student)
    subject = models.ForeignKey(Subject)
    term = models.CharField(max_length=1, choices=TERMS)
    study = models.CharField(max_length=1, choices=MARKS)
    work = models.CharField(max_length=1, choices=MARKS)
    attitude = models.CharField(max_length=1, choices=MARKS)

class Remarks(models.Model):
    student = models.ForeignKey(Student)
    subject = models.ForeignKey(Subject)
    term = models.CharField(max_length=1, choices=TERMS)
    remarks = models.TextField()
