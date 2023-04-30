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
import numpy as np

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
keys = [item[0] for item in items[:10]]
values = [item[1] for item in items[:10]]
keys.reverse()
values.reverse()
plt.bar(sorted(keys), values)
plt.ylabel("Number of Tweets")
if args.input_path[-1] == 'g':
    plt.title("The Top 10 Languages that tweeted" + args.key[1:] + "in 2020")
    plt.xlabel("Language")
    plt.savefig(args.key[1:] + '_lang.png')
elif args.input_path == 'country':
    plt.title("The Top 10 Countries that tweeted" + args.key[1:] + "in 2020")
    plt.xlabel("Country")
    plt.savefig(args.key[1:] + '_country.png')
else:
    plt.xlabel("Unknown Key")
    plt.savefig(args.key[1:] + '_unknown.png')
