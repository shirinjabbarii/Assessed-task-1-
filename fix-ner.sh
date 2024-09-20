#!/bin/bash

# Input and output files
input_file=$1
output_file=$2

# Replace NER tags for punctuation with "O"
sed 's/[[:punct:]]\/[A-Z]\+/\0\/O/g' $input_file > $output_file
