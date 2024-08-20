import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('insurance.csv')

#prints data to check organizatiion
#print(df.head())
#print(df.info())

#checking the different regions
different_regions = df.region.unique()
#print(different_regions)

#checking for missing datat
null_data = df[df.isnull().any(axis=1)]
#print(null_data) empty results which is a good sign

# checks percentage differences between males and females
female_vs_male_counts = round(df['sex'].value_counts(normalize=True) * 100, 2)
print(f'Percentage between males and females:', female_vs_male_counts)

#calculates bmi 
total_bmi = df['bmi'].sum()
average_bmi = df['bmi'].mean()
print(f'Average BMI: {average_bmi:.2f}')
#calculates percent of smokers vs non-smokers
smokers_vs_nonsmokers_count = round(df['smoker'].value_counts(normalize=True) * 100, 2)
print(f'Percentage between smokers and non-smokers:',smokers_vs_nonsmokers_count)

# calculating total costs and average costs
total_charges = df['charges'].sum()
average_costs = df['charges'].mean()
print(f'Total costs: {total_charges:.2f}')
print(f'Average costs: {average_costs:.2f}')
# Calculates percentage of records by region, pretty similar across the boardd with a slight larger influence in the southeast region
counts_by_region = df['region'].value_counts(normalize=True) * 100
print(f'Customers per region: ', counts_by_region)


#calculating average insurance customer's age

average_age = round(df['age'].mean())
print(f'Average customer age:',average_age)
#describes the aggregates of different columns based on mean, standard deviation, minumum and maximum values as well as their points in-between
#print(df.describe())

#print(df.smoker)

#Distribution of charges by smoker status
sns.histplot(data=df, x='charges', hue='smoker', multiple='stack', bins=30)
plt.title('Distribution of Charges based on Smoking status')
plt.xlabel('Charges')
plt.ylabel('Frequency')
plt.show()

plt.clf()
# Average charges based on region
sns.boxplot(data=df, x='region', y='charges')
plt.title('Distribution of Average cost based on region')
plt.xlabel('Regional origin')
plt.ylabel('Charges per Region')
plt.show()