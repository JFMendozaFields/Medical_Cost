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
female_vs_male_counts = round(df['sex'].value_counts('female'), 2)
print(f'Percentage between males and females',female_vs_male_counts)

smokers_vs_nonsmokers_count = round(df['smoker'].value_counts('no'), 1)
print(f'Percentage between smokers and non-smokers:',smokers_vs_nonsmokers_count)

# calculating total costs and average costs
total_charges = 0
for charge in df['charges']:
    total_charges += charge
total_charges = round(total_charges, 2)
print(f'total costs:', total_charges)
average_costs = round(total_charges / len(df['charges']), 2)
print(f'total costs:',average_costs)

# Calculates percentage of records by region, pretty similar across the boardd with a slight larger influence in the southeast region
counts_by_region = round(df['region'].value_counts('northeast'), 2)
print(f'Customers per region:',counts_by_region)


#calculating average insurance customer's age
total_ages = 0
for age in df.age:
    total_ages += age
#print(total_ages)
average_age = round(total_ages / len(df.age))
print(f'Average customer age:',average_age)
#describes the aggregates of different columns based on mean, standard deviation, minumum and maximum values as well as their points in-between
#print(df.describe())

#print(df.smoker)

unpivoted_data = df.groupby(['region', 'sex', 'smoker'].mean().reset_index())
print(unpivoted_data)