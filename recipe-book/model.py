# -*- coding: utf-8 -*-
import json, math
src=open('build.py').read()
ns={}
exec(src.split("PACK=0.100")[0].split("R=[")[0], ns)
DB=ns['DB']
# تحديث أسعار الخام (ر.ع/كجم) وفق مسح السوق
PRICE_NOTES={
 "صدر دجاج":(2.30,"موثّق جزئياً","Lulu عُمان: مجمّد 1.60–2.49 /كجم (عبوات 1–2 كجم)، طازج 4.58 /كجم؛ اعتُمد سعر جملة 2.30"),
 "أرز بسمتي (نيء)":(0.85,"موثّق","Lulu: Excel بسمتي 5 كجم = 3.950 (0.79/كجم)، Tilda 5 كجم = 6.570 (1.31/كجم)"),
 "لحم بقري (ستيك)":(5.50,"تقديري","مرجع: متوسط قطعة لحم بقري 4.0 ر.ع/كجم (نطاق 2.5–6.0)؛ قطع الستيك أعلى"),
 "لحم بقري مفروم":(3.80,"تقديري","تقدير قريب من متوسط اللحم البقري المحلي"),
 "روبيان":(5.00,"تقديري","لم يُعثر على سعر 2026 موثّق؛ يُؤخذ عرض سعر من مورّد"),
 "فيليه سمك":(3.80,"تقديري","أسماك محلية: تونة 1.4–1.6 /كجم (كاملة)، كنعد >4 /كجم؛ الفيليه الجاهز أعلى"),
 "بطاطا":(0.40,"تقديري","سوق الجملة المركزي"),
 "حليب قليل الدسم":(0.65,"تقديري",""),"زبدة":(2.80,"تقديري",""),"طماطم مهروسة":(0.85,"تقديري",""),
 "بصل":(0.35,"تقديري","سوق الجملة"),"زبادي قليل الدسم":(0.90,"تقديري",""),"زيت زيتون":(3.80,"تقديري","لم يُعثر على سعر موثّق"),
 "ثوم وزنجبيل":(1.20,"تقديري",""),"بهارات":(4.00,"تقديري",""),"ملح":(0.30,"تقديري",""),"فطر":(1.80,"تقديري",""),
 "كريمة طبخ خفيفة":(2.50,"تقديري",""),"فلفل ملوّن":(1.00,"تقديري",""),"خضار مشكلة للشوي":(0.95,"تقديري",""),
 "بقسماط":(1.20,"تقديري",""),"بيض":(2.40,"تقديري",""),"ليمون":(0.80,"تقديري",""),"صوص بني خفيف":(1.50,"تقديري",""),"أعشاب (بقدونس)":(2.00,"تقديري",""),
}
for k,(p,_,_) in PRICE_NOTES.items():
    d=list(DB[k]); d[4]=p; DB[k]=tuple(d)
data=json.load(open('data.json'))
PACK=0.100; DELIV=0.350; FEE=0.025; APP=0.25; WASTE=0.02; VAT=1.05
PRICES={'MRB-01':(3.2,3.6),'MRB-02':(3.2,3.6),'MRB-03':(3.4,3.8),'MRB-04':(3.9,4.3),'MRB-05':(3.2,3.6),'MRB-06':(3.8,4.2),'MRB-07':(3.3,3.7),'MRB-08':(3.5,3.9),'MRB-09':(3.2,3.6),'MRB-10':(3.6,4.0)}
def r050(x): return round(x*20)/20
for o in data:
    o['raw']=sum(DB[n][4]*g/1000 for n,g in o['ing'])
    sub,app=PRICES[o['code']]; o['sub']=sub; o['app']=app
    sn,an=sub/VAT,app/VAT
    kmax=lambda m:min(sn*(1-FEE-WASTE-m)-PACK-DELIV, an*(1-APP-WASTE-m)-PACK)
    o['n_open']=kmax(0.30); o['n_target']=kmax(0.25); o['n_max']=kmax(0.15)
    o['K']=r050((o['n_target']+o['n_max'])/2)   # سعر المطبخ المفترض في الحالة الأساسية
    o['sub_net']=sn; o['app_net']=an
    o['sub_cost']=o['K']+PACK+DELIV+FEE*sn+WASTE*sn
    o['app_cost']=o['K']+PACK+APP*an+WASTE*an
    o['sub_profit']=sn-o['sub_cost']; o['app_profit']=an-o['app_cost']
    o['sub_m']=o['sub_profit']/sn*100; o['app_m']=o['app_profit']/an*100
N=len(data)
avg=lambda k:sum(o[k] for o in data)/N
UE=dict(sub_price=avg('sub'),app_price=avg('app'),K=avg('K'),sub_profit=avg('sub_profit'),app_profit=avg('app_profit'),sub_net=avg('sub_net'),app_net=avg('app_net'),
        sub_cost=avg('sub_cost'),app_cost=avg('app_cost'))
