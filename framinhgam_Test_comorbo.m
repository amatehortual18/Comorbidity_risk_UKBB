clear
close all
clc

%% 

testv='Framingham';  % Framingham


test='class';
disease1='Diabetes';  % Depre Diabetes
disease2='CVD';
set_f='TEST'; % TRAIN TEST
rep=1;

folder='../CSV_unbalanced_torun_data3/';


file_nameI=[folder,disease1,'vs',disease1,disease2,'_',test,'_',set_f,'_imputed_repet',num2str(rep),'.csv'];


tb=readtable([file_nameI]);
%tb(1,:)=[];

ms=size(tb);
classes=table2array(tb(:,ms(2)));
id_all=table2array(tb(:,1));

data=table2array(tb(:,2:ms(2)-1));

c = date;
y=year(c);

header=tb.Properties.VariableNames(2:ms(2)-1);

for k=1:size(data,1)
    specificB='31';
    positions = find(contains(header, ['x', specificB, '_0_0']));
    gender = data(k,positions);
    
    specificB='21022';
    positions = find(contains(header, ['x', specificB, '_0_0']));
    age = data(k,positions);
    
    specificB='30690';
    positions = find(contains(header, ['x', specificB, '_0_0']));
    totalcholesterol=(data(k,positions)*(386.65))/10;
    
    specificB='1239';
    positions = find(contains(header, ['x', specificB, '_0_0']));  % only 1 frequent smoker is considered
    smoker=data(k,positions);
    
    specificB='30760';
    positions = find(contains(header, ['x', specificB, '_0_0']));
    hdlcholesterol=(data(k,6)*(386.65))/10;
    
    
    specificB='4080';
    positions = find(contains(header, ['x', specificB, '_0_1'])); % the last one
    syspressure=data(k,positions);
    port_totalRisk(k,1) = getFraminghamScore(gender,age,totalcholesterol,smoker,hdlcholesterol,syspressure);
end

%%
clase=port_totalRisk>0.5;
txb=table(id_all,port_totalRisk,clase,classes); 
file_nameIs=[disease1,'vs',disease1,disease2,'_',test,'_','FraminghamValues_Comorbo.csv'];

txb.Properties.VariableNames=["ID","FraminghamScore","prediction","classe"];
writetable(txb,[folder,file_nameIs])

fprintf('Values were saved \n')
