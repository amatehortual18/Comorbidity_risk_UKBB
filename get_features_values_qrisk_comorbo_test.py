import pandas as pd
from datetime import datetime


def cvd_female_raw(age, b_AF, b_atypicalantipsy, b_corticosteroids, b_migraine, b_ra, b_renal, b_semi, b_sle, b_treatedhyp, b_type1, b_type2, bmi, ethrisk, fh_cvd, rati, sbp, sbps5, smoke_cat, surv, town):
    survivor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.988876402378082, 0, 0, 0, 0, 0]

    # Conditional arrays
    Iethrisk = [0, 0, 0.28040314332995425, 0.56298994142075398, 0.29590000851116516, 0.072785379877982545, -0.17072135508857317, -0.39371043314874971, -0.32632495283530272, -0.17127056883241784]
    Ismoke = [0, 0.13386833786546262, 0.56200858012438537, 0.66749593377502547, 0.84948177644830847]

    # Applying the fractional polynomial transforms (which includes scaling)
    dage = age / 10
    age_1 = dage**-2
    age_2 = dage
    dbmi = bmi / 10
    bmi_1 = dbmi**-2
    bmi_2 = dbmi**-2 * math.log(dbmi)

    # Centring the continuous variables
    age_1 -= 0.053274843841791
    age_2 -= 4.332503318786621
    bmi_1 -= 0.154946178197861
    bmi_2 -= 0.144462317228317
    rati -= 3.476326465606690
    sbp -= 123.130012512207030
    sbps5 -= 9.002537727355957
    town -= 0.392308831214905

    # Start of Sum
    a = 0

    # The conditional sums
    a += Iethrisk[ethrisk]
    a += Ismoke[smoke_cat]

    # Sum from continuous values
    a += age_1 * -8.1388109247726188
    a += age_2 * 0.79733376689699098
    a += bmi_1 * 0.29236092275460052
    a += bmi_2 * -4.1513300213837665
    a += rati * 0.15338035820802554
    a += sbp * 0.013131488407103424
    a += sbps5 * 0.0078894541014586095
    a += town * 0.077223790588590108

    # Sum from boolean values
    a += b_AF * 1.5923354969269663
    a += b_atypicalantipsy * 0.25237642070115557
    a += b_corticosteroids * 0.59520725304601851
    a += b_migraine * 0.301267260870345
    a += b_ra * 0.21364803435181942
    a += b_renal * 0.65194569493845833
    a += b_semi * 0.12555308058820178
    a += b_sle * 0.75880938654267693
    a += b_treatedhyp * 0.50931593683423004
    a += b_type1 * 1.7267977510537347
    a += b_type2 * 1.0688773244615468
    a += fh_cvd * 0.45445319020896213

    # Sum from interaction terms
    a += age_1 * (smoke_cat == 1) * -4.7057161785851891
    a += age_1 * (smoke_cat == 2) * -2.7430383403573337
    a += age_1 * (smoke_cat == 3) * -0.86608088829392182
    a += age_1 * (smoke_cat == 4) * 0.90241562369710648
    a += age_1 * b_AF * 19.938034889546561
    a += age_1 * b_corticosteroids * -0.98408045235936281
    a += age_1 * b_migraine * 1.7634979587872999
    a += age_1 * b_renal * -3.5874047731694114
    a += age_1 * b_sle * 19.690303738638292
    a += age_1 * b_treatedhyp * 11.872809733921812
    a += age_1 * b_type1 * -1.2444332714320747
    a += age_1 * b_type2 * 6.86523420000096
    a += age_1 * bmi_1 * 23.802623412141742
    a += age_1 * bmi_2 * -71.184947692087007
    a += age_1 * fh_cvd * 0.99467807940435127
    a += age_1 * sbp * 0.034131842338615485
    a += age_1 * town * -1.0301180802035639
    a += age_2 * (smoke_cat == 1) * -0.075589244643193026
    a += age_2 * (smoke_cat == 2) * -0.11951192874867074
    a += age_2 * (smoke_cat == 3) * -0.10366306397571923
    a += age_2 * (smoke_cat == 4) * -0.13991853591718389
    a += age_2 * b_AF * -0.076182651011162505
    a += age_2 * b_corticosteroids * -0.12005364946742472
    a += age_2 * b_migraine * -0.065586917898699859
    a += age_2 * b_renal * -0.22688873086442507
    a += age_2 * b_sle * 0.077347949679016273
    a += age_2 * b_treatedhyp * 0.00096857823588174436
    a += age_2 * b_type1 * -0.28724064624488949
    a += age_2 * b_type2 * -0.097112252590695489
    a += age_2 * bmi_1 * 0.52369958933664429
    a += age_2 * bmi_2 * 0.045744190122323759
    a += age_2 * fh_cvd * -0.076885051698423038
    a += age_2 * sbp * -0.0015082501423272358
    a += age_2 * town * -0.031593414674962329

    # Calculate the score itself

    score = 100.0 * (1 - math.pow(survivor[surv], math.exp(a)))
    return score


