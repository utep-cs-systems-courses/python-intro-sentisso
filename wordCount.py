#! /usr/bin/env python3

import sys
import re
import os
import subprocess

if len(sys.argv) != 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()

text_fname = sys.argv[1]
output_fname = sys.argv[2]

if not os.path.exists(text_fname):
    print("text file input %s doesn't exist! Exiting" % text_fname)
    exit()


w_freq = {}

with open(text_fname, 'r') as f:
    for line in f:
        # get rid of newline characters
        line = line.strip()

        # remove punctuation, quotes, etc.
        line = re.sub(r'[,.":;]', '', line.strip())

        # split line to words by spaces, tab characters, dashes and quotes
        words = re.split(r'[\' \t-]', line)

        for word in words:
            # ignore excessive spaces
            if len(word) == 0:
                continue

            word = word.lower()
            w_freq[word] = w_freq.get(word, 0) + 1


# sort the words in ascending order
asc = sorted(w_freq.keys())

# write, not append
with open(output_fname, 'w') as f:
    for word in asc:
        f.write('%s %s\n' % (word, w_freq[word]))