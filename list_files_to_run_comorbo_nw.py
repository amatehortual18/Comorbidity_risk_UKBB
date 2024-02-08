import function_prediction_undersampling_comorbo_test
import pandas as pd
import os

n_repetitions=1
name_files=[]

folderSave='output_comorbo_data3'
folderInputv='CSV_unbalanced_torun_data3'
code_id = 'eid' #ID
code_outcome = 'class'
disease1='Depre'
disease2='CVD'
disease3='Diabetes'
disease4='Healthy'
disease5='Control'
test='class'

# run

for k in range(n_repetitions):
    ff = disease5 + 'vs' + disease5 + disease2 + '_' + test + '_' + 'TRAIN' + '_repet' + str(k + 1) + '.csv'
    name_files.append(ff)

        # ff = disease1 + 'vs' + disease1 + disease2 + '_' + test + '_' + 'TRAIN' + '_repet' + str(k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease2 + 'vs' + disease2 + disease1 + '_' + test + '_' + 'TRAIN' + '_repet' + str(k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease3 + 'vs' + disease3 + disease2 + '_' + test + '_' + 'TRAIN' + '_repet' + str(k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease2 + 'vs' + disease2 + disease3 + '_' + test + '_' + 'TRAIN' + '_repet' + str(k + 1) + '.csv'
        # name_files.append(ff)
        #
        # # clinical
        #
        # category='clinical'
        #
        # ff = disease1 + 'vs' + disease1 + disease2 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease2 + 'vs' + disease2 + disease1 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease3 + 'vs' + disease3 + disease2 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease2 + 'vs' + disease2 + disease3 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(k + 1) + '.csv'
        # name_files.append(ff)
        #
        # # biological
        #
        # category = 'biological'

        # ff = disease1 + 'vs' + disease1 + disease2 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        #     k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease2 + 'vs' + disease2 + disease1 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        #     k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease3 + 'vs' + disease3 + disease2 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        #     k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease2 + 'vs' + disease2 + disease3 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        #     k + 1) + '.csv'
        # name_files.append(ff)
        #
        # # clinical+biological
        #
        # category = 'biological+clinical'
        #
        # ff = disease1 + 'vs' + disease1 + disease2 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        #     k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease2 + 'vs' + disease2 + disease1 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        #     k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease3 + 'vs' + disease3 + disease2 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        #     k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease2 + 'vs' + disease2 + disease3 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        #     k + 1) + '.csv'
        # name_files.append(ff)

        # exposome

    # category = 'exposome'
    # ff = disease5 + 'vs' + disease5 + disease2 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
    #     k + 1) + '.csv'
    # name_files.append(ff)
    #
    # category = 'biological'
    # ff = disease5 + 'vs' + disease5 + disease2 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
    #     k + 1) + '.csv'
    # name_files.append(ff)
    #
    # category = 'clinical'
    # ff = disease5 + 'vs' + disease5 + disease2 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
    #     k + 1) + '.csv'
    # name_files.append(ff)

    category = 'clinical'
    ff = disease5 + 'vs' + disease5 + disease2 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        k + 1) + '.csv'
    name_files.append(ff)


        # ff = disease1 + 'vs' + disease1 + disease2 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        #     k + 1) + '.csv'
        # name_files.append(ff)

        # ff = disease2 + 'vs' + disease2 + disease1 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        #     k + 1) + '.csv'
        # name_files.append(ff)

        # ff = disease3 + 'vs' + disease3 + disease2 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        #     k + 1) + '.csv'
        # name_files.append(ff)

        # ff = disease2 + 'vs' + disease2 + disease3 + '_' + test + '_' + 'TRAIN' + '_' + category + '_repet' + str(
        #     k + 1) + '.csv'
        # name_files.append(ff)


        # ff = disease4 + 'vs' + disease4 + disease1 + '_' + test + '_' + 'TRAIN' + '_repet' + str(k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease4 + 'vs' + disease4 + disease2 + '_' + test + '_' + 'TRAIN' + '_repet' + str(k + 1) + '.csv'
        # name_files.append(ff)
        #
        # ff = disease4 + 'vs' + disease4 + disease3 + '_' + test + '_' + 'TRAIN' + '_repet' + str(k + 1) + '.csv'
        # name_files.append(ff)

    print(ff)

path_parent="/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/"+folderInputv+"/"

output_folder="/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/"+folderSave+"/"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for k in range(0,len(name_files)):
    print(name_files[k])
    function_prediction_undersampling_comorbo_test.run_prediction(path_parent, name_files[k], output_folder,  code_id,
    code_outcome )