import math

def cvd_male_raw(age, b_AF, b_atypicalantipsy, b_corticosteroids, b_impotence2, b_migraine, b_ra, b_renal, b_semi, b_sle, b_treatedhyp, b_type1, b_type2, bmi, ethrisk, fh_cvd, rati, sbp, sbps5, smoke_cat, surv, town):
    survivor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.977268040180206, 0, 0, 0, 0, 0]

    # Conditional arrays
    Iethrisk = [0, 0, 0.27719248760308279, 0.47446360714931268, 0.52961729919689371, 0.035100159186299017, -0.35807899669327919, -0.4005648523216514, -0.41522792889830173, -0.26321348134749967]
    Ismoke = [0, 0.19128222863388983, 0.55241588192645552, 0.63835053027506072, 0.78983819881858019]

    # Applying the fractional polynomial transforms (which includes scaling)
    dage = age
    dage = dage / 10
    age_1 = dage**-1
    age_2 = dage**3
    dbmi = bmi
    dbmi = dbmi / 10
    bmi_2 = dbmi**-2 * math.log(dbmi)
    bmi_1 = dbmi**-2

    # Centring the continuous variables
    age_1 -= 0.234766781330109
    age_2 -= 77.284080505371094
    bmi_1 -= 0.149176135659218
    bmi_2 -= 0.141913309693336
    rati -= 4.300998687744141
    sbp -= 128.57157897949219
    sbps5 -= 8.756621360778809
    town -= 0.526304900646210

    # Start of Sum
    a = 0

    # The conditional sums
    a += Iethrisk[ethrisk]
    a += Ismoke[smoke_cat]

    # Sum from continuous values
    a += age_1 * -17.839781666005575
    a += age_2 * 0.0022964880605765492
    a += bmi_1 * 2.4562776660536358
    a += bmi_2 * -8.3011122314711354
    a += rati * 0.17340196856327111
    a += sbp * 0.012910126542553305
    a += sbps5 * 0.010251914291290456
    a += town * 0.033268201277287295

    # Sum from boolean values
    a += b_AF * 0.88209236928054657
    a += b_atypicalantipsy * 0.13046879855173513
    a += b_corticosteroids * 0.45485399750445543
    a += b_impotence2 * 0.22251859086705383
    a += b_migraine * 0.25584178074159913
    a += b_ra * 0.20970658013956567
    a += b_renal * 0.71853261288274384
    a += b_semi * 0.12133039882047164
    a += b_sle * 0.4401572174457522
    a += b_treatedhyp * 0.51659871082695474
    a += b_type1 * 1.2343425521675175
    a += b_type2 * 0.85942071430932221
    a += fh_cvd * 0.54055469009390156

    # Sum from interaction terms
    a += age_1 * (smoke_cat == 1) * -0.21011133933516346
    a += age_1 * (smoke_cat == 2) * 0.75268676447503191
    a += age_1 * (smoke_cat == 3) * 0.99315887556405791
    a += age_1 * (smoke_cat == 4) * 2.1331163414389076
    a += age_1 * b_AF * 3.4896675530623207
    a += age_1 * b_corticosteroids * 1.1708133653489108
    a += age_1 * b_impotence2 * -1.506400985745431
    a += age_1 * b_migraine * 2.3491159871402441
    a += age_1 * b_renal * -0.50656716327223694
    a += age_1 * b_treatedhyp * 6.5114581098532671
    a += age_1 * b_type1 * 5.3379864878006531
    a += age_1 * b_type2 * 3.6461817406221311
    a += age_1 * bmi_1 * 31.004952956033886
    a += age_1 * bmi_2 * -111.29157184391643
    a += age_1 * fh_cvd * 2.7808628508531887
    a += age_1 * sbp * 0.018858524469865853
    a += age_1 * town * -0.1007554870063731
    a += age_2 * (smoke_cat == 1) * -0.00049854870275326121
    a += age_2 * (smoke_cat == 2) * -0.00079875633317385414
    a += age_2 * (smoke_cat == 3) * -0.00083706184266251296
    a += age_2 * (smoke_cat == 4) * -0.00078400319155637289
    a += age_2 * b_AF * -0.00034995608340636049
    a += age_2 * b_corticosteroids * -0.0002496045095297166
    a += age_2 * b_impotence2 * -0.0011058218441227373
    a += age_2 * b_migraine * 0.00019896446041478631
    a += age_2 * b_renal * -0.0018325930166498813
    a += age_2 * b_treatedhyp * 0.00063838053104165013
    a += age_2 * b_type1 * 0.0006409780808752897
    a += age_2 * b_type2 * -0.00024695695588868315
    a += age_2 * bmi_1 * 0.0050380102356322029
    a += age_2 * bmi_2 * -0.013074483002524319
    a += age_2 * fh_cvd * -0.00024791809907396037
    a += age_2 * sbp * -0.00001271874191588457
    a += age_2 * town * -0.000093299642323272888

    #print('a')
    #print(a)
    #print(math.pow(survivor[surv], math.exp(a)))

    # Calculate the score itself
    score = 100.0 * (1 - math.pow(survivor[surv], math.exp(a)))
    return score




