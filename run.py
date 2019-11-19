from cpicture import CPicture
import os

c = CPicture()
testdir = '/mnt/data/PycharmProjects/imagepixel/images/kitti/'

for file in os.listdir(os.fsencode(testdir)):
    filename = os.fsdecode(file)
    c.print33ToFile(testdir+filename, 'test4.txt')

# for i in range(10):
#     c.print33ToFile('test.png', 'test3.txt')
