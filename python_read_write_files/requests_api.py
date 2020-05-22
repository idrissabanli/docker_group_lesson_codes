import requests

response = requests.get('http://35.225.243.133/api/products/')

# print(response.text)
response_dict = response.json()
print(response_dict)
for product in response_dict:
    print(product['category'])
    # print(product['id'])
