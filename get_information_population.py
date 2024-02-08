

import pandas as pd
folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/CSV_unbalanced_torun_data3/'


repetition=1
disease1='Diabetes' #Depre, Diabetes
disease2='CVD'
set='TRAIN' # TRAIN TEST
test='exposome'  # exposome biological

filer=folderRoot+disease1+'vs'+disease1+disease2+'_class_'+set+'_'+test+'_repet'+str(repetition)+'.csv'

print(filer)
df=pd.read_csv(filer)

n_disease2 = (df['class'] == 1).sum()
n_disease1 = (df['class'] == 0).sum()

print(disease1+':'+str(n_disease1))
print(disease2+':'+str(n_disease2))



