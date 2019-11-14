from PIL import Image
from numpy import asarray

i = Image.open('images/image4995.png')
data = asarray(i)

with open('images/image4995.txt', 'w') as outfile:
    for row in data:
        outfile.write('# New row\n')
        for pix in row:
            pixel = pix.tolist()
            rgb = '['+','.join(map(str, pixel))+']\n'
            outfile.write(rgb)
        outfile.write('\n')