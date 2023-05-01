#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--keys', nargs='+', required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import glob
import datetime
import numpy as np

data = defaultdict(lambda: defaultdict(list))
inputs = glob.glob('outputs/geoTwitter*.country')
fig, ax = plt.subplots()

for key in args.keys:
    total = defaultdict(lambda: Counter())
    y_axis = []
    for path in sorted(inputs):
        with open(path) as f:
            tmp = json.load(f)
            total = 0
            try:
                for k in tmp[key]:
                    total += tmp[key][k]
            except:
                pass
            y_axis.append(total)
    x_axis = np.arange(len(y_axis))
    ax.plot(x_axis, y_axis, label = key)

ax.set_title("Number of Tweets using " + str(args.keys)+ " in 2020")
ax.set_ylabel("Number of Tweets Using Hashtag")
ax.set_xlabel("Days passed in 2020")
plt.legend()
plt.savefig('hashtag_comparison_' + '_'.join(args.keys) + '.png')
