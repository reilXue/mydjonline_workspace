import os,django,time,datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mydjonline.settings')
django.setup()
from accounting.models import Agency_t,Line_Price_t,Ref_Price_t,Application_t,Tourist_t,Settlement_t
from django.db.models import Q
import random

def populate():
    def add_agency(name):
        age=Agency_t.objects.get_or_create(name=name)[0]
        age.save()
        return age

    def add_line_price(name,local_agency_fk,remark='',detail=''):
        lin=Line_Price_t.objects.get_or_create(name=name,local_agency_fk=local_agency_fk)[0]
        lin.remark=remark
        lin.detail=detail
        lin.save()
        return lin

    def add_ref_price(level,kind,price,line_price_fk,chose=False):
    	ref=Ref_Price_t.objects.get_or_create(line_price_fk=line_price_fk,level=level,kind=kind)[0]
    	ref.price=price
    	ref.chose=chose
    	ref.save()
    	return ref

    def add_application(agency_fk,local_agency_fk,line_name_fk,date,def_price_fk):
        app=Application_t.objects.get_or_create(
            agency_fk=agency_fk,
            local_agency_fk=local_agency_fk,
            line_name_fk=line_name_fk,
            def_price_fk=def_price_fk)[0]
        app.date=date
        app.save()
        return app

    def add_tourist(name,application_fk,ref_price_fk,final_price,
    	trans_price=0,trans_remark='',trans_agency='0',agent_price=0,
    	agent_remark='',amount=1,fix_price=0,fix_remark=''):
    	tou=Tourist_t.objects.get_or_create(
            name=name,application_fk=application_fk,
            ref_price_fk=ref_price_fk)[0]
    	tou.amount=amount
    	tou.fix_price=fix_price
    	tou.final_price=final_price
    	tou.fix_remark=fix_remark
    	tou.trans_price=trans_price
    	tou.trans_remark=trans_remark
    	tou.trans_agency=trans_agency
    	tou.agent_price=agent_price
    	tou.agent_remark=agent_remark
    	tou.save()
    	return tou

    def add_settlement(price,kind,rec_agency_fk,pay_agency_fk,application_fk):
    	se=Settlement_t.objects.get_or_create(price=price,application_fk=application_fk,
    		rec_agency_fk=rec_agency_fk,pay_agency_fk=pay_agency_fk,kind=kind)[0]
    	se.save()
    	return se

    agency_list=['中国国际旅行社总社','中国旅行社总社','中国康辉旅行社有限责任公司',
    '中青旅控股股份有限公司','中信旅游总公司','招商局国际旅行社有限责任公司','中国和平国际旅游有限责任公司',
    '百恒国际旅行社','交通公社新纪元国际旅行社有限公司']
    
    line_price_list=[
    {"name":"西安市内一日游（旺季）","remark":"基础报价"},
    {"name":"西安北线二日游（旺季）","remark":"西安本地，老李"},
    {"name":"西安东线三日游（旺季）","remark":"刘一平，7月报价"},
    {"name":"兵马俑一日游（旺季）","remark":"英文导游，欧美游客"}
    ]



    ref_Price_list001=[
    {"level":1,"kind":"成人","price":200},
    {"level":2,"kind":"车导","price":150},
    {"level":3,"kind":"吃","price":100}]

    ref_Price_list002=[
    {"level":1,"kind":"成人","price":270},
    {"level":2,"kind":"车住","price":160},
    {"level":3,"kind":"车费","price":130}]

    ref_Price_list003=[
    {"level":1,"kind":"成人","price":350},
    {"level":2,"kind":"学生","price":260},
    {"level":3,"kind":"车住","price":230}]


    ref_Price_list004=[
    {"level":1,"kind":"成人","price":600},
    {"level":2,"kind":"车住","price":430},
    {"level":3,"kind":"吃住","price":500}]

    ref_price_dic={
    "西安市内一日游（旺季）":ref_Price_list001,
    "西安北线二日游（旺季）":ref_Price_list002,
    "西安东线三日游（旺季）":ref_Price_list003,
    "兵马俑一日游（旺季）":ref_Price_list004
    }

    
    tourist_list001=[
    {"name":"景天","amount":3,"fix_price":300,"fix_remark":"专车接送","trans_price":0,"agent_price":0},
    {"name":"重楼","amount":1,"fix_price":800,"fix_remark":"5星住宿","trans_price":0,"agent_price":0},
    {"name":"龙葵","amount":2,"fix_price":-50,"fix_remark":"餐费自理","trans_price":0,"agent_price":200},
    {"name":"赵灵儿","amount":5,"fix_price":0,"fix_remark":"","trans_price":700,"agent_price":0},
    {"name":"伊千觞","amount":1,"fix_price":2000,"fix_remark":"82年的茅台","trans_price":1800,"agent_price":2000},
    ]

    tourist_list002=[
    {"name":"卡卡西","amount":4,"fix_price":0,"fix_remark":"","trans_price":0,"agent_price":0},
    {"name":"雏田","amount":2,"fix_price":0,"fix_remark":"","trans_price":0,"agent_price":0},
    {"name":"我爱罗","amount":2,"fix_price":-80,"fix_remark":"无需床位，不睡觉","trans_price":0,"agent_price":300},
    {"name":"卡卡罗特","amount":5,"fix_price":0,"fix_remark":"","trans_price":700,"agent_price":0},
    {"name":"蜡笔小新","amount":1,"fix_price":100,"fix_remark":"马杀鸡","trans_price":200,"agent_price":0},
    ]
    
    tourist_list003=[
    {"name":"林动","amount":3,"fix_price":0,"fix_remark":"","trans_price":0,"agent_price":0},
    {"name":"孟浩","amount":2,"fix_price":0,"fix_remark":"","trans_price":0,"agent_price":0},
    {"name":"萧炎","amount":1,"fix_price":0,"fix_remark":"","trans_price":0,"agent_price":0},
    ]

    tourist_list004=[
    {"name":"复仇者联盟","amount":7,"fix_price":1000000,"fix_remark":"封口费","trans_price":0,"agent_price":0},
    {"name":"金刚狼","amount":1,"fix_price":0,"fix_remark":"","trans_price":0,"agent_price":0},
    {"name":"忍者神龟","amount":5,"fix_price":5000,"fix_remark":"披萨管饱","trans_price":0,"agent_price":0},
    ]

    #key代表出团申请单id，一个出团申请单对应一组游客
    tourist_list=[
    {1:tourist_list001},
    {2:tourist_list002},
    {3:tourist_list003},
    {4:tourist_list004}
    ]

    for name in agency_list:
        add_agency(name)

    for lin_dic in line_price_list:
        add_line_price(name=lin_dic["name"],local_agency_fk=Agency_t.objects.filter(name='百恒国际旅行社')[0],
            remark=lin_dic["remark"])

    for line,ref_list in ref_price_dic.items():
        for ref_dic in ref_list:
            chose=False
            if ref_dic["level"]==1:
                chose=True
            else:
                chose=False
            add_ref_price(
                level=ref_dic["level"],
                kind=ref_dic["kind"],
                price=ref_dic["price"],
                line_price_fk=Line_Price_t.objects.filter(name=line)[0],
                chose=chose)

    #填充出团申请单
    for i in range(1,5):
        line_name_fk=Line_Price_t.objects.filter(id=i)[0]
        add_application(
            agency_fk=Agency_t.objects.filter(id=i)[0],
            local_agency_fk=Agency_t.objects.filter(name="百恒国际旅行社")[0],#百恒是默认的地接社
            line_name_fk=line_name_fk,
            date=datetime.datetime.now(),
            def_price_fk=Ref_Price_t.objects.filter(line_price_fk=line_name_fk)[0])
    
    for tourist_dic in tourist_list:
        for k,t_list in tourist_dic.items():
            application_fk=Application_t.objects.filter(id=k)[0]
            ref_price_obj=Ref_Price_t.objects.filter(line_price_fk=application_fk.line_name_fk)
            ref_price=ref_price_obj.filter(chose=True)[0].price
            for t_dic in t_list:
                amount=t_dic["amount"]
                fix_price=t_dic["fix_price"]
                final_price=ref_price*amount+fix_price
                trans_price=t_dic["trans_price"]
                if trans_price !=0:#如果有调拨价格，就随机填充一个调拨组织的ID
                    trans_agency_obj=Agency_t.objects.exclude(Q(name="百恒国际旅行社")|Q(id=application_fk.agency_fk.id))
                    i=random.randint(0,len(trans_agency_obj)-1)
                    trans_agency=str(trans_agency_obj[i].id)
                else:
                    trans_agency='0'
                add_tourist(
                    name=t_dic["name"],
                    application_fk= application_fk,
                    ref_price_fk=ref_price_obj[0],
                    final_price=final_price,
                    trans_price=trans_price,
                    trans_remark="",
                    trans_agency=trans_agency,
                    agent_price=t_dic["agent_price"],
                    agent_remark='',
                    amount=amount,
                    fix_price=fix_price,
                    fix_remark=t_dic["fix_remark"])
    
