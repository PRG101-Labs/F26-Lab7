# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Create Series.
# Usage: ./lab7e.py

# TO DO 1: Import pandas module.

# TO DO 2: Create a series according to instructions given in readme.md file.

# TO DO 3: Perform the operations on this series given in readme.md file.

# TO DO 4: Run the script.

import pandas as pd
grade_list=["<50", "50-59", "60-69", "70-79", "80-89", "90-100"]
grades.pdSeries(grade_list,index=["F", "D", "C", "B", "A", "A+"])
print(grades)
print(grades.loc[["C","A+"]])
print(grades.iloc[2])