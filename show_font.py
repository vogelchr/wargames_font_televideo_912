#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

fn = 'A3-2.bin'

img = np.frombuffer(open(fn,'rb').read(),dtype=np.uint8)

###
# assume 8x8 pixels
###

xyz_arr = list()

for c in range(256) :
        char_y = 10 * (c // 16 )
        char_x = 10 * (c % 16 )

        for line in range(8) :
                if line == 7 :
                        d = img[c*8]
                else :
                        d = img[c*8 + (line+1)]

                # after studying the schematic, I'm only halfway sure
                # how this works, and also the 3029900 Maintenance Training
                # Manual Mar1983 seems to refer to a slightly different version
                # of the circuit, also the ROM is loaded into the character
                # generation RAM by the firmware, so some bit-flipping may
                # happen there, too.

                # Basically there are two bits that define whether a delayed
                # or a non-delayed version of the graphics bit is output, and
                # depending on whether we are in the right or the left half of
                # the bit pattern.

                # this is visible with lower case letters: bpqh where ther's
                # straight part (not to be delayed) and a courvy part.

                for bit in range(6) :
                        bitoffs = 0.5
                        if bit >= 3 and (d & 0x01) :
                                bitoffs = 0
                        if bit < 3 and (d & 0x02) :
                                bitoffs = 0

                        x = float(char_x + bit + bitoffs)
                        y = float(char_y + line)
                        if d & (1<<(7-bit)) :
                                xyz_arr.append( (x, y, (d & 0x03) ))

xyz_arr = np.array(xyz_arr, dtype=[('x','f'),('y','f'),('c', 'f')])

plt.close('all')
fig, ax = plt.subplots()
ax.set_title(fn)
ax.invert_yaxis()
ax.set_xlabel('Pixel Number, Characters Low Nibble')
ax.set_ylabel('Line Number, Characters High Nibble')

mesh = ax.scatter(xyz_arr['x'], xyz_arr['y'], c=xyz_arr['c'])
fig.colorbar(mesh, label='Low 2 Bits of Bit Pattern')

fig.show()
plt.show()