'''
    #计算结算信息
    def settle(app_fk):
        #基础业务
        tou_obj=Tourist_t.objects.filter(application_fk=app_fk)
        sum_final_price=0
        sum_agent_price=0
        sum_trans_price=0
        for i in range(0,len(tou_obj)):
            sum_final_price=tou_obj[i].final_price+sum_final_price
            sum_agent_price=tou_obj[i].agent_price+sum_agent_price
            if tou_obj[i].trans_agency!='0':#如果存在调拨单位
                sum_trans_price=tou_obj[i].trans_price+sum_trans_price
                sum_trans_price=sum_trans_price-tou_obj[i].agent_price
                kind_trans="调拨业务"
                if sum_trans_price>=0:
                    rec_trans=app_fk.local_agency_fk

                set_trans_dit={"price":price_trans,"kind":kind_trans,"rec":rec_trans,"pay":pay_trans}
            

        price_base=sum_final_price-sum_agent_price
        kind_base="基础业务"
        if price_base>=0:
            rec_base=app_fk.local_agency_fk
            pay_base=app_fk.agency_fk
        else:
            pay_base=app_fk.local_agency_fk
            rec_base=app_fk.agency_fk
            price_base=-price_base       
        set_base_dit={"price":price_base,"kind":kind_base,"rec":rec_base,"pay":pay_base}



        set_trans_dit
        set_agent_dit=
        return set_dit

    #填充结算表
    for app_obj in Application_t.objects.all():
        set_dit=settle(app_obj[0])
        add_settlement(price=set_dit["price"],kind=set_dit["kind"],
            rec_agency_fk=set_dit["rec"],pay_agency_fk=set_dit["pay"],app_obj[0])        
'''


if __name__=='__main__':
	print('starting populate ...make codes fly～～～～')
	populate()
	print('ok~')