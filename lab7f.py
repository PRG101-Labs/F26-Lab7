# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Create Data Frames.
# Usage: ./lab7f.py

# TO DO 1: Create dataframe from provided dictionaries in readme.md file.

# TO DO 2: create a data frame provided in dataframe.jpg file.

# TO DO 3: Run the script.
import pandas as pd
# this wont work so use : pip install numpy
dict1={"Apple": "Green", "Carrot": "Red", "Radish": "Purple"}
dict2={'Okra': 'Thin', 'Potato': 'blob', 'Radish': 'Round'}
dict3={'Apple': 2.1, 'Okra': 3.5, 'Carrot': 1.3, 'Potato': 2.0, 'Radish': 3.0}

fruits={"color":dict1,"shape":dict2,"weight":dict3}
fruit_stuff = pd.DataFrame(fruits)
