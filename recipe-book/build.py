# -*- coding: utf-8 -*-
import math, json
# name: (kcal, P, C, F per 100g, cost OMR/kg)
DB = {
 "صدر دجاج":(120,22.5,0,2.6,2.2),
 "لحم بقري (ستيك)":(150,21,0,7,6.0),
 "لحم بقري مفروم":(190,19,0,12,3.8),
 "روبيان":(85,18,0.5,1,5.0),
 "فيليه سمك":(100,20,0,2,3.5),
 "أرز بسمتي (نيء)":(350,7.5,78,0.6,0.9),
 "بطاطا":(77,2,17,0.1,0.35),
 "حليب قليل الدسم":(50,3.4,4.8,2,0.6),
 "زبدة":(717,0.9,0,81,2.5),
 "طماطم مهروسة":(25,1.2,5,0.2,0.8),
 "بصل":(40,1.1,9,0.1,0.4),
 "زبادي قليل الدسم":(60,4,6,1.5,0.9),
 "زيت زيتون":(884,0,0,100,3.5),
 "ثوم وزنجبيل":(80,3,17,0.5,1.2),
 "بهارات":(300,10,55,10,4.0),
 "ملح":(0,0,0,0,0.3),
 "فطر":(22,3.1,3.3,0.3,1.8),
 "كريمة طبخ خفيفة":(150,3,4,15,2.5),
 "فلفل ملوّن":(30,1,6,0.3,1.0),
 "خضار مشكلة للشوي":(30,1.5,6,0.3,0.9),
 "بقسماط":(395,13,72,5,1.2),
 "بيض":(143,12.6,0.7,9.5,2.4),
 "ليمون":(29,1,9,0.3,0.8),
 "صوص بني خفيف":(60,1,10,2,1.5),
 "أعشاب (بقدونس)":(36,3,6,0.8,2.0),
}
PACK=0.100; DELIV=0.350; FEE=0.025; APP=0.25
R=[
("MRB-01","تشكين مسالا مع الأرز","Chicken Masala",450,2.050,
 [("صدر دجاج",160),("أرز بسمتي (نيء)",65),("طماطم مهروسة",90),("بصل",35),("زبادي قليل الدسم",35),("زيت زيتون",8),("ثوم وزنجبيل",10),("بهارات",4),("ملح",1.5)],
 ["في مقلاة سخّن زيت الزيتون وأضف البصل وقلّبه حتى يذبل.","أضف الثوم والزنجبيل واظهما دقيقة حتى تظهر الرائحة.","أضف الدجاج المقطع وقلّبه حتى يتحمّر خفيفاً.","أضف الطماطم المهروسة والبهارات والملح، اترك المزيج على نار هادئة 10–12 دقيقة حتى ينضج الدجاج ويتكاثف الصوص، ثم أضف الزبادي بعد إطفاء النار.","اطهُ الأرز البسمتي بشكل منفصل، ثم قدّم المسالا مع الأرز في طبق واحد."],
 "ألبان (زبادي)","—"),
("MRB-02","تشكين مشروم","Chicken Mushroom",450,2.050,
 [("صدر دجاج",150),("أرز بسمتي (نيء)",65),("فطر",80),("كريمة طبخ خفيفة",40),("بصل",25),("ثوم وزنجبيل",8),("زيت زيتون",8),("بهارات",3),("ملح",1.5),("أعشاب (بقدونس)",2)],
 ["سخّن الزيت وحمّر البصل والثوم.","أضف الدجاج المقطّع وقلّبه حتى يتغيّر لونه.","أضف الفطر والبهارات واطهِ 5 دقائق حتى يجفّ ماؤه.","أضف الكريمة الخفيفة واتركها على نار هادئة 8 دقائق حتى يتماسك الصوص.","اطهُ الأرز منفصلاً، قدّم الدجاج بالمشروم فوقه أو بجانبه مع رشة بقدونس."],
 "ألبان (كريمة)","—"),
("MRB-03","كرات اللحم مع الأرز","Meatballs with Rice",450,2.250,
 [("لحم بقري مفروم",140),("أرز بسمتي (نيء)",65),("طماطم مهروسة",100),("بقسماط",15),("بيض",15),("بصل",25),("ثوم وزنجبيل",6),("زيت زيتون",6),("بهارات",3),("ملح",1.5),("أعشاب (بقدونس)",2)],
 ["اخلط اللحم المفروم مع البقسماط والبيض والبصل المبشور والبهارات والملح.","شكّل كرات وزن الواحدة نحو 35 جم (4 كرات للوجبة).","اشوِ الكرات في فرن 200°م لمدة 12 دقيقة.","حضّر صوص الطماطم بالثوم والزيت والأعشاب واطهِه 10 دقائق.","أضف الكرات إلى الصوص 5 دقائق ثم قدّمها مع الأرز الأبيض."],
 "غلوتين (بقسماط)، بيض","غلوتين، بيض"),
("MRB-04","أرز أبيض مع الروبيان","White Rice with Shrimp",430,2.450,
 [("روبيان",150),("أرز بسمتي (نيء)",65),("فلفل ملوّن",60),("بصل",25),("ثوم وزنجبيل",8),("زيت زيتون",10),("ليمون",10),("بهارات",3),("ملح",1.5),("أعشاب (بقدونس)",2)],
 ["نظّف الروبيان وتبّله بالليمون والبهارات والملح 10 دقائق.","سخّن الزيت وأضف البصل والثوم والفلفل الملوّن، قلّب 3 دقائق.","أضف الروبيان واطهِه 3–4 دقائق فقط حتى يتحوّل إلى اللون الوردي.","اطهُ الأرز الأبيض منفصلاً، وقدّم الروبيان فوقه مع رشة بقدونس."],
 "قشريات (روبيان)","قشريات"),
("MRB-05","ستيك دجاج مع البطاطا المهروسة","Chicken Steak with Mashed Potatoes",480,2.050,
 [("صدر دجاج",180),("بطاطا",200),("حليب قليل الدسم",40),("زبدة",5),("زيت زيتون",5),("بهارات",3),("ملح",1.5),("أعشاب (بقدونس)",2)],
 ["تبّل صدر الدجاج بالبهارات والملح والزيت 30 دقيقة على الأقل.","اشوِ الدجاج على الجريل حتى درجة حرارة داخلية 74°م أو أكثر.","اسلق البطاطا حتى تنضج ثم اهرسها مع الحليب والزبدة والملح.","قدّم الستيك بجانب البطاطا المهروسة مع بقدونس."],
 "ألبان (حليب، زبدة)","—"),
("MRB-06","ستيك لحم مع البطاطا المهروسة","Beef Steak with Mashed Potatoes",480,2.400,
 [("لحم بقري (ستيك)",160),("بطاطا",200),("حليب قليل الدسم",40),("زبدة",5),("صوص بني خفيف",30),("زيت زيتون",5),("بهارات",3),("ملح",1.5)],
 ["تبّل قطعة اللحم بالبهارات والملح وأخرجها من الثلاجة 15 دقيقة قبل الشوي.","اشوِها على جريل ساخن حتى درجة الاستواء المطلوبة (داخلياً 71°م أو أكثر للحم المطبوخ جيداً).","حضّر البطاطا المهروسة بالحليب والزبدة.","سخّن الصوص البني وقدّمه فوق الستيك بجانب البطاطا."],
 "ألبان، قد يحتوي الصوص على غلوتين","غلوتين (محتمل)"),
("MRB-07","أرز مع ستيك الدجاج والخضار المحمّص","Rice with Chicken Steak & Roasted Vegetables",470,2.050,
 [("صدر دجاج",170),("أرز بسمتي (نيء)",65),("خضار مشكلة للشوي",130),("زيت زيتون",10),("ثوم وزنجبيل",5),("ليمون",5),("بهارات",3),("ملح",1.5)],
 ["تبّل الدجاج بالثوم والليمون والبهارات والملح.","قطّع الخضار (كوسا، بروكلي، جزر، طماطم) وقلّبها بالزيت والملح.","حمّص الخضار في الفرن 200°م لمدة 15–18 دقيقة.","اشوِ الدجاج حتى 74°م داخلياً، واطهُ الأرز منفصلاً.","قدّم الأرز مع الستيك والخضار المحمّصة."],
 "—","—"),
("MRB-08","قطعة سمك مع الخضار المحمّص أو البطاطا المهروسة","Fish Fillet with Roasted Vegetables or Mashed Potatoes",460,1.800,
 [("فيليه سمك",180),("بطاطا",150),("حليب قليل الدسم",30),("خضار مشكلة للشوي",80),("زبدة",3),("زيت زيتون",8),("ليمون",15),("بهارات",2),("ملح",1.5),("أعشاب (بقدونس)",2)],
 ["تبّل الفيليه بالليمون والبهارات والملح والزيت 15 دقيقة.","اخبز الفيليه في فرن 190°م لمدة 10–12 دقيقة حتى يتحوّل إلى الأبيض/الوردي المتماسك (74°م داخلياً).","حمّص الخضار في الفرن 15 دقيقة، أو حضّر البطاطا المهروسة بالحليب والزبدة (خيار الزبون).","قدّم السمك مع الجانب المختار وشريحة ليمون."],
 "أسماك، ألبان","أسماك"),
("MRB-09","أرز أبيض مع الفاهيتا","White Rice with Fajita",430,2.050,
 [("صدر دجاج",150),("أرز بسمتي (نيء)",65),("فلفل ملوّن",100),("بصل",40),("زيت زيتون",8),("ليمون",10),("بهارات",5),("ملح",1.5)],
 ["قطّع الدجاج شرائح رفيعة وتبّله ببهارات الفاهيتا والليمون والملح.","سخّن مقلاة بقوة وأضف الزيت ثم الدجاج 5–6 دقائق.","أضف شرائح البصل والفلفل الملوّن وقلّب 3–4 دقائق ليبقى الخضار مقرمشاً.","اطهُ الأرز منفصلاً وقدّم الفاهيتا فوقه."],
 "—","—"),
("MRB-10","أرز أبيض مع ستيك اللحم","White Rice with Beef Steak",450,2.250,
 [("لحم بقري (ستيك)",160),("أرز بسمتي (نيء)",65),("خضار مشكلة للشوي",80),("زبدة",5),("صوص بني خفيف",20),("زيت زيتون",5),("ثوم وزنجبيل",4),("بهارات",3),("ملح",1.5)],
 ["تبّل اللحم بالثوم والبهارات والملح.","اشوِ الستيك على جريل ساخن حتى الاستواء المطلوب (71°م أو أكثر).","اسلق الخضار أو حمّصها وقلّبها بقليل من الزبدة.","اطهُ الأرز منفصلاً، وقدّم الستيك فوقه مع الخضار وقطعة زبدة صغيرة وصوص خفيف."],
 "ألبان","—"),
]
def r3(x): return f"{x:.3f}"
def ceil1(x): return math.ceil(round(x*10,6))/10
out=[]
for code,ar,en,w,K,ing,steps,alg,_ in R:
    kc=P=C=F=raw=0
    for n,g in ing:
        d=DB[n]; kc+=d[0]*g/100;P+=d[1]*g/100;C+=d[2]*g/100;F+=d[3]*g/100;raw+=d[4]*g/1000
    sub=ceil1((K+PACK+DELIV)/(1-FEE-0.30))
    sub_cost=K+PACK+DELIV+FEE*sub
    app=ceil1((K+PACK)/(1-APP-0.20))
    app_cost=K+PACK+APP*app
    out.append(dict(code=code,ar=ar,en=en,w=w,K=K,ing=ing,steps=steps,alg=alg,kcal=round(kc/5)*5,P=round(P),C=round(C),F=round(F),raw=raw,
      sub=sub,sub_cost=sub_cost,sub_profit=sub-sub_cost,sub_m=(sub-sub_cost)/sub*100,
      app=app,app_cost=app_cost,app_profit=app-app_cost,app_m=(app-app_cost)/app*100))
