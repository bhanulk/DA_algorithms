import pandas as pd

data=pd.read_csv('data_matrix.csv')
col=len(data.columns)
row=len(data)
print(data)


print("number of attributes:",col)
print("number of instances:",row)

numeric_att=data.select_dtypes(include=['number']).columns.tolist()
nominal_att=data.select_dtypes(exclude=['number']).columns.tolist()

data[numeric_att]=(data[numeric_att]-data[numeric_att].min())/(data[numeric_att].max()-data[numeric_att].min())

print('normalized dataframe')
print(data)

n=data.shape[0]

num_dismatrix=[[0.0 for _ in range (n)]for i in range (n)]
nom_dismatrix=[[0 for _ in range (n)]for i in range (n)]
mix_dismatrix=[[0.0 for _ in range (n)]for i in range (n)]

#dissimilarity matrix for nominal attributes 
for i in range (n):
    for j in range (n):
        if i>=j:
            dissimilarity=sum([1 if data[nominal_att].iloc[i,k]!= data[nominal_att].iloc[j,k] else 0 for k in range (len(nominal_att))])
            nom_dismatrix[i][j]=round(dissimilarity,2)

print("nominal attributes dissimilarity matrix")
for row in nom_dismatrix:
    print(row)

#dissimilarity martix for numeric attributes
for i in range (n):
    for j in range (n):
        if i>=j:
             dissimilarity=sum([abs(data[numeric_att].iloc[i,k]-data[numeric_att].iloc[j,k])for k in range(len(numeric_att))])
             num_dismatrix[i][j]=round(dissimilarity,2)

print("numeric attributes dissimilarity matrix")
for row in num_dismatrix:
    print(row)

#dissimilarity matrix for mixed attributes
for i in range(n):
    for j in range(n):
        if i>=j:
            num=num_dismatrix[i][j]/len(numeric_att) if len(numeric_att)>0 else 0
            nom=nom_dismatrix[i][j]/len(nominal_att) if len(nominal_att)>0 else 0
            mix_dismatrix[i][j]=round((num+nom)/2,2)

print("mixed attribute dissimilarity matrix")            
for row in mix_dismatrix:
    print(row)








