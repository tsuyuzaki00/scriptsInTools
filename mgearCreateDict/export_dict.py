#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

#json内の "name":[@] の＠を置き換えるスクリプト
#json内の "name":[@] の＠に加えるスクリプト

import json
import pprint

file_pass = 'D:/GMR/MgearGuide/mgear_guide/jic_rig/dict/addjoint.json'

def read_json(file_pass):
    with open(file_pass, 'r') as f:
        roots = json.load(f)
        return roots

def update_dict_json(new_dict,file_pass):
    dict = read_json(file_pass)
    update_json = new_dict
    dict.update(update_json)
    with open(file_pass, 'w') as f:
        json.dump(dict, f, indent = 4, ensure_ascii =False)