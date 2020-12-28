import requests

#登录地址
post_addr="http://10.102.2.2/0.htm"

#构造头部信息
post_header={
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
             "Accept-Encoding": "gzip, deflate",
             "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
             "Cache-Control":" max-age=0",
             "Connection": "keep-alive",
             "Content-Length": "109",
             "Content-Type": "application/x-www-form-urlencoded",
             "Cookie": "drcom_login=1910181028%7C010721rr",
             "DNT": "1",
             "Host": "10.102.2.2",
             "Origin": "http://10.102.2.2",
             "Referer": "http://10.102.2.2/0.htm",
             " Upgrade-Insecure-Requests": "1",
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
}

#构造登录数据
post_data={
    "DDDDD": "1910181028@cmcc",
    "upass": "ec8ea63ff295943cb1c350326e1b97cf123456782",
    "R1": "0",
    "R2": "1",
    "para": "00",
    "0MKKey": " 123456",
}
#发送post请求登录网页
z=requests.post(post_addr,data=post_data,headers=post_header)import requests