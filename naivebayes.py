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


def classify(prior,likelihood,sample):
    posterior={}
    for label in prior:
        posterior[label]=prior[label]
        for i in range(len(sample)):
            if sample[i] in likelihood[label][i]:
                posterior[label]*=likelihood[label][i][sample[i]]
            else:
                posterior[label]*=0
    for label in posterior:
        print(f"posterior probabililty of {label}:{posterior[label]}")
    return max(posterior,key=posterior.get)

def naive_bayes_classifier(data,sample):
    prior=calculate_priorprobability(data)
    likelihood=calculate_likelihood(data)
    return classify(prior,likelihood,sample)
filename = 'nadat.csv'
training_data = read_file(filename)

new_sample = ['youth', 'medium', 'yes', 'fair'] 
predicted_class = naive_bayes_classifier(training_data, new_sample) 
print(f'Predicted class for {new_sample}: {predicted_class}')

        