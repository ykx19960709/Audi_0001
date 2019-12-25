import os, sys
sys.path.append(os.getcwd())
from Base.getData import GetData



import pytest
import yaml


def get_sum_data():
    # 创建一个空列表
    sum_list = []
    # 读n
    # with open("./Data"+os.sep+"value5.yaml","r",encoding="utf-8") as f:
    #     # 解析
    data = GetData().get_yml_data("value5.yaml")
    # data = yaml.safe_load(f)
    for i in data.values():
        # 追加数据到空列表
        sum_list.append(tuple(i.values()))


    return sum_list


class TestNum:
    @pytest.mark.parametrize("a,b,c", get_sum_data())
    def test_sum(self, a, b, c):
        print("{}+{}={}".format(a, b, c))
        assert a + b == c
