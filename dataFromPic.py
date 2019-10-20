from PIL import Image
import numpy as np

i = Image.open('images/image4995.png')
data = np.asarray(i)
# np.savetxt('images/image4995.txt', iar)

with open('images/image4995.txt', 'w') as outfile:
    # I'm writing a header here just for the sake of readability
    # Any line starting with "#" will be ignored by numpy.loadtxt
    outfile.write('# Array shape: {0}\n'.format(data.shape))

    # Iterating through a ndimensional array produces slices along
    # the last axis. This is equivalent to data[i,:,:] in this case
    for data_slice in data:
        outfile.write('# New row\n')
        # The formatting string indicates that I'm writing out
        # the values in left-justified columns 7 characters in width
        # with 2 decimal places.
        np.savetxt(outfile, data_slice, fmt=repr(['%d', '%d', '%d', '%d']), newline='\n')

        # Writing out a break to indicate different slices...
        outfile.write('\n')