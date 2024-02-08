
import shap
import pandas as pd
import numpy as np
from shap import summary_plot
from sklearn.datasets import fetch_california_housing
from sklearn.feature_selection import SelectFromModel
from sklearn.model_selection import train_test_split
import xgboost as xgb
import numpy as np
from xgboost import XGBClassifier, plot_importance
from sklearn.ensemble import RandomForestClassifier
import joblib
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

from shap import TreeExplainer, summary_plot
import os


test='class' # Exposome Biological ExposomeBio
disease1='diabetes'  # Depre Diabetes CVD control
disease2='CVD'
category='' # _exposome clinical biological ''
id_c='eid'

n_repetitions=1 # 1 or 2
n_features=30 #30 14
font_size=30
model_ml='BRF_GR' #LGB XGB CAT BBC BRF EEC LGR  LGB_SM  EEC80  BRF_GR


folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'
folderSave=folderRoot+'OUTPUT_SHAP_data3'
folderOutputs=folderRoot+'output_comorbo_data3'
folderInputs=folderRoot+'CSV_unbalanced_torun_data3'

if not os.path.exists(folderSave):
    os.makedirs(folderSave)

name_features=folderRoot+'data/features_variables3.xlsx'
#tx= pd.read_csv(name_features)

fileFileds=folderRoot+'data/list_variables_nw.csv'

df= pd.read_csv(fileFileds,delimiter=";")

#dfdd = pd.read_excel(name_features)
#df=pd.DataFrame(dfdd).reset_index(drop=True)
print(df)

#print(tx)

for k in range(n_repetitions):

    n_repetition=str(k+1)

    fileOutput = folderOutputs + '/'+disease1 + 'vs' + disease1 + disease2 + '_' + test + '_' + 'TRAIN' + category + '_repet' + str(
        k + 1) + '.csv/'

    fileTest = folderInputs +'/' +disease1 + 'vs' + disease1 + disease2 + '_' + test + '_' + 'TEST_imputed' + category + '_repet' + str(
        k + 1) + '.csv'
    modelName = disease1 + 'vs' + disease1 + disease2 + '_' + test + '_' + 'TRAIN' + category + '_repet' + str(
        k + 1) + '.csv'

    fileTrain = folderInputs+'/'+disease1 + 'vs' + disease1 + disease2 + '_' + test + '_' + 'TRAIN' + category + '_repet' + str(
        k + 1) + '.csv'

    #fileOutput=folderOutputs + '/' + disease1 + 'vs' + disease1 + disease2 + "_"+gneral+"_" + test +'_'+name_f+'TRAIN_repet' + n_repetition + '.csv/'
    fileSave = folderSave +'/'+ disease1 + 'vs' + disease1 + disease2 + "_"+ test +'_'+category+ '_Screening_shapvalues.csv'

    #fileTest = folderInputs +'/' +disease1 + 'vs' + disease1 + disease2 + "_"+gneral+"_" + test +'_'+name_f+ 'TEST_imputed_repet' + n_repetition + '.csv'

    #fileTrain = folderInputs + '/'+disease1 + 'vs' + disease1 + disease2 + "_"+gneral+"_" + test +'_'+name_f+ 'TRAIN_repet' + n_repetition +'.csv'
    #modelName=disease1 + 'vs' + disease1 + disease2 + "_"+gneral+"_" + test +'_'+name_f+ 'TRAIN_repet' + n_repetition + '.csv'

    train_b = pd.read_csv(fileTrain, delimiter="\,")
    test_b = pd.read_csv(fileTest, delimiter="\,")

    imputer = SimpleImputer(strategy='median')

    train = pd.DataFrame(imputer.fit_transform(train_b))
    train.columns = train_b.columns

    fileModel = fileOutput + 'Modelkfold'+modelName+'_'+model_ml+'.joblib'  # pkl joblib

    model_xgb = joblib.load(fileModel)

    Y = train['class']
    eids = train[id_c]
    del train['class']
    del train[id_c]
    X = pd.DataFrame(train)

    y = test_b['class']
    eids = test_b[id_c]
    del test_b['class']
    del test_b[id_c]
    x = pd.DataFrame(test_b)

    model_xgb.fit(X,Y)

    import shap
    shap.initjs()

    selected_features=model_xgb[:-1].get_feature_names_out()

    print('number of features=======>>>>:')
    print(len(selected_features))
    print(selected_features)

    explainer = shap.Explainer(model_xgb['clf'])
    #
    df1= pd.DataFrame(selected_features, columns = ['code'])
    #
    df1['code'] = df1['code']
    #
    df2=df.iloc[pd.Index(df['cols']).get_indexer(df1['code'])]
    #
    x2 = x[x.columns.intersection(selected_features)]
    #
    x2.columns = df2['description']
    #
    print('number of features x2=======>>>>:')
    print(x2.shape)

    shap_values = explainer.shap_values(x2)
    #
    exp = TreeExplainer(model_xgb['clf'])
    sv = exp.shap_values(x2)

    print('number of features sv =======>>>>:')
    print(len(sv[1]))

    fig = plt.figure(figsize=(25,15),facecolor='w')

    summary_plot(sv[1], x2, feature_names = x2.columns.tolist(), plot_type='violin',show=False,max_display=n_features)
    plt.rcParams["font.family"] = "Helvetica"
    #plt.rcParams["font.size"] = font_size
    plt.rcParams.update({'font.size': font_size})
    plt.tight_layout()
    plt.rcParams["figure.autolayout"] = True
    figure_name=folderSave+'/'+modelName+'_'+model_ml+'.png'
    print('figure name----')
    print(figure_name)
    plt.savefig(folderSave+"/"+modelName+'_'+model_ml+".png",bbox_inches='tight',dpi=300)

    file_name_var=folderSave+"/"+modelName+'_'+model_ml+".csv"
    x2.to_csv(file_name_var, index=False)


