#!/bin/bash
if [ -f "$1" ]; then
    if [-s "$1"]; then
        echo "1"
    else
        echo "0"
    fi
else
    echo "2"
fi
