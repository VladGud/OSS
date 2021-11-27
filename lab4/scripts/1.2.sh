#!/bin/bash
DIR=~
find $DIR -maxdepth 1 -type f -name "*.txt" | wc -l
