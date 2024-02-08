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

from sklearn.metrics import auc


folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'

test='class' # Exposome Biological ExposomeBio
disease1='Control'  # Depre Diabetes CVD
disease2='CVD'
category='_clinical' # _exposome  '' _biological _biological+clinical _clinical

model_ml='BRF_GR' #LGB XGB CAT BBC BRF EEC LGR  LGB_SM  EEC80  BRF_GR BRF_simple
code_id = 'eid' # ID f_eid eid
code_outcome = 'class'

n_repetitions=1

folderOutputs=folderRoot+'output_comorbo_data3/'
folderInputs=folderRoot+'CSV_unbalanced_torun_data3/'
folderSave=folderRoot+'OUTPUT_SHAP_data3/'

if not os.path.exists(folderSave):
    os.makedirs(folderSave)

aucf = []
auc_pr = []
aucpcr = []
recall = []
precision = []
specificity = []
acc_balanced = []
weight_f1 = []
recall1 = []
precision1 = []


for k in range(n_repetitions):

    fileOutput = folderOutputs + disease1 + 'vs' + disease1 + disease2 +'_' +test +'_'+'TRAIN'+category+'_repet'+str(k+1)+'.csv/'

    fileTest= folderInputs + disease1 + 'vs' + disease1 + disease2 + '_'+test +'_'+'TEST_imputed'+category+'_repet'+str(k+1)+'.csv'
    fileTrain = disease1 + 'vs' + disease1 + disease2 + '_'+test +'_'+'TRAIN'+category+'_repet'+str(k+1)+'.csv'

    data = pd.read_csv(fileTest)

    X = data.drop([code_id, code_outcome], axis=1)
    Y = data[code_outcome]
    Z = data[code_id]

    X_test = X.iloc[:, :]

    fileModel = fileOutput + 'Modelkfold'+fileTrain+'_'+model_ml+'.joblib'  # pkl joblib
    xgb = joblib.load(fileModel)

    Y_pr = xgb.predict_proba(X_test)[:, 1]
    Y_p = xgb.predict(X_test)


    # Save values in excel file

    namefileX=disease1+disease1+'vs'+disease2+ "_" +'_'+model_ml+'_'+test+'_'+'_YYpr_repetition'+str(k+1)+'.csv'
    datacl = {'ID':Z,'Y': Y, 'Y_p': Y_p, 'Y_pr': Y_pr}
    fi_dfc = pd.DataFrame(datacl)
    fi_dfc.to_csv(folderSave+namefileX, index=False)

    #end Save

    aucf.append(round(metrics.roc_auc_score(Y, Y_pr,average=None), 2))
    aucpcr.append(round(metrics.average_precision_score(Y, Y_pr,average=None), 2))
    precision.append(round(metrics.precision_score(Y, Y_p,average='binary'), 2))
    recall.append(round(metrics.recall_score(Y, Y_p,average='binary'), 2))
    tn, fp, fn, tp = confusion_matrix(Y, Y_p).ravel()
    specificity.append(tn / (tn + fp))
    acc_balanced.append(round(metrics.balanced_accuracy_score(Y, Y_p), 2))
    weight_f1.append(round(metrics.f1_score(Y, Y_p, average='binary'), 2))

    #precisionb, recallb, thresholdsb = precision_recall_curve(Y,Y_pr)
    lr_precision, lr_recall, _ = precision_recall_curve(Y,Y_pr)
    print('sss')
    auc_l = auc(lr_recall, lr_precision)
    print(auc_l)
    auc_pr.append(auc_l)
    #precision1.append()
    #recall1.append(recallb)


    print(classification_report(Y, Y_p))

    plt.figure()

    PrecisionRecallDisplay.from_estimator(xgb, X_test, Y)

    plt.savefig(folderSave+disease1+disease1+'vs'+disease2+ "_" +'_'+model_ml+'_precision_recall_curve.png', bbox_inches='tight')
    plt.clf()
#

print('auc')
print(round(np.mean(aucf),2))
print(round(np.std(aucf),2))

print('precision')
print(round(np.mean(precision), 2))
print(round(np.std(precision), 2))
#
# print('precisionb')
# print(round(np.mean(precision1), 2))
# print(round(np.std(precision1), 2))
#
# print('aucpcr')
# print(round(np.mean(aucpcr),2))
# print(round(np.std(aucpcr),2))

print('sensitivity')
print(round(np.mean(recall),2))
print(round(np.std(recall),2))

# print('recallb')
# print(round(np.mean(recall1), 2))
# print(round(np.std(recall1), 2))

print('specificity')
print(round(np.mean(specificity), 2))
print(round(np.std(specificity), 2))

print('macro_f1 xx')
print(round(np.mean(weight_f1), 2))
print(round(np.std(weight_f1), 2))

print('balanced_acc')
print(round(np.mean(acc_balanced), 2))
print(round(np.std(acc_balanced), 2))

print('auc precision-recall')
print(round(np.mean(auc_pr), 2))
print(round(np.std(auc_pr), 2))



