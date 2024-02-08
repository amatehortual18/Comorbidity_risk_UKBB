import pandas as pd
import numpy as np
import re


folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'

file_ukbb='ukb46359.csv'   # ukb669914.csv   ukb46359.csv

save_healthy=folderRoot+'data/healthy.csv'

save_Diabetes2CVD=folderRoot+'/data/patientsDiabetes2CVD.csv'
save_CVD2Diabetes=folderRoot+'/data/patientsCVD2Diabetes.csv'
save_Depre2CVD=folderRoot+'/data/patientsDepre2CVD.csv'
save_CVD2Depre=folderRoot+'/data/patientsCVD2Depre.csv'

save_onlyCVD=folderRoot+'/data/patientsonlyCVD.csv'
save_onlyDepre=folderRoot+'/data/patientsonlyDepre.csv'
save_onlyDiabetes=folderRoot+'/data/patientsonlyDiabetes.csv'

# to save
save_Diabetes2CVD_c=folderRoot+'/data2/Diabetes2CVD_class.csv'
save_CVD2Diabetes_c=folderRoot+'/data2/CVD2Diabetes_class.csv'
save_Depre2CVD_c=folderRoot+'/data2/Depre2CVD_class.csv'
save_CVD2Depre_c=folderRoot+'/data2/CVD2Depre_class.csv'

save_onlyCVD_c=folderRoot+'/data2/HealthyvsCVD_class.csv'
save_onlyDepre_c=folderRoot+'/data2/HealthyvsDepre_class.csv'
all_data=folderRoot+'/data2/all_data_v.csv'
save_onlyDiabetes_c=folderRoot+'/data2/HealthyvsDiabetes_class.csv'

folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'
nan_threshold = 0.6  # 70% threshold

pattern = '\d+-0.\d+'

healthy = pd.read_csv(save_healthy)
on_cvd = pd.read_csv(save_onlyCVD)
on_diabetes = pd.read_csv(save_onlyDiabetes)
on_depre = pd.read_csv(save_onlyDepre)
cvd2depre = pd.read_csv(save_CVD2Depre)
depre2cvd = pd.read_csv(save_Depre2CVD)
cvd2diabetes = pd.read_csv(save_CVD2Diabetes)
diabetes2cvd = pd.read_csv(save_Diabetes2CVD)

common_ids = set(on_cvd['ID']).intersection(cvd2depre['ID'])
on_cvd = on_cvd[~on_cvd['ID'].isin(common_ids)]
cvd2depre = cvd2depre[~cvd2depre['ID'].isin(common_ids)]

common_ids = set(on_cvd['ID']).intersection(depre2cvd['ID'])
on_depre = on_depre[~on_depre['ID'].isin(common_ids)]
depre2cvd = depre2cvd[~depre2cvd['ID'].isin(common_ids)]

common_ids = set(on_cvd['ID']).intersection(diabetes2cvd['ID'])
on_diabetes = on_diabetes[~on_diabetes['ID'].isin(common_ids)]
diabetes2cvd = diabetes2cvd[~diabetes2cvd['ID'].isin(common_ids)]

common_ids = set(on_cvd['ID']).intersection(cvd2diabetes['ID'])
on_cvd = on_cvd[~on_cvd['ID'].isin(common_ids)]
cvd2diabetes = cvd2diabetes[~cvd2diabetes['ID'].isin(common_ids)]

healthy_t=pd.DataFrame()
healthy_t['ID']=healthy['eid']

all_subjectes_v = pd.concat([on_diabetes, on_cvd,on_depre, cvd2depre,cvd2diabetes, depre2cvd, diabetes2cvd], ignore_index=True)
all_subjects=pd.DataFrame({'ID': (all_subjectes_v['ID'].unique()).tolist()})

print(all_subjects)

# filter data in csv
file_U1=folderRoot+'data/'+file_ukbb
rx1 = pd.read_csv(file_U1)

save_file_U1ind=folderRoot+'data2/allindividuals_'+file_ukbb
all_individuals=rx1['eid']

all_individuals.to_csv(save_file_U1ind, index=False)

#rx1 = rx1.loc[rx1['eid'].isin(all_subjects['ID'])].reset_index(drop=True)

numbers_to_remove = ['44', '3166', '55', '20001', '41202', '41204', '41262', '41245', '41270', '41280', '42038', '42039', '42040', '53','20003']

# Use list comprehension to generate a list of columns to remove
pattern = re.compile(r'^\d+-0\.\d$')
columns_to_remove1 = [col for col in rx1.columns if pattern.match(col) and col.split('-')[0] in numbers_to_remove]

# Remove the specified columns if they exist
df1 = rx1.drop(columns=[col for col in columns_to_remove1 if col in rx1.columns])

del rx1

file_output1=folderRoot+'data2/'+'filter_'+file_ukbb

df1.to_csv(file_output1, index = False)


#
# tx2 = pd.merge(rx1, rx2, on='eid', how='outer')
#
# del rx1, rx2
# #
# tx = tx2.drop(['eid'],axis=1)
# tx = tx.filter(regex=pattern).reset_index(drop=True)
# tx.insert(0, 'ID', tx2['eid'].iloc[0])
#
# del tx2
#
# tx.to_csv(all_data, index=False)

