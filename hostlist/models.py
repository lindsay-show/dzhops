# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class CmccUser(models.Model):
    username = models.CharField(max_length=30, blank=True, verbose_name=u'用户名')
    engineer = models.CharField(max_length=30, blank=True, verbose_name=u'维护人员')

    def __unicode__(self):
        return u'%s %s' %(self.username, self.engineer)

class DataCenter(models.Model):
    dcen = models.CharField(max_length=30, blank=True, verbose_name=u'机房简称')
    dccn = models.CharField(max_length=30, blank=True, verbose_name=u'机房全称')

    def __unicode__(self):
        return u'%s %s' %(self.dcen, self.dccn)

'''class NetworkOperator(models.Model):
    noen = models.CharField(max_length=30, blank=True, verbose_name=u'运营商简称')
    nocn = models.CharField(max_length=30, blank=True, verbose_name=u'运营商全称')

    def __unicode__(self):
        return u'%s %s' %(self.noen, self.nocn)

class ProvinceArea(models.Model):
    paen = models.CharField(max_length=30, blank=True, verbose_name=u'省份地区简称')
    pacn = models.CharField(max_length=30, blank=True, verbose_name=u'省份地区全称')

    def __unicode__(self):
        return u'%s %s' %(self.paen, self.pacn)'''
class Catagory(models.Model):
    catagoryen = models.CharField(max_length=30, blank=True, verbose_name=u'环境类别')
    catagorycn = models.CharField(max_length=30, blank=True, verbose_name=u'类别全称')

    def __unicode__(self):
        return u'%s %s' %(self.catagoryen, self.catagorycn)

class HostList(models.Model):
    dccn = models.CharField(max_length=30, blank=True, verbose_name=u'机房全称')
    catagorycn = models.CharField(max_length=30, blank=True, verbose_name=u'环境类别')
    privateip = models.CharField(max_length=15,  blank=True,verbose_name=u'内网地址')
    publicip = models.CharField(max_length=15,  blank=True,verbose_name=u'外网地址')
    hostname = models.CharField(max_length=30, verbose_name=u'主机名')
    minionid = models.CharField(max_length=60, verbose_name=u'MinionID')
    engineer = models.CharField(max_length=30, blank=True, verbose_name=u'维护人员')
    engineer = models.ForeignKey(CmccUser, related_name='CmccUser_hostlist')
    minionidip = models.CharField(max_length=15,  blank=True,verbose_name=u'MinionID中的IP地址')
    note = models.TextField(max_length=200, blank=True, verbose_name=u'备注')

    def __unicode__(self):
        return u'%s %s %s %s %s' %(self.hostname, self.privateip, self.catagorycn, self.dccn,self.engineer)
    class Meta:
        ordering = ['minionid']
