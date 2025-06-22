# 題目一：
# 請根據 address 欄位，輸出格式如下：
# 地址：21 2nd Street, New York, NY 10021

# 題目二：
# 請列出所有電話，格式如下：
# home: 212 555-1234
# fax: 646 555-4567


data={
     "firstName": "John",
     "lastName": "Smith",
     "sex": "male",
     "age": 25,
     "address": 
     {
         "streetAddress": "21 2nd Street",
         "city": "New York",
         "state": "NY",
         "postalCode": "10021"
     },
     "phoneNumber": 
     [
         {
           "type": "home",
           "number": "212 555-1234"
         },
         {
           "type": "fax",
           "number": "646 555-4567"
         }
     ]
 }

# 第一題
address = data["address"]
print("地址：", f'{address["streetAddress"]}, {address["city"]}, {address["state"]} {address["postalCode"]}')

# 第二題
for phoneNumber in data["phoneNumber"]:
    print(f'{phoneNumber["type"]}: {phoneNumber["number"]}')