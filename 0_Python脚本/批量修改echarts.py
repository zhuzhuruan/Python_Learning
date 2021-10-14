# -*- coding:utf-8 -*-

import pandas as pd
import regex


color_dict = {'路灯报修':'#84B56C', '路灯建议':'#3A9ADD', '路灯投诉':'#FFB506', '路灯咨询':'#6A869E'}




def read_data(path, district, sheet_name='Sheet1'):
    data = pd.read_excel(path, sheet_name=sheet_name)
    var_data = []
    var_tips = []
    color = []
    num = 0
    type_count = data[data['区域']==district].groupby(['类型']).size().to_dict()
    for i in data.index:
        if data.loc[i]['区域'] == district:
            # word = '{name:"' + data.loc[i]['问题'] + '",value:' + str(data.loc[i]['比例']) + ',label:' + "'" + str(data.loc[i]['数量'])+ "'" + '},\n'
            var_data.append(str(data.loc[i]['比例']))
            var_tips.append(data.loc[i]['问题'] + '(' + str(data.loc[i]['数量']) + ')')
            var_legend = "['" + district + "']"
            color.append(color_dict[data.loc[i]['类型']])
            num += (data.loc[i]['数量'])
    print(type_count)
    print(var_data)
    print(var_tips)
    print(var_legend)
    print(color)
    print('总量: ' + str(num))

    return var_data, var_tips, var_legend, color, '总量: ' + str(num), type_count


def read_file(path, result, district):
    file_data = ""
    with open(path, 'rt', encoding='utf-8') as f:
        for line in f:
            if line.strip() == 'var data = [[]]':
                line = 'var data = [\n' + str(result[0]) + ']\n'
            if line.strip() == 'var tips = []':
                line = 'var tips = ' + str(result[1]) + '\n'
            if line.strip() == 'var legends = []':
                line = 'var legends =' + str(result[2]) + '\n'
            if '颜色配置' in line:
                line = 'color:' + str(result[3]) + ',\n'
            if '总量' in line:
                line = 'text:"' + result[4] + '",\n'
            if '//路灯报修' in line:
                line = 'value: ' + str(result[5].get('路灯报修',0)) + ',\n'
            if '//路灯建议' in line:
                line = 'value: ' + str(result[5].get('路灯建议',0)) + ',\n'
            if '//路灯投诉' in line:
                line = 'value: ' + str(result[5].get('路灯投诉',0)) + ',\n'
            if '//路灯咨询' in line:
                line = 'value: ' + str(result[5].get('路灯咨询',0)) + ',\n'
            file_data += line

    new_path = 'D:\\mydata\\visual\\pages\\综管中心\\' + district + '区域画像.html'

    with open(new_path, 'wt', encoding='utf-8') as f:
        f.write(file_data)



if __name__ == '__main__':
    file = r'D:\mydata\16_综管中心第六版修改\区域画像脚本示例.txt'
    path = r'D:\mydata\16_综管中心第六版修改\区域画像数据配置.xlsx'
    for district in ['闵行区','杨浦区','宝山区','普陀区','静安区','黄浦区','虹口区','长宁区','徐汇区','金山区','嘉定区','奉贤区','浦东新区','青浦区','松江区','崇明区']:
        result = read_data(path, district=district)
        read_file(file, result, district=district)
    # result = read_data(path, district='宝山区')
    # read_file(file, result, district='宝山区')