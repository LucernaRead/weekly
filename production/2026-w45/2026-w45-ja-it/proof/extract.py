import re, sys, xml.etree.ElementTree as ET
NS='{http://www.w3.org/2000/svg}'
def texts(path):
    out=[]
    tree=ET.parse(path)
    for el in tree.iter():
        if el.tag.endswith('text'):
            t=''.join(el.itertext())
            out.append((float(el.get('x',0)), float(el.get('y',0)), el.get('font-size'), t))
    return out
def alltext(path):
    return ''.join(t for _,_,_,t in texts(path))
if __name__=='__main__':
    import json
    d=sys.argv[1]
    for p in ['p1-hyoushi','p2-kurashi','p3-bunka','p4-supotsu','p5-wakamono','p6-fukayomi','p7-kotoba','p8-tesuto']:
        ts=texts(f'{d}/svg/{p}.svg')
        print(p, 'elements:', len(ts), 'chars:', sum(len(t) for *_,t in ts))
