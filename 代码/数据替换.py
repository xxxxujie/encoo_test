data = """{"grant_type" :"password" ,"client_id" :"thirdpartyservice" ,"username" :"admin@encootech.com"
        ,"password" :"123456","flag":"${flag_o}","mobile":"${mobile_o}"}"""

# replace
flag = 'wieuqo'
mobile = '18855667713'

# 新方法
import string

template = string.Template(data)
new_data = template.substitute(flag_o=flag, mobile_o=mobile)
print(new_data)
