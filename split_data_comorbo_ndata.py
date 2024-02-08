import numpy as np
import pandas as pd
from sklearn.model_selection import GridSearchCV, StratifiedKFold, KFold, train_test_split, StratifiedShuffleSplit
import os


# inputs

folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'
folderCSV=folderRoot+'data2/'
folderSave=folderRoot+'CSV_unbalanced_torun_data/'

disease1='Control'  # Depre Diabetes CVD Control
disease2='CVD'

test_pr=0.20  # A) 20% for testing 80% for training  B) 10% for testing 90% for training
n_repetitions=5
test='class'

code_id = 'eid'
code_outcome = 'class'


# end inputs

isExist = os.path.exists(folderSave)
if not isExist:
   # Create a new directory because it does not exist
   os.makedirs(folderSave)
   print("The new directory is created!")

#CVD2Diabetes_class.csv
file_name = folderCSV + disease1 + 'vs' + disease2 + '_' + test+'.csv'
dataT = pd.read_csv(file_name)

X = dataT.drop([code_outcome], axis=1)
X_id = dataT[code_id]
Y = dataT[code_outcome]


sss=StratifiedShuffleSplit(n_splits=n_repetitions,  test_size=test_pr, random_state=0)

for i, (train_index, test_index) in enumerate(sss.split(X, Y)):

    print(f"Fold {i}:")
    file_name = folderCSV + disease1 + 'vs' +  disease2 + '_' + test + '.csv'
    dataT = pd.read_csv(file_name)

    print(test_index)

    data_train = dataT.loc[train_index,:].reset_index(drop=True)
    data_test = dataT.loc[test_index,:].reset_index(drop=True)


    output_test=folderSave+disease1+'vs'+disease1+disease2+'_'+test+'_TEST_repet'+str(i+1)+'.csv'
    output_train=folderSave+disease1+'vs'+disease1+disease2+'_'+test+'_TRAIN_repet'+str(i+1)+'.csv'

    data_train.to_csv(output_train, index=False)
    data_test.to_csv(output_test, index=False)
    del data_train, data_test, dataT


    print('====>>> Data '+test+ ' -> repetition '+str(i+1)+' saved')
