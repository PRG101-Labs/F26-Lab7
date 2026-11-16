# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Marcus Lau
# Date: 2026/11/11
# Purpose: Create Arrays.
# Usage: ./lab7a.py

# TO DO 1: Create array1 and array2 according to instructions given in readme.md file.

# TO DO 2: Create array3 according to instructions given in readme.md file.

# TO DO 3: Create array4 according to instructions given in readme.md file.
import numpy as np
array1=np.arange(20,50)
print("1D array: ",array1)

array2=np.array(range(20,50))
print(array2,'\n')

grid=[[num+(row*3)+1 for num in range(3)]for row in range(3)]

array3=np.array(grid)
print("3D array: \n",array3)

array4=np.array([
    [
        ["January, February, March"],
        ["April, May, June"],
        ["July, August, September"],
        ["October, November, December"]
    ]
])
print(array4)