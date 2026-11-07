# Rebuild web PDF from DELIVERY cards with the render.py recipe (Pillow default quality, optimize=True), in scratch only.
import os
from PIL import Image
CARDS='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-es/cards'
OUT='/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/fr-es-proof/work/webcheck'
names=['p1-une.png','p2-vie.png','p3-culture.png','p4-sport.png','p5-jeunesse.png','p6-politique.png','p7-langue.png','p8-exercices.png']
imgs=[]; tmp=os.path.join(OUT,'.webpage.jpg')
for n in names:
    im=Image.open(os.path.join(CARDS,n)).convert('RGB')
    im.save(tmp,'JPEG',optimize=True)
    imgs.append(Image.open(tmp).copy())
os.remove(tmp)
web=os.path.join(OUT,'Le-Lucerna-VOL3-ES-web.pdf')
imgs[0].save(web, save_all=True, append_images=imgs[1:], resolution=150.0)
print('candidate:', web, os.path.getsize(web))