def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI using weight in kilograms and height in meters.

    Parameters:
    - weight_kg (float): Weight in kilograms
    - height_m (float): Height in meters

    Returns:
    - float: BMI value
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")

    bmi = weight_kg / (height_m ** 2)
    return bmi

def getlist_disease(search_words,eidv):
    save_diseases=folderRoot+'data/diseasesComorbo_qrisk.csv'

    df1 = pd.read_csv(save_diseases)

    dfc = df1[df1['date'] <= '2012-01-01']

    print(dfc)
    diseases_var=pd.DataFrame({'eid':eidv})


    for search_word in search_words:
        # Create a new column 'result' in the DataFrame
        dv = []
        for ei in eidv:
            dvc = pd.DataFrame()
            # Create a new column 'result' with 1 if the number is in the "eid" column and has the specific code in the "code" column, otherwise 0
            # Create a new column 'result' with 1 if the number is in the "ID" column and has "cvd" in the same rows of the "code" column, otherwise 0
            dvc['result'] = (dfc['eid'] == ei) & (dfc['code'] == search_word)



            # Convert boolean values to 1s and 0s
            dvc['result'] = dvc['result'].astype(int)

            if sum(dvc['result'])>0:
                dv.append(1)
            else:
                dv.append(0)
        diseases_var[search_word] = dv#(dfc['eid'].isin(eidv)) & (dfc['code'] == search_word)
        #print('ill')
        #diseases_var[search_word]
        # Convert boolean values to 1s and 0s
        #diseases_var[search_word] = dfc[search_word].astype(int)



    return diseases_var


folderRoot='/Users/angelicaatehortua/Documents/posdoctorado/UKBIOBANK-TEST/comorbidity-screening/'

disease1='Diabetes'
disease2='CVD'
set_f='TEST'
test='class'
rep=1

folder='CSV_unbalanced_torun_data3/'

fileTest=folderRoot+folder+disease1+'vs'+disease1+disease2+'_'+test+'_'+set_f+'_imputed_repet'+str(rep)+'.csv'
data = pd.read_csv(fileTest)

code_id = 'eid'
code_outcome = 'class'

dataAPP = data.copy(deep=True)

ID = data[code_id]
X = data.drop([code_id, code_outcome], axis=1)

current_year = datetime.now().year

codes_qrisk=['31','34','50','1239','4080','21002','5553','5556']
sex=X['31-0.0']
age_t=X['21022-0.0']
height=X['50-0.0']
sis=X['4080-0.1']
weight=X['21002-0.0']
# angina=X['5553']
# hypertension=X['5552']
# diabetes=X['5556']
tobacco1=X['1239-0.0']

q_risk_value=[]
tobacco=[]
bmi_r=[]
c=0
cho = X['30690-0.0']
hdl = X['30760-0.0']
bpr = X['6177-0.0']

cho_hdl_ratio=cho/hdl
#tdep = X['189-0.0'] doesn't exist
#
# # Get rows from df_a where numbers in 'f.eid' are in 'ID' from df_b
# result_cho = pd.merge(cho, data, how='inner', left_on='f.eid', right_on='ID')
# # Sort the result by the 'ID' column from df_b
# result_cho = result_cho.sort_values(by='ID')
# # Drop the duplicate 'ID' column if needed
# result_cho = result_cho.drop('ID', axis=1)
#
# # Get rows from df_a where numbers in 'f.eid' are in 'ID' from df_b
# result_hdl = pd.merge(hdl, data, how='inner', left_on='f.eid', right_on='ID')
# # Sort the result by the 'ID' column from df_b
# result_hdl = result_hdl.sort_values(by='ID')
# # Drop the duplicate 'ID' column if needed
# result_hdl = result_hdl.drop('ID', axis=1)
#
# # Get rows from df_a where numbers in 'f.eid' are in 'ID' from df_b
# result_sis = pd.merge(sis, data, how='inner', left_on='f.eid', right_on='ID')
# # Sort the result by the 'ID' column from df_b
# result_sis = result_sis.sort_values(by='ID')
# # Drop the duplicate 'ID' column if needed
# result_sis = result_sis.drop('ID', axis=1)
#
# # Get rows from df_a where numbers in 'f.eid' are in 'ID' from df_b
# result_bpr = pd.merge(bpr, data, how='inner', left_on='f.eid', right_on='ID')
# # Sort the result by the 'ID' column from df_b
# result_bpr = result_bpr.sort_values(by='ID')
# # Drop the duplicate 'ID' column if needed
# result_bpr = result_bpr.drop('ID', axis=1)