# ===== النموذج المالي 36 شهراً =====
def lin(m,pts):
    for (m0,v0),(m1,v1) in zip(pts,pts[1:]):
        if m0<=m<=m1: return v0+(v1-v0)*(m-m0)/(m1-m0)
SUBS=[(1,20),(12,150),(24,350),(36,600)]
APPD=[(1,8),(12,40),(24,80),(36,120)]
FIXED={1:dict(gm=1000,cs=450,mk=500,nut=200,ops=0,sales=0),2:dict(gm=1200,cs=450,mk=600,nut=250,ops=500,sales=0),3:dict(gm=1500,cs=700,mk=800,nut=300,ops=700,sales=600)}
OTHER={1:800,2:1000,3:1300}      # برمجيات، محاسبة، تراخيص، تأمين، متفرقات
BRAND={1:500,2:600,3:800}; CAC={1:25,2:28,3:30}
CHURN=0.08; MEALS_PER_SUB=44; SOC=0.115
def run(volx=1.0,kx=1.0,verbose=False):
    rows=[];cum=-STARTUP_TOTAL;prev=0;loss_cf=0;peak=cum
    for m in range(1,37):
        y=(m-1)//12+1
        subs=round(lin(m,SUBS)*volx); appd=lin(m,APPD)*volx
        sm=subs*MEALS_PER_SUB; am=appd*30
        rev_s=sm*UE['sub_net']; rev_a=am*UE['app_net']
        K=UE['K']*kx
        var=sm*(K+PACK+DELIV)+am*(K+PACK)+rev_s*(FEE+WASTE)+rev_a*(APP+WASTE)
        f=FIXED[y]; sal=sum(f.values()); sal+= (sal-f['gm'])*SOC
        adds=max(0,subs-prev)+CHURN*prev
        mk=adds*CAC[y]+BRAND[y]
        fixed=sal+OTHER[y]+mk
        ebit=rev_s+rev_a-var-fixed
        rows.append(dict(m=m,y=y,subs=subs,sm=sm,am=am,rev=rev_s+rev_a,var=var,fixed=fixed,mk=mk,ebit=ebit,adds=adds))
        prev=subs
    # ضريبة 15% مع ترحيل الخسائر
    cf=0;cum=-STARTUP_TOTAL;peak=cum;be=None;yr={}
    for r in rows:
        r['tax']=0
    for y in (1,2,3):
        ys=[r for r in rows if r['y']==y]
        e=sum(r['ebit'] for r in ys)
        taxable=e
        if taxable<0: cf+= -taxable; tax=0
        else:
            use=min(cf,taxable); cf-=use; tax=(taxable-use)*0.15
        yr[y]=dict(rev=sum(r['rev'] for r in ys),var=sum(r['var'] for r in ys),fixed=sum(r['fixed'] for r in ys),mk=sum(r['mk'] for r in ys),ebit=e,tax=tax,net=e-tax,
                   meals=sum(r['sm']+r['am'] for r in ys),subs_end=ys[-1]['subs'])
        for r in ys: r['tax']=tax/12
    for r in rows:
        cum+=r['ebit']-r['tax']; r['cum']=cum; peak=min(peak,cum)
        if be is None and r['ebit']>0 and r['m']>1: be=r['m'] if all(x['ebit']>0 for x in rows[r['m']-1:r['m']+2]) else None
    pay=next((r['m'] for r in rows if r['cum']>=0),None)
    return rows,yr,peak,be,pay
STARTUP=[("السجل التجاري والتراخيص (بلدية/صحة) والعقود القانونية",900),("الهوية البصرية والموقع وتطبيق/نظام الطلبات",4200),("تصوير احترافي للوجبات والمحتوى",800),("عبوات وملصقات (مخزون أولي)",1500),("حقائب/صناديق تبريد وتجهيزات التوصيل",1500),("تجارب أولية وعيّنات ومراجعة التغذية",600),("حملة الإطلاق (ما قبل الإطلاق)",2500),("رأس مال تشغيلي احتياطي (3 أشهر تشغيل)",9000)]
STARTUP_TOTAL=sum(v for _,v in STARTUP)
base=run(); cons=run(0.7,1.10); opt=run(1.25,0.95)
if __name__=="__main__":
    rows,yr,peak,be,pay=base
    print(UE); print(STARTUP_TOTAL)
    for y in yr: print(y,{k:round(v) for k,v in yr[y].items()})
    for n,s in (("base",base),("cons",cons),("opt",opt)):
        print(n,'peak',round(s[2]),'be',s[3],'payback',s[4],[round(s[1][y]['net']) for y in (1,2,3)])
    for o in data: print(o['code'],o['K'],round(o['n_open'],3),round(o['n_target'],3),round(o['n_max'],3),'raw',round(o['raw'],3),round(o['sub_m']),round(o['app_m']))
