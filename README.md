# learn-scraper-base
学习爬虫基础

## requests发送请求
- 下载requests模块
  - pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
- requests使用参考“requests模块下载和使用.py”文件
- requests常用属性
  - response.status_code: 响应状态码
  - response.text: 响应体内容为str类型
    - response.text修改编码: response.encoding="编码格式"
  - response.json: 响应体内容为json类型
    - response.json修改编码: 
  - response.content: 响应体内容为bytes类型(二进制类型: 图片、视频、文件等)
    - response.content修改编码格式: response.content.decode("编码格式")
  - response.request.headers: 请求头
  - response.headers: 响应头
  - response.cookies: 响应的cookies
  
