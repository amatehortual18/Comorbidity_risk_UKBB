import numpy as np
import pandas as pd
from sklearn import metrics
import sys
import os
from sklearn.metrics import confusion_matrix
import joblib
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score

from sklearn.metrics import precision_recall_curve
from sklearn.metrics import PrecisionRecallDisplay

test='class' # Framingham class
disease1='Diabetes'  # Depre Diabetes CVD
disease2='CVD'

n_repetitions=1

folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'
#folderOutputs=folderRoot+'output_Framingham/'
folderOutputs=folderRoot+'CSV_unbalanced_torun_data3/'

auc = []
aucpcr = []
recall = []
precision = []
specificity = []
acc_balanced = []
weight_f1 = []


for k in range(n_repetitions):

    #fileTest= folderOutputs + disease1 + 'vs' + disease1 + disease2 + '_' + test + '_score_TEST_imputed_repet'+str(k+1)+'.csv'

    'DiabetesvsDiabetesCVD_class_FraminghamValues_Comorbo.csv'

    fileTest = folderOutputs + disease1 + 'vs' + disease1 + disease2 + '_' + test + '_FraminghamValues_Comorbo.csv'

    data = pd.read_csv(fileTest)

    Y = data['classe']
    Y_pr = data['FraminghamScore']
    Y_p = data['prediction']

    auc.append(round(metrics.roc_auc_score(Y, Y_pr,average=None), 2))
    aucpcr.append(round(metrics.average_precision_score(Y, Y_pr,average=None), 2))
    precision.append(round(metrics.precision_score(Y, Y_p,average='binary'), 2))
    recall.append(round(metrics.recall_score(Y, Y_p,average='binary'), 2))
    tn, fp, fn, tp = confusion_matrix(Y, Y_p).ravel()
    specificity.append(tn / (tn + fp))
    acc_balanced.append(round(metrics.balanced_accuracy_score(Y, Y_p), 2))
    weight_f1.append(round(metrics.f1_score(Y, Y_p, average='binary'), 2))

    print(classification_report(Y, Y_p))



#

print('auc')
print(round(np.mean(auc),2))
print(round(np.std(auc),2))

print('precision')
print(round(np.mean(precision), 2))
print(round(np.std(precision), 2))

print('aucpcr')
print(round(np.mean(aucpcr),2))
print(round(np.std(aucpcr),2))

print('sensitivity')
print(round(np.mean(recall),2))
print(round(np.std(recall),2))

print('specificity')
print(round(np.mean(specificity), 2))
print(round(np.std(specificity), 2))

print('macro_f1 xx')
print(round(np.mean(weight_f1), 2))
print(round(np.std(weight_f1), 2))

print('balanced_acc')
print(round(np.mean(acc_balanced), 2))
print(round(np.std(acc_balanced), 2))
