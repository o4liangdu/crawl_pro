from urllib import request

px=request.ProxyHandler({'http':'106.60.44.145:80'})
opener=request.build_opener(px)
req=request.Request('http://travel.qunar.com/p-oi5740179-guangzhouta')
res=opener.open(req)
'''如果我们使用install_opener(),以下代码可以把之前自定义的opener设置成全局的'''
# request.install_opener(opener)
# res=request.urlopen(req)
with open('a.html','wb') as f:
    f.write(res.read())


