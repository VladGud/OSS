#!/bin/bash

find ~ -maxdepth 1 -type f -name "*.txt" > /tmp/help
cat /tmp/help
cat /tmp/help | xargs du -acb 2>/dev/null| tail -1 | cut -f1
cat /tmp/help | xargs wc -l 2>/dev/null | tail -1 | awk '{print $1}'
rm /tmp/help
