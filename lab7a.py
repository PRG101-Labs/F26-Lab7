# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Eliana Seymour
# Date: November 11, 2026
# Purpose: Create Arrays.
# Usage: ./lab7a.py

# TO DO 1: Create array1 and array2 according to instructions given in readme.md file.

# TO DO 2: Create array3 according to instructions given in readme.md file.

# TO DO 3: Create array4 according to instructions given in readme.md file.

import numpy as np
array1=np.array([20,43,36,45,49,21,25,28,32])
print(array1)
array2=np.arange(20 , 40 + 1)
print(array2)

array3=np.arange(1,9+1).reshape(3,3)
print(array3)

array4=np.array([["January","February","March"], ["April","May","June"]], [["July","August","September"], ["October", "November", "December"]], dtype="string")
print(array4)