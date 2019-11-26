from PIL import Image
from numpy import asarray
import random
import requests

class CPicture:
    imageData = 'images/'

    def randomPicture(self):
        response = requests.get("https://picsum.photos/200/300.jpg")
        name = response.url[25:-12]

        f = open(self.imageData + 'picsum/' + name + '.jpg', 'wb')
        f.write(response.content)
        f.close()

        # response = requests.get("https://source.unsplash.com/random")


    def listsToString(self, lista):
        strr = ''
        for l in lista:
            for i in l:
                strr = strr + str(i) + ','
        return strr[0:-1]

    def print33ToFile(self, image, target):
        i = Image.open(image)
        data = asarray(i)
        size = i.size
        pos = [random.randint(0, size[1] - 3), random.randint(0, size[0] - 3)]
        with open(self.imageData+target, 'a') as out3:
            L = []
            for i in range(3):
                for j in range(3):
                    pixel = data[pos[0] + i, pos[1] + j].tolist()
                    L.append(pixel)
            out3.write(image+','+self.listsToString(L)+'\n')
