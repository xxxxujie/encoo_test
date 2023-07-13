import jsonschema

"""
json的结构--》 jsonschema
1、某个字段是否存在
2、某个字段长度、类型、空
3、列表中的数据
----
requird,['access_token','token_type']
'access_token':{"type":"string","length":34}
----
"""

response = {
    'access_token': '12344321',
    'token_type': 'bearer',
    'refresh_token': '1233333',
    'expires_in': 12331,
    'msg': 'ok'
}

# 最重要：断言有没有access_token
schemas = {"required": ["access_token", "msg", "token_type"]}
resp = jsonschema.validate(response, schema=schemas)
print(resp)

# # 属性个数
# schemas = {"required": ["access_token", "msg", "token_type"],
#            "minProperties": 1,
#            "maxProperties": 3
#            }
# resp = jsonschema.validate(response, schema=schemas)
# print(resp)
