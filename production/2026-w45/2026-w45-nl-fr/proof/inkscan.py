import re, sys
from PIL import ImageFont
FONTS={
 ('Noto Serif CJK SC', False): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc",2),
 ('Noto Serif CJK SC', True): ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc",2),
 ('Noto Sans CJK SC', False): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",2),
 ('Noto Sans CJK SC', True): ("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",2),
 ('UnifrakturMaguntia', False): ("/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf",0),
 ('UnifrakturMaguntia', True): ("/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf",0),
}
_cache={}
def font(family, bold, size):
    k=(family,bold,size)
    if k not in _cache:
        p,idx=FONTS[(family,bold)]
        _cache[k]=ImageFont.truetype(p, int(round(size)) if float(size)==int(float(size)) else size, index=idx) if False else ImageFont.truetype(p, size, index=idx)
    return _cache[k]
def elems(path):
    t=open(path,encoding='utf-8').read()
    out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', t, re.S):
        attrs=m.group(1); s=re.sub(r'<[^>]+>','',m.group(2)).replace('&amp;','&').replace('&lt;','<').replace('&gt;','>')
        def a(n):
            mm=re.search(n+r'="([^"]*)"',attrs); return mm.group(1) if mm else ''
        if not a('x') or not a('y'): continue
        f=font(a('family'), a('weight')=='700', float(a('size')))
        bb=f.getbbox(s, anchor='ls')
        adv=f.getlength(s)
        x=float(a('x')); y=float(a('y')); anch=a('anchor') or 'start'
        if anch=='middle': x0=x-adv/2
        elif anch=='end': x0=x-adv
        else: x0=x
        out.append({'x0':x0+bb[0],'x1':x0+bb[2],'yt':y+bb[1],'yb':y+bb[3],'y':y,'x':x,'size':a('size'),'text':s,'anchor':anch})
    return out
def scan(path):
    es=elems(path)
    by={}
    for e in es: by.setdefault(e['y'],[]).append(e)
    bad=[]
    for y,group in sorted(by.items()):
        group=sorted(group,key=lambda e:e['x0'])
        for a,b in zip(group,group[1:]):
            gap=b['x0']-a['x1']
            if gap<2.0:
                bad.append((y,gap,a['text'][:60],b['text'][:60],round(a['x1'],1),round(b['x0'],1)))
    return bad
if __name__=='__main__':
    for path in sys.argv[1:]:
        bad=scan(path)
        print(f'== {path}: same-baseline pairs with gap<2px: {len(bad)}')
        for row in bad: print('  y=%s gap=%.2f | %r || %r | x1=%s x0=%s'%row)
