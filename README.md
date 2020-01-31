# baidu-migration
a spider for baidu migration data

## 本项目仅用于获取武汉疫情相关科研数据，武汉加油

百度迁徙数据http://qianxi.baidu.com

### 使用方法：

1. 在程序根目录下新建文件夹data

2. 运行crawler.py


### 数据配置：

1. 目前仅支持抓取武汉市迁出人口数据

2. crawler.py，main函数中，revert_days为抓取天数，从当前日期向前抓取


### 其他：

1. 若需要武汉市迁入人口数据，可以自行在在crawler.py  move_in_crawl函数中实现，相关url已经提供

2. 若需要其他城市迁徙数据，可以自行获取相关城市的百度cityid，替换相关url中的id参数

