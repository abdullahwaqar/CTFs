#!/bin/bash

nc 2018shell.picoctf.com 44310 | grep -oE "picoCTF{.*}" --color=none