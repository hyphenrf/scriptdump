#!/usr/bin/env python3

import csv
import json

RYMFILE = "user_albums_export.csv"

def csv2t(f):
    with open(f, encoding="UTF-8") as csvfile:
        table = csv.reader(csvfile)
        l = []
        for row in table:
            l.append(row)
    return (l[0],l[1:])

def entrydict(head, row):
    return dict(zip(head,row))

def t2json(fn,table,f):
    json.dump(fp=open(f.replace(".csv",".json"), 'w', encoding="UTF-8"), 
              obj=list(map(lambda x: fn(table[0],x), table[1])),
              ensure_ascii=False
              )



t2json(entrydict, csv2t(RYMFILE), RYMFILE)



