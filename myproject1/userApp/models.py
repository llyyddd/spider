# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class      Aijob(models.Model):
    jobname = models.CharField(max_length=100, blank=True, null=True)
    jobtype = models.CharField(max_length=100, blank=True, null=True)
    pubtime = models.TimeField(blank=True, null=True)
    neednum = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    cptype = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    recruittype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aijob'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Javajob(models.Model):
    jobname = models.CharField(max_length=100, blank=True, null=True)
    jobtype = models.CharField(max_length=100, blank=True, null=True)
    pubtime = models.DateField(blank=True, null=True)
    neednum = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    cptype = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    recruittype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'javajob'


class Job(models.Model):
    jobname = models.CharField(max_length=100, blank=True, null=True)
    jobtype = models.CharField(max_length=100, blank=True, null=True)
    pubtime = models.DateField(blank=True, null=True)
    neednum = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    cptype = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    recruittype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'


class Jobanalyse(models.Model):
    jobname = models.CharField(max_length=100, blank=True, null=True)
    jobtype = models.CharField(max_length=100, blank=True, null=True)
    pubtime = models.TimeField(blank=True, null=True)
    neednum = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    cptype = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=255, blank=True, null=True)
    recruittype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobanalyse'


class Message(models.Model):
    messageid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    concent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class User(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    passworrd = models.CharField(max_length=10, blank=True, null=True)
    telephone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
