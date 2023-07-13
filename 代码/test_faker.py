"""
faker pip install

"""

from faker import Faker


# 生成一个手机号
fk = Faker(locale='zh-CN')
phone = fk.phone_number()
print(phone)

print(fk.name())
print(fk.address())
print(fk.company())