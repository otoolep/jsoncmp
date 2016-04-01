#!/usr/bin/env python

import json
import os
import argparse
import sys



def main():
    p = argparse.ArgumentParser(description='Compare two JSON data sets')
    p.add_argument('file1', metavar='FILE', type=str, help='path to first input file')
    p.add_argument('file2', metavar='FILE', type=str, help='path to second input file')

    args = p.parse_args()

    file1 = args.file1
    file2 = args.file2

    files = []
    for f in [file1, file2]:
        try:
            files.append(open(f))
        except IOError:
            print 'failed to open file %s' % f
            sys.exit(1)

    data1 = json.load(files[0])
    data2 = json.load(files[1])

    if json.dumps(data1, sort_keys=True) == json.dumps(data2, sort_keys=True):
        print 'Data are identical.'
    else:
        print 'Data are NOT identical.'

if __name__ == '__main__':
    main()
