# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Slice NumPy Arrays.
# Usage: ./lab7c.py

# TO DO 1: Create numArray according to instructions given in readme.md file.

# TO DO 2: Perform the operations on numArray given in readme.md file.

# TO DO 3: Run the script.
import numpy as np
slice_array=np.random.rand(100)

slice_1 = slice_array[1:10]
print(slice_1)

slice_2 = slice_array[90:]
print(slice_2)

slice_3 = slice_array[21:]