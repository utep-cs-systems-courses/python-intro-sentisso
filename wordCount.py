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

fd = os.open(text_fname, os.O_RDONLY)
n_bytes = os.fstat(fd).st_size
bytes = os.read(fd, n_bytes)

os.close(fd)

lines = bytes.decode().split("\n")

for line in lines:
    if len(line) == 0:
        continue

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
fd = os.open(output_fname, os.O_WRONLY)

for word in asc:
    line = '%s %s\n' % (word, w_freq[word])
    os.write(fd, line.encode())

os.close(fd)