search_words = ['mental_illness','Diabetes','SLE','Atrial_Fib','Rheum_arth','Migraine','Chronic_kid','erectil_disf','HYP','Anginas']
dataIDv=getlist_disease(search_words,ID)

print(dataIDv)

for s in sex:
    bmi_r.append(calculate_bmi(weight[c], (height[c]*0.01)))
    if tobacco1[c] == 1:
        tobacco.append(3)
    elif tobacco1[c] == 2:
        tobacco.append(2)
    else:
        tobacco.append(0)
    c += 1
#
# data1 = {'sex': sex, 'age': age_t,'height': height, 'weight':weight,'angina':angina,'hypertension':hypertension,'diabetes':diabetes,'bmi': bmi_r, 'tobacco': tobacco, 'cho_hdl':cho_hdl_ratio, 'sistole': sistole_1,'std_sis': std_deviation_sis, 'bpr': result_bpr_imputed['f.6177.0.0'],'town': result_tdep_imputed['f.189.0.0']}
# df1 = pd.DataFrame(data1)
#
# new_df = pd.concat([data['ID'],df1,data[search_words]], axis=1)

q_risk_value=[]
c=0
# b_AF_t=new_df['Atrial_Fib']
# b_migraine_t=new_df['Migraine']
# b_sle_t=new_df['SLE']
# sbps5_t=new_df['std_sis']
# b_renal_t=new_df['Chronic_kid']
# b_ra_t=new_df['Rheum_arth']
# rati_t=new_df['cho_hdl']
# b_semi_t=new_df['mental_illness']
# town_t=new_df['town']
# b_impotence2_t=new_df['erectil_disf']

for t in sex:
    if t==0: # female

        result = cvd_female_raw(age=age_t[c], b_AF=dataIDv.loc[c, 'Atrial_Fib'], b_atypicalantipsy=0, b_corticosteroids=0, b_migraine=dataIDv.loc[c, 'Migraine'], b_ra=dataIDv.loc[c, 'Rheum_arth'],
                                       b_renal=dataIDv.loc[c, 'Chronic_kid'], b_semi=dataIDv.loc[c, 'mental_illness'], b_sle=dataIDv.loc[c, 'SLE'], b_treatedhyp=dataIDv.loc[c, 'HYP'], b_type1=0, b_type2=dataIDv.loc[c, 'Diabetes'], bmi=bmi_r[c],
                                       ethrisk=0, fh_cvd=0, rati=cho_hdl_ratio[c], sbp=sis[c], sbps5=0, smoke_cat=tobacco[c], surv=10, town=0)
        #print(result_female)

    elif t==1: # male

        result = cvd_male_raw(age=age_t[c], b_AF=dataIDv.loc[c, 'Atrial_Fib'], b_atypicalantipsy=0, b_corticosteroids=0, b_impotence2=dataIDv.loc[c, 'erectil_disf'],
                                   b_migraine=dataIDv.loc[c, 'Migraine'], b_ra=dataIDv.loc[c, 'Rheum_arth'], b_renal=dataIDv.loc[c, 'Chronic_kid'], b_semi=dataIDv.loc[c, 'mental_illness'], b_sle=dataIDv.loc[c, 'SLE'], b_treatedhyp=dataIDv.loc[c, 'HYP'], b_type1=0,
                                   b_type2=dataIDv.loc[c, 'Diabetes'], bmi=bmi_r[c], ethrisk=0, fh_cvd=0, rati=cho_hdl_ratio[c], sbp=sis[c], sbps5=0, smoke_cat=tobacco[c],
                                   surv=10, town=0)  #town_t[c]
        #print(result_male)
    q_risk_value.append(result)
    c+=1


print(q_risk_value)


df_q=pd.DataFrame({'ID': ID,'q_risk17':q_risk_value ,'class':data[code_outcome]})
df_q.to_csv(folderRoot+folder+disease1+disease1+'vs'+disease2+'_Qrisk17'+'.csv', index = False, header=True)

