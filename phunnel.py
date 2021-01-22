#!/usr/bin/env python

# A simple script to filter password lists for a desired complexity policy

from __future__ import print_function
import re
import os
import sys
import argparse

__version__ = 0.03

SPECIAL_CHARS = "[\+\!\@\#\$\%\^\&\*\(\)\{\}\[\]\;\:\'\"\\\?\/\.\>\,\<\`\~\_\-\=\|]"

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    parser.add_argument('outfile', help="Output file",default=sys.stdout, type=argparse.FileType('w'))
    parser.add_argument('-m', help="Minimum password length", default=1, type=int)
    parser.add_argument('-max', help="Maximum password length", default=30, type=int)
    parser.add_argument('-u', help="Require at least 1 uppercase", action='store_true', default=0)
    parser.add_argument('-l', help="Require at least 1 lowercase", action='store_true', default=0)
    parser.add_argument('-n', help="Require at least 1 number", action='store_true', default=0)
    parser.add_argument('-s', help="Require at least 1 special", action='store_true', default=0)
    parser.add_argument('-ns', help="Password can contain NO special", action='store_true', default=0)

    args = parser.parse_args(arguments)

    #with open(args.infile) as file:
    #    print(file.read())
    #print(args.infile.readline())

    for lines in args.infile:
        # Ensure minimum length
        if (len(lines) < args.m):
            continue
        # Ensure max length
        if (len(lines) > args.max):
            continue
        # Ensure an uppercase char is used
        if (args.u and (re.search("[A-Z]", lines) is None)):
            continue
        # Ensure a lowercase char is used
        if (args.l and (re.search("[a-z]", lines) is None)):
            continue
        # Ensure a number is used
        if (args.n and (re.search("[0-9]", lines) is None)):
            continue
        # Ensure a special char is used - may want to allow user-defined set
        if (args.s and (re.search(SPECIAL_CHARS, lines) is None)):
            continue
        # Ensure no special chars (not strictly exaustive - should make NOT num/alpha)
        if (args.ns and (re.search(SPECIAL_CHARS, lines) is not None)):
            continue
        args.outfile.write(lines)

    # No need to print args
    #print(args)
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

