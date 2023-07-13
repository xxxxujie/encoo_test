import string

from faker import Faker


# 数据替换
def replace_data(data, **kw):
    template = string.Template(data)
    data = template.substitute(**kw)
    return data


def replace_data_2(data, map):
    template = string.Template(data)
    data = template.substitute(map)
    return data


def generate_mobile():
    fk = Faker(locale='zh-CN')
    mobile = fk.phone_number()
    return mobile


if __name__ == '__main__':
    data = 'hello ${a} world'
    new_data = replace_data_2(data, {"a": "along"})
    print(new_data)
