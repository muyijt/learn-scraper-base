import requests
import retrying

# 抓文本类型数据

# 指定请求路径
url = "http://www.baidu.com"
# 指定请求头信息
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}
# 使用get请求方式请求
response = requests.get(url=url, headers=headers)
# 指定响应编码(根据网页head标签中指定的编码格式来设置这个值)
response.encoding = "utf-8"
# 响应体为str类型的内容
response_text = response.text
# 打印响应
print(response_text)

print("----------------------------------------------------------------------------------------------------------------------------")

# 抓bytes类型数据

# 指定请求路径
url = "http://www.baidu.com"
# 指定请求头信息
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}
# 使用get请求方式请求
response = requests.get(url=url, headers=headers)
# 指定响应编码(根据网页head标签中指定的编码格式来设置这个值)
response.content.decode("utf-8")
# 响应体为bytes类型的内容
response_content = response.content
# 打印响应
print(response_content)

print("----------------------------------------------------------------------------------------------------------------------------")

# 下载图片
url = "https://img1.baidu.com/it/u=2635663701,2375960330&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500"
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
response_content = response.content
with open("大雪.jpg", "wb") as f:
    f.write(response.content)
print("保存完毕")

print("----------------------------------------------------------------------------------------------------------------------------")

# post请求抓数据
url = "https://www.ccgp-anhui.gov.cn/api/core/supplierList"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "125",
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": "_zcy_log_client_uuid=9b969e90-cd60-11f1-9c97-adc9ef37e175",
    "Host": "www.ccgp-anhui.gov.cn",
    "Origin": "https://www.ccgp-anhui.gov.cn",
    "Referer": "https://www.ccgp-anhui.gov.cn/site/supplierTable?isOrg=supplier&utm=site.site-PC-4718.899-pc-websitegroup-anhuiTwoLink-front.12.9b9788f0cd6011f19c97adc9ef37e175",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Google Chrome";v="155", "Chromium";v="155", "Not(A:Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"'
}
data = {
    "pageNo":2,
    "pageSize":15,
    "district":340000,
    "regDistName":"已入库",
    "status":"OFFICIAL",
    "isSuspend":"0",
    "_t":1792595042000
}
# 传递的数据，如果是form表单需要用data=，如果是json数据需要用json=
response = requests.post(url, json=data, headers=headers)
response.encoding="utf-8"
print(response.json())

print("----------------------------------------------------------------------------------------------------------------------------")

# 作业

url = "https://i.news.qq.com/web_feed/getHotModuleList"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Content-Length": "157",
    "Content-Type": "application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}
data = {"base_req":{"from":"pc"},"forward":"2","qimei36":"0_wzHiQm4MYtdMm","device_id":"0_wzHiQm4MYtdMm","flush_num":5,"channel_id":"news_news_top","item_count":20}
response = requests.post(url, json=data, headers=headers)
print(response.json())

print("----------------------------------------------------------------------------------------------------------------------------")

# cookie

url = "https://www.mashangpa.com/api/problem-detail/1/data/?page=2"
headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Priority": "u=1, i",
    "Referer": "https://www.mashangpa.com/problem-detail/1/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"155\", \"Chromium\";v=\"155\", \"Not(A:Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36"
}
cookies = {
    "Hm_lvt_0d2227abf9548feda3b9cb6fddee26c0": "1792644775",
    "HMACCOUNT": "70B96D8190AF6397",
    "sessionid": "a1fl0ht51j7ogtg4gc5jcf9hd6a43glx",
    "Hm_lpvt_0d2227abf9548feda3b9cb6fddee26c0": "1792644833"
}
response = requests.get(url, headers=headers, cookies=cookies)
print(response.json())

print("----------------------------------------------------------------------------------------------------------------------------")

# ssl证书问题
# 请求时加上verify=False即可
url = 'https://www.siti.com.cn/default/list/20051816VVUEz.html?page=1'
response = requests.get(url, verify=False)
print(response.text)

print("----------------------------------------------------------------------------------------------------------------------------")

# 设置超时时间
# timeout=xx 单位: 秒
url = "https://www.baidu.com"
response = requests.get(url, timeout=2)
print(response.text)

print("----------------------------------------------------------------------------------------------------------------------------")

# 重试
num = 1
@retrying.retry(stop_max_attempt_number=3)
def get():
    global num
    num += 1
    print(num)
    raise Exception("异常")

get()