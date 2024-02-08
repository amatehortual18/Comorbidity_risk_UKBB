function port_totalRisk = getFraminghamScore(gender,age,totalcholesterol,smoker,hdlcholesterol,syspressure)

%  Framingham Risk Score for Women
    
points=0;

%% women

if gender == 0 % women 
    %% age

    if age>=20 && age<=34 
        points=points-7;
    end
    if age>=35 && age<=39 
        points=points-3;
    end
    if age>=40 && age<=44 
        points=points+0;
    end
    if age>=45 && age<=49 
        points=points+3;
    end
    if age>=50 && age<=54 
        points=points+6;
    end
    if age>=55 && age<=59 
        points=points+8;
    end
    if age>=60 && age<=64 
        points=points+10;
    end
    if age>=65 && age<=69 
        points=points+12;
    end
    if age>=70 && age<=74 
        points=points+14;
    end
    if age>=75 && age<=79 
        points=points+16;
    end

    %% totalcholesterol

    if age>=20 && age <=39
        if totalcholesterol <160
            points = points+0;
        end
        if totalcholesterol >=160 && totalcholesterol<=199
            points = points+4;
        end
        if totalcholesterol >=200 && totalcholesterol<=239
            points = points+8;
        end
        if totalcholesterol >=240 && totalcholesterol<=279
            points = points+11;
        end  
        if totalcholesterol >=280
            points = points+13;
        end
    end

    if age>=40 && age <=49
        if totalcholesterol <160
            points = points+0;
        end
        if totalcholesterol >=160 && totalcholesterol<=199
            points = points+3;
        end
        if totalcholesterol >=200 && totalcholesterol<=239
            points = points+6;
        end
        if totalcholesterol >=240 && totalcholesterol<=279
            points = points+8;
        end  
        if totalcholesterol >=280
            points = points+10;
        end
    end

    if age>=50 && age <=59
        if totalcholesterol <160
            points = points+0;
        end
        if totalcholesterol >=160 && totalcholesterol<=199
            points = points+2;
        end
        if totalcholesterol >=200 && totalcholesterol<=239
            points = points+4;
        end
        if totalcholesterol >=240 && totalcholesterol<=279
            points = points+5;
        end  
        if totalcholesterol >=280
            points = points+7;
        end
    end

    if age>=60 && age <=69
        if totalcholesterol <160
            points = points+0;
        end
        if totalcholesterol >=160 && totalcholesterol<=199
            points = points+1;
        end
        if totalcholesterol >=200 && totalcholesterol<=239
            points = points+2;
        end
        if totalcholesterol >=240 && totalcholesterol<=279
            points = points+3;
        end  
        if totalcholesterol >=280
            points = points+4;
        end
    end

    if age>=70 && age <=79
        if totalcholesterol <160
            points = points+0;
        end
        if totalcholesterol >=160 && totalcholesterol<=199
            points = points+1;
        end
        if totalcholesterol >=200 && totalcholesterol<=239
            points = points+1;
        end
        if totalcholesterol >=240 && totalcholesterol<=279
            points = points+2;
        end  
        if totalcholesterol >=280
            points = points+2;
        end
    end

    if smoker==1
        if age>=20 && age <=39
            points=points+9;
        end
        if age>=40 && age <=49
            points=points+7;
        end
        if age>=50 && age <=59
            points=points+4;
        end
        if age>=60 && age <=69
            points=points+2;
        end
        if age>=70 && age <=79
            points=points+1;
        end
    end

    %% HDL cholesterol

    if hdlcholesterol >=60
        points=points-1;
    end

    if hdlcholesterol >=50 && hdlcholesterol <=59
        points=points+0;
    end

    if hdlcholesterol >=40 && hdlcholesterol <=49
        points=points+1;
    end

    if hdlcholesterol <40 
        points=points+2;
    end

    %% Systolic blood pressure

    if syspressure<120 
        points =points+0;
    end

    if syspressure>=120 && syspressure <=129 
        points =points+1;
    end

    if syspressure>=130 && syspressure <=139 
        points =points+2;
    end

    if syspressure>=140 && syspressure <=159 
        points =points+3;
    end

    if syspressure>=160
        points =points+4;
    end
    
    %% totalRisk
    
    totalRisk=0;
    if points <=9 
        totalRisk=1;
    end
    if points>9 && points <=12
        totalRisk=1;
    end
    if points>=13 && points <=14
        totalRisk=2;
    end
    if points==15
        totalRisk=3;
    end
    if points==16
        totalRisk=4;
    end
    if points==17
        totalRisk=5;
    end
    if points==18
        totalRisk=6;
    end
    if points==19
        totalRisk=8;
    end
    if points==20
        totalRisk=11;
    end
    if points==21
        totalRisk=14;
    end
    if points==22
        totalRisk=17;
    end
    if points==23
        totalRisk=22;
    end
    if points==24
        totalRisk=27;
    end
    if points>25
        totalRisk=30;
    end
