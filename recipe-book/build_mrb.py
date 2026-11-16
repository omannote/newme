# -*- coding: utf-8 -*-
import base64, re
from model import *
def b64(path,mime="image/jpeg"): return f"data:{mime};base64,"+base64.b64encode(open(path,"rb").read()).decode()
def r3(x): return f"{x:.3f}"
def fg(g): return f"{g:g} جم" if g<1000 else f"{g/1000:.2f} كجم"
CAT={'MRB-01':'p','MRB-02':'p','MRB-03':'m','MRB-04':'s','MRB-05':'p','MRB-06':'m','MRB-07':'p','MRB-08':'s','MRB-09':'p','MRB-10':'m'}
CATN={'p':'وصفات الدواجن','m':'وصفات اللحوم','s':'وصفات الأسماك والمأكولات البحرية'}
EMO={"صدر دجاج":"🍗","لحم بقري (ستيك)":"🥩","لحم بقري مفروم":"🥩","روبيان":"🦐","فيليه سمك":"🐟","أرز بسمتي (نيء)":"🍚","بطاطا":"🥔","حليب قليل الدسم":"🥛","زبدة":"🧈","طماطم مهروسة":"🍅","بصل":"🧅","زبادي قليل الدسم":"🥣","زيت زيتون":"🫒","ثوم وزنجبيل":"🧄","بهارات":"🌶️","ملح":"🧂","فطر":"🍄","كريمة طبخ خفيفة":"🥛","فلفل ملوّن":"🫑","خضار مشكلة للشوي":"🥦","بقسماط":"🍞","بيض":"🥚","ليمون":"🍋","صوص بني خفيف":"🍯","أعشاب (بقدونس)":"🌿"}
PROT={"صدر دجاج","لحم بقري (ستيك)","لحم بقري مفروم","روبيان","فيليه سمك"}; STAR={"أرز بسمتي (نيء)","بطاطا"}
VEG={"طماطم مهروسة","بصل","فطر","فلفل ملوّن","خضار مشكلة للشوي","زبادي قليل الدسم","كريمة طبخ خفيفة","صوص بني خفيف","حليب قليل الدسم"}
FIX=[("(داخلياً 71°م أو أكثر للحم المطبوخ جيداً)","(حرارة داخلية 63°م على الأقل ثم راحة 3 دقائق)"),("حتى الاستواء المطلوب (71°م أو أكثر)","حتى حرارة داخلية 63°م على الأقل ثم راحة 3 دقائق"),("(74°م داخلياً)","(63°م داخلياً)")]
for o in data:
    o['steps']=[ (lambda s:[s:=s.replace(a,b) for a,b in FIX][-1])(s) for s in o['steps']]
QB={'p':["يكون الدجاج ناضجاً تماماً وطرياً (حرارة داخلية 74°م على الأقل).","نكهة متوازنة دون زيادة في الملح أو الحدّة.","قوام الأرز/الجانب مفلفل وغير متكتل ودافئ.","الصوص أو الخضار متجانس وبقوام مناسب."],
    'm':["اللحم طري وعصيري بنضج متجانس (63°م على الأقل مع راحة 3 دقائق، والمفروم 71°م).","نكهة متوازنة وتتبيلة واضحة دون زيادة الملح.","الجوانب (أرز/بطاطا/خضار) بقوام صحيح وخالية من التكتلات.","الصوص لامع ومتماسك ولا يغطي الطبق."],
    's':["السمك/الروبيان ناضج ومتماسك وغير جاف (63°م على الأقل).","لا رائحة سمك قوية، ونكهة الليمون والأعشاب ظاهرة.","الخضار أو الجانب طازج ومتوازن اللون.","التقديم نظيف والصلصة لا تفيض خارج الطبق."]}
