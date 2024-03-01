import xml.etree.ElementTree as et
from itertools import groupby
import os

PATH = "./ad4-itupeva"
PATTERN = "{http://www.portalfiscal.inf.br/nfe}"
'''FILES = ["1305.xml", "1313.xml", "1338.xml", "1357.xml", "1378.xml", "1386.xml"]'''
FILES = [d for d in os.listdir(PATH)]

global_results = {}

all_products = []

for f in FILES:
    file = et.parse(f'{PATH}/{f}')
    root = file.getroot()

    for child in root.findall(f"""./{PATTERN}NFe/{PATTERN}infNFe/{PATTERN}det/{PATTERN}prod"""):
        """loop through every product"""

        product = {
            "cod": child.find(f"{PATTERN}cProd").text,
            "desc": child.find(f"{PATTERN}xProd").text,
            "quant": child.find(f"{PATTERN}qCom").text,
            "und": child.find(f"{PATTERN}uCom").text,
            "val": round(float(child.find(f"{PATTERN}vUnCom").text), 2),
        }

        all_products.append(product)

all_products = sorted(all_products, key=lambda k: k["val"])

products_measurements = []

for key, value in groupby(all_products, key=lambda k: k["val"]):
    measurement = {
        "name": "",
        "total": 0,
        "und": "",
        "val": "",
    }
    for v in value:
        measurement["name"] = v["desc"]
        measurement["total"] += float(v["quant"])
        measurement["und"] = v["und"]
        measurement["val"] = v["val"]

    products_measurements.append(measurement)

for p in sorted(products_measurements, key=lambda k: k["name"]):
    for key, value in p.items():
        print(key, ":", value)
    print("-"*80)
