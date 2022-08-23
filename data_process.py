# -*- coding:utf-8 -*-
# @Date:2022-08-17
# @Author:susu
'''
预处理数据为ner模型需要的格式:
    将txt文本按句切割，并进行转换成BIO格式
    1.获取全部数据集的entity_type：实体类别去重
    2.统一数据集中实体类别：对应数据集中entity_type进行替换



'''
import json
import os
from collections import defaultdict


replace_dict = {
    "company_name":"Company",
    "company":"Company",
    "location":"Location",
    "LOC":"Location",
    "address":"Location",
    "GPE":"Location",
    "organization":"Organization",
    "org_name":"Organization",
    "ORG":"Organization",
    "person_name":"Person",
    "PER":"Person",
    "NAME":"Person",
    "name":"Person",
    "PERSON":"Person",
    "time":"Time",
    "DATE":"Time",
    "government":"Government",
    "book":"Book",
    "boo":"Book",
    "game":"Game",
    "movie":"Movie",
    "position":"Position",
    "music":"Music",
    "musi":"Music",
    "scene":"Scene",
    "video":"Video",
    "vide":"Video",
    "product_name":"Product",
    "CONT":"Country",
    "EDU":"Education",
    "TITLE":"Position",
    "PRO":"Major",
    "RACE":"Nation",
}


# 公司、地址、组织、人物、时间、政府、书籍、游戏、电影、职位、音乐、景点、影视、产品、国籍、学历、专业、民族
entity_types = ["Company", "Location", "Organization", "Person", "Time","Government",
                "Book","Game","Movie","Position","Music","Scene","Video","Product","Country",
                "Education", "Major", "Nation", ]

# 统计实体类型和个数
def static_entity(files, num=None):
    sta_dict = defaultdict(int)
    for file in files:
        with open(file, encoding="utf-8") as f:
            data_list = list(f.readlines())

            length = len(data_list) if not num else len

            entity_type = []
            for line in data_list[:length]:
                text_e = json.loads(line)
                for e in text_e["entity_list"]:
                    if e["entity_type"] not in entity_type:
                        entity_type.append(e["entity_type"])
                    sta_dict[e["entity_type"]] += 1

            entity_type.sort()
            # print("实体类型：",entity_type)
    print("实体类型及个数：", sta_dict)
    return entity_type

# 将实体类型进行统一命名
def replcae_entity(source_files, target_files, num=None):
    for file, target_file in zip(source_files, target_files):
        with open(file, encoding="utf-8") as f,open(target_file, "w+", encoding="utf-8") as g:
            data_list = list(f.readlines())
            length = len(data_list) if not num else len

            for line in data_list[:length]:
                text_e = json.loads(line)
                for e in text_e["entity_list"]:
                    entity_type = e["entity_type"]
                    if entity_type in replace_dict.keys():
                        e["entity_type"] = replace_dict[entity_type]

                g.write(json.dumps(text_e, ensure_ascii=False) + "\n")



if __name__ == '__main__':
    source_files = [r"./boson/boson.txt",
            r"./cluener_public/train.txt",
             r"./cluener_public/test.txt",
             r"./cluener_public/dev.txt",
            r"./MSRA/msra.txt",
            r"./people_daily/people_daily_ner.txt",
            r"./ResumeNER/train.txt",
             r"./ResumeNER/test.txt",
             r"./ResumeNER/dev.txt",
            r"./video_music_book_datasets/train.txt",
             r"./video_music_book_datasets/test.txt",
             r"./video_music_book_datasets/dev.txt",
             r"./video_music_book_datasets/valid.txt",
            ]
    target_files = [r"./processed_data/boson/boson.txt",
             r"./processed_data/cluener_public/train.txt",
             r"./processed_data/cluener_public/test.txt",
             r"./processed_data/cluener_public/dev.txt",
             r"./processed_data/MSRA/msra.txt",
             r"./processed_data/people_daily/people_daily_ner.txt",
             r"./processed_data/ResumeNER/train.txt",
             r"./processed_data/ResumeNER/test.txt",
             r"./processed_data/ResumeNER/dev.txt",
             r"./processed_data/video_music_book_datasets/train.txt",
             r"./processed_data/video_music_book_datasets/test.txt",
             r"./processed_data/video_music_book_datasets/dev.txt",
             r"./processed_data/video_music_book_datasets/valid.txt",
             ]

    # entity_types = []
    # for file in files:
    #     print(file)
    #     entity_type = static_entity(file, num=None)
    #     for i in entity_type:
    #         if i not in entity_types:
    #             entity_types.append(i)
    #     print("-----------------------")
    #
    # print(entity_types)

    static_entity(target_files, num=None)
    # replcae_entity(source_files, target_files, num=None)

