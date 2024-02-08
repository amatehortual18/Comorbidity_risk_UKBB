
import pandas as pd
import numpy as np
import re
import os

folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'
folderSave=folderRoot+'CSV_unbalanced_torun_data/'
output_folder=folderRoot+'CSV_unbalanced_torun_data3/'

fileFileds=folderRoot+'data/list_variables_nw.csv'

disease1='Control'  # Depre Diabetes CVD Control
disease2='CVD'
test='class'
n_repetitions=3

set_f=['TRAIN','TEST']  # TRAIN TEST

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def filter_columns(df, pattern):
    columns_to_remove = [col for col in df.columns if re.search(pattern, col)]
    df_filtered = df.drop(columns=columns_to_remove)
    return df_filtered

rx= pd.read_csv(fileFileds,delimiter=";")

for t in set_f:

    for k in range(n_repetitions):
        file_name_train= folderSave+disease1+'vs'+disease1+disease2+'_'+test+'_'+t+'_repet'+str(k+1)+'.csv'

        tx = pd.read_csv(file_name_train)

        values_to_replace = [-1,-3,-7, -818]
        tx = tx.replace(values_to_replace, np.nan)

        numbers_to_remove = ['44-', '3166-', '55-', '20001-', '41202-', '41204-', '41262-', '41245-', '41270-', '41280-', '42038-',
                             '42039-', '42040-', '53-', '20003-', '131286-']

        columns_to_remove = [col for col in tx.columns if any(num in col for num in numbers_to_remove)]

        # Remove the selected columns
        df = tx.drop(columns=columns_to_remove)

        # Remove fields not required by file

        result_df = rx[rx['use'] == 0]

        columns_to_remove = [col for col in df.columns if any(num in col for num in result_df['cols'])]


        #df.drop(columns=result_df['cols'], inplace=True)
        df.drop(columns=columns_to_remove, inplace=True)

        file_name_train2= output_folder+disease1+'vs'+disease1+disease2+'_'+test+'_'+t+'_repet'+str(k+1)+'.csv'

        df.to_csv(file_name_train2, index=False)












