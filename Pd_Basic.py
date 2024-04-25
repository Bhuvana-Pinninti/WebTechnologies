import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
print("Version of Pandas:",pd.__version__)

#loading dataset
ds = pd.read_csv("c:\\Users\\Bhuvana\\Desktop\\DSP_LAB\\Dataset.csv",na_values='?') # \ is considered as constant( use \\ for location )

#Creating a dataframe 
df = pd.DataFrame(ds)
#print(df.to_string())  #prints all rows




#Replacing default header
headers =["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors",
          "body-style","drive-wheels","engine-location","wheel-base",
          "length","width","height","curb-weight","engine-type",
          "num-of-cylinders","engine-size","fuel-system","bore","stroke",
          "compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price"
          ]
df.columns = headers

print(df.info())
print(df)

#print("After Adding headers:\n")
#print(df.head())


'''print("First five rows of the dataset:\n")
print(df.head())
print("\nLast Five ROws of the Dataset:\n")
print(df.tail())



#shape of the dataset
print("shape of the dataset is: ",df.shape)

#checking the datatypes
print('\nDatatypes of Dataset\n')
print(df.dtypes)

#information about the data
print("\n INFO OF THE DATA\n")
print(df.info())

#Return a statistical summary
print('\nStatistics\n')
print(df.describe())  #gives only the columns of dtype int64,float64 etc...(excpet object)

#return a full statistics
print('\n FUll Statistics\n')
print(df.describe(include='all'))


#INDEXING AND SLICING

print("\n***** INDEXING AND SLICING *******\n")
print("displaying makers\n",df["make"])
print("\ndisplaying makers and body-style\n",df[["make","body-style"]][0::50]) 

'''

#dropping null values
print("\nAfter dropping null values\n",df.dropna()) #does not change the dataframe
print('\nAfter dropping price null values\n',df.dropna(subset=['price'],axis=0))

#df.dropna(inplace=True) #make changes in the dataframe
#print(df)


#Replacing the null values
mean = df["normalized-losses"].mean() #replacing with average value (others - median, mode)
df["normalized-losses"]=df["normalized-losses"].replace(np.nan,mean) #df["normalized-losses"].fillna(mean,inplace=True)

print('\nAfter Replacing the missing values of normalized losses:\n',df)

print("\n\n After Data Cleaning\n")
df.info()
print(df)

#Data Formatting

#applying changes to entire col
df["city-mpg"] = 235/df["city-mpg"]
df.rename(columns={"city-mpg":"city-L/100km"},inplace=True)
print('\nAfter Applying changes\n',df)


#binning

bins=np.linspace(min(df['price']),max(df['price']),4)
group_labels = ["Low","Medium","High"]
df["price-binned"] = pd.cut(df["price"],bins,labels=group_labels,include_lowest=True)
print("\nAfter BInning\n",df)

#Categorical variables to numeric values
print(pd.get_dummies(df['fuel-type']))


# EXPLORATORY DATA ANALYSIS

print("\n\n ***** EDA *****\n")

#summarazing numerical values
print('Numerical values:\n')
print(df.describe())

#summarizing categorical values
print('\nCategorical Values\n')
drive_wheels_count = df['drive-wheels'].value_counts()

print(drive_wheels_count)



#box plots 
#sns.boxplot(x="drive-wheels",y="price",data=df)

#scatter plots - continuous data

x = df["engine-size"]
y = df["price"]
plt.scatter(x,y)
plt.title("Scatter Plot of engine size and price")
plt.xlabel("Engine size")
plt.ylabel("price")
#plt.show()

#group by