json.dump(out,open("/home/user/newme/recipe-book/data.json","w"),ensure_ascii=False,indent=1)
for o in out:
    print(o["code"],o["en"],o["kcal"],"kcal P",o["P"],"C",o["C"],"F",o["F"],"| K",o["K"],"raw~%.3f"%o["raw"],"| sub",o["sub"],"cost %.3f"%o["sub_cost"],"profit %.3f (%.0f%%)"%(o["sub_profit"],o["sub_m"]),"| app",o["app"],"profit %.3f (%.0f%%)"%(o["app_profit"],o["app_m"]))

def fmt_g(g):
    return f"{g:g} جم" if g<1000 else f"{g/1000:.2f} كجم"
css="""
@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;font-family:'Noto Naskh Arabic','Cairo','Tajawal','DejaVu Sans',sans-serif;background:#eee;color:#2b3a2b;direction:rtl}
.page{width:210mm;height:297mm;margin:0 auto 8mm;padding:10mm 12mm;background:#fbf8ef;position:relative;overflow:hidden;page-break-after:always;border-top:10mm solid #5f7d52}
@media print{body{background:none}.page{margin:0}}
h1,h2,h3{margin:0}
.hd{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #c9d5bd;padding-bottom:3mm;margin-bottom:5mm;font-size:11pt;color:#5f7d52}
.title{font-size:22pt;font-weight:700;color:#2f4a2a;margin:2mm 0}
.en{font-size:10pt;color:#7a8a70;direction:ltr;text-align:right}
.code{background:#e7edda;border-radius:3mm;padding:1.5mm 5mm;font-weight:700;color:#2f4a2a}
.kpis{display:flex;gap:3mm;margin:4mm 0}
.kpi{flex:1;background:#fff;border:1px solid #d7dfc9;border-radius:3mm;padding:3mm;text-align:center}
.kpi b{display:block;font-size:15pt;color:#2f4a2a}.kpi span{font-size:9pt;color:#6b7a62}
.sec{background:#5f7d52;color:#fff;display:inline-block;padding:1.2mm 6mm;border-radius:0 3mm 3mm 0;margin:4mm 0 2mm;font-size:12pt}
table{width:100%;border-collapse:collapse;background:#fff;font-size:9.5pt}
th{background:#e7edda;color:#2f4a2a}th,td{border:1px solid #d7dfc9;padding:1.1mm 2.5mm;text-align:right}
td.n,th.n{text-align:center;white-space:nowrap}
.steps{counter-reset:s;list-style:none;padding:0;margin:0;font-size:10pt}
.steps li{counter-increment:s;background:#fff;border:1px solid #d7dfc9;border-radius:3mm;margin-bottom:1.6mm;padding:1.8mm 11mm 1.8mm 3mm;position:relative;line-height:1.6}
.steps li:before{content:counter(s);position:absolute;right:2.5mm;top:2mm;width:6mm;height:6mm;border-radius:50%;background:#e7edda;color:#2f4a2a;text-align:center;font-weight:700;font-size:9pt;line-height:6mm}
.two{display:flex;gap:5mm}.two>div{flex:1}
.q li{margin:1mm 0;font-size:9.5pt}
.note{font-size:8.5pt;color:#6b7a62;margin-top:2mm}
.tot td{background:#e7edda;font-weight:700}
.foot{position:absolute;bottom:2.5mm;left:12mm;right:12mm;font-size:8.5pt;color:#8a9a80;display:flex;justify-content:space-between}
.cover{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;height:100%}
.cover h1{font-size:34pt;color:#2f4a2a}.cover p{font-size:14pt;color:#5f7d52}
"""
H=[f"<!doctype html><html lang='ar' dir='rtl'><meta charset='utf-8'><title>الدليل الرئيسي للوصفات القياسية</title><style>{css}</style><body>"]
H.append("<div class='page'><div class='cover'><div style='font-size:60pt'>🌿</div><h1>الدليل الرئيسي للوصفات القياسية</h1><p>Master Recipe Book</p><p style='margin-top:12mm;font-size:12pt'>برنامج اشتراكات التغذية الصحية<br>الإصدار 1.0 · 10 وصفات · سلطنة عُمان</p></div></div>")
# standards page
H.append("""<div class='page'><div class='hd'><span>الدليل الرئيسي للوصفات القياسية</span><span>معايير التشغيل والإنتاج</span></div>
<h2 class='title'>معايير التشغيل والإنتاج</h2>
<div class='sec'>مبادئ عامة</div>
<ul class='q'><li>تُنفَّذ كل وجبة وفق الوصفة القياسية حرفياً، والأوزان المذكورة للمكوّنات <b>نيئة</b> وللوجبة الواحدة.</li>
<li>الوزن النهائي المستهدف لكل وجبة موضّح في بطاقتها، بتسامح ± 10 جم.</li>
<li>الحد الأدنى لدرجة الحرارة الداخلية: الدجاج 74°م · اللحم المفروم 71°م · السمك والروبيان 63–74°م.</li>
<li>سلسلة التبريد: تبريد الوجبة إلى أقل من 5°م خلال ساعتين من الطهي، وتخزينها عند 0–4°م، واستهلاكها خلال 72 ساعة.</li>
<li>الأرز يُطهى منفصلاً ويُقدَّم قوامه مفلفلاً غير متكتل.</li>
<li>التعبئة في عبوات محكمة صالحة للمايكروويف، مع ملصق: اسم الوجبة، السعرات، البروتين، مسببات الحساسية، تاريخ الإنتاج والانتهاء.</li></ul>
<div class='sec'>منهجية حساب السعرات</div>
<p style='font-size:10pt;line-height:1.8'>تُحسب السعرات بجمع (سعرات كل مكوّن لكل 100 جم × وزنه بالجرام ÷ 100) اعتماداً على جداول التركيب الغذائي المرجعية للأغذية النيئة، ثم تُقرَّب لأقرب 5 سعرات. الأرقام تقديرية ويُنصح بالتحقق منها بالوزن الفعلي لدى المطبخ ومراجعتها من أخصائي تغذية مرخّص قبل الطباعة على العبوة.</p>
<div class='sec'>فرضيات التكلفة والتسعير</div>
<ul class='q'><li><b>تكلفة الشراء من المطبخ:</b> سعر الوجبة في قائمة المطبخ المتعاقد (الصورة المرفقة) ويشمل المواد والعمالة والطهي.</li>
<li><b>التغليف والملصق:</b> 0.100 ر.ع لكل وجبة.</li>
<li><b>التوصيل (اشتراكات):</b> 0.350 ر.ع لكل وجبة (توصيل مجمّع ليومين/أسبوع).</li>
<li><b>رسوم الدفع الإلكتروني:</b> 2.5% من سعر البيع.</li>
<li><b>عمولة تطبيقات التوصيل:</b> 25% من سعر البيع (يلزم تأكيدها من العقد الفعلي).</li>
<li><b>الهدف:</b> هامش ربح صافٍ 30% على الاشتراكات و20% على التطبيقات، قبل التسويق والرواتب والإيجار.</li></ul>
<p class='note'>جميع الأسعار بالريال العُماني (ر.ع). أسعار المواد الخام المستخدمة مرجع تقديري لسوق عُمان وتُحدَّث دورياً.</p></div>""")
# recipes
for o in out:
    rows=""
    tot=dict(g=0)
    for n,g in o["ing"]:
        rows+=f"<tr><td>{n}</td><td class='n'>{fmt_g(g)}</td><td class='n'>{fmt_g(g*10)}</td><td class='n'>{fmt_g(g*50)}</td><td class='n'>{fmt_g(g*100)}</td></tr>"
    H.append(f"""<div class='page'><div class='hd'><span>الدليل الرئيسي للوصفات القياسية</span><span class='code'>{o['code']}</span></div>
<h2 class='title'>{o['ar']}</h2><div class='en'>{o['en']}</div>
<div class='kpis'><div class='kpi'><b>{o['w']} جم</b><span>الوزن النهائي المستهدف</span></div><div class='kpi'><b>{o['kcal']} سعرة</b><span>السعرات التقديرية</span></div><div class='kpi'><b>{o['P']} جم</b><span>البروتين</span></div><div class='kpi'><b>{o['C']} جم</b><span>الكربوهيدرات</span></div><div class='kpi'><b>{o['F']} جم</b><span>الدهون</span></div></div>
<div class='sec'>المكوّنات والكميات (وزن نيء)</div>
<table><tr><th>المكوّن</th><th class='n'>وجبة واحدة</th><th class='n'>10 وجبات</th><th class='n'>50 وجبة</th><th class='n'>100 وجبة</th></tr>{rows}</table>
<div class='two'><div><div class='sec'>طريقة التحضير</div><ol class='steps'>{''.join(f'<li>{s}</li>' for s in o['steps'])}</ol></div>
<div><div class='sec'>التكلفة والتسعير (للوجبة)</div><table>
<tr><td>تكلفة الشراء من المطبخ</td><td class='n'>{r3(o['K'])}</td></tr>
<tr><td>التغليف والملصق</td><td class='n'>{r3(PACK)}</td></tr>
<tr><td>التوصيل (اشتراك)</td><td class='n'>{r3(DELIV)}</td></tr>
<tr><td>رسوم الدفع (2.5%)</td><td class='n'>{r3(FEE*o['sub'])}</td></tr>
<tr class='tot'><td>إجمالي التكلفة (اشتراك)</td><td class='n'>{r3(o['sub_cost'])}</td></tr>
<tr class='tot'><td>سعر البيع (اشتراك)</td><td class='n'>{r3(o['sub'])}</td></tr>
<tr><td>صافي الربح / الهامش</td><td class='n'>{r3(o['sub_profit'])} ({o['sub_m']:.0f}%)</td></tr>
<tr class='tot'><td>سعر تطبيقات التوصيل</td><td class='n'>{r3(o['app'])}</td></tr>
<tr><td>صافي الربح / الهامش (بعد عمولة 25%)</td><td class='n'>{r3(o['app_profit'])} ({o['app_m']:.0f}%)</td></tr>
</table><p class='note'>تكلفة المواد الخام التقديرية للوجبة: {r3(o['raw'])} ر.ع (مرجع للتفاوض مع المطبخ).</p>
<div class='sec'>الجودة والسلامة</div><ul class='q'><li>الالتزام بالأوزان وفحص الوزن النهائي ({o['w']} جم ± 10).</li><li>درجة حرارة داخلية آمنة وتبريد سريع.</li><li>قوام صوص متجانس ونكهة متوازنة.</li><li>مسببات الحساسية: {o['alg']}.</li></ul></div></div>
<div class='foot'><span>{o['code']}</span><span>Master Recipe Book v1.0</span></div></div>""")
# summary
rows="".join(f"<tr><td>{o['code']}</td><td>{o['ar']}</td><td class='n'>{o['kcal']}</td><td class='n'>{o['P']}</td><td class='n'>{r3(o['K'])}</td><td class='n'>{r3(o['sub_cost'])}</td><td class='n'>{r3(o['sub'])}</td><td class='n'>{r3(o['sub_profit'])}</td><td class='n'>{o['sub_m']:.0f}%</td><td class='n'>{r3(o['app'])}</td><td class='n'>{r3(o['app_profit'])}</td></tr>" for o in out)
H.append(f"""<div class='page'><div class='hd'><span>الدليل الرئيسي للوصفات القياسية</span><span>الملاحق والجداول</span></div><h2 class='title'>ملخص السعرات والتكلفة والتسعير</h2>
<table style='font-size:8.5pt'><tr><th>الرمز</th><th>الوجبة</th><th class='n'>سعرات</th><th class='n'>بروتين (جم)</th><th class='n'>سعر المطبخ</th><th class='n'>إجمالي التكلفة</th><th class='n'>سعر الاشتراك</th><th class='n'>الربح</th><th class='n'>الهامش</th><th class='n'>سعر التطبيق</th><th class='n'>ربح التطبيق</th></tr>{rows}</table>
<p class='note'>جميع المبالغ بالريال العُماني. الربح صافٍ قبل التسويق والرواتب والمصاريف الإدارية.</p></div></body></html>""")
open("/home/user/newme/recipe-book/master-recipe-book.html","w").write("".join(H))
