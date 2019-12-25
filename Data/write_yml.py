import yaml

data = {"Audi": {"ss":{"aa":"66"},
                 "mm":{"MM":"55"}}}
with open('./ww.yml',"w",encoding="utf-8") as f:
    yaml.dump(data,f,encoding="utf-8",allow_unicode=True)

"""
Audi:
    ss:
        aa : 66
    mm:
        MM : 55


"""