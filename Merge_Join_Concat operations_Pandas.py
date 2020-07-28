#SEIES OBJECT

import pandas as pd
data = [1,2,3,4]
series1 = pd.Seies(data)
print(series1)

#Changing the Index
import pandas as pd
data = [1,2,3,4]
series1 = pd.Series(data, index=['a','b','c','d'])
print(series1)

#Creating a Data Frame using List
import pandas as pd
data = [1,2,3,4]
df = pd.DataFrame(data)
print(df)

#Creating a Data Frame using Dictionary
import pandas as pd
dictionary = {'Fruits': ['Apple','Orange','Mango','Banana'], 'Count':[10,15,7,20]}
df = pd.DataFrame(dictionary)
print(df)

#Creating a Data Frame using Seies
import pandas as pd
series1 = pd.Series([2,3], index=['a','b'])
df = pd.DataFrame(series1)
print(df)

#Creating a Data Frame using Numpy Array
import pandas as pd
import numpy as np
numpy_array = np.array([[50000,60000],['Vishal', 'Guru']])
df = pd.DataFrame({'Name':numpy_array[1], 'Salary':numpy_array[0]})
print(df)

-------------------------------------------------------------------------------------------------------------

# MERGE OPERATIONS

import pandas as pd
import numpy as np
player = ['Player1','Player2','Player3']
points = [10,20,30]
title = ['Game1','Game2','Game3']
df1 = pd.DataFrame({'Player':player, 'Points':points, 'Title':title})
print(df1)

player = ['Player1','Player4','Player5']
power = ['Fly', 'Heal', 'Lightning']
title = ['Game1','Game4','Game5']
df2 = pd.DataFrame({'Player':player, 'Power':power, 'Title':title})
print(df2)

#Inner Merge
print(df1.merge(df2, how="inner", on='Player'))
print(df1.merge(df2, how="inner", on='Title'))
print(df1.merge(df2))

#Left Merge
print(df1.merge(df2, how="left", on='Player'))

#Right Merge
print(df1.merge(df2, how="right", on='Player'))

#Outer Merge
print(df1.merge(df2, how="outer", on='Player'))

-----------------------------------------------------------------------------------------------

#JOIN OPERATIONS

import pandas as pd
import numpy as np
player = ['Player1','Player2','Player3']
points = [10,20,30]
title = ['Game1','Game2','Game3']
df1 = pd.DataFrame({'Player':player, 'Points':points, 'Title':title}, index=['L1','L2','L3'])
print(df1)

players = ['Player1','Player4','Player5']
power = ['Fly', 'Heal', 'Lightning']
titles = ['Game1','Game4','Game5']
df2 = pd.DataFrame({'Players':player, 'Power':power, 'Titles':title}, index=['L2','L3','L4'])
print(df2)

#Inner Join
print(df2.join(df1,how='inner',on=None))

#Left Join
print(df2.join(df1,how='left'))


#Right Join
print(df2.join(df1,how='right'))

#Outer Join
print(df2.join(df1,how='outer'))

---------------------------------------------------------------------------------------------------

#CONCATINATE OPERATIONS

import pandas as pd
import numpy as np
player = ['Player1','Player2','Player3']
points = [10,20,30]
title = ['Game1','Game2','Game3']
df1 = pd.DataFrame({'Player':player, 'Points':points, 'Title':title}, index=['L1','L2','L3'])
print(df1)

players = ['Player1','Player4','Player5']
power = ['Fly', 'Heal', 'Lightning']
titles = ['Game1','Game4','Game5']
df2 = pd.DataFrame({'Players':player, 'Power':power, 'Titles':title}, index=['L2','L3','L4'])
print(df2)

print(pd.concat([df1,df2]))

--------------------------------------------------------------------------------------------------