QC={'p':["مطابقة المقادير الموزونة للوصفة القياسية.","قياس الحرارة الداخلية للدجاج بالمسبار (≥ 74°م).","فحص نكهة الصوص/التتبيلة بالتذوق العشوائي.","التأكد من قوام الأرز: مفلفل وغير متكتل.","وزن الوجبة النهائية للعيّنة ({w} ± 10 جم).","مراجعة المظهر العام والملصق قبل الإغلاق."],
    'm':["مطابقة نوع القطعة ووزنها وجودة اللحم عند الاستلام.","قياس الحرارة الداخلية (≥ 63°م للستيك، 71°م للمفروم).","التأكد من راحة اللحم قبل التقطيع والتعبئة.","قوام الجانب (أرز/بطاطا) ونظافة الطبق.","وزن الوجبة النهائية للعيّنة ({w} ± 10 جم).","مراجعة المظهر العام والملصق قبل الإغلاق."],
    's':["فحص طزاجة السمك/الروبيان عند الاستلام (رائحة، لون، حرارة ≤ 4°م).","قياس الحرارة الداخلية (≥ 63°م) وعدم الإفراط في الطهي.","التأكد من خلو الفيليه من العظام.","الحفاظ على قوام الخضار طازجاً (مقرمشاً وخالياً من الترهل).","وزن الوجبة النهائية للعيّنة ({w} ± 10 جم).","مراجعة المظهر العام والملصق قبل الإغلاق."]}
TIMES={'p':(35,25,72),'m':(35,22,72),'s':(30,15,48)}
ALG={"ألبان":("🥛","منتجات الألبان"),"غلوتين":("🌾","الغلوتين"),"بيض":("🥚","البيض"),"قشريات":("🦐","القشريات"),"أسماك":("🐟","الأسماك")}
def allergens(o):
    t=o['alg']+" "+(o.get('alg2') or '')
    return [v for k,v in ALG.items() if k in t]
