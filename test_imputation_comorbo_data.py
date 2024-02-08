import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer


folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'
folderSave=folderRoot+'CSV_unbalanced_torun_data3/'

test='class' # Exposome Biological ExposomeBio Framingham
disease1='Control'  # Depre Diabetes CVD
disease2='CVD'
category='biological+clinical' # exposome biological '' clinical biological+clinical
n_repetitions=3

for k in range(n_repetitions):

    if not category:
        file_name_train=folderSave+disease1 + 'vs' + disease1 + disease2 + '_'+test +'_'+'TRAIN_repet'+str(k+1)+'.csv'
        file_name_test=folderSave+disease1 + 'vs' + disease1 + disease2 + '_'+test +'_'+'TEST_repet'+str(k+1)+'.csv'
        file_name_test_imp = folderSave + disease1 + 'vs' + disease1 + disease2 + '_'+test +'_'+'TEST_imputed_repet'+str(k+1)+'.csv'
    else:
        file_name_train = folderSave + disease1 + 'vs' + disease1 + disease2 + '_' + test + '_' + 'TRAIN_' + category + '_repet' + str(
            k + 1) + '.csv'
        file_name_test = folderSave + disease1 + 'vs' + disease1 + disease2 + '_' + test + '_' + 'TEST_' + category + '_repet' + str(
            k + 1) + '.csv'
        file_name_test_imp = folderSave + disease1 + 'vs' + disease1 + disease2 + '_' + test + '_' + 'TEST_imputed_' + category + '_repet' + str(
            k + 1) + '.csv'

    X_train = pd.read_csv(file_name_train)
    X_test = pd.read_csv(file_name_test)

    imputer = SimpleImputer(strategy ='median')

    #fit and transform on training data
    imputed_X_train = imputer.fit_transform(X_train)

    #apply transform on the test data
    imputed_X_test = pd.DataFrame(imputer.transform(X_test))
    imputed_X_test.columns = X_train.columns

    imputed_X_test.to_csv(file_name_test_imp, index=False)

    print('=====>>>> Simple imputation finished...')
    print('file saved as: ' + file_name_test_imp)

