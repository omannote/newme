# -*- coding: utf-8 -*-
import base64
from model import *
def b64(code): return "data:image/jpeg;base64,"+base64.b64encode(open(f"img/{code}.jpg","rb").read()).decode()
def r3(x): return f"{x:.3f}"
def fg(g): return f"{g:g} جم" if g<1000 else f"{g/1000:.2f} كجم"
css="""
@page{size:A4;margin:0}*{box-sizing:border-box}
body{margin:0;font-family:'Noto Naskh Arabic','Cairo','Tajawal','DejaVu Sans',sans-serif;background:#e9e9e4;color:#2b3a2b;direction:rtl}
.page{width:210mm;height:297mm;margin:0 auto 8mm;padding:9mm 12mm;background:#fbf8ef;position:relative;overflow:hidden;page-break-after:always;border-top:9mm solid #5f7d52}
@media print{body{background:none}.page{margin:0}}
h2{margin:0}.hd{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #c9d5bd;padding-bottom:2mm;margin-bottom:3mm;font-size:10.5pt;color:#5f7d52}
.title{font-size:20pt;font-weight:700;color:#2f4a2a;margin:1mm 0}.en{font-size:9.5pt;color:#7a8a70;direction:ltr;text-align:right}
.code{background:#e7edda;border-radius:3mm;padding:1mm 5mm;font-weight:700;color:#2f4a2a}
.top{display:flex;gap:5mm;align-items:center}.top img{width:34mm;height:34mm;border-radius:50%;border:2mm solid #fff;box-shadow:0 0 0 1px #d7dfc9}
.kpis{display:flex;gap:2.5mm;margin:3mm 0}.kpi{flex:1;background:#fff;border:1px solid #d7dfc9;border-radius:3mm;padding:2mm;text-align:center}
.kpi b{display:block;font-size:13pt;color:#2f4a2a}.kpi span{font-size:8.5pt;color:#6b7a62}
.sec{background:#5f7d52;color:#fff;display:inline-block;padding:1mm 6mm;border-radius:0 3mm 3mm 0;margin:3mm 0 2mm;font-size:11pt}
table{width:100%;border-collapse:collapse;background:#fff;font-size:9pt}th{background:#e7edda;color:#2f4a2a}
th,td{border:1px solid #d7dfc9;padding:1mm 2mm;text-align:right}td.n,th.n{text-align:center;white-space:nowrap}
.steps{counter-reset:s;list-style:none;padding:0;margin:0;font-size:9.5pt}
.steps li{counter-increment:s;background:#fff;border:1px solid #d7dfc9;border-radius:3mm;margin-bottom:1.4mm;padding:1.4mm 10mm 1.4mm 3mm;position:relative;line-height:1.55}
.steps li:before{content:counter(s);position:absolute;right:2.5mm;top:1.8mm;width:5.5mm;height:5.5mm;border-radius:50%;background:#e7edda;text-align:center;font-weight:700;font-size:8.5pt;line-height:5.5mm}
.two{display:flex;gap:5mm}.two>div{flex:1}.q li{margin:.8mm 0;font-size:9pt}.note{font-size:8pt;color:#6b7a62;margin-top:1.5mm}
.tot td{background:#e7edda;font-weight:700}.foot{position:absolute;bottom:2.5mm;left:12mm;right:12mm;font-size:8pt;color:#8a9a80;display:flex;justify-content:space-between}
.cover{display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;height:100%}
.cover h1{font-size:32pt;color:#2f4a2a;margin:4mm 0}.cover p{font-size:13pt;color:#5f7d52;margin:1mm}
.grid{display:grid;grid-template-columns:repeat(5,1fr);gap:3mm;margin-top:10mm;width:100%}.grid img{width:100%;border-radius:50%;border:1.5mm solid #fff;box-shadow:0 0 0 1px #d7dfc9}
.tag{font-size:8pt;padding:0 2mm;border-radius:2mm}.ok{background:#d7ecc8}.est{background:#f5e4b8}
"""
H=[f"<!doctype html><html lang='ar' dir='rtl'><meta charset='utf-8'><title>دليل الوصفات التنفيذي</title><style>{css}</style><body>"]
imgs="".join(f"<img src='{b64(o['code'])}'>" for o in data)
H.append(f"<div class='page'><div class='cover'><div style='font-size:40pt'>🌿</div><h1>دليل الوصفات التنفيذي</h1><p>Executive Master Recipe Book</p><p>الوصفات القياسية · المقادير · التكاليف · التسعير</p><div class='grid'>{imgs}</div><p style='margin-top:12mm;font-size:11pt'>برنامج اشتراكات التغذية الصحية · سلطنة عُمان<br>الإصدار 2.0 · نوفمبر 2026</p></div></div>")
H.append("""<div class='page'><div class='hd'><span>دليل الوصفات التنفيذي</span><span>معايير التشغيل ومنهجية الحساب</span></div><h2 class='title'>معايير التشغيل والإنتاج</h2>
<ul class='q'><li>تُنفَّذ كل وجبة وفق الوصفة القياسية حرفياً، والمقادير للمكوّنات <b>نيئة</b> وللوجبة الواحدة، والوزن النهائي بتسامح ± 10 جم.</li>
<li>درجات الحرارة الداخلية الدنيا: الدجاج 74°م · اللحم المفروم 71°م · الروبيان والسمك 63–74°م.</li>
<li>التبريد إلى أقل من 5°م خلال ساعتين، والتخزين عند 0–4°م، والاستهلاك خلال 72 ساعة من الإنتاج.</li>
<li>الأرز يُطهى منفصلاً بقوام مفلفل. التعبئة في عبوات صالحة للمايكروويف بملصق (الاسم، السعرات، البروتين، مسببات الحساسية، تاريخي الإنتاج والانتهاء).</li>
<li>الصور المرفقة توضّح شكل التقديم المستهدف، وتُعتمد مرجعاً بصرياً عند فحص الجودة.</li></ul>
<div class='sec'>منهجية حساب السعرات</div><p style='font-size:9.5pt;line-height:1.8'>مجموع (سعرات المكوّن لكل 100 جم × وزنه ÷ 100) بالاعتماد على جداول تركيب غذائي مرجعية للأغذية النيئة، مقرَّبة لأقرب 5 سعرات. الأرقام تقديرية وتُراجَع بالوزن الفعلي لدى المطبخ ومن أخصائي تغذية مرخّص قبل طباعتها على العبوات.</p>
<div class='sec'>فرضيات التكلفة والتسعير</div><ul class='q'>
<li><b>أسعار البيع</b> شاملة ضريبة القيمة المضافة 5%، والإيراد المحتسب = السعر ÷ 1.05.</li>
<li><b>سعر المطبخ:</b> لم يُتفق مع أي مطبخ بعد، والقيمة المعروضة هي <b>سعر الشراء المستهدف</b> (متوسط الهدف والحد الأقصى في جدول التفاوض).</li>
<li>التغليف 0.100 · التوصيل للاشتراكات 0.350 · رسوم الدفع 2.5% · هدر وتعويضات 2% · عمولة التطبيقات 25% (تُؤكَّد من العقد).</li>
<li>أسعار الخام: جزء منها موثّق من Lulu عُمان وجزء تقديري، وموضّح في صفحة مسح الأسعار.</li></ul></div>""")
rows=""
seen=set()
for o in data:
    for n,g in o['ing']:
        if n in seen: continue
        seen.add(n); p,st,nt=PRICE_NOTES[n]
        rows+=f"<tr><td>{n}</td><td class='n'>{p:.2f}</td><td class='n'><span class='tag {'ok' if st!='تقديري' else 'est'}'>{st}</span></td><td style='font-size:8pt'>{nt}</td></tr>"
