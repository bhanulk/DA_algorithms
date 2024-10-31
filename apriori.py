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

min_support=2
for i in range  (1,4):
    item_counts=generate_item_frequencies(transactions,i)
    #generating frequent item sets
    frequent_itemsets={itemset: count for itemset, count in item_counts.items() if count >= min_support}
    print(f"Frequent {i}-item sets:", frequent_itemsets)

