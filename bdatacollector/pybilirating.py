# -*- coding:utf-8 -*-
 
import requests
import json
import csv

import cmlineutil.progbar


payload = {'callback': 'seasonListCallback'}
TITLE = ['序号', '名称', '播放', '弹幕数', '收藏', '硬币', '是否完结', '评分(默认0分)', '评分人数(人数不足为0人)']


class PyBiliRating:
    timeouterr = 0
    csv_file = None
    basicInfo = True
    showRating = True
    showProgress = True
    title = []

    __writer = None

    def __init__(self, csv_file, basicInfo=True, show_rating=True, progress=True):
        if csv_file is None:
            raise FileNotFoundError
        else:
            self.csv_file = csv_file
        self.basicInfo = basicInfo
        self.showRating = show_rating
        self.showProgress = progress
        self.title += TITLE[:2]
        if basicInfo:
            self.title += TITLE[2:7]
        if show_rating:
            self.title += TITLE[7:]
        self.__writer = csv.writer(self.csv_file, delimiter=',')


    def continueWithCsv(self):
        pass


    def startOver(self, start=1, end=7000):
        self.__writer.writerow(self.title)
        p = None
        if self.showProgress:
            p = cmlineutil.progbar.ProgressBar(dataend=end - start)
        for i in range(start, end):
            if self.showProgress:
                p.update(i)
            self.rating(i)
            self.csv_file.flush()


    def close(self):
        self.csv_file.close()


    def rating(self, bangumi_id):
        try:
            response = requests.get('https://bangumi.bilibili.com/jsonp/seasoninfo/{0}.ver'.format(bangumi_id),
                                    params=payload, timeout=5)
        except:
            self.timeouterr += 1
            print("ERROR: timeout[" + str(self.timeouterr) + ']')
            return None

        data = json.loads(response.text[19:-2])
        try:
            season_id = int(data['result']['season_id'])
            title = '{0}'.format(data['result']['media']['title'])
            li = [season_id, title]
            if self.basicInfo:
                favorites = int(data['result']['favorites'])
                playcount = int(data['result']['play_count'])
                danmaku_count = int(data['result']['danmaku_count'])
                coins = int(data['result']['coins'])
                is_finish = 'true' if int(data['result']['is_finish']) == 1 else 'false'
                li += [playcount, favorites, danmaku_count, coins, is_finish]
            if self.showRating:
                score = float(data['result']['media']['rating']['score'])
                count = int(data['result']['media']['rating']['count'])
                li += [score, count]
            try:
                self.__writer.writerow(li)
            except:
                #print("WRONG: 1")
                pass
        except KeyError:
            try:
                season_id = int(data['result']['season_id'])
                title = '{0}'.format(data['result']['media']['title'])
                li = [season_id, title]
                if self.basicInfo:
                    favorites = int(data['result']['favorites'])
                    playcount = int(data['result']['play_count'])
                    danmaku_count = int(data['result']['danmaku_count'])
                    coins = int(data['result']['coins'])
                    is_finish = 'true' if int(data['result']['is_finish']) == 1 else 'false'
                    li += [playcount, favorites, danmaku_count, coins, is_finish]
                if self.showRating:
                    li += [0., 0]
                try:
                    self.__writer.writerow(li)
                except:
                    #print("WRONG: 2")
                    pass
            except:
                #print("WRONG: 3")
                return None
            return None
