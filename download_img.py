import requests
url = "https://img.zcool.cn/community/0177335e43e7c1a801216518e9bc16.gif"

print(url[-9:])

path = url[-9:]
response = requests.get(url)
with open(path, "wb") as f:
    f.write(response.content)
