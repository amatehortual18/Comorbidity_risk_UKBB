# Import libraries
import numpy as np
import pandas as pd
import csv
from datetime import datetime

folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'

save_healthy=folderRoot+'data/healthy.csv'
save_diseases=folderRoot+'data/diseases.csv'
save_CVD_before=folderRoot+'/data/patientsCVD_before.csv'
save_Depre_before=folderRoot+'/data/patientsDepre_before.csv'
save_Diabetes_before=folderRoot+'/data/patientsDiabetes_before.csv'

save_CVD_after=folderRoot+'/data/patientsCVD_after.csv'
save_Depre_after=folderRoot+'/data/patientsDepre_after.csv'
save_Diabetes_after=folderRoot+'/data/patientsDiabetes_after.csv'


save_Diabetes2CVD=folderRoot+'/data/patientsDiabetes2CVD.csv'
save_CVD2Diabetes=folderRoot+'/data/patientsCVD2Diabetes.csv'
save_Depre2CVD=folderRoot+'/data/patientsDepre2CVD.csv'
save_CVD2Depre=folderRoot+'/data/patientsCVD2Depre.csv'

save_onlyCVD=folderRoot+'/data/patientsonlyCVD.csv'
save_onlyDepre=folderRoot+'/data/patientsonlyDepre.csv'
save_onlyDiabetes=folderRoot+'/data/patientsonlyDiabetes.csv'


df=pd.read_csv(save_diseases)
healthy = pd.read_csv(save_healthy)

#print(healthy)
#print(df)

# Assuming df is your DataFrame
# Convert the date column to datetime if it's not already
df['date'] = pd.to_datetime(df['date'])

# Baseline date
threshold_date = pd.to_datetime('2011-01-01')
threshold_date_after = pd.to_datetime('2012-01-01')

# Set the word to search for in the other column
search_word = 'CVD'
# Filter rows based on conditions
before_cvd = df[(df['date'] < threshold_date) & (df['code'].str.contains(search_word))]
after_cvd = df[(df['date'] > threshold_date_after) & (df['code'].str.contains(search_word))]

# Set the word to search for in the other column
search_word = 'Depression'
# Filter rows based on conditions
before_depre = df[(df['date'] < threshold_date) & (df['code'].str.contains(search_word))]
after_depre = df[(df['date'] > threshold_date_after) & (df['code'].str.contains(search_word))]

# Set the word to search for in the other column
search_word = 'Diabetes'
# Filter rows based on conditions
before_diabetes = df[(df['date'] < threshold_date) & (df['code'].str.contains(search_word))]
after_diabetes = df[(df['date'] > threshold_date_after) & (df['code'].str.contains(search_word))]

cvd_depre = df[df['code'].str.contains('CVD') | df['code'].str.contains('Depression')]
cvd_diabetes = df[df['code'].str.contains('CVD') | df['code'].str.contains('Diabetes')]
depre_diabetes = df[df['code'].str.contains('CVD') | df['code'].str.contains('Depression')]


# before_cvd.to_csv(save_CVD_before, index = False, header=True)
# before_depre.to_csv(save_Depre_before, index = False, header=True)
# before_diabetes.to_csv(save_Diabetes_before, index = False, header=True)
# after_cvd.to_csv(save_CVD_after, index = False, header=True)
# after_depre.to_csv(save_Depre_after, index = False, header=True)
# after_diabetes.to_csv(save_Diabetes_after, index = False, header=True)


# CVD-DIABETES
filtered_df = df[df['code'].isin(['CVD', 'Diabetes'])]
filtered_df = filtered_df.groupby('eid').filter(lambda group: set(['CVD', 'Diabetes']).issubset(group['code'].values))
cvd_diabetes = filtered_df.sort_values(by=['eid']).reset_index(drop=True)
cvd_diabetes_id = cvd_diabetes['eid'].unique().tolist()

# CVD-DEPRESSION
filtered_df = df[df['code'].isin(['CVD', 'Depression'])]
filtered_df = filtered_df.groupby('eid').filter(lambda group: set(['CVD', 'Depression']).issubset(group['code'].values))
cvd_depre = filtered_df.sort_values(by=['eid']).reset_index(drop=True)
cvd_depre_id = cvd_depre['eid'].unique().tolist()

# DIABETES-DEPRESSION
filtered_df = df[df['code'].isin(['Diabetes', 'Depression'])]
filtered_df = filtered_df.groupby('eid').filter(lambda group: set(['Diabetes', 'Depression']).issubset(group['code'].values))
diabetes_depre = filtered_df.sort_values(by=['eid']).reset_index(drop=True)
diabetes_depre_id = (diabetes_depre['eid'].unique()).tolist()


# Step 1: Count occurrences of each 'eid'
eid_counts = df['eid'].value_counts()
# Step 2: Filter 'eid' values with only one occurrence
unique_eids = eid_counts[eid_counts == 1].index
# Step 3: Filter rows based on unique 'eid' values and 'code' containing only 'CVD'
only_CVD = df[(df['eid'].isin(unique_eids)) & (df['code'] == 'CVD')]
only_Depre = df[(df['eid'].isin(unique_eids)) & (df['code'] == 'Depression')]
only_Diabetes = df[(df['eid'].isin(unique_eids)) & (df['code'] == 'Diabetes')]

