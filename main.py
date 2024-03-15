from reader import Reader

PATH = "C:/Users/Usuario/AppData/Roaming/JetBrains/PyCharmCE2023.2/scratches/nfe-reader/ad3-louveira"

r = Reader(PATH)
while len(r.files):
    r.read_nfe_products()
r.show_total_measurement()