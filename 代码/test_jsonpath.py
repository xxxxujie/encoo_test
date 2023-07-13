import jsonpath


"""
jsonpath:指的是获取json指定字段的路径
"""

a_json = {
    "msg":"ok",
    "data":{
        "token_info":"abc",
        "token":"abc",
        "token_type":"Bearer"
    },
    "id":1234,
    "name":"xujie"
}

a = a_json["data"]["token_info"]


result = jsonpath.jsonpath(a_json,expr="$.msg")
print(result)
# 获取data
data = jsonpath.jsonpath(a_json,'$.data')
print(data)
# 获取token_type
token_type = jsonpath.jsonpath(a_json,'$.data.token_info.token_type')
print(token_type)

# 重点    。。不是表示两个层级，而是表示子孙层级，不管多少个层级（缺点：不同级可能存在同名情况）
# 如果有同名的key，指明父级目录
token_type = jsonpath.jsonpath(a_json,'$..token_type')
print(token_type)



