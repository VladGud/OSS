#!/bin/bash
AMOUNT=`echo -e "$USER$HOME" | tr -d "\n" | wc -c`
echo "$USER $HOME $AMOUNT"
