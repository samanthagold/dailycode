# Python basics - 
# material: https://rebeccabarter.com/blog/2023-09-11-from_r_to_python#pandas-data-frames


# library() equivalent 
import numpy as np 
import pandas as pd 

# when using a function within a library, you need to 
# make sure to include the library that it comes from
# even AFTER loading it...
np.sqrt(7) 

# generating a dataframe 
pandas_df = pd.DataFrame({'a': [1,2,3,4], 
                          'b': [5,6,7,8]})
pandas_df

# lists 
my_py_list = [1, [1,2], [3,4], ['a', 'b', 'c']]
my_py_list

# indexing: python uses 0-indexing whereas R doesn't 
# my_py_list[[1]] in R is equal to my_py_list[0]
my_py_list[0]

# dictionaries are named list. the above dataframe is a 
# dictionary. 
pandas_df['a']
pandas_df['b']
# you can't extract things positionally in a dictionary aka 
# you can't do pandas_df[0]. but you can do this
pandas_df['a'][0]

# methods 
pandas_df.mean()
# object.function() 
# if you want to get the mean of each column, you need to use 
# the following syntax. 

#something to note: 
