#coding:utf-8
from __future__ import unicode_literals

from django.db import models

class hosts(models.Model):
    hostid=models.PositiveSmallIntegerField(primary_key=True)
    sn=models.CharField(max_length=20)
    brand=models.CharField(max_length=20) #add
    hostname=models.CharField(max_length=50)
    #productdate=models.DateField()
    updatedate=models.DateField(auto_now=True)
    statusid=models.PositiveSmallIntegerField()
    regionid=models.PositiveSmallIntegerField()
    envid=models.PositiveSmallIntegerField()
    cpuid=models.PositiveSmallIntegerField()
    memid=models.PositiveSmallIntegerField()

class status(models.Model):
    statusid=models.PositiveSmallIntegerField(primary_key=True)
    status=models.CharField(max_length=10)

class regions(models.Model):
    regionid=models.PositiveSmallIntegerField(primary_key=True)
    region=models.CharField(max_length=10)

class envs(models.Model):
    envid=models.PositiveSmallIntegerField(primary_key=True)
    env=models.CharField(max_length=10)

class cpus(models.Model):
    cpuid=models.PositiveSmallIntegerField(primary_key=True)
    cpuname=models.CharField(max_length=50)
    vcpus=models.PositiveSmallIntegerField()
    
class memory(models.Model):
    memid=models.PositiveSmallIntegerField(primary_key=True)
    capacity=models.PositiveSmallIntegerField()
    #DDR
    #mhz=models.PositiveSmallIntegerField()

class net(models.Model):
    ipid= models.AutoField(primary_key=True)
    hostid=models.PositiveSmallIntegerField()
    ip=models.GenericIPAddressField()
    nic=models.CharField(max_length=10)
    mac=models.CharField(max_length=20)
    
class services(models.Model):
    serviceid=models.PositiveSmallIntegerField(primary_key=True)
    service=models.CharField(max_length=20)

class engineer(models.Model):
    engineerid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=10)
    phone=models.PositiveSmallIntegerField()
    role=models.CharField(max_length=10)
    status=models.PositiveSmallIntegerField()

class service_engineer(models.Model):
    service_engineerid=models.PositiveSmallIntegerField(primary_key=True)
    serviceid=models.PositiveSmallIntegerField()
    engineerid=models.PositiveSmallIntegerField()

class disks(models.Model):
    diskid=models.PositiveSmallIntegerField()
    space=models.PositiveSmallIntegerField()
    brand=models.CharField(max_length=15)
    model=models.CharField(max_length=20)

class hostsdisks(models.Model):
    hostsdisksid=models.AutoField(primary_key=True)
    hostid=models.PositiveSmallIntegerField()
    diskid=models.PositiveSmallIntegerField()
