# encoding:utf-8
import requests
import pandas as pd
import json
from bs4 import BeautifulSoup

url = "https://iftp.chinamoney.com.cn/r/cms/www/chinamoney/html/bond/bondInfoSearch.html"  # 因为没有在测试题目中的链接中找到含有那些列名的数据，所以手动去网站找了一下能够返回相关内容的url
data = {
    "Bond Type": "Treasury Bond",
    "Issue Year": "2023"
}
response = requests.get(url, data=data)
html = response.text
soup = BeautifulSoup(html, "html.parser")
head = soup.find("tr").text
columns = head.split("\n")[1:-1]
df = pd.DataFrame(columns=columns)
filename = 'last.csv'
df.to_csv(filename, index=False)
