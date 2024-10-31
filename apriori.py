import pandas as pd
from itertools import combinations
#reading the csv file
df=pd.read_csv('data.csv')
#count frequency
def generate_item_frequencies(transactions, itemset_size):
    itemcount ={}
    for transaction in transactions:
        for itemset in combinations(transaction,itemset_size):
            itemset=tuple(sorted(itemset)) 
            if itemset in itemcount:
                itemcount[itemset] += 1
            else:
                itemcount[itemset] = 1
    return itemcount



#converting into transactions
df['ITEMS']=df['ITEMS'].apply(lambda x: x.split(','))
transactions=df['ITEMS'].tolist()
min_confidence=0.5
min_support=2
for i in range  (1,4):
    item_counts=generate_item_frequencies(transactions,i)
    #generating frequent item sets
    frequent_itemsets={itemset: count for itemset, count in item_counts.items() if count >= min_support}
    print(f"Frequent {i}-item sets:", frequent_itemsets)

association_rules=[]
for itemset in frequent_itemsets:
    for i in range (1,len(itemset)):
        for antecedent in combinations(itemset,i):
            antecedent = tuple(sorted(set(antecedent)))
            consequent=tuple(sorted(set(itemset) - set(antecedent)))
            support_antecedent=frequent_itemsets.get(antecedent,0)
            support_full=frequent_itemsets.get(itemset,0)
            if support_antecedent > 0:
                confidence=support_full/support_antecedent
                print(confidence)
                if confidence>=min_confidence:
                    association_rules.append((antecedent,consequent,confidence))
           


for rule in association_rules:
    print(f"Rule: {rule[0]} -> {rule[1]}, Confidence: {rule[2]:.2f}")
