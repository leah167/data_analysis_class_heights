import pandas as pd
import matplotlib.pyplot as plt


'''
Using the class_heights.txt file and Pandas
1) Clean the data
2) Make column names Title Case
3) Sort gender column by Gender. Female first.
4) Convert heights to centimeters
5) Count how many of each gender are in the total class_heights
6) Calc the average height of each gender and the class total
7) Calc the median, mode, and standard deviantion for the total class
8) Plot female heights against male heights in matplotlib using different colors.
'''
# 1) Clean the data
# /Users/leahsanchez/Workspace/intro_to_python/class_heights.txt
df = pd.read_csv('/Users/leahsanchez/Workspace/intro_to_python/class_heights.txt')
# df = pd.DataFrame(df) -- Not neccesary

# 2) Make column names Title Case
df[['Gender', 'Height']] = df['gender|height'].str.split("|", expand=True)
df['Gender'] = df['Gender'].astype('string')
print('Df with before and after cleanup: ')
print(df)
df.pop('gender|height')
print('Part 1 and 2 done:')
print(df)

# 3) Sort gender column by Gender. Female first.
df = df.sort_values(by='Gender')

print(df['Gender'])
print(df.dtypes)
print('Part 3:')
print(df)

# 4) Convert heights to centimeters
# cm = [30.48, 2.54] --- just here for reference
df['Feet'] = df['Height'].apply(lambda x: int(x.split("'")[0]))
df['Inches'] = df['Height'].apply(lambda x: int(x.split("'")[1]))
print('Added columns separating Feet and Inches:')
print(df)
df['Feet(cm)'] = df['Feet'] * 30.48
df['Inches(cm)'] = df['Inches'] * 2.54
print('Added columns converting to cm: ')
print(df)
df['Height(cm)'] = df['Feet(cm)'] + df['Inches(cm)']
print('Created column for total height in cm: ')
print(df)
df.drop(['Height', 'Feet', 'Inches', 'Feet(cm)', 'Inches(cm)'], axis = 1, inplace = True)
print('Part 4 completed:')
print(df)

# 5) Count how many of each gender are in the total class_heights
print('Number of Females:', df['Gender'].value_counts()['female'])
print('Number of Males:', df['Gender'].value_counts()['male'])

# 6) Calc the average height of each gender and the class total
avg_heights = df.pivot_table('Height(cm)', columns='Gender')
avg_total = df['Height(cm)'].mean()
print('Average Heights Pivot Table: ')
print(avg_heights)
print('Class Total Average Height: ', avg_total)

# 7) Calc the median, mode, and standard deviantion for the total class
med_total = df['Height(cm)'].median()
print('Median Height(cm): ', med_total)

mode_total = df['Height(cm)'].mode()
print('Mode: ', mode_total)

std_total = df['Height(cm)'].std()
print('Standard Dev: ', std_total)   
print(df)    

# 8) Plot female heights against male heights in matplotlib using different colors.
# df.sort_values(by='Height(cm)', inplace=True)
# print('sorted:')
# print(df)
groupby_gender = df.groupby('Gender')
groupby_gender.boxplot(column='Height(cm)', subplots=False)
plt.title('Female v Male Heights')
# plt.show()

# df.groupby(['Gender'])['Height(cm)'].plot(legend=True) ---let's you plot two separate lines of diff color for m and f heights, but doesn't display data well.

'''
Using the class heights file from last class:
1) Plot the heights in cm as a line plot in matplotlib
2) Plot the average height of males against females in the class using a scatterplot in either seaborn or matplotlib
3) Create a separate column in the data frame to hold the difference from the mean height. Plot the difference from the mean against the heights on the same plot.

'''

# 1) Plot the heights in cm as a line plot in matplotlib
# d = df['Height(cm)'].drop_duplicates()

df['Height(cm)'].sort_index().plot(x='index', y='Height(cm)')
plt.title('Height(cm) of all students')
# plt.show()

# 2) Plot the average height of males against females in the class using a scatterplot in either seaborn or matplotlib
female = df.loc[lambda df: df['Gender'] == 'female'].sort_index() #Callable that returns a boolean Series
male = df.loc[lambda df: df['Gender'] == 'male'].sort_index()
print('female heights')
print(female)
print('male heights')
print(male)
f_avg = [female['Height(cm)'].mean().round(2)] * len(female['Height(cm)'])
print(f_avg)
m_avg = [male['Height(cm)'].mean().round(2)] * len(male['Height(cm)'])
print(m_avg)

plt.rcParams["figure.autolayout"] = True
plt.rcParams["figure.figsize"] = [10, 10]
fig, axes = plt.subplots(1,2, sharex=True, sharey=True)
plt.subplots_adjust(wspace=0, hspace=0)
plt.title('Female v Male Heights(cm) with averages')
axes[0].scatter(female.index, female['Height(cm)'],label='female heights')
axes[0].plot(female.index, f_avg, color='purple', lw=6, ls='--', label='average female height')
axes[0].legend(loc='upper left')
axes[0].set_xlabel('Student', fontsize=20)
axes[0].set_ylabel('Height(cm)', fontsize=20)

axes[1].scatter(male.index, male['Height(cm)'], color='green',label='male heights')
axes[1].plot(male.index, m_avg, color='pink', lw=6, ls='--', label='average male height')
axes[1].legend(loc='lower right')


plt.legend()
plt.show()

# 3) Create a separate column in the data frame to hold the difference from the mean height. Plot the difference from the mean against the heights on the same plot.
female['Diff from mean'] = female['Height(cm)'].mean() - female['Height(cm)']
print('female with new column')
print(female)
male['Diff from mean'] = male['Height(cm)'].mean() - male['Height(cm)']
print('male with new column')
print(male)
plt.scatter(female['Height(cm)'], female['Diff from mean'], color='purple', label='Female')
plt.scatter(male['Height(cm)'], male['Diff from mean'], color='pink', label='Male')
plt.title('difference from the mean against heights ')
plt.xlabel('Height(cm)')
plt.ylabel('Diff from mean')
plt.legend()
plt.show()




