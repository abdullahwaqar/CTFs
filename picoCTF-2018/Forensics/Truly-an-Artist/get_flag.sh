#!/bin/bash

strings 2018.png | grep -oE "picoCTF{.*}" --color=none