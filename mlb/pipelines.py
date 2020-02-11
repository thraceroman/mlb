import pymysql
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MlbPipeline(object):
    def process_item(self, item, spider):
        print("-------写入数据库---------")
        conn = pymysql.connect(host = "127.0.0.1",user = "root",password = "root",db = "note")
        for i in range(0,len(item["title"])):
            title = item["title"][i]
            author = item["author"][i]
            num = item["num"][i]
            # print(title + author + num)
            sql = "insert into volmoe(title,author,num) values('"+title+"','"+author+"','"+num+"')"
            print(sql)
            conn.query(sql)
            # 一定别忘记有提交这一项
            conn.commit()
        conn.close()
        return item
