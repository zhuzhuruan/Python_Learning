# -*- coding: utf-8 -*-
# @Time : 2024/12/1012:15
# @Author : cyy
# @File : TextClassificationModel.py.py
# @desc :


from gensim.models import word2vec
from sklearn.feature_extraction.text import TfidfVectorizer
# from torchtext.data.utils import get_tokenizer
# from torchtext.vocab import build_vocab_from_iterator
from torch.utils.data import Dataset, DataLoader
from app_classifiter_clean import read_data


# tokenizer = jieba.lcut


# 构建训练迭代器
class Data_iter(Dataset):
    def __init__(self, text, label, mode='train'):
        self.text = text
        self.label = label
        self.mode = mode

    def __len__(self):
        return len(self.label) - 1

    def __getitem__(self, idx):
        if self.mode == 'train':
            return self.text[idx], self.label[idx]
        return self.text[idx]


def word2vec_class_model():
    """
    训练Word2Vec浅层神经网络模型
    :return:
    """
    sentences = word2vec.LineSentence('../config/cutWords_list.txt')
    w2v = word2vec.Word2Vec(sentences, vector_size=100, min_count=1, epochs=20, window=5)
    return w2v


if __name__ == '__main__':
    path = '../dataset'
    file_name = 'file_data'
    # data = read_data(path, file_name)
    # train_iter = Data_iter(data['appname'].values, data['cate'].values)
    # print(next(iter(train_iter)))
    w2v = word2vec_class_model()
    print(w2v.wv['黄瓜'])
    print(w2v.wv.similarity('黄瓜', '蜜桃'))
    print(w2v.wv['paajlv'])
    print(w2v.wv.similarity('91', '抖阴'))
    print(w2v.wv.similarity('旋风', '加速器'))
