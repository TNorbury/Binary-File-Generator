import random
import struct

fileToOpen = "binaryData"

# The max file size should be in kb
maxFileSize = 1024

# The number of line (chunks of data) is equal to the number of bits in the file / 16
numLines = (maxFileSize * 1024) / 16

# Open the file to write to and begin to write to it
with open(fileToOpen, 'wb') as output:

   # Write numLines chunks of data to the file
   for x in range(0, numLines):
      # Create a random sequence of 16 bits, with the first 12 all being set to 1
      dataToWrite = 1048560 + random.randint(0, 15)
      output.write(struct.pack("=i", dataToWrite))
      output.write("\n")