print('CVD: '+str(only_CVD))
print('DEPRE: '+str(only_Depre))
print('T2D: '+str(only_Diabetes))

df_v = pd.DataFrame({'ID': only_CVD['eid']})
df_v=df_v.reset_index(drop=True)
df_v.to_csv(save_onlyCVD, index = False, header=True)
del df_v

df_v = pd.DataFrame({'ID': only_Depre['eid']})
df_v=df_v.reset_index(drop=True)
df_v.to_csv(save_onlyDepre, index = False, header=True)
del df_v

df_v = pd.DataFrame({'ID': only_Diabetes['eid']})
df_v=df_v.reset_index(drop=True)
df_v.to_csv(save_onlyDiabetes, index = False, header=True)
del df_v
# Print or use the result_df as needed
#print(only_CVD)

print('run diab')
print(len(cvd_diabetes_id))
diabetes2cvd=[]
depre2cvd=[]
cvd2depre=[]
cvd2diabetes=[]


## Diabetes -> CVD
for i in range(len(cvd_diabetes_id)):
    cvd_diabetes_f = cvd_diabetes[cvd_diabetes['eid']== cvd_diabetes_id[i]]
    cvd_diabetes_cvd = cvd_diabetes_f[cvd_diabetes_f['code'].str.contains('CVD')]
    cvd_diabetes_diabetes = cvd_diabetes_f[cvd_diabetes_f['code'].str.contains('Diabetes')]

    cvd_diabetes_diabetes = cvd_diabetes_f[cvd_diabetes_f['code']== 'Diabetes']
    cvd_diabetes_cvd = cvd_diabetes_f[cvd_diabetes_f['code']== 'CVD']

    # Diabetes --> CVD
    condition_1 = cvd_diabetes_diabetes[cvd_diabetes_diabetes['date'] < threshold_date]
    condition_2 = cvd_diabetes_cvd[cvd_diabetes_cvd['date'] > threshold_date_after]
    if not condition_1.empty and not condition_2.empty:
        diabetes2cvd.append(condition_2['eid'].iloc[0])

    # CVD --> Diabetes
    condition_22 = cvd_diabetes_diabetes[cvd_diabetes_diabetes['date'] > threshold_date_after]
    condition_11 = cvd_diabetes_cvd[cvd_diabetes_cvd['date'] < threshold_date]
    if not condition_11.empty and not condition_22.empty:
        cvd2diabetes.append(condition_11['eid'].iloc[0])

    del condition_11
    del condition_22
    del condition_2
    del condition_1

## Depression -> CVD
for i in range(len(cvd_depre_id)):
    cvd_depre_f = cvd_depre[cvd_depre['eid']== cvd_depre_id[i]]
    cvd_depre_cvd = cvd_depre_f[cvd_depre_f['code'].str.contains('CVD')]
    cvd_depre_depre = cvd_depre_f[cvd_depre_f['code'].str.contains('Depression')]

    cvd_depre_depre = cvd_depre_f[cvd_depre_f['code']== 'Depression']
    cvd_depre_cvd = cvd_depre_f[cvd_depre_f['code']== 'CVD']

    # Depression --> CVD
    condition_1 = cvd_depre_depre[cvd_depre_depre['date'] < threshold_date]
    condition_2 = cvd_depre_cvd[cvd_depre_cvd['date'] > threshold_date_after]
    if not condition_1.empty and not condition_2.empty:
        depre2cvd.append(condition_2['eid'].iloc[0])

    # CVD --> Depression
    condition_22 = cvd_depre_depre[cvd_depre_depre['date'] > threshold_date_after]
    condition_11 = cvd_depre_cvd[cvd_depre_cvd['date'] < threshold_date]
    if not condition_11.empty and not condition_22.empty:
        cvd2depre.append(condition_11['eid'].iloc[0])


df_v = pd.DataFrame({'ID': diabetes2cvd})
df_v=df_v.reset_index(drop=True)

df_v2 = pd.DataFrame({'ID': cvd2diabetes})
df_v2=df_v2.reset_index(drop=True)

df_v.to_csv(save_Diabetes2CVD, index = False, header=True)
df_v2.to_csv(save_CVD2Diabetes, index = False, header=True)

del df_v, df_v2

df_v = pd.DataFrame({'ID': depre2cvd})
df_v=df_v.reset_index(drop=True)

df_v2 = pd.DataFrame({'ID': cvd2depre})
df_v2=df_v2.reset_index(drop=True)

df_v.to_csv(save_Depre2CVD, index = False, header=True)
df_v2.to_csv(save_CVD2Depre, index = False, header=True)

del df_v
df_v = pd.DataFrame({'ID': before_cvd['eid']})
df_v=df_v.reset_index(drop=True)
df_v.to_csv(save_CVD_before, index = False, header=True)

del df_v
df_v = pd.DataFrame({'ID': after_cvd['eid']})
df_v=df_v.reset_index(drop=True)
df_v.to_csv(save_CVD_after, index = False, header=True)


#
# print(cvd_diabetes_diabetes)
# if (pd.to_datetime(cvd_diabetes_diabetes['date']) < threshold_date) & (pd.to_datetime(cvd_diabetes_cvd['date']) > threshold_date_after):
#
#     diabetes2cvd.append(cvd_diabetes_cvd['eid'])
#
# print(diabetes2cvd)
# # Print or use the filtered DataFrame as needed
#print(filtered_df)