#
# rx1 = None
#
# tx2 = rx2.drop(['eid'],axis=1)
# tx2 = tx2.filter(regex=pattern).reset_index(drop=True)
# tx2.insert(0, 'ID', rx2['eid'].iloc[0])
#
# rx2 = None
#
# #tx = pd.concat([tx1, tx2], axis=1)
# tx01=tx1
# tx02=tx2
#
# tx1 = None
# tx2 = None
#
# # Calculate the percentage of NaN values in each column
# nan_percentage1 = tx01.isna().mean()
# nan_percentage2 = tx02.isna().mean()
#
# # Identify columns with more than pr% NaN values
# columns_to_remove1 = nan_percentage1[nan_percentage1 > nan_threshold].index
# columns_to_remove2 = nan_percentage2[nan_percentage2 > nan_threshold].index
#
# # Drop those columns from the DataFrame
# tx01 = tx01.drop(columns=columns_to_remove1)
# tx02 = tx02.drop(columns=columns_to_remove2)
#
# values_to_replace = [-1,-3,-7, -818]
# tx01 = tx01.replace(values_to_replace, np.nan)
# tx02 = tx02.replace(values_to_replace, np.nan)
#
# numbers_to_remove = ['44', '3166', '55', '20001', '41202', '41204', '41262', '41245', '41270', '41280', '42038', '42039', '42040', '53','20003']
#
# # Use list comprehension to generate a list of columns to remove
# pattern = re.compile(r'^\d+-0\.\d$')
# columns_to_remove1 = [col for col in tx01.columns if pattern.match(col) and col.split('-')[0] in numbers_to_remove]
# columns_to_remove2 = [col for col in tx02.columns if pattern.match(col) and col.split('-')[0] in numbers_to_remove]
#
# # Remove the specified columns if they exist
# tx01 = tx01.drop(columns=[col for col in columns_to_remove1 if col in tx01.columns])
# tx02 = tx02.drop(columns=[col for col in columns_to_remove1 if col in tx02.columns])
#
# tx = pd.merge(tx01, tx02, on='ID', how='outer')
#
# tx01 = None
# tx02 = None
# nan_percentage1 = None
# nan_percentage2 = None
#
# #
# only_cvd_t = tx.loc[tx['ID'].isin(on_cvd['ID'])].reset_index(drop=True)
# only_diabetes_t = tx.loc[tx['ID'].isin(on_diabetes['ID'])].reset_index(drop=True)
# only_depre_t = tx.loc[tx['ID'].isin(on_depre['ID'])].reset_index(drop=True)
#
# cvd2diabetes_t = tx.loc[tx['ID'].isin(cvd2diabetes['ID'])].reset_index(drop=True)
# cvd2depre_t = tx.loc[tx['ID'].isin(cvd2depre['ID'])].reset_index(drop=True)
# diabetes2cvd_t = tx.loc[tx['ID'].isin(diabetes2cvd['ID'])].reset_index(drop=True)
# depre2cvd_t = tx.loc[tx['ID'].isin(depre2cvd['ID'])].reset_index(drop=True)
#
# only_cvd_t['class']=0
# only_diabetes_t['class']=0
# only_depre_t['class']=0
# cvd2diabetes_t['class']=1
# cvd2depre_t['class']=1
# diabetes2cvd_t['class']=1
# depre2cvd_t['class']=1
#
# cvd2diabetes_final = pd.concat([only_cvd_t, cvd2diabetes_t], ignore_index=True)
# cvd2depre_final = pd.concat([only_cvd_t, cvd2depre_t], ignore_index=True)
# diabetes2cvd_final = pd.concat([only_diabetes_t, diabetes2cvd_t], ignore_index=True)
# depre2cvd_final = pd.concat([only_depre_t, depre2cvd_t], ignore_index=True)
#
# only_cvd_t2=only_cvd_t
# only_diabetes_t2=only_diabetes_t
# only_depre_t2=only_depre_t
#
# only_cvd_t2['class']=1
# only_diabetes_t2['class']=1
# only_depre_t2['class']=1
# healthy['class']=0
#
# healthy2cvd_final = pd.concat([healthy, only_cvd_t2], ignore_index=True)
# healthy2depre_final = pd.concat([healthy, only_depre_t2], ignore_index=True)
# healthy2diabetes_final = pd.concat([healthy, only_diabetes_t2], ignore_index=True)
#
# healthy2cvd_final.to_csv(save_onlyCVD_c, index=False)
# healthy2depre_final.to_csv(save_onlyDepre_c, index=False)
# healthy2diabetes_final.to_csv(save_onlyDiabetes_c, index=False)
#
# depre2cvd_final.to_csv(save_Depre2CVD_c, index=False)
# diabetes2cvd_final.to_csv(save_Diabetes2CVD_c, index=False)
# cvd2depre_final.to_csv(save_CVD2Depre_c, index=False)
# cvd2diabetes_final.to_csv(save_CVD2Diabetes_c, index=False)
#