FRAMECSS="""
@page{size:297mm 210mm;margin:0}*{box-sizing:border-box}
body{margin:0;font-family:'Noto Naskh Arabic','Cairo','DejaVu Sans',sans-serif;color:#2c3b2d;direction:rtl}
.sp{width:297mm;height:210mm;background:#2f4a38;padding:4.5mm;page-break-after:always;overflow:hidden}
.book{width:100%;height:100%;display:flex;background:#d9d3c0;border-radius:3mm;padding:0 .6mm;box-shadow:inset 0 0 0 .6mm #e8e2cf}
.pg{flex:1;height:100%;background:#fbf8ee;position:relative;padding:5mm 6mm 8mm;overflow:hidden}
.pg.r{border-radius:1mm 3mm 3mm 1mm;background:linear-gradient(to left,#fbf8ee 94%,#ece6d2)}.pg.l{border-radius:3mm 1mm 1mm 3mm;background:linear-gradient(to right,#fbf8ee 94%,#ece6d2);display:flex;gap:3mm}
.pn{position:absolute;bottom:2.5mm;width:8mm;height:8mm;border-radius:50%;background:#f1dcb4;text-align:center;line-height:8mm;font-weight:700;font-size:9pt;color:#4b5a3b}.r .pn{right:5mm}.l .pn{left:5mm}
.deco{position:absolute;bottom:3mm;left:50%;transform:translateX(-50%);font-size:11pt;opacity:.55}
.hd{text-align:center;font-weight:700;font-size:10.5pt;color:#2f4a38;border-bottom:.3mm solid #cdd8be;padding-bottom:1mm;margin-bottom:2mm}
.pill{background:#efe3c8;border-radius:5mm;padding:1.2mm 4mm;font-weight:700;color:#33492f;display:flex;align-items:center;gap:2mm;font-size:12pt}
.ico{display:inline-block;width:7mm;height:7mm;border-radius:50%;background:#e1ead2;text-align:center;line-height:7mm;font-size:10pt}
.row{display:flex;gap:3mm}.col{flex:1;min-width:0}
.code{border:.4mm solid #cdd8be;border-radius:3mm;padding:.8mm 4mm;font-size:8pt;text-align:center;background:#fff}.code b{display:block;font-size:11pt;color:#2f4a38;direction:ltr}
.ttl{font-size:19pt;font-weight:700;color:#1f3322;margin:1.5mm 0;display:flex;align-items:center;gap:2mm}
.hero{height:53mm;border-radius:3mm;background-size:cover;background-position:center;border:.5mm solid #fff;box-shadow:0 0 0 .3mm #d4dcc4}
.kc{background:#efe9d6;border-radius:3mm;padding:1.5mm 2.5mm;margin-bottom:1.6mm;display:flex;align-items:center;gap:2mm;font-size:8pt}.kc b{display:block;font-size:12pt;color:#1f3322}
.sec{background:#e9e0c6;border-radius:4mm;display:flex;align-items:center;gap:2mm;padding:.8mm 4mm;font-weight:700;font-size:10.5pt;color:#33492f;margin:2mm 0 1.2mm}
.sec.g{background:#7b9669;color:#fff}
table{width:100%;border-collapse:collapse;font-size:7.8pt}th{background:#dfe8cd;color:#2f4a38}th,td{border:.25mm solid #d5dcc6;padding:.8mm 1.6mm;background:#fffefa}td.n,th.n{text-align:center;white-space:nowrap}
table.i td{border-left:0;border-right:0}.tot td{background:#e3ecd0;font-weight:700}
.st{counter-reset:s;list-style:none;margin:0;padding:0;font-size:7.8pt;line-height:1.5}.st li{counter-increment:s;position:relative;padding:1.2mm 8mm 1.2mm 1.5mm;border-bottom:.25mm solid #e1e5d3}
.st li:before{content:counter(s);position:absolute;right:0;top:1.5mm;width:5.5mm;height:5.5mm;border-radius:50%;background:#e9e0c6;text-align:center;line-height:5.5mm;font-weight:700;font-size:8pt}
ul.b{margin:0;padding:0;list-style:none;font-size:7.8pt;line-height:1.5}ul.b li{padding-right:4mm;position:relative;margin:.5mm 0}ul.b li:before{content:'●';position:absolute;right:0;color:#6c8a58;font-size:6pt;top:1mm}
ul.c li:before{content:'☑';color:#4f7d3a;font-size:9pt;top:0}
.box{background:#fffefa;border:.3mm solid #d5dcc6;border-radius:3mm;padding:1.5mm 2.5mm}
.side{width:25mm;font-size:7pt;line-height:1.35;flex:none}.side .t{border:.3mm solid #d5dcc6;border-radius:3mm;text-align:center;padding:1mm;margin-bottom:1.5mm;font-weight:700;background:#fff}
.side .it{background:#efe3c8;border-radius:2mm;padding:.8mm 1.2mm;margin-bottom:1mm}.side .h{background:#e9e0c6;font-weight:700;border-radius:2mm;padding:1mm 1.5mm;margin:1.2mm 0}.side .s{padding:.6mm 1.2mm;color:#4f5c47}
.chips{display:flex;gap:1.5mm}.chip{flex:1;background:#efe9d6;border-radius:2.5mm;padding:1mm;text-align:center;font-size:7pt}.chip b{display:block;font-size:10pt;color:#1f3322}
.alg{display:flex;gap:2mm;align-items:center}.algt{background:#efe3c8;border-radius:3mm;padding:1.5mm 3mm;text-align:center;font-size:7.5pt;font-weight:700;min-width:25mm}.algt span{font-size:18pt;display:block}
.big table{font-size:9.5pt}.big td,.big th{padding:1.8mm 2mm}.big ul.b{font-size:9.6pt;line-height:1.75}.big p{font-size:10pt!important;line-height:1.85!important}.big .sec{font-size:12pt;margin:4mm 0 2mm}.big .pill{font-size:14pt}
.cover{width:297mm;height:210mm;background:radial-gradient(circle at 50% 40%,#3f6049,#233a2b);color:#f6efd8;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;page-break-after:always;position:relative;overflow:hidden}
.cover h1{font-size:44pt;margin:2mm 0}.cover .sub{font-size:16pt;color:#d9d2b2}.cover .ph{display:flex;gap:4mm;margin-top:8mm}.cover .ph img{width:23mm;height:23mm;border-radius:50%;border:1.2mm solid #f6efd8}
.cover .fr{position:absolute;inset:6mm;border:.5mm solid #c9b97a;border-radius:3mm}
"""
def hero(c): return f"background-image:url({b64('hero/'+c+'.jpg')})"
def sidebar(cur):
    s=f"<div class='side'><div class='t'>📖 محتويات القسم</div>"
    for k,n in CATN.items():
        if CAT[cur['code']]==k:
            s+=f"<div class='h'>{n}</div>"
            for o in data:
                if CAT[o['code']]==k:
                    cls='it' if o['code']==cur['code'] else 's'
                    s+=f"<div class='{cls}'><b style='direction:ltr;display:block'>{o['code']}</b>{o['ar']}</div>"
        else: s+=f"<div class='h'>{n} ◂</div>"
    s+="<div class='h'>الملاحق والجداول ◂</div></div>"
    return s