end

%% men

if gender == 1 % men 
    %% age

    if age>=20 && age<=34 
        points=points-9;
    end
    if age>=35 && age<=39 
        points=points-4;
    end
    if age>=40 && age<=44 
        points=points+0;
    end
    if age>=45 && age<=49 
        points=points+3;
    end
    if age>=50 && age<=54 
        points=points+6;
    end
    if age>=55 && age<=59 
        points=points+8;
    end
    if age>=60 && age<=64 
        points=points+10;
    end
    if age>=65 && age<=69 
        points=points+11;
    end
    if age>=70 && age<=74 
        points=points+12;
    end
    if age>=75 && age<=79 
        points=points+13;
    end

    %% totalcholesterol

    if age>=20 && age <=39
        if totalcholesterol <160
            points = points+0;
        end
        if totalcholesterol >=160 && totalcholesterol<=199
            points = points+4;
        end
        if totalcholesterol >=200 && totalcholesterol<=239
            points = points+7;
        end
        if totalcholesterol >=240 && totalcholesterol<=279
            points = points+9;
        end  
        if totalcholesterol >=280
            points = points+11;
        end
    end


    if age>=40 && age <=49
        if totalcholesterol <160
            points = points+0;
        end
        if totalcholesterol >=160 && totalcholesterol<=199
            points = points+3;
        end
        if totalcholesterol >=200 && totalcholesterol<=239
            points = points+5;
        end
        if totalcholesterol >=240 && totalcholesterol<=279
            points = points+6;
        end  
        if totalcholesterol >=280
            points = points+8;
        end
    end

    if age>=50 && age <=59
        if totalcholesterol <160
            points = points+0;
        end
        if totalcholesterol >=160 && totalcholesterol<=199
            points = points+2;
        end
        if totalcholesterol >=200 && totalcholesterol<=239
            points = points+3;
        end
        if totalcholesterol >=240 && totalcholesterol<=279
            points = points+4;
        end  
        if totalcholesterol >=280
            points = points+5;
        end
    end

    if age>=60 && age <=69
        if totalcholesterol <160
            points = points+0;
        end
        if totalcholesterol >=160 && totalcholesterol<=199
            points = points+1;
        end
        if totalcholesterol >=200 && totalcholesterol<=239
            points = points+1;
        end
        if totalcholesterol >=240 && totalcholesterol<=279
            points = points+2;
        end  
        if totalcholesterol >=280
            points = points+3;
        end
    end

    if age>=70 && age <=79
        if totalcholesterol <160
            points = points+0;
        end
        if totalcholesterol >=160 && totalcholesterol<=199
            points = points+0;
        end
        if totalcholesterol >=200 && totalcholesterol<=239
            points = points+0;
        end
        if totalcholesterol >=240 && totalcholesterol<=279
            points = points+1;
        end  
        if totalcholesterol >=280
            points = points+1;
        end
    end

    if smoker==1
        if age>=20 && age <=39
            points=points+8;
        end
        if age>=40 && age <=49
            points=points+5;
        end
        if age>=50 && age <=59
            points=points+3;
        end
        if age>=60 && age <=69
            points=points+1;
        end
        if age>=70 && age <=79
            points=points+1;
        end
    end

    %% HDL cholesterol

    if hdlcholesterol >=60
        points=points-1;
    end

    if hdlcholesterol >=50 && hdlcholesterol <=59
        points=points+0;
    end

    if hdlcholesterol >=40 && hdlcholesterol <=49
        points=points+1;
    end

    if hdlcholesterol <40 
        points=points+2;
    end

    %% Systolic blood pressure

    if syspressure<120 
        points =points+0;
    end

    if syspressure>=120 && syspressure <=129 
        points =points+0;
    end

    if syspressure>=130 && syspressure <=139 
        points =points+1;
    end

    if syspressure>=140 && syspressure <=159 
        points =points+1;
    end

    if syspressure>=160
        points =points+2;
    end
    
    %% totalRisk
    
    totalRisk=0;
    if points==0
        totalRisk=1;
    end
    if points>=1 && points <=4
        totalRisk=1;
    end
    if points>=5 && points <=6
        totalRisk=2;
    end
    if points==7
        totalRisk=3;
    end
    if points==8
        totalRisk=4;
    end
    if points==9
        totalRisk=5;
    end
    if points==10
        totalRisk=6;
    end
    if points==11
        totalRisk=8;
    end
    if points==12
        totalRisk=10;
    end
    if points==13
        totalRisk=12;
    end
    if points==14
        totalRisk=16;
    end
    if points==15
        totalRisk=20;
    end
    if points==16
        totalRisk=25;
    end
    if points>=17
        totalRisk=30;
    end
end

port_totalRisk=totalRisk/30;