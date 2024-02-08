# Import libraries
import numpy as np
import pandas as pd
import csv
from datetime import datetime



folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'

save_healthy=folderRoot+'data/healthy.csv'
save_diseases=folderRoot+'data/diseases.csv'
file_dates=folderRoot+'data/f.41280_ukbb.csv'
file_codes=folderRoot+'data/f.41270_ukbb.csv'

CVD_ICD10=folderRoot+'data/CVD.csv'
T2D_ICD10=folderRoot+'data/T2D.csv'
DEPRE_ICD10=folderRoot+'data/DEPRE.csv'

x_cvd = pd.read_csv(CVD_ICD10)
x_depre = pd.read_csv(DEPRE_ICD10)
x_t2d = pd.read_csv(T2D_ICD10)

print(x_depre['ID'])

depre_list = [str(obj) for obj in x_depre['ID']]
cvd_list = [str(obj) for obj in x_cvd['ID']]
t2d_list = [str(obj) for obj in x_t2d['ID']]


print(depre_list)


# File containing all types of codes:
dates = pd.read_csv(file_dates,delimiter="\,")
codes = pd.read_csv(file_codes,delimiter="\,")

del codes['Unnamed: 0']
del dates['Unnamed: 0']

Healthy = pd.DataFrame()
Healthy['eid'] = codes[pd.isna(codes['41270-0.0'])]['eid']

Healthy.to_csv(save_healthy, index = False, header=True)

codes_dis = [depre_list,cvd_list,t2d_list]
names_dis = ['Depression','CVD','Diabetes']
dataframe_disease = {"eid":[], "code":[], "date":[]}

# Iterate over codes and names for diseases
for x in range(0, len(codes_dis)):

    # Get disease codes and names for current iteration
    my_list = codes_dis[x]
    disease_name = names_dis[x]

    # Create a mask to filter rows that contain disease codes
    mask = codes.applymap(lambda x: x.startswith(tuple(my_list)) if isinstance(x, str) else False)
    # Apply the mask to get a filtered version of 'codes' dataframe
    codes_n = codes[mask.any(axis=1)]

    # Filter 'dates' dataframe to include only entries present in 'codes_n'
    dates_n = dates.loc[dates['eid'].isin(codes_n['eid'])].sort_values(by=['eid']).reset_index(drop=True)
    # Filter 'codes_n' similarly
    codes_n = codes_n.loc[codes_n['eid'].isin(dates_n['eid'])].sort_values(by=['eid']).reset_index(drop=True)

    # Save filtered dataframes to csv
    codes_n.to_csv(r'codes_n.csv', index=False, header=True)
    dates_n.to_csv(r'dates_n.csv', index=False, header=True)

    # Specify disease code prefixes
    code_prefixes = my_list

    # create an empty dictionary to store the information
    data = {}

    # Read the disease codes file
    with open("codes_n.csv", "r") as f:
        reader = csv.reader(f)
        headers = next(reader)  # save the header row

        for row in reader:
            eid = row[0]  # get the eid
            for i in range(1, len(row)):
                code = row[i]

                # If code starts with the specified prefixes, add it to the dictionary
                if code and any(code.startswith(prefix) for prefix in code_prefixes):
                    if eid not in data:
                        data[eid] = {}
                    data[eid][headers[i]] = {"code": disease_name}

                    # Get list of eids
    rows = list(pd.DataFrame(data).columns)
    dates_n = dates_n.set_index(['eid'])

    # Add date information for each eid and disease code
    for row in rows:
        for col in range(0, pd.DataFrame(data[row]).shape[1]):
            cols = list(data[row].keys())
            cols_r = [s.replace('41270', '41280') for s in cols]
            date = dates_n[cols_r[col]][int(row)]
            data[row][cols[col]]['date'] = date

            # Transform data dictionary into a pandas dataframe
    df_data = pd.DataFrame(data)

    # Find the earliest date for each disease for each eid
    for colum in range(0, df_data.shape[1]):
        min_time = '2024-1-1'
        min_time = datetime.strptime(min_time, '%Y-%m-%d').date()
        eid = ''
        for row in range(0, df_data.shape[0]):
            if str(df_data.values[row][colum]) != 'nan':
                date_string = df_data.values[row][colum]['date']
                date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
                if min_time > date_object:
                    min_time = date_object
                    eid = df_data.columns[colum]

        # Store the earliest date along with corresponding eid and disease code
        dataframe_disease.setdefault("eid", []).append(eid)
        dataframe_disease.setdefault("code", []).append(disease_name)
        dataframe_disease.setdefault("date", []).append(min_time)

pd.DataFrame(dataframe_disease['code']).value_counts()

diseases = pd.DataFrame(dataframe_disease)

# Sort the dataframe
diseases = diseases.sort_values(by=['eid', 'date']).reset_index(drop=True)

diseases.to_csv(save_diseases, index = False, header=True)