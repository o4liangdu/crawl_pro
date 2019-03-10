"""
@user:Do丶
@time:2018/10/31 16:58
"""

from bs4 import BeautifulSoup
import requests
import random
#随机生成useragent
from fake_useragent import UserAgent
import random

ua = UserAgent()
print(ua.random)
#print(random.random())
headers={
    "'User-Agent':"+ua.random
}


def getHTMLText(url, proxies):
    try:
        r = requests.get(url, proxies=proxies)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except BaseException:
        return 0
    else:
        return r.text

#从代理ip网站获取代理ip列表函数，并检测可用性，返回ip列表
def get_ip_list(url):
    web_data = requests.get(url, headers)
    soup = BeautifulSoup(web_data.text, 'html')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
# 检测ip可用性，移除不可用ip：（这里其实总会出问题，你移除的ip可能只是暂时不能用，剩下的ip使用一次后可能之后也未必能用）
    for ip in ip_list:
        try:
            proxy_host = "https://" + ip
            proxy_temp = {"https": proxy_host}
            res = urllib.urlopen(url, proxies=proxy_temp).read()
        except Exception as e:
            ip_list.remove(ip)
            continue
    return ip_list

#从ip池中随机获取ip列表
def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

#调用代理
if __name__ == '__main__':
    url = 'http://www.xicidaili.com/nn/'
    ip_list = get_ip_list(url)
    proxies = get_random_ip(ip_list)
    print(proxies)
