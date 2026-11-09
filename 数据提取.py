import requests
import json
from lxml import etree
from bs4 import BeautifulSoup
import re

# json转字符串
json_obj = {
    "name":"华安",
    "age":22,
}
json_str = json.dumps(json_obj, ensure_ascii=False)
print(json_str)

# 字符串转json
json_str = '{"name":"华安", "age": 33}'
json_obj = json.loads(json_str)
print(type(json_obj))
print(json_obj)

print("----------------------------------------------------------------------------------------------------------------------------")

# 从json中提取数据
url = "https://i.news.qq.com/web_feed/getHotModuleList"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}
data = {"base_req":{"from":"pc"},"forward":"2","qimei36":"0_wzHiQm4MYtdMm","device_id":"0_wzHiQm4MYtdMm","flush_num":5,"channel_id":"news_news_top","item_count":20}
response = requests.post(url, json=data, headers=headers)
data_list = response.json().get("data")
for data in data_list:
    print(data.get("title", "") +"\t\t"+ data.get("long_summary", ""))

print("----------------------------------------------------------------------------------------------------------------------------")

# xpath提取数据
url = "https://movie.douban.com/top250?start=25&filter="
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
html = etree.HTML(response.text)
a_list = html.xpath("//div[@id='content']//li/div[@class='item']/div[@class='info']/div[@class='hd']/a")
title_list = []
for a in a_list:
    temp_title_list = a.xpath('./span/text()')
    title_str = "".join([title.replace("\xa0", "").strip() for title in temp_title_list])
    title_list.append(title_str)

p_list = html.xpath("//div[@id='content']//li/div[@class='item']/div[@class='info']/div[@class='bd']/p[1]")
content_list = []
for p in p_list:
    temp_content_text = ";".join([x.replace("\xa0", "").replace("\n", "").strip() for x in p.xpath('./text()')])
    content_list.append(temp_content_text)

for x, y in zip(title_list, content_list):
    print(x, y)

print("----------------------------------------------------------------------------------------------------------------------------")

# bs4提取数据
url = "https://www.77xsw.cc/"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, features="lxml")

# 查找第一个a标签；如果找不到返回None(根据标签名找)
a_first = soup.find("a")
print(a_first)

# 查找所有a标签(根据标签名找)
a_all = soup.find_all("a")
print(a_all)

# 正则查找标签(根据标签名找)
for tag in soup.find_all(re.compile("^f")):
    print(tag)

# 挨个遍历列表中标签，挨个找，最后所有结果放一个列表中(根据标签名找)
a_or_span_all = soup.find_all(["a", "span"])
print(a_or_span_all)

# 查找所有class="s2"的标签(根据属性找。冒号前为属性名，冒号后为属性值)
tag_by_class = soup.find_all(attrs={"class": "s2"})
print(tag_by_class)

# 使用css选择器查找标签(遵循css选择器标准)
tag_by_css = soup.select("a")
print(tag_by_css)

# 提取标签的属性值(找a标签的href属性的值)
tag_by_css = soup.select("a")
for tag in tag_by_css:
    print(tag.get("href"))

print("----------------------------------------------------------------------------------------------------------------------------")

# 正则提取数据
temp_str = "aaa|bbb|aaa"
response = re.match(".*\|(.*)\|.*", temp_str)
print(response.group(1))

print("----------------------------------------------------------------------------------------------------------------------------")

url = "https://weixin.sogou.com/weixin?_sug_type_=1&type=2&query=python"
headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
response_text = response.text
soup = BeautifulSoup(response_text, features="lxml")
tag_list = soup.select("ul.news-list>li>.txt-box>h3>a")
for tag in tag_list:
    print(tag.text)
