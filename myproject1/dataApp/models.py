# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Djob(models.Model):
    jobname = models.CharField(max_length=100, blank=True, null=True)
    jobtype = models.CharField(max_length=100, blank=True, null=True)
    pubtime = models.CharField(max_length=100, blank=True, null=True)
    neednum = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    cptype = models.CharField(max_length=100, blank=True, null=True)
    recruittype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djob'


class Jjob(models.Model):
    jobname = models.CharField(max_length=100, blank=True, null=True)
    jobtype = models.CharField(max_length=100, blank=True, null=True)
    pubtime = models.CharField(max_length=100, blank=True, null=True)
    neednum = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    cptype = models.CharField(max_length=100, blank=True, null=True)
    recruittype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjob'


class Jjobb(models.Model):
    jobname = models.CharField(max_length=100, blank=True, null=True)
    jobtype = models.CharField(max_length=100, blank=True, null=True)
    pubtime = models.CharField(max_length=11, blank=True, null=True)
    neednum = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    cptype = models.CharField(max_length=100, blank=True, null=True)
    recruittype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jjobb'


class Job(models.Model):
    jobname = models.CharField(max_length=100, blank=True, null=True)
    jobtype = models.CharField(max_length=100, blank=True, null=True)
    pubtime = models.CharField(max_length=10, blank=True, null=True)
    neednum = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    cptype = models.CharField(max_length=100, blank=True, null=True)
    recruittype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'


class Message(models.Model):
    messageid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    concent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Pjob(models.Model):
    jobname = models.CharField(max_length=100, blank=True, null=True)
    jobtype = models.CharField(max_length=100, blank=True, null=True)
    pubtime = models.CharField(max_length=100, blank=True, null=True)
    neednum = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    cptype = models.CharField(max_length=100, blank=True, null=True)
    recruittype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pjob'


class Rjob(models.Model):
    jobname = models.CharField(max_length=100, blank=True, null=True)
    jobtype = models.CharField(max_length=100, blank=True, null=True)
    pubtime = models.CharField(max_length=100, blank=True, null=True)
    neednum = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    cptype = models.CharField(max_length=100, blank=True, null=True)
    recruittype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rjob'


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    passworrd = models.CharField(max_length=10, blank=True, null=True)
    telephone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
