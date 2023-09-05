import pandas as pd
import openpyxl as op
from Tools.scripts.dutree import display


magCurve = pd.read_excel("MagCurve.xlsx")
areaSecTransv = 3
largLamina = 0.3

def calcBMax(area):

    bMax = magCurve['Fluxo'].iloc[0]/area
    for i in range(45):

        if(magCurve['Fluxo'].iloc[i]/area > bMax):
            bMax = magCurve['Fluxo'].iloc[i]/area

    print(bMax)



print(calcBMax(areaSecTransv))




#valor_desejado = magCurve['MMF'].iloc[1]
#valor_desejado2 = magCurve['MMF'].iloc[2]


#print(magCurve)


#ALTERAÇÃO ADICIONADA AO PROJETO



