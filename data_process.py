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



# 处理boson数据集
def transfer_boson(source_file, target_file):
    # {"text": "浙江在线杭州4月25日讯（记者 施宇翔 通讯员 方英）毒贩很“时髦”，用微信交易毒品。没料想警方也很“潮”，将计就计，一举将其擒获。记者从杭州江干区公安分局了解到，经过一个多月的侦查工作，江干区禁毒专案组抓获吸贩毒人员5名，缴获“冰毒”400余克，毒资30000余元，扣押汽车一辆。黑龙江籍男子钱某长期落脚于宾馆、单身公寓，经常变换住址。他有一辆车，经常半夜驾车来往于杭州主城区的各大宾馆和单身公寓，并且常要活动到凌晨6、7点钟，白天则在家里呼呼大睡。钱某不寻常的特征，引起了警方注意。禁毒大队通过侦查，发现钱某实际上是在向落脚于宾馆和单身公寓的吸毒人员贩送“冰毒”。\n", "entity_list": [{"entity_index": {"begin": 0, "end": 6}, "entity_type": "product_name", "entity": "浙江在线杭州"}, {"entity_index": {"begin": 6, "end": 11}, "entity_type": "time", "entity": "4月25日"}, {"entity_index": {"begin": 15, "end": 19}, "entity_type": "person_name", "entity": " 施宇翔"}, {"entity_index": {"begin": 24, "end": 26}, "entity_type": "person_name", "entity": "方英"}, {"entity_index": {"begin": 36, "end": 38}, "entity_type": "product_name", "entity": "微信"}, {"entity_index": {"begin": 69, "end": 78}, "entity_type": "org_name", "entity": "杭州江干区公安分局"}, {"entity_index": {"begin": 94, "end": 102}, "entity_type": "org_name", "entity": "江干区禁毒专案组"}, {"entity_index": {"begin": 141, "end": 144}, "entity_type": "location", "entity": "黑龙江"}, {"entity_index": {"begin": 147, "end": 149}, "entity_type": "person_name", "entity": "钱某"}, {"entity_index": {"begin": 184, "end": 189}, "entity_type": "location", "entity": "杭州主城区"}, {"entity_index": {"begin": 207, "end": 214}, "entity_type": "time", "entity": "凌晨6、7点钟"}, {"entity_index": {"begin": 215, "end": 217}, "entity_type": "time", "entity": "白天"}, {"entity_index": {"begin": 226, "end": 228}, "entity_type": "person_name", "entity": "钱某"}, {"entity_index": {"begin": 254, "end": 256}, "entity_type": "person_name", "entity": "钱某"}]}
    #
    # {
    #     "index": 0,
    #     "globalType": "",
    #     "tags": [
    #         {
    #             "name": "人物",
    #             "tag": "Person",
    #             "content": "安玮",
    #             "start": 0,
    #             "end": 2
    #         },
    # }






    pass


# 处理clueNer_public数据集
def transfer_clueNerPublic(source_file, target_file):
    pass


# 处理MSRA数据集
def transfer_MSRA(source_file, target_file):
    pass


# 处理people_daily数据集
def transfer_peopleDaily(source_file, target_file):
    pass


# 处理ResumeNER数据集
def transfer_ResumeNER(source_file, target_file):
    pass


# 处理VideoMusicBookDatasets数据集
def transfer_VideoMusicBookDatasets(source_file, target_file):
    pass


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

