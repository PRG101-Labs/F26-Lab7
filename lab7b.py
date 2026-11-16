# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Change Dimensions and create special arrays.
# Usage: ./lab7b.py

# TO DO 1: Copy the code from your lab7a.py file and paste here.

# TO DO 2: Reshape array1 reshapes array2 according to instructions given in readme.md file.

# TO DO 3: Create array5 according to instructions given in readme.md file.

# TO DO 4: Create array6 according to instructions given in readme.md file.

# TO DO 5: Run the script.

import numpy as np
array1=np.arange(20,50)
arr1_rshpe=np.reshape(array1,(5,6))
print(arr1_rshpe,'\n')

array2=np.array(range(20,50))
arr2_rshpe=np.reshape(array2,(2,3,5))
print(arr2_rshpe,'\n')

array5=np.diag([45, 7, 61, 8, 9])
print("Diagonal array: \n",array5)

array6=np.random.randn(7,7)
print("\n",array6)