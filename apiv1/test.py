import pandas as pd

tb = pd.read_csv('stunt_boy.csv')
tg = pd.read_csv('stunt_girl.csv')

def dentistsmile_classification(sex, age_month, height):
    if sex==0:
        table = tb
    else:
        table = tg
    data = table.loc[table['age_month']==age_month].iloc[0]

    median = float(data['Median'].strip())
    

    if height < median:
        sd = float(data['-1_SD'].strip())
    elif height > median:
        sd = float(data['3_SD'].strip())
    else:
        return 0

    z_score = ((height-median)/abs(median-sd))

    print(z_score)
    if z_score < -3:
        return -2
    elif -3 <= z_score < -2:
        return -1
    elif -2 <= z_score <= 2:
        return 1
    else:
        return 2

if __name__=='__main__':
    print(dentistsmile_classification(0, 26, 90))