import pandas as pd
import numpy as np
a=0
b=0
df = pd.read_csv("jadamiantranscryption.txt",sep="   ",header=None)
#print(df)
zmienna = pd.DataFrame()
start=0
end=0
speaker=""
tekst =""
df2 = pd.read_csv("jadamianspeakers.txt", sep=" ",header=None)
#df2[df2.columns[0]] = np.floor(df2[df2.columns[0]])
df2[df2.columns[0]] = np.round(df2[df2.columns[0]])
df2[df2.columns[1]] = np.round(df2[df2.columns[1]])
#df2[df2.columns[1]] = np.ceil(df2[df2.columns[1]])

df["3"] = df2[df2.columns[2]]
#print(df)

a=0
b=0
for i in range(0,int(max(df2[df2.columns[1]]))):
    try:
        if( df2[df2.columns[1]][a] - df[df.columns[1]][b] < 1):
            df["3"][a] = df2[df2.columns[2]][b]
            a=a+1
            b=b+1       
            
        elif ( df2[df2.columns[1]][a]  <  df[df.columns[1]][b]):
            a=a+1
        else:
            b=b+1
    except:
        print(i)
        break

print(df)