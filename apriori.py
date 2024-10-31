import pandas as pd
from itertools import combinations

# Reading the CSV file
df = pd.read_csv('data.csv')

# Count frequency of itemsets
def generate_item_frequencies(transactions, itemset_size):
    itemcount = {}
    for transaction in transactions:
        for itemset in combinations(transaction, itemset_size):
            itemset = tuple(sorted(itemset))
            if itemset in itemcount:
                itemcount[itemset] += 1
            else:
                itemcount[itemset] = 1
    return itemcount

# Converting into transactions
df['ITEMS'] = df['ITEMS'].apply(lambda x: x.split(','))
transactions = df['ITEMS'].tolist()
min_confidence = 0.5
min_support = 2

# Dictionary to store all frequent itemsets across different sizes
all_frequent_itemsets = {}

# Generate frequent itemsets
for i in range(1, 4):
    item_counts = generate_item_frequencies(transactions, i)
    # Filter itemsets based on minimum support
    frequent_itemsets = {itemset: count for itemset, count in item_counts.items() if count >= min_support}
    all_frequent_itemsets.update(frequent_itemsets)
    print(f"Frequent {i}-item sets:", frequent_itemsets)

# Generate association rules
association_rules = []
for itemset in all_frequent_itemsets:
    if len(itemset) > 1:  
        for i in range(1, len(itemset)):
            for antecedent in combinations(itemset, i):
                antecedent = tuple(sorted(antecedent))
                consequent = tuple(sorted(set(itemset) - set(antecedent)))
                support_antecedent = all_frequent_itemsets.get(antecedent, 0)
                support_full = all_frequent_itemsets[itemset]
                
                if support_antecedent > 0:
                    confidence = support_full / support_antecedent
                    if confidence >= min_confidence:
                        association_rules.append((antecedent, consequent, confidence))

# Printing association rules
for rule in association_rules:
    print(f"Rule: {rule[0]} -> {rule[1]}, Confidence: {rule[2]:.2f}")
