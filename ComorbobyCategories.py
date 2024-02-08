
import pandas as pd
import numpy as np
import re
import os


folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'
folderSave=folderRoot+'CSV_unbalanced_torun_data3/'
output_folder=folderRoot+'CSV_unbalanced_torun_data3/'

fileFileds=folderRoot+'data/list_variables_nw.csv'

disease1='Control'  # Depre Diabetes CVD Control
disease2='CVD'
test='class'
save_category='exposome'


if save_category=='exposome':
    category = ['lifestyle', 'early-life', 'mental health', 'physical', 'environment', 'sociodemographics',
                'blood pressure']
if save_category=='clinical':
    category =['clinical']
if save_category=='biological':
    category=['biological']
if save_category == 'biological+clinical':
    category = ['biological','clinical']

n_repetitions=3

set_f=['TRAIN','TEST']  # TRAIN TEST

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

rx= pd.read_csv(fileFileds,delimiter=";")

for t in set_f:

    for k in range(n_repetitions):
        file_name_train= folderSave+disease1+'vs'+disease1+disease2+'_'+test+'_'+t+'_repet'+str(k+1)+'.csv'

        df = pd.read_csv(file_name_train)

        # Remove fields not required by file

        #result_df = rx[rx['category'] == category]
        result_df = rx[rx['category'].isin(category)]

        columns=[col for col in result_df['cols'] if col in df.columns]

        tx = pd.concat([df['eid'], df[columns], df['class']], axis=1)

        file_name_train_cat=output_folder+disease1+'vs'+disease1+disease2+'_'+test+'_'+t+'_'+save_category+'_repet'+str(k+1)+'.csv'

        tx.to_csv(file_name_train_cat, index=False)






print('Category '+ save_category +' saved')






