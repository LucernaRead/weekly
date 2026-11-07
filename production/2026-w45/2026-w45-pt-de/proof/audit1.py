import re, glob, html, json, unicodedata, sys
BASE='/home/hatch/workspace/goals/lucernaread-social-media-operations'
ED=f'{BASE}/files/weekly-report-w45-pt-de/svg'
CO=f'{BASE}/files/weekly-report-w45-pt-core/svg'
W43=f'{BASE}/files/weekly-report-pt-de/svg'
def texts(path):
    t=open(path,encoding='utf-8').read()
    out=[]
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>',t,re.S):
        attrs,raw=m.group(1),html.unescape(m.group(2))
        x=re.search(r'x="([\d.]+)"',attrs); y=re.search(r'y="([\d.]+)"',attrs)
        out.append({'x':float(x.group(1)) if x else None,'y':float(y.group(1)) if y else None,'attrs':attrs,'t':raw})
    return out
def full(path):
    return ' '.join(x['t'] for x in texts(path))
def is_cjk(ch):
    o=ord(ch)
    return (0x4E00<=o<=0x9FFF or 0x3400<=o<=0x4DBF or 0x3040<=o<=0x30FF or 0xAC00<=o<=0xD7AF or 0xF900<=o<=0xFAFF)
FW=set('，。、；：？！（）【】《》「」『』～—…·')  # fullwidth punct approx; also check unicode category Pf/Po fullwidth ranges
def fw_count(s):
    n=0; chars=[]
    for ch in s:
        o=ord(ch)
        if 0xFF01<=o<=0xFF5E or o in (0x3001,0x3002,0x3008,0x3009,0x300A,0x300B,0x300C,0x300D,0x300E,0x300F,0x3010,0x3011,0xFF08,0xFF09,0xFF0C,0xFF1A,0xFF1B,0xFF1F,0xFF01):
            n+=1; chars.append(ch)
    return n,chars
EN=['the','and','with','from','your','this','that','have','has','will','would','can','should']
print("=== 1. CJK / fullwidth / English-function-word per page (edition) ===")
for pg in sorted(glob.glob(ED+'/*.svg')):
    name=pg.split('/')[-1]; s=full(pg)
    cjk=sum(1 for ch in s if is_cjk(ch))
    fw,fwc=fw_count(s)
    hits={w:len(re.findall(r'(?<![A-Za-zÀ-ÿ])'+w+r'(?![A-Za-zÀ-ÿ])',s,re.I)) for w in EN}
    hits={k:v for k,v in hits.items() if v}
    print(f"{name}: CJK={cjk} FW={fw}{fwc if fw else ''} EN={hits if hits else 0}")
print("=== core CJK per page ===")
for pg in sorted(glob.glob(CO+'/*.svg')):
    s=full(pg); print(pg.split('/')[-1], 'CJK=',sum(1 for ch in s if is_cjk(ch)))
print("=== 2. gloss() source counts: edition build vs core build ===")
import ast
def gloss_counts(builddir):
    # find gloss("...") calls in content files; attribute to page by file+order? Use per-file mapping:
    # content12 -> P1,P2 ; content34 -> P3,P4 ; content56 -> P5,P6 ; content7 -> P7 ; content8 -> P8
    # gloss calls appear in order; we need page attribution: parse file, split by page markers? Simpler: report per-file totals and per-call lists.
    res={}
    for f in ['content12.py','content34.py','content56.py','content7.py','content8.py']:
        src=open(f'{builddir}/{f}',encoding='utf-8').read()
        calls=re.findall(r'\.gloss\(\s*"((?:[^"\\]|\\.)*)"',src)
        calls=[c.encode().decode('unicode_escape') if '\\' in c else c for c in calls]
        res[f]=[(c, len([x for x in c.split('·') if x.strip()])) for c in calls]
    return res
for label,bd in [('ED-build',f'{BASE}/hidden_files/weekly-report-w45-pt-de-build'),('CORE-build',f'{BASE}/hidden_files/weekly-report-w45-pt-build')]:
    print('---',label)
    for f,lst in gloss_counts(bd).items():
        print(' ',f,'ncalls=',len(lst),'items-per-call=',[n for _,n in lst])
        for c,n in lst: print('    ',n,'|',c[:160])
