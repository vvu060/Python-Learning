#Different Operations availabe on a Data Frame

import pandas as pd
import numpy as np
cars = pd.read_csv("C:/Users/Vishal/Downloads/cars.csv")
print(type(cars))
print(cars.head(10))
print(cars.tail(10))
print(cars.shape)
print(cars.info(null_counts=True))
print(cars.mean())
print(cars.median())
print(cars.std())
print(cars.max())
print(cars.min())
print(cars.count())
print(cars.describe())

----------------------------------------------------------------------------------------

#Cleaning the dataset

import pandas as pd
import numpy as np
cars = pd.read_csv("C:/Users/Vishal/Downloads/cars.csv")

#Renaming a Column
cars1 = cars.rename(columns={'Unnamed: 0': 'Make'})

#Fill the null values with mean of the column
#cars.qsec = cars.qsec.fillna(cars.qsec.mean())

#Dropping a Column
#cars1 = cars.drop(columns=['hp'])

#Find Correlation matrix
df = cars[['mpg', 'cyl', 'qsec']].corr()
print(df)

#Change the data type of a column
cars.mpg = cars.mpg.astype(float)

---------------------------------------------------------------------------------------------

#Manuplating the dataset

import pandas as pd
import numpy as np
cars = pd.read_csv("C:/Users/Vishal/Downloads/cars.csv")

print(cars.iloc[:,:])
print(cars.iloc[4:5,5:7])
print(cars.iloc[4:,4:])
print(cars.iloc[:5,:2])
print(cars.loc[4:,"qsec"])
print(cars.loc[4:,"am"])
print(cars.loc[4:6,"qsec":"am"])

#Set value of whole column to 1
cars['am'] = 1

#Douuble the records in a column using lambda function
f = lambda x:x*2
cars['am'] = cars['am'].apply(f)

#Sort data in ascending order
cars.sort_values(by = 'cyl')

#Sort data in descending order
cars.sort_values(by = 'cyl', ascending=False)

#Filter records with threshold value
cars['cyl'] > 6

#Applying filter to the dataframe
filter = cars['cyl'] > 6
filter_new = cars[filter]
print(filter_new)


#Applying 2 filters to the dataframe
filter = (cars['cyl'] > 6) & (cars['hp'] > 300)
filter_new = cars[filter]
print(filter_new)
 ----------------------------------------------------------------------------------------
