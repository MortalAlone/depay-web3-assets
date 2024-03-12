import requests 
# 导入CSV安装包
import csv
import json
import datetime
url = 'http://127.0.0.1:5500/api/private/v1/media'

def run(path):
    try:

        name_list = [text for text in csv.DictReader(open(path, encoding='utf-8'))]

        for row in name_list:
            
            # "id","cid","title","add_date","format","guid"
            # "1","2","311627728099535263","2021-07-31","image/jpeg","/upload/files/2021/07/311627728099535263.jpg"
            data = { "appType": json.dumps({"post_parent":row['cid'],"post_title":row['title'], "post_date":row['add_date'], "post_format":row['format'], "guid": row['guid']})}
            res = requests.post(url, data=data)
            print(res)




    except OSError:
        print(path, '文件打开失败')
        return False


if __name__ == '__main__':
    run('C:/Users/raozhanghua/Desktop/media.csv')
    

    # data = { "appType": json.dumps({"post_parent":"2","post_title":"168293722269440662", "post_date":"2023-05-01 19:08:05.289882", "post_format":"image/jpeg", "guid": "/upload/files/2021/07/311627728099535263.jpg"})}
    # res = requests.post(url, data=data)
    # print(res.text)