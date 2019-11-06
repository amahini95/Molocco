'''
most popular = number of purchasers 
			   total qty of each product sold.

Ties: output the product ids that are tied.

Format: {"user_id" : "uid_1", "product_id" : "pid_1", "quantity" : 45}

'''

import csv
import json
from collections import defaultdict

def findMostPopProd(file):

	qty = defaultdict(int)
	user = defaultdict(set)

	for line in file:
		line = json.loads(line[0])
		user[line["product_id"]].add(line["user_id"])
		qty[line["product_id"]] += line["quantity"]

	customers = 0
	for u in user:
		customers = max(customers,len(user[u]))
	num_purch = []
	for u in user:
		if(len(user[u])) == customers:
			num_purch.append(u)

	quantities = 0
	for q in qty:
		quantities = max(quantities, qty[q])
	num_prods = []
	for q in qty:
		if(qty[q] == quantities):
			num_prods.append(q)

	print("Most popular based on the unique number of users who purchased each:{0}".format(num_purch))
	print("Most popular Based on the total quantity of each product sold:{0}".format(num_prods))

if __name__ == "__main__":
	f = open('SWE sample data - Q2 data.csv', 'r', encoding = 'utf-8')
	r = csv.reader(f, delimiter = ' ', skipinitialspace = True)
	findMostPopProd(r)
	