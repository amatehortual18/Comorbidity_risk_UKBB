import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt
import os

from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestClassifier

from catboost import CatBoostClassifier
from imblearn.combine import SMOTEENN
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import xgboost as xgb
import numpy as np
import joblib
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier, plot_importance
from imblearn.ensemble import BalancedRandomForestClassifier, BalancedBaggingClassifier, EasyEnsembleClassifier
#from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.experimental import enable_hist_gradient_boosting  # noqa
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.svm import LinearSVC

plt.style.use('fivethirtyeight')
plt.rcParams.update({'font.size': 30})
from imblearn.under_sampling import RandomUnderSampler
from sklearn import metrics
from imblearn.under_sampling import TomekLinks
import time
from sklearn.svm import SVC

import sys
import warnings
import argparse


if not sys.warnoptions:
    warnings.simplefilter("ignore")

from numpy import mean
from numpy import std

from sklearn.model_selection import GridSearchCV, StratifiedKFold, KFold


def plot_feature_importance(importance,names,model_type,namefilex):

    #Create arrays from feature importance and feature names
    feature_importance = np.array(importance)
    feature_names = np.array(names)

    #Create a DataFrame using a Dictionary
    data={'feature_names':feature_names,'feature_importance':feature_importance}
    fi_df = pd.DataFrame(data)

    #Sort the DataFrame in order decreasing feature importance
    fi_df.sort_values(by=['feature_importance'], ascending=False,inplace=True)
    fi_df.to_csv(namefilex)
    #Define size of bar plot
    plt.figure()
    #Plot Searborn bar chart
    #sns.barplot(x=fi_df['feature_importance'], y=fi_df['feature_names'])

    if fi_df.shape[0]>20 :
        nfeatures = 20
    else :
        nfeatures = fi_df.shape[0]

    sns.barplot(x=fi_df.iloc[0:nfeatures,1], y=fi_df.iloc[0:nfeatures,0])
    #Add chart labels
    plt.title(model_type + 'FEATURE IMPORTANCE')
    plt.xlabel('FEATURE IMPORTANCE')
    plt.ylabel('FEATURE NAMES')


def tic():
    global _start_time
    _start_time = time.time()

def tac():
    t_sec = round(time.time() - _start_time)
    (t_min, t_sec) = divmod(t_sec, 60)
    (t_hour, t_min) = divmod(t_min, 60)
    print('Time passed: {}hour:{}min:{}sec'.format(t_hour, t_min, t_sec))
    return (str('Time passed: {}hour:{}min:{}sec'.format(t_hour, t_min, t_sec)))

def run_prediction(path_parent, csv_file_name,output_folder, code_id, code_outcome):

    foldername_figures = csv_file_name
    file_results=output_folder + '/' + csv_file_name + '.txt'

    file_input = path_parent + '/' + csv_file_name
    print("Input csv file: " + file_input)
    folder_figure = output_folder + '/' + foldername_figures

    if not os.path.exists(folder_figure):
        os.makedirs(folder_figure)

    seed = 45

# ===========  process ===========

    text_file_output = open(file_results, "w+")
    time_learning = list()


    #_start_time = time.time()
    #tic()

    data = pd.read_csv(file_input)
    #====>>> imputation
    imp = SimpleImputer(strategy='median')
    data2 = pd.DataFrame(imp.fit_transform(data))
    data2.columns = data.columns
    #
    print('Imputation performed....')
    print(data2.shape)
    X_train = data2.drop([code_id, code_outcome], axis=1)
    X_tr = data2.drop([code_outcome], axis=1)
    y_train = data2[code_outcome]



