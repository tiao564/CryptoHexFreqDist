#! /usr/bin/env python
#################
#Dylan Guldy    #
#Cryptogropy    #
#Doctor Craver  #
#Homework 1     #
#################
#############################################################
#This program takes a file converted to hex form and finds  #
#   the frequency distribution of the values                #
#File was obtained by the vim command :r !xxd -i file name, #
#   then stripping all new lines, commas, and double spaces #
#############################################################
    
import sys
hex_name = sys.argv[1]
hex_file = open(hex_name)
hex_file = hex_file.read()
hex_file = hex_file.split(" ")
hex_vals = {}
hex_count = []

for val in hex_file:
    if val in hex_vals:
        hex_vals[val] = hex_vals[val]+1
    else:
        hex_vals[val] = 0

print hex_vals
