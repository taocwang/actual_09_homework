#!/bin/bash python


srcfile = '/Users/yang/Downloads/www_access_20140823.log'

def print_file(srcfile):
    read_file = open(srcfile,'r')
    for line  in read_file.readlines():
        return  line

print_file(srcfile)


wfile = '/Users/yang/Downloads/www_access_20140823.log'

def write_file(wfile):
    read_file = open('/Users/yang/Downloads/dstfile','w')
    read_file.write(wfile)
    read_file.close()

