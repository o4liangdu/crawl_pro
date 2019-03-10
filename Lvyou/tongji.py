import jieba
import wordcloud
'''
def getjson():
    txt=open("xianggang.json","r").read()
    for ch in '！，；。‘’“”@#￥%……&*（）？{}:"",':
        txt=txt.replace(ch,"")
    return txt

markTxt=getjson()
words=markTxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)

for i in range(20):
    word,count=items[i]
    print("{0:<20}{1:>5}".format(word,count))
'''
excludes = {
    "markText",
    "地方",
    "可以",
    "一个",
    "我们",
    "很多",
    "就是",
    "还是",
    "这里",
    "感觉",
    "没有",
    "但是",
    "比较",
    "真的",
    "还有",
    "所以",
    "时间",
    "不过",
    "因为",
    "这个",
    "什么",
    "时候",
    "非常",
    "喜欢",
    "一定"}
txt = open("xianggang.json", "r").read()
txt2 = open("xianggang.txt", "w", encoding='utf8')
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

for word in excludes:
    del counts[word]


items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(20):
    word, count = items[i]
    print("{0:<20}{1:>5}".format(word, count))
    # txt2.write(word*count)

# txt3=open("zhongshan.txt","r", encoding='utf8').read()
# words2=jieba.lcut(txt3)
# txt3 = " ".join(words2)
# w = wordcloud.WordCloud( \
#     width=1000, height=700, \
#     background_color="white",
#     font_path = "msyh.ttc", collocations=False,prefer_horizontal = 0.8,min_font_size = 2
# )
# w.generate(txt3)
# w.to_file("中山.png")