def hd(): return "<div class='hd'>الدليل الرئيسي للوصفات القياسية</div>"
def spread(right,left,rn,ln,big=False):
    z=' big' if big else ''
    return f"<div class='sp'><div class='book'><div class='pg r{z}'>{right}<div class='deco'>🌿</div><div class='pn'>{rn}</div></div><div class='pg l{z}'>{left}<div class='deco'>🌿</div><div class='pn'>{ln}</div></div></div></div>"
def recipe(i,o):
    c=o['code'];k=CAT[c];tm=TIMES[k];w=o['w']
    ing="".join(f"<tr><td>{EMO.get(n,'•')} {n}</td><td class='n'>{fg(g)}</td></tr>" for n,g in o['ing'])
    steps="".join(f"<li>{s}</li>" for s in o['steps'])
    qb="".join(f"<li>{x}</li>" for x in QB[k])+f"<li>الوزن النهائي المستهدف للوجبة: {w} جم ± 10 جم.</li>"
    right=f"""{hd()}<div class='row' style='align-items:center;margin-bottom:1mm'><div class='col'><div class='pill'><span class='ico'>📋</span>بطاقة الوصفة القياسية</div></div><div class='code'>رمز الوصفة:<b>{c}</b></div></div>
<div class='ttl' style='font-size:{19 if len(o["ar"])<26 else 15}pt'><span style='font-size:15pt'>🍽️</span>{o['ar']}</div>
<div class='row'><div class='col' style='flex:2.3'><div class='hero' style="{hero(c)};height:{53-max(0,len(o['ing'])-8)*2.6:.0f}mm"></div></div>
<div class='col' style='flex:1'><div class='kc'><span class='ico'>⚖️</span><div>الوزن النهائي المستهدف<b>{w} جم</b></div></div><div class='kc'><span class='ico'>🔥</span><div>السعرات التقديرية<b>{o['kcal']} سعرة</b></div></div><div class='kc'><span class='ico'>💪</span><div>البروتين<b>{o['P']-3}–{o['P']+3} جم</b></div></div></div></div>
<div class='row' style='margin-top:1mm'><div class='col'><div class='sec g'><span>🥗</span>المكونات</div><table class='i'><tr><th>المكوّن</th><th class='n'>الكمية للوجبة الواحدة</th></tr>{ing}</table></div>
<div class='col'><div class='sec g'><span>👨‍🍳</span>طريقة التحضير</div><ol class='st'>{steps}</ol></div></div>
<div class='row' style='margin-top:2mm'><div class='col'><div class='sec g' style='margin-top:0'><span>🏅</span>معيار الجودة</div></div></div><div class='box'><ul class='b'>{qb}</ul></div>"""
    # left page
    prot=[(n,g) for n,g in o['ing'] if n in PROT]; stars=[(n,g) for n,g in o['ing'] if n in STAR]
    pg=sum(g for n,g in prot); sg=sum(g for n,g in stars); vg=sum(g for n,g in o['ing'] if n in VEG)
    pn_={"صدر دجاج":"الدجاج","لحم بقري (ستيك)":"اللحم","لحم بقري مفروم":"اللحم المفروم","روبيان":"الروبيان","فيليه سمك":"السمك"}[prot[0][0]]
    sn_="الأرز (نيء)" if stars and stars[0][0].startswith("أرز") else "البطاطا"
    yr_="".join(f"<tr><td class='n'><b>{n} وجبة</b></td><td class='n'>{fg(pg*n)}</td><td class='n'>{fg(sg*n)}</td><td class='n'>{fg(vg*n)}</td><td class='n'>{fg(w*n)}</td></tr>" for n in (1,10,50,100))
    qc="".join(f"<li>{x.format(w=w)}</li>" for x in QC[k])
    kitchen=o['K']-o['raw']; fees=DELIV+(FEE+WASTE)*o['sub_net']
    cost=f"""<tr><td>تكلفة المواد الخام (تقديرية)</td><td class='n'>{r3(o['raw'])}</td></tr><tr><td>التشغيل والطهي لدى المطبخ</td><td class='n'>{r3(kitchen)}</td></tr><tr><td>التغليف والملصق</td><td class='n'>{r3(PACK)}</td></tr><tr><td>التوصيل والدفع والهدر</td><td class='n'>{r3(fees)}</td></tr><tr class='tot'><td>إجمالي التكلفة</td><td class='n'>{r3(o['sub_cost'])}</td></tr><tr class='tot'><td>سعر البيع (اشتراك)</td><td class='n'>{r3(o['sub'])}</td></tr><tr><td>هامش المساهمة بعد الضريبة</td><td class='n'>{r3(o['sub_profit'])} ({o['sub_m']:.0f}%)</td></tr><tr><td>سعر التطبيقات / الهامش</td><td class='n'>{r3(o['app'])} / {r3(o['app_profit'])}</td></tr>"""
    al=allergens(o)
    altile="".join(f"<div class='algt'><span>{e}</span>{n}</div>" for e,n in al) or "<div class='algt'><span>✅</span>لا مسببات حساسية رئيسية</div>"
    sb=[f"تحتوي الوصفة على: {o['alg']}." if o['alg']!='—' else "لا تحتوي الوصفة على مسببات حساسية رئيسية معلنة (يُتحقق من مكونات التوابل والصلصات).","يجب تحقيق درجة الحرارة الداخلية الآمنة: "+{'p':'الدجاج 74°م على الأقل.','m':'الستيك 63°م مع راحة 3 دقائق، والمفروم 71°م.','s':'السمك والروبيان 63°م على الأقل.'}[k],"تُحفظ المكوّنات والوجبة المبرّدة عند 0–4°م، وتُبرَّد الوجبة المطبوخة إلى أقل من 5°م خلال ساعتين.","الالتزام بإجراءات النظافة الشخصية وسلامة الغذاء أثناء التحضير والتخزين."]
    sbl="".join(f"<li>{x}</li>" for x in sb)
    left=f"""<div class='col' style='flex:1;min-width:0'>{hd()}<div class='pill' style='justify-content:center'><span class='ico'>⚙️</span>معايير التشغيل والإنتاج</div>
<div class='sec'><span>🍲</span>مخرجات الإنتاج (العائد) — وزن نيء</div>
<table><tr><th class='n'>حجم الإنتاج</th><th class='n'>{pn_}</th><th class='n'>{sn_}</th><th class='n'>الخضار والصوص</th><th class='n'>الوزن النهائي</th></tr>{yr_}</table>
<div class='chips' style='margin-top:1.5mm'><div class='chip'>تحضير 10 وجبات<b>{tm[0]} د</b></div><div class='chip'>زمن الطهي<b>{tm[1]} د</b></div><div class='chip'>الصلاحية المبرّدة<b>{tm[2]} ساعة</b></div><div class='chip'>إعادة التسخين<b>2–3 د</b></div></div>
<div class='row'><div class='col'><div class='sec'><span>✅</span>ضبط الجودة</div><ul class='b c'>{qc}</ul></div>
<div class='col'><div class='sec'><span>🪙</span>ملخص التكلفة (للوجبة)</div><table class='i'>{cost}</table><div style='font-size:6.5pt;color:#6b7a62;margin-top:.8mm'>سعر المطبخ مستهدف تفاوضي، ويُحدَّث بعد توقيع العقد.</div></div></div>
<div class='sec g'><span>🛡️</span>السلامة والحساسية</div><div class='alg'><div class='algbox' style='display:flex;gap:1.5mm'>{altile}</div><div class='col'><ul class='b' style='font-size:7.3pt;line-height:1.4'>{sbl}</ul></div></div></div>{sidebar(o)}"""
    return spread(right,left,6+2*i,7+2*i)
