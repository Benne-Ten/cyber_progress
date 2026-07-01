import json
import os
path = os.path.join(os.path.expanduser("~/dossier_entrainement/"), "data.json")
with open(path, 'r', encoding='utf-8') as f:
	data=json.load(f)
print(data)
