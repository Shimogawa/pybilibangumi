# -*- coding:utf-8 -*-
 
import requests
import json
import csv

import numpy as np
import pandas as pd

import cmlineutil.progbar


payload = {'callback': 'seasonListCallback'}
TITLE = ['序号', '名称', '播放', '弹幕数', '收藏', '硬币', '是否完结', '评分(默认0分)', '评分人数(人数不足为0人)']


class PyBiliRating:
    timeouterr = 0
    csv_file_path = None
    csv_file = None
    basicInfo = True
    showRating = True
    showProgress = True
    title = []
    mode = 'w'

    __writer = None

    def __init__(self, csv_file_path=None, mode='w', basicInfo=True, show_rating=True, progress=True):
        if csv_file_path is None:
            raise FileNotFoundError
        else:
            self.csv_file = open(csv_file_path, mode, encoding='utf-8', newline='')
            self.csv_file_path = csv_file_path
        self.basicInfo = basicInfo
        self.showRating = show_rating
        self.showProgress = progress
        self.title += TITLE[:2]
        if basicInfo:
            self.title += TITLE[2:7]
        if show_rating:
            self.title += TITLE[7:]
        self.__writer = csv.writer(self.csv_file, delimiter=',')


    def continueOnCsv(self, start=None, end=None):
        '''
        Make sure you open the file with `append` mode before using this method!
        And, you also need the path!
        '''
        if start is None:
            df = pd.read_csv(self.csv_file_path)
            start = df['序号'].max() + 1
        if end is None:
            end = start + 100
        self._write_thing(start, end)
        print("\nDone!")


    def startOver(self, start=1, end=7000):
        '''
        Make sure you open the file with `write` mode before using this method!
        '''
        self.__writer.writerow(self.title)
        self._write_thing(start, end)
        print("\nDone!")


    def _write_thing(self, start, end):
        p = None
        if self.showProgress:
            p = cmlineutil.progbar.ProgressBar(dataend=end - start)
        for i in range(start, end):
            if self.showProgress:
                p.update(i - start + 1)
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
                is_finish = int(data['result']['is_finish'])
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
                    is_finish = int(data['result']['is_finish'])
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