# bagging
    brf_params = {
        'n_estimators': [10, 20, 30,80, 100],
        'sampling_strategy':[0.48,0.49,0.5,0.51,0.53,0.55],
       # 'max_depth': [50, 60, 70],
       # 'max_features': [10, 15],
       # 'min_samples_leaf': [1, 2, 3]
    }


    # Metrics for Evualation:
    met_grid = ['average_precision', 'roc_auc']



    import lightgbm as lgb



    lgbc_balanced = lgb.LGBMClassifier(random_state=42, n_jobs=-1, class_weight="balanced")


    brfc = BalancedRandomForestClassifier(random_state=42, n_jobs=-1)

    brfc_simple = BalancedRandomForestClassifier(
        criterion="entropy",
        random_state=42, n_jobs=-1
    )

    brfsimple_params = {
        'n_estimators': [10, 30, 80, 100, 120],
        'sampling_strategy': [0.48, 0.49, 0.5, 0.51, 0.53, 0.55],
         #'max_depth': [2, 50, 60, 70],
        # 'max_features': [10, 15],
        'min_samples_leaf': [1, 2, 3],
    }

    #brfc_search_simple = GridSearchCV(brfc_simple, brfsimple_params, scoring=met_grid, refit="average_precision",n_jobs=-1, cv=7).fit(X_train,
    #                                                                                                 y_train)
    #best_model_brfc_simple = brfc_search_simple.best_estimator_
    #classifier_brfc_simple = best_model_brfc_simple.fit(X_train, y_train)




    # pipe = Pipeline([("smote", smote_01), ("clf", lgbc)])
    #
    # gridsearch_pipe = GridSearchCV(
    #     pipe,
    #     param_grid={
    #         "clf__max_depth": [5, 50, 100],  BUENOS
    #         "clf__num_leaves": [10, 100, 1000]
    #     },
    #     scoring="f1_macro",
    #     n_jobs=-1,
    #     cv=5,
    #     verbose=1
    # ).fit(X_train, y_train)
    #
    #
    # best_model_lgbc = gridsearch_pipe.best_estimator_
    # classifier_lgbc = best_model_lgbc.fit(X_train, y_train)

    # pipe = Pipeline([("feature_selection", SelectFromModel(RandomForestClassifier(), max_features=20)),
    #                 ("clf", lgbc_balanced)])

    # pipe = Pipeline([
    #     ("feature_selection", SelectFromModel(RandomForestClassifier(n_estimators=100, random_state=42), max_features=15)),
    #     #('feature_selection', SelectFromModel(RandomForestClassifier(n_estimators=100, random_state=42), threshold="median")),
    #     ("clf", lgbc_balanced)])

    pipe1 = Pipeline([
        ('feature_selection',SelectFromModel(RandomForestClassifier(n_estimators=100, random_state=42), threshold="median")),
        ("clf", brfc),
                     ])

    # funcionando::
    # gridsearch_pipe = GridSearchCV(
    #     pipe,
    #     param_grid={
    #         "clf__max_depth": [3, 5, 10, 30],
    #         "clf__num_leaves": [100, 1000, 1100],
    #         "clf__min_data_in_leaf": [35, 45, 65],
    #         "clf__learning_rate": [0.01, 0.02,0.05,0.1],
    #         "clf__max_depth": [2,3,6,10]
    #     },
    #     scoring="roc_auc",
    #     n_jobs=-1,
    #     cv=5,
    #     verbose=1
    # ).fit(X_train, y_train)

    # gridsearch_pipe = GridSearchCV(
    #     pipe,
    #      param_grid={
    #        # "clf__max_depth": [3, 5, 10, 30],
    #        # "clf__num_leaves": [100, 1000, 1100],
    #        # "clf__min_data_in_leaf": [35, 45, 65],
    #        # "clf__learning_rate": [0.01, 0.02, 0.05, 0.1],
    #     #     #"clf__max_depth": [2, 3, 6, 10]
    #      },
    #     scoring=met_grid,
    #     refit='average_precision',
    #     n_jobs=-1,
    #     cv=7,
    #     verbose=1
    # ).fit(X_train, y_train)
    # #
    gridsearch_pipe1 = GridSearchCV(
        pipe1,
        param_grid={
            "clf__n_estimators": [10, 50,80, 100],
            #"clf__num_leaves": [10, 100, 1000]
        },
        scoring=met_grid,
        refit="average_precision",
        n_jobs=-1,
        cv=7,
        verbose=1
    ).fit(X_train, y_train)


    # best_model_lgbc = gridsearch_pipe.best_estimator_
    # classifier_lgbc = best_model_lgbc.fit(X_train, y_train)

    best_model_brfc = gridsearch_pipe1.best_estimator_
    classifier_brfc = best_model_brfc.fit(X_train, y_train)


        # save outcome distribution
    figure_data_balanced = folder_figure + '/'+ 'OriginalOutcome'+csv_file_name+'.png'
    bar_y = [(y_train == 1).sum(), (y_train == 0).sum()]
    bar_x = ["1", "0"]
    plt.figure()
    splot = sns.barplot(bar_x, bar_y)
    for p in splot.patches:
        splot.annotate(format(p.get_height(), '.1f'),
                       (p.get_x() + p.get_width() / 2., p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords='offset points')
    plt.xlabel("Disease")
    plt.ylabel("Number of subjects")
    plt.savefig(figure_data_balanced, bbox_inches='tight')
    plt.clf()


    # nameModel9 = 'Modelkfold' + csv_file_name + '_LGB_SM.joblib'
    # fileModel9 = folder_figure + '/' + nameModel9
    # joblib.dump(classifier_lgbc, fileModel9)

    nameModel10 = 'Modelkfold' + csv_file_name + '_BRF_GR.joblib'
    fileModel10 = folder_figure + '/' + nameModel10
    joblib.dump(classifier_brfc, fileModel10)

    # nameModel11 = 'Modelkfold' + csv_file_name + '_BRF_simple.joblib'
    # fileModel11 = folder_figure + '/' + nameModel11
    # joblib.dump(classifier_brfc_simple, fileModel11)

    print('---- Models saved ----')

