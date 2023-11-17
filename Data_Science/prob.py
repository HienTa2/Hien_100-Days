import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the column names based on the attribute information provided earlier
column_names = [
    'party',
    'handicapped-infants',
    'water-project-cost-sharing',
    'adoption-of-the-budget-resolution',
    'physician-fee-freeze',
    'el-salvador-aid',
    'religious-groups-in-schools',
    'anti-satellite-test-ban',
    'aid-to-nicaraguan-contras',
    'mx-missile',
    'immigration',
    'synfuels-corporation-cutback',
    'education-spending',
    'superfund-right-to-sue',
    'crime',
    'duty-free-exports',
    'export-administration-act-south-africa'
]

# Read the CSV data into a DataFrame
df = pd.read_csv('house-votes-84.data', header=None, names=column_names)

# Replace '?' with NaN to mark missing values
df.replace('?', pd.NA, inplace=True)

# Check the first few rows of the DataFrame
print(df.head())

# Get information about the DataFrame
print(df.info())

# Get descriptive statistics of the DataFrame
print(df.describe())

# show the number of votes from both parties
plt.figure()
sns.countplot(x='el-salvador-aid', hue='party', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()

