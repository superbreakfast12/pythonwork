import requests
import pandas as pd
from parsel import Selector

# 模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
# 定位网页位置
base_url = 'https://wh.lianjia.com/ershoufang/hanyang/?sug=%E6%B1%89%E9%98%B3&pn='

# 初始化一个空列表来收集字典
house_list = []
# 循环50页
for page in range(1, 51):  # 从第1页到第50页建立循环遍历
    url = base_url + str(page * 20)  # 网站每页取20条数据
    response = requests.get(url=url, headers=headers)   #使用requests库的get发送请求到之前构建的url
    if response.status_code == 200: #如果HTTP响应的状态码是200，说明请求成功。
        selector = Selector(response.text)  # 选择器对象，使用selector来解析响应内容
        # 获取所有房源所在li标签
        lis = selector.css('.sellListContent li .info')
        # 从网页获取具体信息
        for li in lis:
            title = li.css('.title a::text').get()  # 标题
            area_info = li.css('.positionInfo a::text').getall()  # 区域信息
            area_1 = area_info[0]  # 小区
            area_2 = area_info[1]  # 区域
            totalPrice = li.css('.totalPrice span::text').get()  # 总价
            unitPrice = li.css('.unitPrice span::text').get().replace('元/平', '')  # 单价
            houseInfo = li.css('.houseInfo::text').get().split(' | ')  # 房源信息
            HouseType = houseInfo[0]  # 户型
            HouseArea = houseInfo[1].replace('平米', '')  # 面积
            HouseFace = houseInfo[2]  # 朝向
            HouseInfo_1 = houseInfo[3]  # 装修
            fool = houseInfo[4]  # 楼层
            HouseInfo_2 = houseInfo[-1]  # 建筑结构
            href = li.css('.title a::attr(href)').get()  # 详情页
            #储存信息到house字典
            house = {
                '标题': title,
                '小区': area_1,
                '区域': area_2,
                '总价': totalPrice,
                '单价': unitPrice,
                '户型': HouseType,
                '面积': HouseArea,
                '朝向': HouseFace,
                '装修': HouseInfo_1,
                '楼层': fool,
                '建筑结构': HouseInfo_2,
                '详情页': href,
            }
            house_list.append(house)
    else:
        print(f"第{page}页请求失败")
        break  # 退出循环

# 创建DataFrame
df = pd.DataFrame(house_list)
excel_filename = '汉阳区二手房.xlsx'
df.to_excel(excel_filename, index=False)
print(f"DataFrame已保存为Excel文件：{excel_filename}")