import requests
from jsonpath import jsonpath
import pandas as pd

url = "http://bang.dangdang.com/books/"
fivestars_data = {
    "mode": "ajax",
    "ajax_type": "fivestars",
    "cat_path_fivestars": "01.00.00.00.00.00",
    "page": 0
}
# 生成fivestars-datalist
fivestars_datalist = list()
for i in range(1,6):
    fivestars_data["page"] = i
    fivestars_datalist.append(fivestars_data.copy())

product_name_list = list()
for data in fivestars_datalist:
    # 发送请求
    response = requests.post(url=url, data=data)

    content = response.json()
    product_name_list.extend(jsonpath(content, "$..product_name"))

pd_data = pd.DataFrame(product_name_list)
pd_data.to_csv("当当五星好评.csv", header=False)