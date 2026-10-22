import requests
# 'https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches'import requests

url = input("Enter API URL: ").strip()
  
response = requests.get(url)
print(response)


data = response.json()
print("Data successfully:")
print(data)




