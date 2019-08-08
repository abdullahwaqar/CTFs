#!/bin/bash

for i in {1..26};
    do
    cat chipertext | cut -d "{" - f2 | cut -d "}" -f1 | caesar $i; done