import pandas as pd
import timeit as t

def getPandas(df,sex):
    if (sex != ""):
        numsurv = df[df.Sex == sex].Survived.value_counts()
        print(numsurv)
    else:
        print(len(df))
        newdf = df.dropna(subset=['Age'])
        print(len(newdf))
        numsurv = newdf[newdf.Age < 16].Survived.value_counts()
        print(numsurv)
    return (numsurv[1] / (numsurv[0] + numsurv[1])) * 100

def getKidz(data):
    # the math numsurv / numkids * 100
    numkids = 0
    numsurv = 0 # var scope!!! local var, deleted after function runs
    for p in data:
        temp = p.split(",")
        if (temp[6] != ""): # error check for missing data
            if (float(temp[6]) < 16.0):
                numkids = numkids + 1
                if (temp[1] == "1"):
                    numsurv = numsurv + 1
    return (numsurv / numkids) * 100

def getGrp(data,sex):
    # the math numsurv / numgrp * 100
    numgrp = 0
    numsurv = 0
    for p in data:
        temp = p.split(",")
        if (temp[5] == sex):
            numgrp = numgrp + 1
            if (temp[1] == "1"):
                numsurv = numsurv + 1
    return (numsurv / numgrp) * 100       

# open our titanic database
def vanilla():
    file = open("titanic.csv","r") # r is read only
    cols = file.readline() # gets first line of data
    data = file.readlines()
    file.close()

    print("This is vanilla")
    w = getGrp(data,"female")
    m = getGrp(data,"male")
    k = getKidz(data)
    print(w,k,m)

def usepandas():
    df = pd.read_csv("titanic.csv",usecols=['Age','Sex','Pclass','Name','Survived'])
    print("This is pandas")
    w = getPandas(df,"female")
    m = getPandas(df,"male")
    k = getPandas(df,"")
    print(w,k,m)

    # Did the price of the ticket affect survival rate?
    print(df.groupby('Pclass').Survived.value_counts())
    

print(t.timeit(vanilla,number=1))
print(t.timeit(usepandas,number=1))

"""
fo = open("index1.html","w")
fo.write("<html>")
fo.write("<h1>Women and Children first?</h1>")
fo.write("<p>This is the result of our Titanic analysis.</p>")
fo.write("<img src='titanic.jpg' width='500px'>")
fo.write("<br>")
fo.write("<h2>Study conclusion</h2>")
fo.write("<svg width='800' height='500'>")
fo.write("<rect width='740' height='100' fill='#ff0303'></rect>")
fo.write("<text x='25' y='25' fill='white'>Women</text>")
fo.write("<rect y='125' width='590' height='100' fill='green'></rect>")
fo.write("<rect y='250' width='190' height='100' fill='yellow'></rect>")
fo.write("</html>")
fo.close()
"""





