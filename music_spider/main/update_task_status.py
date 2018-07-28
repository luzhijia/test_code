# encoding: utf-8
"""
@author: xsren 
@contact: bestrenxs@gmail.com
@site: xsren.me

@version: 1.0
@license: Apache Licence
@file: update_task_status.py
@time: 2017/6/9 下午2:24

"""

import sys

sys.path.append('../common')
import settings

mc = settings.getMCInstance()
db = mc["songs"]


def run():
    coll_list = ["qq_playlist_tasks", "qq_singer_tasks", "qq_album_tasks", "qq_song_tasks"]
    for coll in coll_list:
        print(coll)
        db[coll].update_many({'status': 1}, {'$set': {'status': 0}})
        db[coll].update_many({'status': 3}, {'$set': {'status': 0}})
        db[coll].update_many({'status': 4}, {'$set': {'status': 0}})
        print(db[coll].count())
        print(db[coll].count({'status': 0}))


if __name__ == '__main__':
    run()
