import os
import xml.etree.ElementTree as et
from itertools import groupby
from nfe import NFe


class Reader:

    def __init__(self, path):
        self.PATTERN = "{http://www.portalfiscal.inf.br/nfe}"
        self.path = path
        self.files = self.get_files()
        self.number_of_files = len(self.get_files())
        self._all_products = []
        self._final_sum = []

    def get_files(self):
        return [file_path for file_path in os.listdir(self.path)]

    def get_nfe(self):
        return self.files.pop(0)

    def set_all_products(self, list_of_products):
        return self._all_products.extend(list_of_products)

    def get_all_products(self):
        return self._all_products

    def read_nfe_products(self):
        nfe_path = et.parse(f'{self.path}/{self.get_nfe()}')
        root = nfe_path.getroot()

        new_nfe = NFe()

        for product in root.findall(f"./{self.PATTERN}NFe/{self.PATTERN}infNFe/{self.PATTERN}det/{self.PATTERN}prod"):

            product_object = {
                "code": product.find(f"{self.PATTERN}cProd").text,
                "description": product.find(f"{self.PATTERN}xProd").text,
                "quantity": product.find(f"{self.PATTERN}qCom").text,
                "unity": product.find(f"{self.PATTERN}uCom").text,
                "value": round(float(product.find(f"{self.PATTERN}vUnCom").text), 2),
            }

            new_nfe.set_products(product=product_object)

        self.set_all_products(new_nfe.get_products())

    def get_total_sum_of_products(self):

        sorted_products = sorted(self._all_products, key=lambda p: p["value"])
        grouped_products = groupby(sorted_products, key=lambda p: p["value"])

        for p_grouper, p_elements in grouped_products:
            measurement = {
                "name": "",
                "total": 0,
                "und": "",
                "val": "",
            }

            for i, p_element in enumerate(p_elements):
                measurement["name"] = p_element["description"]
                measurement["total"] += float(p_element["quantity"])
                measurement["und"] = p_element["unity"]
                measurement["val"] = p_element["value"]

            self._final_sum.append(measurement)

    def show_total_measurement(self):

        self.get_total_sum_of_products()

        for fs in sorted(self._final_sum, key=lambda k: k["name"]):
            for p_key, p_val in fs.items():
                print(p_key, ":", p_val)
            print("-"*80)

