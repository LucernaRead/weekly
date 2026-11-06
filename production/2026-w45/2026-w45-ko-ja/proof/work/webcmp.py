from PIL import Image
import numpy as np, glob
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
cards=["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"]
for i,c in enumerate(cards):
    web=np.asarray(Image.open(f"{BASE}/hidden_files/w45/ko-ja-proof/work/webimg/p-{i:03d}.png").convert("RGB"), dtype=np.int16)
    card=Image.open(f"{BASE}/files/weekly-report-w45-ko-ja/cards/{c}.png").convert("RGB").resize((web.shape[1], web.shape[0]), Image.LANCZOS)
    ca=np.asarray(card, dtype=np.int16)
    d=np.abs(web-ca)
    s=d.sum(axis=2)
    print(f"p{i+1}: websize={web.shape[1]}x{web.shape[0]} mean_sum3={s.mean():.2f} mean_perchan={d.mean():.2f} frac>30(full)={(s>30).mean()*100:.3f}% frac>30(stride2)={(s[::2,::2]>30).mean()*100:.3f}% max={s.max()}")
# control: p1 web vs p2 card
web=np.asarray(Image.open(f"{BASE}/hidden_files/w45/ko-ja-proof/work/webimg/p-000.png").convert("RGB"), dtype=np.int16)
card=Image.open(f"{BASE}/files/weekly-report-w45-ko-ja/cards/p2-saenghwal.png").convert("RGB").resize((web.shape[1], web.shape[0]), Image.LANCZOS)
d=np.abs(web-np.asarray(card, dtype=np.int16)); s=d.sum(axis=2)
print(f"CONTROL p1web vs p2card: mean_sum3={s.mean():.2f} frac>30={(s>30).mean()*100:.3f}%")
