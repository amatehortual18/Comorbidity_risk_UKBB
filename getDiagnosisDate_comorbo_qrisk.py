import numpy as np
import pandas as pd
import csv
from datetime import datetime



folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'

save_diseases=folderRoot+'data/'
file_dates=folderRoot+'data/f.41280_ukbb.csv'
file_codes=folderRoot+'data/f.41270_ukbb.csv'

dates = pd.read_csv(file_dates,delimiter="\,")
codes = pd.read_csv(file_codes,delimiter="\,")


mental_illness = ['F32','F320','F321','F322','F323','F328','F329',
                  'F200', 'F201','F202', 'F203','F204','F205', 'F206','F208', 'F209',
                  'F310', 'F311', 'F312', 'F313', 'F314','F315','F316','F317','F318','F319',
                  ]

diabetes = ['E100','E101','E102','E103','E104','E105','E106','E107','E108','E109','E110',
            'E111','E112','E113','E114','E115','E116','E117','E118','E119','E121','E123',
            'E125','E128','E129','E130','E131','E132','E133','E134','E134','E135','E136',
            'E137','E138','E139','E140','E141','E142','E143','E144','E145','E146','E147','E148','E149']

SLE = ['M32','M320','M321','M328']

Atrial_fibrillation = ['I48','I480','I481','I482','I483','I484','I489']

Rheumatoid_arthritis = ['M06']

migraine = ['G43']

Chronic_kidney = ['N18']

erectile_disfunction=['F522']

codes_dis = [mental_illness,diabetes, SLE, Atrial_fibrillation,Rheumatoid_arthritis, migraine, Chronic_kidney, erectile_disfunction]

names_dis = ['mental_illness','Diabetes','SLE','Atrial_Fib','Rheum_arth','Migraine','Chronic_kid','erectil_disf']

dataframe_disease = {"eid":[], "code":[], "date":[]}

len(names_dis)


for x in range(0,len(codes_dis)):

    my_list = codes_dis[x]
    disease_name = names_dis[x]

    mask = codes.applymap(lambda x: x.startswith(tuple(my_list)) if isinstance(x, str) else False)
    codes_n = codes[mask.any(axis=1)]

    #print(codes_n)

    dates_n = dates.loc[dates['eid'].isin(codes_n['eid'])].sort_values(by=['eid']).reset_index(drop=True)
    codes_n = codes_n.loc[codes_n['eid'].isin(dates_n['eid'])].sort_values(by=['eid']).reset_index(drop=True)

    del codes_n['eid']
    del dates_n['Unnamed: 0']

    codes_n.to_csv(r'codes_n.csv', index = False, header=True)
    dates_n.to_csv(r'dates_n.csv', index = False, header=True)

    code_prefixes = my_list

    # create an empty dictionary to store the information
    data = {}

    # read the first matrix (disease codes)
    with open("codes_n.csv", "r") as f:
        reader = csv.reader(f)
        headers = next(reader)  # save the header row

        for row in reader:
            eid = row[0]  # get the eid
            for i in range(1, len(row)):
                code = row[i]

                if code and any(code.startswith(prefix) for prefix in code_prefixes):
                    if eid not in data:
                        data[eid] = {}
                    data[eid][headers[i]] = {"code": code}

    rows = list(pd.DataFrame(data).columns)
    dates_n = dates_n.set_index(['eid'])
    for row in rows:
        for col in range(0,pd.DataFrame(data[row]).shape[1]):
            cols = list(data[row].keys())
            cols_r = [s.replace('f.41270', 'f.41280') for s in cols]
            date = dates_n[cols_r[col]][int(row)]
            data[row][cols[col]]['date'] = date

    df_data = pd.DataFrame(data)

    for colum in range(0,df_data.shape[1]):
        min_time = '2024-1-1'
        min_time = datetime.strptime(min_time, '%Y-%m-%d').date()
        eid=''
        for row in range(0,df_data.shape[0]):
            if str(df_data.values[row][colum]) != 'nan':
                date_string = df_data.values[row][colum]['date']
                date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
                if min_time > date_object:
                    min_time = date_object
                    eid = df_data.columns[colum]

        dataframe_disease.setdefault("eid", []).append(eid)
        dataframe_disease.setdefault("code", []).append(disease_name)
        dataframe_disease.setdefault("date", []).append(min_time)


# In[155]:


pd.DataFrame(dataframe_disease['code']).value_counts()


diseases = pd.DataFrame(dataframe_disease)

diseases = diseases.sort_values(by=['eid', 'date']).reset_index(drop=True)


wide_diseases = diseases.pivot(index='eid', columns='code', values='date')
wide_diseases.reset_index(inplace=True)



wide_diseases.to_csv(save_diseases+'wide_diseasesComorbo_raw.csv', index = False, header=True)
diseases.to_csv(save_diseases+'diseasesComorbo_raw.csv', index = False, header=True)

