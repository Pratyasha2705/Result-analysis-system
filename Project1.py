import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("student_scores.csv")
print(df.head())
df.describe()
df.info()
df.isnull().sum()
df.drop("Unnamed: 0",axis=1)

#change things in weekly hour
df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct","5-10")
df.head()

#from this we get to now the number of female and male 
#from observation we see that female is more
plt.figure(figsize=(5,5))
ax=sns.countplot(data=df,x="Gender")
ax.bar_label(ax.containers[0])
plt.show()


#from this we get to know that there is more impact of parent education on their child education
gb = df.groupby("ParentEduc").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb)

#from heatMap we get to analysis easily through photos and chart
plt.figure(figsize=(5,5))
sns.heatmap(gb,annot=True)
plt.show()

#here we will see that is there is impact of parent relation on child studies
gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":"mean","ReadingScore":"mean","WritingScore":"mean"})
print(gb)

#we get to now that there is negligible impact
plt.figure(figsize=(5,5))
sns.heatmap(gb1,annot=True)
plt.show()

#to check the outlier and same we can check for WritingScore and MathScore and many more 
sns.boxplot(data=df,x="ReadingScore")
plt.show()

#print unique ethinic groups
print(df["EthnicGroup"].unique())


#to see number of students in each ethinic group through the pie chart and through percentages also.
groupA = df.loc[(df["EthnicGroup"]=="group A")].count()
groupB = df.loc[(df["EthnicGroup"]=="group B")].count()
groupC = df.loc[(df["EthnicGroup"]=="group C")].count()
groupD = df.loc[(df["EthnicGroup"]=="group D")].count()
groupE = df.loc[(df["EthnicGroup"]=="group E")].count()

l=["group A","group B","group C","group D","group E"]
mylist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
print(mylist)
plt.pie(mylist,labels=l,autopct="%1.2f%%")
plt.show()

#to check if the number give above is correct or not 
ax=sns.countplot(data=df, x="EthnicGroup")
ax.bar_label(ax.containers[0])




#and we can do many more analysis like this only 