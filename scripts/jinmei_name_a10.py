# coding:utf-8
# 人名辞書をjson形式に変換
import sys
import json
import re

args = sys.argv

path = args[1] # '~/name_a10/A10_SEI.TXT' or '~/name_a10/A10_MEI.TXT' 
outpath = args[2] # './sei.json' or './mei.json'
with open(path, mode='r', encoding='shift_jis') as f:
    lines = f.readlines()

jinmei = dict()
for l in lines:
    if not re.match(r'^[ぁ-ん]', l):
        continue
    elements = l.split(',')
    yomi = elements[0]
    kanji = elements[1]
    if yomi in jinmei:
        jinmei[yomi].append(kanji)
    else:
        jinmei[yomi] = [kanji]

with open(outpath, mode='w', encoding='utf_8') as o:
    o.write(json.dumps(jinmei, ensure_ascii=False))

