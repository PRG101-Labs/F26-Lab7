# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

# TO DO 1: Create numArray according to instructions given in readme.md file.

# TO DO 2: Perform the operations on numArray given in readme.md file.

# TO DO 3: Run the script.
# Creating a 1D NumPy array
import numpy as np

numArray=np.random.randint(0,100,100)
print(numArray)

print("\n First 10 numbers:\n",numArray[0:10])

print("\n Last 10 numbers:\n",numArray[-10:])

print('\n',numArray[21:51])

numArray[50:65]=101
print("\nArray after setting values from index 50 to 64 to 101:\n",numArray[45:70])
