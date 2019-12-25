# import yaml
# with open("./value.yaml","r",encoding="utf-8") as f:
#     data = yaml.safe_load(f)
#     print(data)
#     print(type(data))

# 导包
import yaml
with open("./value04.yaml","r",encoding="utf-8") as f:
    data = yaml.safe_load(f)
    print("data:{}".format(data))
    print("leixing:{}".format(type(data)))