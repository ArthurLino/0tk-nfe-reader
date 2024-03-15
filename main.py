from reader import Reader

PATH = ""

r = Reader(PATH)
while len(r.files):
    r.read_nfe_products()
r.show_total_measurement()
