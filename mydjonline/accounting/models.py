from django.db import models
from django.utils import timezone
import time,datetime

# Create your models here.
#组织信息表
class Agency_t(models.Model):
	name = models.CharField(max_length=128)
	def __str__(self):
		return self.name

#线路报价表 remark备注；detail详细报价
class Line_Price_t(models.Model):
	name = models.CharField(max_length=64)
	remark = models.CharField(max_length=128,blank=True)
	detail = models.TextField(max_length=2048, blank=True)
	local_agency_fk =models.ForeignKey(Agency_t,on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.name


#参考报价表 
# level挡位；kind类型，price报价，chose是否为默认报价，line_price_fk所属线路报价单
class Ref_Price_t(models.Model):
	level = models.IntegerField()
	kind = models.CharField(max_length=64)
	price = models.FloatField(default=0)
	chose = models.BooleanField(default=False)
	line_price_fk = models.ForeignKey(Line_Price_t, on_delete=models.DO_NOTHING)
	def __str__(self):
		return self.kind

#出团申请单
#data出团日期；loca_agency_fk地接社名称；angency_fk组团社名称；line_name_fk线路名称
class Application_t(models.Model):
	date = models.DateTimeField(default=datetime.datetime.now())
	local_agency_fk = models.ForeignKey(Agency_t,related_name='local',on_delete=models.DO_NOTHING)
	agency_fk = models.ForeignKey(Agency_t,on_delete=models.DO_NOTHING)
	line_name_fk = models.ForeignKey(Line_Price_t,on_delete=models.DO_NOTHING)
	def_price_fk = models.ForeignKey(Ref_Price_t, on_delete=models.DO_NOTHING)
	def __str__(self):
		return self.agency_fk.name+'-'+self.line_name_fk.name+'-'+str(self.date)


class Tourist_t(models.Model):#游客表
	name = models.CharField(max_length=64)
	amount = models.IntegerField(default=1)#数量
	application_fk = models.ForeignKey(Application_t,on_delete=models.DO_NOTHING)
	ref_price_fk = models.ForeignKey(Ref_Price_t,on_delete=models.DO_NOTHING)#参考报价
	fix_price = models.FloatField(default=0)#修正报价
	final_price= models.FloatField(default=0)#最终报价
	fix_remark = models.CharField(max_length=128, blank=True)#修正备注
	trans_price = models.FloatField(default=0)#调拨报价
	trans_remark =models.CharField(max_length=128, blank=True)#调拨备注
	trans_agency = models.CharField(max_length=128,default='0')
	#调拨单位
	agent_price = models.FloatField(default=0)#代收金额
	agent_remark = models.CharField(max_length=128,blank=True)#代收备注
	def __str__(self):
		return self.name	

class Settlement_t(models.Model):#结算表
	price = models.FloatField()#结算金额
	kind = models.CharField(max_length=64)#类型
	rec_agency_fk = models.ForeignKey(Agency_t,
	                related_name='rec_agency',on_delete=models.DO_NOTHING)#收款方
	pay_agency_fk = models.ForeignKey(Agency_t,on_delete=models.DO_NOTHING)#付款方
	application_t =models.OneToOneField(Application_t,on_delete=models.DO_NOTHING)#所属出团申请单
	def __str__(self):
		return self.application_t.name+'-'+self.rec_angecy_fk.name+'-'+self.pay_angecy_fk.name+'-'+self.kind


