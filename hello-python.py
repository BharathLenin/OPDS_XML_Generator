import requests

response = requests.get("https://reqres.in/api/users/2")

# print(response.ok)
print(response.status_code)
# print(response.text)
# print(response.json())

data = response.json()

print(data['data']['email'])
# print('Hello, world!')

# age=14
# print("name " +  14 )

# for i in range(1,5):
#     print(i)