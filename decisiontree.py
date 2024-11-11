import csv
import  math

def printtree(node,headers,space=""):
    if node.prediction is not None:
        print(space+f"prediction:{node.prediction}")
        return
    print(f"{space}{headers[node.index]}=={node.value}?")
    print(space+'-->true branch')
    printtree(node.truebranch,headers,spacing=" ")
    print(space+'-->false branch')
    printtree(node.falsebranch,headers,spacing=" ")


def splitdata(data,index,value):
    true_branch=[row for row in data if row[0][index]==value]
    false_branch=[row for row in data if row[0][index]!=value]
    return true_branch,false_branch


def bestsplit(data):
    best_gain=0
    best_index=None
    best_value=None
    current_entropy=entropy(data)
    n_features=len(data[0][0])
    for index in (n_features):
        values=set([row[0][index]for row in data])
        for value in values:
            true_branch,false_branch=splitdata(data,index,value)
            if not true_branch or not false_branch:
                continue
            p=len(true_branch)/len(data)
            gain=current_entropy-p*entropy(true_branch)-(1-p)*entropy(false_branch)
            if gain>best_gain:
                best_gain=gain
                best_index=index
                best_value=value
    return best_gain,best_index,best_value


def buildtree(data):
    gain,index,value=bestsplit(data)
    if gain ==0:
        return decisionnode(prediction=data[0][1])
    
    truebranch,falsebranch=splitdata(data,index,value)
    true_node=buildtree(truebranch)
    false_node=buildtree(falsebranch)

    return decisionnode(index=index,value=value,truebranch=true_node,falsebranch=false_node)
     
class decisionnode:
    def __init__(self,index=None,value=None,truebranch=None,falsebranch=None,prediction=None):
        self.index=index
        self.value=value
        self.truebranch=truebranch
        self.falsebranch=falsebranch
        self.prediction=prediction


def classification(tree,sample):
    if tree.prediction is not None:
        return tree.prediction
    if sample[tree.index]==tree.value:
        return classification(tree.truebranch,sample)
    else:
         return classification(tree.falsebranch,sample)


def entropy(data):
    totalsample=len(data)
    label_count={}
    for  features,label in data:
        if label not in label_count:
            label_count[label]=0
        label_count[label]+=1
    entropy=0
    for label in label_count:
        p=label_count[label]/totalsample
        entropy-=p*math.log2(p)
    return entropy


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

data=read_file('decision.py')
tree=buildtree(data)
headers=['age','income','student','credit rating']
sample=[]
for head in headers:
    value=input(f"enter value for {head}")
    sample.append(value)
print("DECISION TREE")
printtree(tree,headers)
predictedclass=classification(tree,sample)
print(f"predicted class:{predictedclass}")