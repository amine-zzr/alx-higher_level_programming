#!/usr/bin/python3
'''add all arguments to a Python list, and then save them to a file'''

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing = load_from_json_file(filename)
except FileNotFoundError:
    existing = []

new = sys.argv[1:]
all_items = existing + new

save_to_json_file(all_items, filename)