H.append(f"""<div class='page'><div class='hd'><span>دليل الوصفات التنفيذي</span><span>مسح أسعار المواد الخام في السوق العُماني</span></div><h2 class='title'>مسح أسعار المواد الخام</h2>
<table><tr><th>المكوّن</th><th class='n'>ر.ع/كجم المعتمد</th><th class='n'>الحالة</th><th>الأساس / المصدر</th></tr>{rows}</table>
<p class='note'>«موثّق» أو «موثّق جزئياً»: من صفحات Lulu Hypermarket عُمان (أسعار عبوات تجزئة) وتقارير محلية. «تقديري»: لم يُعثر على سعر منشور، ويلزم عرض سعر رسمي من مورّد أو مسح ميداني قبل توقيع العقد. الأسعار تختلف بحسب الفرع والتاريخ، والجملة غالباً أقل من التجزئة. تضخم أسعار الغذاء في عُمان بلغ 8.4% سنوياً في سبتمبر 2026 (Muscat Daily)، فيُراجَع الجدول كل ربع سنة.</p></div>""")
H.append("""<div class='page'><div class='hd'><span>دليل الوصفات التنفيذي</span><span>أسعار المنافسين</span></div><h2 class='title'>خريطة المنافسين والأسعار</h2>
<table><tr><th>المنافس</th><th>النوع</th><th class='n'>السعر الظاهر (ر.ع/وجبة)</th><th>المصدر / الحالة</th></tr>
<tr><td>CALO (مسقط الكبرى)</td><td>اشتراكات وجبات صحية</td><td class='n'>من 3.000 (الإفطار من 2.000)</td><td>موثّق: صفحة CALO عُمان</td></tr>
<tr><td>خطة وجبات محلية (قائمة قديمة غير مؤرّخة)</td><td>اشتراك شهري</td><td class='n'>2.3 – 2.7 تقريباً</td><td>غير موثّق التاريخ والجهة (Scribd)</td></tr>
<tr><td>مطاعم صحية على Talabat وغيره</td><td>بيع مباشر عبر التطبيقات</td><td class='n'>لم يُرصد</td><td>يتطلب مسحاً يدوياً داخل التطبيق</td></tr>
<tr><td>Right Bite / Meals on Me (إقليمية)</td><td>اشتراكات (الإمارات)</td><td class='n'>—</td><td>تُراجَع تغطيتها لعُمان</td></tr>
<tr><td><b>مشروعنا</b></td><td>اشتراكات + تطبيقات</td><td class='n'><b>3.200 – 3.900 اشتراك / 3.600 – 4.300 تطبيق</b></td><td>مقترح</td></tr></table>
<div class='sec'>قراءة الموقع السعري</div><ul class='q'><li>سعر CALO المعلن (من 3.000) هو الحد الأدنى لخطة مجتمعة، ووجباته مخصصة بالماكروز، لذا نضع وجباتنا الأقل سعراً (دجاج) عند 3.200 قريبة منه.</li><li>القائمة المحلية القديمة تشير إلى أن السوق عرف أسعاراً أدنى (≈2.5)، وهو خطر ضغط على الأسعار يستلزم التمييز بالجودة والشفافية الغذائية.</li><li>تطبيقات التوصيل أعلى سعراً بسبب العمولة، ويتصدرها Talabat بحصة تُقدَّر بنحو 75% من السوق.</li></ul>
<p class='note'>قبل الإطلاق: يُنفَّذ مسح ميداني لـ10 منافسين على الأقل (التطبيقات والمواقع) وتُحدَّث هذه الصفحة.</p></div>""")
for o in data:
    rows="".join(f"<tr><td>{n}</td><td class='n'>{fg(g)}</td><td class='n'>{fg(g*10)}</td><td class='n'>{fg(g*50)}</td><td class='n'>{fg(g*100)}</td><td class='n'>{DB[n][4]*g/1000:.3f}</td></tr>" for n,g in o['ing'])
    H.append(f"""<div class='page'><div class='hd'><span>دليل الوصفات التنفيذي</span><span class='code'>{o['code']}</span></div>
<div class='top'><img src='{b64(o['code'])}'><div><h2 class='title'>{o['ar']}</h2><div class='en'>{o['en']}</div></div></div>
<div class='kpis'><div class='kpi'><b>{o['w']} جم</b><span>الوزن النهائي</span></div><div class='kpi'><b>{o['kcal']}</b><span>سعرة تقديرية</span></div><div class='kpi'><b>{o['P']} جم</b><span>بروتين</span></div><div class='kpi'><b>{o['C']} جم</b><span>كربوهيدرات</span></div><div class='kpi'><b>{o['F']} جم</b><span>دهون</span></div></div>
<div class='sec'>المكوّنات والمقادير (وزن نيء)</div>
<table><tr><th>المكوّن</th><th class='n'>1 وجبة</th><th class='n'>10</th><th class='n'>50</th><th class='n'>100</th><th class='n'>تكلفة/وجبة</th></tr>{rows}<tr class='tot'><td colspan='5'>تكلفة المواد الخام التقديرية للوجبة</td><td class='n'>{o['raw']:.3f}</td></tr></table>
<div class='two'><div><div class='sec'>طريقة التحضير</div><ol class='steps'>{''.join(f'<li>{s}</li>' for s in o['steps'])}</ol></div>
<div><div class='sec'>التكلفة والتسعير (ر.ع)</div><table>
<tr><td>سعر الشراء المستهدف من المطبخ</td><td class='n'>{r3(o['K'])}</td></tr><tr><td>التغليف والملصق</td><td class='n'>{r3(PACK)}</td></tr><tr><td>التوصيل (اشتراك)</td><td class='n'>{r3(DELIV)}</td></tr>
<tr><td>رسوم الدفع + الهدر</td><td class='n'>{r3((FEE+WASTE)*o['sub_net'])}</td></tr><tr class='tot'><td>إجمالي التكلفة (اشتراك)</td><td class='n'>{r3(o['sub_cost'])}</td></tr>
<tr class='tot'><td>سعر البيع شامل الضريبة (اشتراك)</td><td class='n'>{r3(o['sub'])}</td></tr><tr><td>الصافي بعد الضريبة / الهامش</td><td class='n'>{r3(o['sub_profit'])} ({o['sub_m']:.0f}%)</td></tr>
<tr class='tot'><td>سعر التطبيقات</td><td class='n'>{r3(o['app'])}</td></tr><tr><td>الصافي بعد العمولة / الهامش</td><td class='n'>{r3(o['app_profit'])} ({o['app_m']:.0f}%)</td></tr>
<tr><td>حد التفاوض الأقصى للمطبخ</td><td class='n'>{r3(o['n_max'])}</td></tr></table>
<div class='sec'>الجودة والسلامة</div><ul class='q'><li>الوزن النهائي {o['w']} جم ± 10.</li><li>حرارة داخلية آمنة وتبريد سريع.</li><li>مطابقة الشكل للصورة المرجعية.</li><li>مسببات الحساسية: {o['alg']}.</li></ul></div></div>
<div class='foot'><span>{o['code']}</span><span>Executive Master Recipe Book v2.0</span></div></div>""")
rows="".join(f"<tr><td>{o['code']}</td><td>{o['ar']}</td><td class='n'>{o['kcal']}</td><td class='n'>{o['P']}</td><td class='n'>{o['raw']:.2f}</td><td class='n'>{r3(o['sub'])}</td><td class='n'>{r3(o['app'])}</td><td class='n'>{r3(o['n_open'])}</td><td class='n'>{r3(o['n_target'])}</td><td class='n'>{r3(o['n_max'])}</td></tr>" for o in data)
H.append(f"""<div class='page'><div class='hd'><span>دليل الوصفات التنفيذي</span><span>الملحق: التسعير وحدود التفاوض</span></div><h2 class='title'>التسعير وحدود التفاوض مع المطبخ</h2>
<table style='font-size:8.5pt'><tr><th>الرمز</th><th>الوجبة</th><th class='n'>سعرات</th><th class='n'>بروتين</th><th class='n'>خام تقديري</th><th class='n'>سعر الاشتراك</th><th class='n'>سعر التطبيق</th><th class='n'>افتتاح</th><th class='n'>هدف</th><th class='n'>حد أقصى</th></tr>{rows}</table>
<p class='note'>الافتتاح/الهدف/الحد الأقصى = أعلى سعر شراء من المطبخ يحقق هامشاً صافياً 30% / 25% / 15% بعد الضريبة 5% وعمولة التطبيقات والتغليف والتوصيل والدفع والهدر، على القناة الأضعف. أسعار البيع شاملة الضريبة. المبالغ بالريال العُماني.</p>
<div class='sec'>نقاط ضغط في التفاوض</div><ul class='q'><li>تكلفة الخام التقديرية 0.57–1.09 ر.ع، أي أن سعراً في حدود 1.55–2.00 يترك للمطبخ هامش عمالة وطاقة وربح مجزياً.</li><li>التزام كميات شهرية، وعقد 6–12 شهراً، وجدول إنتاج أسبوعي ثابت.</li><li>إعفاء المطبخ من التغليف والتوصيل (نتولاهما نحن).</li><li>شرط جودة وتدقيق شهري، وحق تغيير الشريك عند الإخلال.</li></ul></div></body></html>""")
open("executive-recipe-book.html","w").write("".join(H))
print("ok")
