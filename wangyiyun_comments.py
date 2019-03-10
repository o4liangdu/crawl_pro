"""
@user:Do丶
@time:2018/12/27 09:13
"""
#coding=utf-8
import requests
import json
import time
from lxml import etree


class GetComments(object):
    def __init__(self):
        self.headers = {
            'Referer': 'http://music.163.com/',
            'Host': 'music.163.com',
            'Accept-Language': "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            'Accept-Encoding': "gzip, deflate",
            'Content-Type': "application/x-www-form-urlencoded",
            'Origin': 'https://music.163.com',
            'Connection': "keep-alive",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        # 构造会话
        self.session = requests.session()
        # 设置代理
        self.proxies = {
            'http': 'http://183.62.22.220:3128',
            'http': 'http://118.190.95.35:9001',
            'http': 'http://61.135.217.7:80',
            'http': 'http://106.75.9.39:8080',
            'http': 'http://118.190.95.43:9001',
            'http': 'http://121.31.157.94:8123',
            'http': 'http://115.46.67.248:8123',
            'http': 'http://182.88.14.243:8123'
        }

    def get_json(self, song_id, offset):
        """
        获取json数据
        :param song_id: 歌曲id
        :param offset: 评论偏移量
        :return: json转成的dict
        """
        url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_%s?limit=20&offset=%s' % (song_id, offset)
        print(url)
        responses = self.session.get(url, headers=self.headers).content
        json_dict = json.loads(responses)
        return json_dict

    def save_data(self, comments, song_name):
        """
         保存数据
        :param comments: 保存评论的列表
        :param song_name: 歌曲名字
        :return:
        """
        filename = song_name + '.txt'
        with open(filename, 'a') as f:
            try:
                f.writelines(comments)
            except UnicodeEncodeError as e:
                pass

    def structure_url(self, song_id, song_name):
        """
        先获取评论总数，再分页爬取
        :param song_id: 歌曲id
        :param song_name: 歌曲名字
        :return:
        """
        json_dict = self.get_json(song_id, 0)
        print(json_dict)
        comments_num = int(json_dict['total'])  # 获取评论总数目
        if not comments_num % 20:
            page = comments_num / 20
        else:
            page = int(comments_num / 20) + 1
        for i in range(page):
            comments_list = []
            json_dict = self.get_json(song_id, i * 20)
            print(page * 20)
            for item in json_dict['comments']:
                comment = item['content'].replace("\n","")  # 获取评论内容 并去掉换行符
                liked_count = item['likedCount']  # 点赞总数
                comment_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(item['time'] / 1000))  # 获取评论时间
                comment_info = comment_time + ' ' + str(liked_count) + ' ' + comment + '\n'
                comments_list.append(comment_info)
            self.save_data(comments_list, song_name)
            print('第 %s 页获取完成.' % i)

    def get_songs_id(self, url):
        """
        获取周杰伦主页的所有歌曲
        :param url: 主页链接
        :return: 所有歌曲名字，id
        """
        html = self.session.get(url, headers=self.headers)
        text = etree.HTML(html.text)
        # print(html.text)
        songs_name = text.xpath('//div[@id="hotsong-list"]/div[@class="f-cb"]/div/ul//a/text()')
        songs_id = text.xpath('//div[@id="hotsong-list"]/div[@class="f-cb"]/div/ul//a/@href') # 获取歌曲id
        songs_id = [s_id[9:] for s_id in songs_id]
        print(songs_name)
        print(songs_id)
        for i in range(len(songs_name)):
            self.structure_url(songs_id[i], songs_name[i])
            print('正在收集 %s 的评论' % songs_name[i])


if __name__ == '__main__':
    singer_url = 'https://music.163.com/artist?id=6452' # 记得要去掉#号，太那啥了
    spider = GetComments()
    spider.get_songs_id(singer_url)