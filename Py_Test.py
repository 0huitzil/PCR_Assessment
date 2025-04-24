#%%
from Py_Segments import segLengths
from itertools import product
from numpy import round
import pandas as pd
pd.options.display.max_colwidth = 999 #To make sure the arrays are shown in their entirety
S1 = [0.7, 1, 5] #List of S1 values 
S2 = [2, 10] #List of S2 values 
L = [0.6, 10, 22.7] #List of L Values
# Creation of the dataframe with all posible combinations of S1, S2 and L
df = pd.DataFrame(list(product(S1, S2, L)), columns=['S1', 'S2', 'L'])
# Creation of the element length arrays
df['elemLengths'] = df.apply(lambda x: segLengths(x['S1'], x['S2'], x['L']), axis=1)
# Counting the number of elements used by the algorithm 
df['numElems'] = df.apply(lambda x: len(x['elemLengths']), axis=1)
# Adding up the lengths of the elements used to compare to L
df['totalLength'] = df.apply(lambda x: sum(x['elemLengths']), axis=1)
# Switching column places for easier visualization
df = df.reindex(columns=['S1', 'S2', 'L', 'numElems', 'totalLength', 'elemLengths'])
# Finally, rounding up the array values for visualization purposes
df['elemLengths'] = df['elemLengths'].apply(lambda x: round(x, 2))

print(df)