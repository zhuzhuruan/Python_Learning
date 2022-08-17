# merge and split pdf
import os

import pdfplumber
import pandas as pd
import tabula
from os import listdir, getcwd
from PyPDF2 import PdfFileReader, PdfFileWriter


# ----------------------------------------------------------
def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            # 把每张PDF页面加入到这个可读取对象中
            pdf_writer.addPage(pdf_reader.getPage(page))

    # 把这个已合并了的PDF文档存储起来
    with open(output, 'wb') as out:
        pdf_writer.write(out)


# -----------------------------------------------------------
def list_all_pdfs():
    # 将当前文件夹中所有的PDF文件枚举出来做成列表
    xlist = listdir(getcwd())
    pdflist = []
    for ele in xlist:
        if '合并成功' not in ele and '.pdf' in ele:
            pdflist.append(ele)

    # 按照数字大小将文件名字做成顺序列表，方便后续按照数字顺序逐个合并文件。
    def takeNo(elem):
        x = elem.split('.')
        return int(x[0])

    pdflist.sort(key=takeNo)  # 升序排列文件名称

    return pdflist


# -----------------------------------------------------------

def getfilename(path):
    file_list = []
    for file_path, dir_names, file_names in os.walk(path):
        for file in file_names:
            file_name = os.path.join(file_path, file)
            file_list.append(file_name)
    return file_list


def split_pdf(file_list):
    for path in file_list:
        pdf = PdfFileReader(path)
        for page in range(pdf.getNumPages()):
            if page == 1:
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf.getPage(page))
                output = os.path.dirname(path) + "\\" + str(page) + ".pdf"
                # print(output)
                with open(output, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)


def test():
    # 创建一个空数据框
    df = pd.DataFrame()

    # 使用with语句打开pdf文件
    with pdfplumber.open(r"D:\mydata\南京场景收\2021年二季度发布应用场景清单 - 城市治理.pdf") as pdf:
        # 使用for循环遍历每个pages
        for page in pdf.pages:
            print(page)
            print(page.extract_text())
            # 取出当前页表格，结果为列表
            d = page.extract_tables()
            # 将列表转为数据框
            df1 = pd.DataFrame(d[1:], columns=d[0])
            # 添加至df数据框中
            df = df.append(df1)
    df.to_excel(r"D:\mydata\南京场景收\10.xls")


def contact_excel(file_list):
    # df = pd.DataFrame(columns=['序号','应用场景所属类别','具体细分领域','所属产业领域','应用场景报送版块','应用场景建设区域','应用场景项目名称','应用场景搭建单位','项目起止日期','项目投资额（万元）','应用场景概述','欢迎合作的方向','联系人','联系方式'])
    datas = []
    for file in file_list:
        data = pd.read_excel(file, header=None)
        if data.loc[0][0] == '2021年二季度应用场景清单':
            data = data.drop(0, axis=0)
        datas.append(data)
    # print(datas)
    df = pd.concat(datas, ignore_index=True)
    df.columns = ['序号','应用场景所属类别','具体细分领域','所属产业领域','应用场景报送版块','应用场景建设区域','应用场景项目名称','应用场景搭建单位','项目起止日期','项目投资额（万元）','应用场景概述','欢迎合作的方向','联系人','联系方式']
    df = df.drop(df[df['序号'] == '序\n号'].index, axis=0)

    df.to_excel("D:\\mydata\\南京场景收\\合并1.xlsx")


# ------------------------------------------------------------
if __name__ == '__main__':
    # mode_selection = input('模式选择<C/S>, C代表合并操作，S 代表拆分成单页：\n').upper()
    # if mode_selection == 'C':
    #     print('程序会按照数字顺序逐个拼接PDF文档，并输出 合并成功.pdf 作为最终文档')
    #     paths = list_all_pdfs()
    #     print(paths)
    #     merge_pdfs(paths, output='合并成功.pdf')
    #     input('合并完毕，回车退出')
    # if mode_selection == 'S':
    #     print('程序会将指定的pdf文件拆分到单页，并以数字命名')
    #     path = input('输入需要拆分的PDF文件名字，包括后缀，例如 XXX.pdf，回车确认\n')
    #     split_pdf(path)
    #     input('拆分完毕，回车退出')

    path = r"D:\mydata\南京场景收\图片\文件\101-200"
    file_list = getfilename(path)
    # print(file_list)
    contact_excel(file_list)
    # split_pdf(file_list)
    # split_pdf(path)
    # test()
