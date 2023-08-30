# -*- coding:utf-8 -*-

import nbformat


def clean_input_code(input_path, output_path):
    with open(input_path, encoding='utf-8') as f:
        raw_notebook = nbformat.read(f, as_version=4)
        for cell in raw_notebook.get("cells"):
            if cell.get("cell_type") == 'code':
                cell.source = []
    # for cell in raw_notebook.get("cells"):
    #     print(cell)
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(raw_notebook, f)


if __name__ == '__main__':
    input_path = r'C:\Users\caoyuanyuan\CYY_Git\Python_Learning\9_和鲸社区\1_Python基础语法及常用库\Numpy\3-这100道练习，带你玩转Numpy.ipynb'
    output_path = r'C:\Users\caoyuanyuan\CYY_Git\Python_Learning\9_和鲸社区\1_Python基础语法及常用库\Numpy\test.ipynb'

    clean_input_code(input_path, output_path)
