import csv
import math

def read_file(filename):
    data=[]
    with open('filename') as file:
        next(file)
        for line in file:
            row=line.strip.split(',')
            features=row[1:-1]
            label=row[-1]
            data.append((features,label))
    return data
def calculate_priorprobability(data):
    class_count={}
    prior_prob={}
    for features, label in data:
        if label not in class_count:
            class_count[label]=0
        class_count[label]+=1
    for labels in class_count:
        prior_prob[label]=class_count[label]/len(data)

    return prior_prob
  
def calculate_likelihood(data):
    class_count={}
    feature_count={}
    likelihood_prob={}
    for features, label in data:
        if label not in class_count:
            class_count[label]=0
            feature_count[label]=[{} for i in range (len(features))]
        class_count[label]+=1
        for i in range (len(features)):
            if features[i] not in feature_count[label][i]:
                feature_count[label][i][features[i]]=0
            feature_count[label][i][features[i]]+=1
    for label in feature_count:
        likelihood_prob[label]=[]
        for i in range(len(feature_count[label])):
            likelihood_prob.append({key:feature_count[label][i][key]/class_count[label]for key in feature_count[label][i]})
    return likelihood_prob




            


        