#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

#create bar graph
top_items = items[:10] 
keys = [item[0] for item in top_items]
values = [item[1] for item in top_items]
keys = keys[::-1]
values = values[::-1]
plt.bar(range(len(keys)), values)
plt.xticks(range(len(keys)), keys)
plt.ylabel("Number of Tweets")
if args.input_path[-1] == 'g':
    plt.title("The Top 10 Languages that tweeted" + args.key[1:] + "in 2020")
    plt.xlabel("Language")
    plt.savefig(args.key[1:] + '_lang.png')
else:
    plt.title("The Top 10 Countries that tweeted" + args.key[1:] + "in 2020")
    plt.xlabel("Country")
    plt.savefig(args.key[1:] + '_country.png')
