# nlp_corpus
[**中文说明**](https://) | [**English**](https://)

<p align="center">
    <a href="">
        <img alt="GitHub" src="https://img.shields.io/github/license/ymcui/Chinese-BERT-wwm.svg?color=blue&style=flat-square">
    </a>
</p>

中文实体识别
- open_ner_data为网上开放的ner数据集，已将不同的数据格式转化为统一的数据格式，格式转换脚本为data_transfer.py
- processed_data为统一实体命名后的数据集，格式转换脚本为data_process.py

1.1 boson数据集

1.2 clue细粒度实体识别数据集

1.3 MSRA数据集

1.4 微软实体识别数据集

1.5 人民网实体识别数据集（98年）

1.6 视频_音乐_图书数据集
```python
# 公司、地址、组织、人物、时间、政府、书籍、游戏、电影、职位、音乐、景点、影视、产品、国籍、学历、专业、民族
entity_types = ["Company", "Location", "Organization", "Person", "Time","Government",
                        "Book","Game","Movie","Position","Music","Scene","Video","Product","Country",
                        "Education", "Major", "Nation"]
# 实体类型及个数：
entity_counts = {'Product': 4122, 'Time': 20285, 'Person': 48626, 'Organization': 36690, 'Location': 71343, 'Company': 5637, 'Game': 2612, 'Movie': 1259, 'Position': 11247, 'Government': 2041, 'Scene': 1661, 'Book': 10044, 'Country': 321, 'Nation': 144, 'Education': 1076, 'Major': 338, 'Music': 5943, 'Video': 4070}
```
