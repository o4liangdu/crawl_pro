"""
@user:Do丶
@time:2018/10/26 13:33
"""
import jieba
import wordcloud
txt3=open("aomen.txt","r", encoding='utf8').read()
words2=jieba.lcut(txt3)
txt3 = " ".join(words2)
w = wordcloud.WordCloud( \
    width=1000, height=700, \
    background_color="white",
    font_path = "msyh.ttc", collocations=False,prefer_horizontal = 0.8,min_font_size = 2
)
w.generate(txt3)
w.to_file("澳门.png")