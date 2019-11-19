from PIL import Image
from numpy import asarray
import random

i = Image.open('images/test.png')
data = asarray(i)
size = i.size
pos = [random.randint(0, size[1]-3), random.randint(0, size[0]-3)]

with open('images/test.txt', 'w') as out3:
    for i in range(3):
        for j in range(3):
            pixel = data[pos[0]+i, pos[1]+j].tolist()
            out3.write(str(pixel)+'\n')

# with open('images/test.txt', 'w') as outfile:
#     for row in data:
#         outfile.write('# New row\n')
#         for pix in row:
#             pixel = pix.tolist()
#             rgb = '['+','.join(map(str, pixel))+']\n'
#             outfile.write(rgb)
#         outfile.write('\n')

# print(i.size)