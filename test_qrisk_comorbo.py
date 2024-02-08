import numpy as np
import pandas as pd
from sklearn import metrics
import joblib
from sklearn.metrics import confusion_matrix


folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'
folder='CSV_unbalanced_torun_data3/'

disease1='Depre'
disease2='CVD'
set_f='TEST'
test='class'
rep=1

fileTest=folderRoot+folder+disease1+disease1+'vs'+disease2+'_Qrisk17'+'.csv'
data = pd.read_csv(fileTest)


print(data)

auc = []
auc_pr = []
aucpcr = []
recall = []
precision = []
specificity = []
acc_balanced = []
weight_f1 = []
recall1 = []
precision1 = []
Y_probability=[]


Y = data['class']
Y_p = (data['q_risk17']>40).astype(int)

Y_pr=(data['q_risk17']*0.01)

print(Y_p)


auc.append(round(metrics.roc_auc_score(Y, Y_pr), 2))
aucpcr.append(round(metrics.average_precision_score(Y, Y_pr), 2))
precision.append(round(metrics.precision_score(Y, Y_p), 2))
recall.append(round(metrics.recall_score(Y, Y_p), 2))
acc_balanced.append(round(metrics.balanced_accuracy_score(Y, Y_p), 2))
weight_f1.append(round(metrics.f1_score(Y, Y_p, average='weighted'), 2))
tn, fp, fn, tp = confusion_matrix(Y, Y_p).ravel()
specificity.append(tn / (tn + fp))

print('sensitivity')
print(round(np.mean(recall), 2))
print(round(np.std(recall), 2))

print('specificity')
print(round(np.mean(specificity), 2))
print(round(np.std(specificity), 2))

print('precision')
print(round(np.mean(precision), 2))
print(round(np.std(precision), 2))

print('auc')
print(round(np.mean(auc), 2))
print(round(np.std(auc), 2))

print('acc_balanced')
print(round(np.mean(acc_balanced), 2))
print(round(np.std(acc_balanced), 2))

print('weighted_f1')
print(round(np.mean(weight_f1), 2))
print(round(np.std(weight_f1), 2))

print('Probability')
print(round(np.mean(Y_probability), 2))
print(round(np.std(Y_probability), 2))

