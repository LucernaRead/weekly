import re
from collections import Counter
def load(p):
    c=Counter()
    for line in open(p,encoding='utf-8'):
        m=re.match(r'^\[(\S+)#\d+ [^\]]*\] (.*)$',line.rstrip('\n'))
        if m: c[(m.group(1),m.group(2))]+=1
        else: c[('?',line)]+=1
    return c
base1='/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-proofread-gates/texts'
base2='/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/en-proofread-gates-round2/texts'
for ed in ['core','de','es','fr','it','ja','ko','nl','pt','ru','zh-tw']:
    a=load(f'{base1}/texts-{ed}.txt'); b=load(f'{base2}/texts-{ed}.txt')
    d1=a-b; d2=b-a
    print(f"== {ed}: only-R1 {sum(d1.values())}, only-R2 {sum(d2.values())}")
    for k,v in sorted(d1.items()): print('  R1-only',v,k)
    for k,v in sorted(d2.items()): print('  R2-only',v,k)