# ===== الصفحات =====
H=[f"<!doctype html><html lang='ar' dir='rtl'><meta charset='utf-8'><title>الدليل الرئيسي للوصفات القياسية</title><style>{FRAMECSS}</style><body>"]
circ="".join(f"<img src='{b64('img/'+o['code']+'.jpg')}'>" for o in data[:5]); circ2="".join(f"<img src='{b64('img/'+o['code']+'.jpg')}'>" for o in data[5:])
H.append(f"<div class='cover'><div class='fr'></div><div style='font-size:34pt'>🌿</div><h1>الدليل الرئيسي للوصفات القياسية</h1><div class='sub'>Master Recipe Book</div><div class='sub' style='margin-top:3mm;font-size:12pt'>بطاقات الوصفات · المقادير · معايير التشغيل والإنتاج · التكلفة · السلامة</div><div class='ph'>{circ}</div><div class='ph' style='margin-top:3mm'>{circ2}</div><div class='sub' style='margin-top:9mm;font-size:11pt'>برنامج اشتراكات التغذية الصحية · سلطنة عُمان · الإصدار 3.0 · نوفمبر 2026</div></div>")
# TOC spread
toc="".join(f"<tr><td class='n'><b style='direction:ltr;display:inline-block'>{o['code']}</b></td><td>{o['ar']}</td><td class='n'>{o['kcal']}</td><td class='n'>{o['P']}</td><td class='n'>{o['w']}</td><td class='n'>{6+2*i}</td></tr>" for i,o in enumerate(data))
R=f"""{hd()}<div class='pill' style='justify-content:center'><span class='ico'>📖</span>عن هذا الدليل</div>
<div class='sec g'><span>🎯</span>الغرض</div><p style='font-size:8.3pt;line-height:1.7;margin:1mm 0'>هذا الدليل هو <b>المرجع الفني الملزم</b> للمطبخ المتعاقد: يحدد لكل وجبة المقادير والوزن النهائي وطريقة التحضير ومعايير الجودة والسلامة، ويوحّد الإنتاج بحيث تتطابق الوجبة في كل مرة وفي أي مطبخ.</p>
<div class='sec g'><span>🗂️</span>كيف تقرأ بطاقة الوصفة</div><ul class='b'><li><b>الصفحة اليمنى:</b> بطاقة الوصفة (صورة، وزن، سعرات، بروتين، مكونات، خطوات، معيار الجودة).</li><li><b>الصفحة اليسرى:</b> معايير التشغيل والإنتاج (العائد لـ 1/10/50/100 وجبة، ضبط الجودة، التكلفة، السلامة والحساسية).</li><li>المقادير كلها <b>أوزان نيئة</b> للوجبة الواحدة، والوزن النهائي هو وزن الوجبة المعبأة بعد الطهي.</li><li>رمز الوصفة MRB-XX ثابت ويُكتب على الملصق وأوامر الإنتاج.</li></ul>
<div class='sec g'><span>⚠️</span>إخلاء مسؤولية</div><p style='font-size:7.8pt;line-height:1.6'>القيم الغذائية تقديرية من جداول مرجعية وتُراجع من أخصائي تغذية مرخّص وبالوزن الفعلي قبل طباعتها على العبوات. أسعار المطبخ في الدليل مستهدفة تفاوضية لا عقدية.</p>"""
L=f"""<div class='col'>{hd()}<div class='pill' style='justify-content:center'><span class='ico'>📑</span>فهرس الوصفات</div><table style='margin-top:2mm'><tr><th class='n'>الرمز</th><th>الوجبة</th><th class='n'>سعرات</th><th class='n'>بروتين جم</th><th class='n'>الوزن جم</th><th class='n'>الصفحة</th></tr>{toc}</table>
<div class='sec g'><span>📊</span>مفتاح الأقسام</div><ul class='b'><li>🍗 وصفات الدواجن: MRB-01، 02، 05، 07، 09</li><li>🥩 وصفات اللحوم: MRB-03، 06، 10</li><li>🐟 وصفات الأسماك والمأكولات البحرية: MRB-04، 08</li></ul></div>"""
H.append(spread(R,L,2,3,True))
# standards spread
R=f"""{hd()}<div class='pill' style='justify-content:center'><span class='ico'>🌡️</span>نقاط التحكم الحرجة (CCP)</div>
<table style='margin-top:2mm'><tr><th>المرحلة</th><th>الحد الحرج</th><th>الإجراء التصحيحي</th></tr>
<tr><td>استلام المواد الباردة</td><td>≤ 4°م (المجمّد ≤ −18°م)</td><td>رفض الشحنة المخالفة</td></tr>
<tr><td>طهي الدجاج</td><td>≥ 74°م داخلياً</td><td>إكمال الطهي وإعادة القياس</td></tr>
<tr><td>طهي ستيك اللحم</td><td>≥ 63°م + راحة 3 دقائق</td><td>إكمال الطهي</td></tr>
<tr><td>اللحم المفروم/الكرات</td><td>≥ 71°م</td><td>إكمال الطهي</td></tr>
<tr><td>السمك والروبيان</td><td>≥ 63°م</td><td>إكمال الطهي دون إفراط</td></tr>
<tr><td>التبريد بعد الطهي</td><td>أقل من 5°م خلال ساعتين</td><td>إتلاف ما تجاوز 4 ساعات</td></tr>
<tr><td>التخزين المبرّد</td><td>0–4°م</td><td>فحص الثلاجة وسجل الحرارة</td></tr>
<tr><td>التوصيل</td><td>≤ 5°م عند التسليم</td><td>استبدال الوجبة</td></tr></table>
<div class='sec g'><span>🧼</span>النظافة الشخصية</div><ul class='b'><li>غسل اليدين والقفازات والشبكة والمريلة لكل مشغّل.</li><li>فصل ألواح التقطيع واللحوم النيئة عن الجاهزة بألوان مميزة.</li><li>سجل صحي للعاملين وفحص دوري.</li></ul>"""
L=f"""<div class='col'>{hd()}<div class='pill' style='justify-content:center'><span class='ico'>📦</span>التعبئة والتخزين والتوصيل</div>
<div class='sec g'><span>🍱</span>التعبئة</div><ul class='b'><li>عبوات محكمة صالحة للمايكروويف وللتبريد، بحاجز للصوص عند الحاجة.</li><li>الأرز والبروتين والصوص بترتيب موحّد وفق صورة الوصفة.</li><li>الملصق: اسم الوجبة، الرمز، السعرات، البروتين، مسببات الحساسية، تاريخ الإنتاج والانتهاء، طريقة التسخين.</li></ul>
<div class='sec g'><span>🧊</span>التخزين والصلاحية</div><ul class='b'><li>الدواجن واللحوم: 72 ساعة عند 0–4°م. الأسماك والروبيان: 48 ساعة.</li><li>لا يُعاد تجميد الوجبة المبرّدة. تُعاد الوجبة المتأخرة عن موعدها إلى الإتلاف.</li><li>مبدأ FIFO (الأقدم أولاً) وسجل حرارة يومي.</li></ul>
<div class='sec g'><span>🚚</span>التوصيل</div><ul class='b'><li>حقائب تبريد وحرارة التسليم ≤ 5°م، ومدة النقل لا تتجاوز 90 دقيقة.</li><li>تسليم مجمّع بجدول أيام (يومان إلى أسبوع) حسب الاشتراك.</li></ul>
<div class='sec g'><span>📏</span>أدوات الإنتاج القياسية</div><ul class='b'><li>ميزان مطبخ دقيق (±1 جم) · مسبار حرارة · مغارف معايرة للصوص · قوالب أرز موحدة.</li><li>تتحقق إدارة الجودة من الوزن النهائي لعيّنة 5% من كل دفعة.</li></ul></div>"""
H.append(spread(R,L,4,5,True))
for i,o in enumerate(data): H.append(recipe(i,o))
# appendix
nut="".join(f"<tr><td class='n'><b style='direction:ltr;display:inline-block'>{o['code']}</b></td><td>{o['ar']}</td><td class='n'>{o['kcal']}</td><td class='n'>{o['P']}</td><td class='n'>{o['C']}</td><td class='n'>{o['F']}</td></tr>" for o in data)
pr="".join(f"<tr><td class='n'><b style='direction:ltr;display:inline-block'>{o['code']}</b></td><td class='n'>{r3(o['raw'])}</td><td class='n'>{r3(o['K'])}</td><td class='n'>{r3(o['n_max'])}</td><td class='n'>{r3(o['sub'])}</td><td class='n'>{r3(o['app'])}</td></tr>" for o in data)
R=f"""{hd()}<div class='pill' style='justify-content:center'><span class='ico'>🔬</span>الملحق أ: القيم الغذائية للوجبة</div><table style='margin-top:2mm'><tr><th class='n'>الرمز</th><th>الوجبة</th><th class='n'>سعرات</th><th class='n'>بروتين جم</th><th class='n'>كربوهيدرات جم</th><th class='n'>دهون جم</th></tr>{nut}</table>
<div class='sec g'><span>🧪</span>منهجية الحساب</div><p style='font-size:7.8pt;line-height:1.6'>سعرات ومغذيات كل مكوّن لكل 100 جم (جداول مرجعية للأغذية النيئة) × الوزن، ثم الجمع، والتقريب لأقرب 5 سعرات. هامش الخطأ المتوقع ±10%.</p>"""
alg_rows="".join(f"<tr><td class='n'><b style='direction:ltr;display:inline-block'>{o['code']}</b></td>"+"".join(f"<td class='n'>{'●' if any(k in (o['alg']+' '+o.get('alg2','')) for k in ks) else ''}</td>" for ks in (("ألبان",),("غلوتين",),("بيض",),("قشريات",),("أسماك",)))+"</tr>" for o in data)
L=f"""<div class='col'>{hd()}<div class='pill' style='justify-content:center'><span class='ico'>🪙</span>الملحق ب: التكلفة والتسعير (ر.ع)</div><table style='margin-top:2mm'><tr><th class='n'>الرمز</th><th class='n'>خام</th><th class='n'>مطبخ</th><th class='n'>حد أقصى</th><th class='n'>اشتراك</th><th class='n'>تطبيق</th></tr>{pr}</table>
<div class='pill' style='justify-content:center;margin-top:2mm'><span class='ico'>⚠️</span>الملحق ج: مصفوفة مسببات الحساسية</div><table style='margin-top:1.5mm'><tr><th class='n'>الرمز</th><th class='n'>🥛 ألبان</th><th class='n'>🌾 غلوتين</th><th class='n'>🥚 بيض</th><th class='n'>🦐 قشريات</th><th class='n'>🐟 أسماك</th></tr>{alg_rows}</table></div>"""
H.append(spread(R,L,26,27))
H.append("</body></html>")
open("master-recipe-book-v3.html","w").write("".join(H)); print("ok")
