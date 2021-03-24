import json

def nClothParam(nClothShape,nClothParams):
    pm.setAttr(nClothShape + ".bounce", nClothParams[0])
    pm.setAttr(nClothShape + ".friction", nClothParams[0])
    pm.setAttr(nClothShape + ".stickiness", nClothParams[0])


objShape = ""
json_file = ".json"
with open(json_file, 'r') as f:
	get_json = json.load(f)
    nClothParam(objShape,get_json)