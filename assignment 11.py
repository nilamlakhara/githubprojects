import numpy as np
import pandas as pd

# Name: Neelam
#Generate ten random numbers
np.random.seed(42)
data = np.random.randint(1, 101, 10)

print("Name: Neelam")
print("Random Numbers:")
print(data)

#  Convert the numbers into a Pandas Series
s = pd.Series(data)

print("\nPandas Series:")
print(s)