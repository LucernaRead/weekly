from PIL import Image
import glob

im = Image.open('files/weekly-report-w45-de-ko/cards/p1-front.png')
print('p1 card size:', im.size)
crop = im.crop((1400, 1400, 1950, 1480)).resize((550 * 3, 80 * 3), Image.NEAREST)
crop.save('hidden_files/w45/de-ko-proof/p1-row1436-zoom.png')
print('saved zoom')
for f in sorted(glob.glob('files/weekly-report-w45-de-ko/cards/*.png')):
    print(f.split('/')[-1], Image.open(f).size)
