# race between Pandas and Vanilla Python

import timeit as t

def vanilla():
    fo = open("records.csv","r") # 5000000 rows
    cols = fo.readline() # read first line into cols
    data = fo.readlines()
    fo.close()

    # sequential or linear search algorithm
    numcan = 0
    for row in data:
        temp = row.split(",")
        if (temp[1] == "Canada"):
            numcan = numcan + 1
    print(numcan)

def mypanda():
    import pandas as pd
    df = pd.read_csv("records.csv")
    print(df[df.Country == 'Canada'].count())
    

print(t.timeit(vanilla,number=1))
print(t.timeit(mypanda,number=1))



            
    
