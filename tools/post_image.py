import sys
from os.path import basename
import json
from pynamodb.attributes import BinaryAttribute

filename = sys.argv[1]

with open(filename, "rb") as input_file:
    content = input_file.read()

print json.dumps({"name": basename(filename), "content": BinaryAttribute().serialize(content)}, ensure_ascii=False)
