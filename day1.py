#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : day1.py
# Author: MuNian
# Date  : 2019/8/25
'''
= 代表赋值
== 代表相等

从事什么方向?
手机APP --> 软件
只有这一期 由AI人工智能化专家亲自指导的AI研发班
网页开发  爬虫  自动化测试 自动化运维  机器学习 云计算 深度学习  AI  数据分析 数据采集 ...
Python 平均薪资(15K)  开发

AI --> 20K 以上的水平
本科以下 --> web开发  爬虫  自动化 (15K) ---> 提升自己的学历
4.5 个月为一期   1 3 5正课 2 4 6解答课  20:30 - 22:30
线上直播上课 + 高清录播 + 随堂笔记 + 源码
保障学员 能够学会才毕业
计算机基础知识 --> Python入门 --> web开发 ---> 爬虫
PHP  Python 软件开发
java 市场就业岗位多 --> 找工作的也多
100 --> 120
30 --> 20
在未来Python发展方向比其他语言都要广
长期发展
35之后笔试管理层 淘汰
Python --> 35之后 AI -->  大数据 算法

1 3 5正课 2  4 6解答课  20:30 - 22:30
课后高清录播 + 随堂代码 笔记
课后作业 课中测试 课后一对一辅导 解答 补课
腾讯认证机构
网页开发 --> 效率最高 学习最快 Python  后端
H5 前端
本科 胜任的
7880 --> 1000优惠 --> 6880 --> 分期 6 8 12  ---> 分期12期 每个月才500多块钱  花呗 借呗 京东白条 信用卡
付出 --> 不断学习  --> 长期发展
VIP学员 8K - 20K


'''
import tushare as ts

# 获取到所有股票列表
data = ts.get_stock_basics()
print(data.head())

data = data[data.industry == '农业综合']
print(data.head())
# 计算股票的数量
print('农业综合股票数量为:', len(data.industry))
# 每日基本指标数据 token值
pro = ts.pro_api(token='deda65f7d7da73c136c81869858d476714f65b1679b9e320b441bc01')
# ts_code == 股票代码 000002.SZ
# df = pro.daily_basic(ts_code='', trade_date='20180726', fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')

def get_code():
    ''' 数据处理变成 字典数据 '''
    global data
    # index ==> 股票代码
    data['code2'] = data.index
    # apply 方法 添加.SZ后缀
    data['code2'] = data['code2'].apply(lambda  i:i + '.SZ')
    data = data.set_index(['code2'])
    # code  name   ---]> dict,  表格中的代码和名称列
    data = data['name']
    data = data.to_dict()
    return data


ts_codes = get_code()
# 提取公司数据
start = '20090101'
end = '20180910'
for key, value in ts_codes.items():
    # 获取到每只股票的时间段数据
    data = pro.daily_basic(ts_code=key, start_date=start, end_date=end)
    # 添加代码(code)列和名称(name)列
    # 替换末尾.SZ
    data['code'] = data['ts_code'].replace('.SZ', '', regex=True)
    # 文件存储 a ==> 文件写入方式为追加
    data.to_csv('123.csv', mode='a', encoding='utf_8_sig', index=False, header=0)
    print('数据提取完毕')

