# -*- coding: utf-8 -*-
"""
@author: jiang
"""

# SMOB: Scoring Modeling and Optimal Binning

def tree_structure(estimator,colnames,round = 2):
    """
    Need CART tree estimator which after fit train data.
    Output a string of tree structure description.
    Print output.
    需要拟合完训练数据的CART树对象.
    输出描述树结构的字符串.
    打印输出.
    
    Parameters.参数.
    estimator:CART tree estimator.CART树对象.
    colnames:列名.
    round:threshold's significant digits.分割点的有效位数.
    
    Returns.输出.
    A string: A string of tree structure.树结构的字符串
    """
    n_nodes = estimator.tree_.node_count
    children_left = estimator.tree_.children_left
    children_right = estimator.tree_.children_right
    feature = estimator.tree_.feature
    threshold = estimator.tree_.threshold.round(2)
    
    import numpy as np
    # calculate each nodes' depth.用于计算每个节点的深度
    node_depth = np.zeros(n_nodes,int)
    # determine if each node is leaf node.用于判断每个节点是否为叶节点
    is_leaves = np.zeros(n_nodes,bool)
    # Storage each node's id and depth of it's father node.seed is root node
    # 用于存放节点的id及其父节点的深度,起始为根节点
    stack = [(0,-1)]

    while len(stack):
        node_id,parent_depth = stack.pop()
        node_depth[node_id] = parent_depth + 1
        
        # if a node is inner node.如果是内部节点
        if(children_left[node_id] != children_right[node_id]):
            stack.append((children_right[node_id],parent_depth +1))
            stack.append((children_left[node_id],parent_depth +1))
        else:
            is_leaves[node_id] = True
    
    out = "The cart tree structure has " + str(n_nodes) +\
          " nodes, tree structure: \n"
    
    for i in range(n_nodes):
        if is_leaves[i]:
            out += node_depth[i] * "\t" +\
                   "node = " + str(i) +\
                   " leaf node.\n"
        else:
            if(type(colnames) != str):
                col = colnames[feature[i]]
            else:
                col = colnames
            out += node_depth[i] * "\t" +\
                   "node = " + str(i) +\
                   " test node: go to node " +\
                   str(children_left[i]) + " if " +\
                   str(col) + " <= " +\
                   str(threshold[i]) + " else to node " +\
                   str(children_right[i]) + ".\n"
    return(out)

def smbin_cu(df,y,x,cutpoints=None,category=False,plot=True):
    """
    customized binning function, user define cutpoints
    y is a binary response variable,1 means Good, 0 means Bad
    
    自定义分箱函数,用户自定义分割点
    y是二元响应变量,1表示好,0表示坏
    
    Parameters.参数
    df:A data frame.一个数据框
    y:name of binary response variable.二元因变量的名字
    x:name of continuous characteristic.连续型特征的名字
    cutpoints: cutpoints selected by the user(sorted,include min and max).
               用户自定义的分割点(已排序,包含最大最小值)
    category:if x a category variable.x是否是一个分类变量
    plot:if plot WOE figure.是否画WOE图
    
    Returns.输出
    A pandas Series.一个pandas序列:
        IVtable:a table including WOE and IV.IV表格,包含WOE和IV值
        IV:IV value.IV值
        Xname:colname of x,x的列名
        Dict:dict of correspondence between bins and woe.箱子和WOE值的对应关系生成字典
        Xbin:binned x.分箱后的x
        Cutpoints:Optimal cutpoints.最优分割点
    
    """

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    # bulit IVtable including WOE and IV informations.创建IVtable,包含WOE和IV值信息
    if category:
        bins = df[x].astype("category")
    else:
        bins = pd.cut(df[x],cutpoints,include_lowest=True)
    CutRec = bins.value_counts(dropna=False,sort=False)
    IVtable = pd.DataFrame({"Bins":CutRec.index.astype(str),
                            "CntRec":CutRec.values})
    IVtable["CntGood"] = bins[df[y]==1].value_counts(dropna=False,sort=False).values
    IVtable["CntBad"] = bins[df[y]==0].value_counts(dropna=False,sort=False).values
    IVtable = IVtable.append(IVtable.sum(axis=0),ignore_index=True)
    IVtable.iloc[-1,0] = "Total"
    IVtable["PctRec"] = IVtable["CntRec"]/IVtable["CntRec"].iloc[-1]
    IVtable["PctGood"] = IVtable["CntGood"]/IVtable["CntGood"].iloc[-1]
    IVtable["PctBad"] = IVtable["CntBad"]/IVtable["CntBad"].iloc[-1]
    IVtable["WOE"] = np.log(IVtable["PctGood"]/IVtable["PctBad"]).round(4)
    IVtable["IV"] = ((IVtable["PctGood"] - IVtable["PctBad"])*IVtable["WOE"]).round(4)
    IVtable["WOE"].iat[-1] = np.nan 
    IVtable["IV"].iat[-1] = IVtable["IV"].iloc[:-1].sum()
    
    # IV value.IV值
    IV = IVtable["IV"].iloc[-1]
    
    # x name.x的列名
    Xname = x
    
    # dict of correspondence between bins and woe.箱子和WOE值的对应关系生成字典
    Dict = dict(zip(IVtable["Bins"].iloc[:-1],IVtable["WOE"].iloc[:-1]))
    
    if plot:
        pd.DataFrame(Dict,index=["WOE"]).T.plot(kind="bar",figsize=(16,10))
        plt.show()
    
    if category:
        cutpoints = np.array(IVtable["Bins"][:-1])
    
    # conbine result.组合结果输出
    out = pd.Series({"IVtable":IVtable,"IV":IV,"Xname":Xname,"Dict":Dict,
                     "Xbin":bins,"Cutpoints":np.array(cutpoints)})
    
    return(out)
    
def smbin(df,y,x,p=0.01,max_bin=20,plot=True):
    """
    Optimal binning function, Supervised discretization.
    The algorithm is CART Tree which initially excludes missiong values to compute the cutpoints.
    Treat missing values as a bin.
    y is a binary response variable,1 means Good, 0 means Bad
    
    最优分箱函数,有监督分箱
    算法基于CART树,建树的时候排除缺失值
    缺失值作为单独的一个箱子
    y是二元响应变量,1表示好,0表示坏
    
    Parameters.参数
    df:A data frame.一个数据框
    y:name of binary response variable.二元因变量的名字
    x:name of continuous characteristic.连续型特征的名字
    p:min percentage of leaf size (0<p<0.5).叶子包含观测数的最小占比(0<p<0.5)
    max_bin:max number of bins(bigger than 2).最大箱子数(大于2)
    plot:if plot WOE figure.是否画WOE图
    
    Returns.输出
    A pandas Series.一个pandas序列:
        IVtable:a table including WOE and IV.IV表格,包含WOE和IV值
        IV:IV value.IV值
        Xname:colname of x,x的列名
        Dict:dict of correspondence between bins and woe.箱子和WOE值的对应关系生成字典
        Xbin:binned x.分箱后的x
        Tree_structure:Output a string of tree structure description.输出描述树结构的字符串
    
    """
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import GridSearchCV
    import numpy as np
    import pandas as pd
    
    # specify X and Y variables, exclude NAs.指明X和Y变量数据,排除NA值
    X = np.array(df[x][df[x].notna()]).reshape(-1,1)
    Y = df[y][df[x].notna()]
    
    # adjust parameters, get best leaf's sample percentage.
    # 调参,得到最合适的叶节点观测占比
    gini_impure = np.linspace(0,0.001,50)
    param_grid = {"min_impurity_decrease":gini_impure}
    Es = GridSearchCV(DecisionTreeClassifier(),param_grid,cv=5,iid=False)
    Es.fit(X,Y)
    
    # use best param build tree model.使用最优参数构建树模型
    ES = DecisionTreeClassifier(min_impurity_decrease = Es.best_params_["min_impurity_decrease"],
                                max_leaf_nodes = max_bin,
                                min_samples_leaf = p)    
    ES.fit(X,Y)
    
    # output tree structure.输出树结构
    TS = tree_structure(ES,x)
    
    # extract threshold of test node.抽取测试节点的阈值
    TH = ES.tree_.threshold[ES.tree_.children_left != ES.tree_.children_right]
    # calculate cutpoints.计算最优分割点
    CP = np.append(TH,np.array([X.max(),X.min()]))
    CP.sort()
    
    # use customized binning function.使用自定义分箱函数
    smbin_cust = smbin_cu(df,y,x,cutpoints = CP,plot = plot)    
    
    out_a = pd.Series({"Tree_structure":TS})
    
    out = smbin_cust.append(out_a)

    return(out)

def smgen(df,xlist):
    """
    Generate a data frame with new predictive characteristic generated from WOE
    input a list of filtered objects' name after applying smbin or smbin_cu
    the data frame used must be same as the data used in smbin or smbin_cu
    使用WOE值生成的新变量得到一个数据框
    输入可用对象的列表,对象由smbin或smbin_cu得到
    使用的数据必须与在smbin或smbin_cu中使用的数据相同
    
    Parameters.参数
    df:A data frame.一个数据框
    xlist:a list of filtered objects' name after applying smbin or smbin_cu.
          输入可用对象的列表,对象由smbin或smbin_cu得到
    
    Returns.输出
    A dataframe:a dataframe with new columns of WOE.包含由WOE值组成的新列的数据框
    """
    df0 = df.copy()
    name_append = "_woe"
    
    for i in xlist:
        df0[i.Xname+name_append] = i.Xbin.astype(str).replace(i.Dict)
    
    out = df0
    return(out)

def smgennew(df,xlist):
    """
    Generate a data frame with new predictive characteristic generated from WOE
    input a list of filtered objects' name after applying smbin or smbin_cu
    support new data
    使用WOE值生成的新变量得到一个数据框
    输入可用对象的列表,对象由smbin或smbin_cu得到
    支持新数据
    
    Parameters.参数
    df:A data frame.一个数据框
    xlist:a list of filtered objects' name after applying smbin or smbin_cu.
          输入可用对象的列表,对象由smbin或smbin_cu得到
    
    Returns.输出
    A dataframe:a dataframe with new columns of WOE.包含由WOE值组成的新列的数据框
    """
    
    import numpy as np
    import pandas as pd
    
    df0 = df.copy()
    name_append = "_woe"
    
    # match x to range,than to woe.将x匹配到范围,再到woe
    def xtowoe(x):
        ind = list(np.all([(i.Cutpoints[:-1]-float(x))<=0.,
              (i.Cutpoints[1:]-float(x))>=0.],axis=0))
        if x < i.Cutpoints[0]:
            ind[0] = True
        if x > i.Cutpoints[-1]:
            ind[-1] = True
        woe = [*i.Dict.values()][ind.index(True)]
        return(woe)
    
    # add woe columns.增加woe列
    for i in xlist:
        if type(i.Cutpoints[0]) == str:
            df0[i.Xname+name_append] = df0[i.Xname].astype(str).replace(i.Dict)
        else:
            if df0[i.Xname].isna().sum() > 0 :
                ind0 = df0[i.Xname].notna()
                df0.loc[ind0,i.Xname+name_append] = list(map(xtowoe,list(df0.loc[ind0,i.Xname])))
                df0.loc[df0[i.Xname].isna(),i.Xname+name_append] = i.Dict["nan"]
            else:
                df0[i.Xname+name_append] = list(map(xtowoe,list(df0[i.Xname])))
                
    out = df0
    return(out)

def smscale(logitmodel,xlist,pdo=20,score=720,odds=50):
    """
    Transform the coefficients of a given logistic regression into
    scaled points based on three parameters pre-selected:pdo,score and odds
    将给定的逻辑回归的参数转化为评分,基于给定的三个参数:pdo,score和odds
    
    Parameters.参数
    logitmodel:logistic regression model.逻辑回归模型
    xlist:a list of filtered objects' name after applying smbin or smbin_cu.
          输入可用对象的列表,对象由smbin或smbin_cu得到
    pdo:points to double the odds.优比变成二倍增加的分数
    score:a specified score.一个指定的分数
    odds:a specified odds.一个指定的优比
    
    Returns.输出
    A pandas Series.一个pandas序列:
        ScoreCard:score card.评分卡
        ScoreCardFull:score card include woe and coefficient.包含woe和系数的评分卡
        minmaxscore:最小和最大分值
        factor:parameters used from odds to score.优比转换成分数时使用的参数
        offset:parameters used from odds to score.优比转换成分数时使用的参数
    """
    
    import numpy as np
    import pandas as pd
    
    # relevant parameters.相关参数
    factor = pdo / np.log(2)
    offset = score - factor * odds
    
    n = len(xlist)
    coef = logitmodel.params[1:]
    beta0 = logitmodel.params[0]
    Score = pd.DataFrame()
    j = 0
    
    # Score card table.评分卡表格
    for i in xlist:
        Score_i = pd.DataFrame({"Characteristic":i.Xname,
                                "Attribute":list(i.Dict.keys()),
                                "WOE":list(i.Dict.values()),
                                "Coef":coef[j]})
        j += 1
        Score = Score.append(Score_i)
    Score["Points"] = offset/n + factor * ( beta0/n + 
                      Score["Coef"] * Score["WOE"])
    Score["Points"] = Score["Points"].astype(int)
    
    # calculate max and min score.计算最高最低分
    ScoreMax = Score[["Characteristic","Points"]].groupby(
                "Characteristic",sort=False).max().sum()
    ScoreMin = Score[["Characteristic","Points"]].groupby(
                "Characteristic",sort=False).min().sum()
    
    minmaxscore = [*ScoreMin,*ScoreMax]
    
    out = pd.Series({"ScoreCard":Score.iloc[:,[0,1,4]],
                     "ScoreCardFull":Score,
                     "minmaxscore":minmaxscore,
                     "factor":factor,
                     "offset":offset})
    
    return(out)

def smscoregen(smscale,dataset):
    """
    Generate a data frame with the final score,
    and score of each characteristic.
    创建一个总得分的数据框
    包含每个特征的得分
    
    Parameters.参数
    smscale:object after smscale.smscale函数得到的对象
    dataset:dataset needed to be scored.需要打分的数据
    
    Returns.输出
    A dataframe:a dataframe with new columns of Scores.得分组成的新列的数据框
    """
    
    import pandas as pd
    
    ncol = dataset.shape[1]
    name_append = "_woe"
    scorelist = list(smscale.ScoreCardFull.groupby(
                "Characteristic",sort=False))

    for i in scorelist:
        right = pd.DataFrame({i[0]+name_append:i[1]["WOE"],
                              i[0]+"_Score":i[1]["Points"]})
        dataset = pd.merge(dataset,right,how="left",on=i[0]+name_append)

    dataset["Score"] = dataset.iloc[:,ncol:].sum(axis=1)
    
    out = dataset
    return(out)

def evaluate01(y,score,index="acc",beta=1,plot=None,report=True):
    """
    Generate a data frame used for evaluation of binary classifiers
    创建用于评估二分类分类模型的数据框
    
    Parameters.参数
    y:actual y value(0/1).真实y值(0/1)
    score:a value generated by a classification model.分类算法预测结果
    index:index used for calculate optimal cutoff:"acc","ks"or"f".
          计算最优阈值的指标:"acc","ks"或"f"
    beta:beta value used in F-measure.F统计量中用到的beta值
    plot:curve to plot:"roc" or "ks".绘制的曲线:"roc"或"ks"
    report:if show report.是否显示报告
    
    Returns.输出
    A pandas Series.一个pandas序列:
        evatable:a dataframe with new columns as following.包含如下新列的数据框:
            TP:true positive.真正例
            FP:false positive.假正例
            FN:false negative.假负例
            TN:ture negative.正负例
            rpp:rate of positive predictions.预测为正例比例
            tpr:true positive rate/sensitivity/recall.真阳性率/灵敏度/召回率
            fpr:false positive rate/1-specificity.假阳性率/1-特异度
            ppv:precision/positive predictive value.精确度
            acc:accuracy.准确率
            f:F-measure.F统计量
            ks:ks statistics.ks统计量
            lift:lift value.lift指标
        AUC:area under ROC curve.ROC曲线下的面积
        optimal_cutoff:a series of optimal cutoff and other metrics of chosen index.
                       选择指标对应的最优阈值,以及其他度量的序列
        cutoff:optimal cutoff value.最优阈值
    """

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    # sort score.分数排序
    eva = pd.DataFrame({"y":y.values,"Score":score.values})
    eva = eva.sort_values(by = "Score",ascending=False)
    eva.index = np.arange(eva.shape[0])
    
    # add characteristic.添加特征
    # positive.正例个数
    P = eva["y"].value_counts()[1]
    # negative.负例个数
    N = eva["y"].value_counts()[0]
    # all samples.总个数
    A = P + N
    # prevalence.流行率/患病率
    Prevalance = P / (P+N)
    # true positive.真正例
    eva["TP"] = eva["y"].cumsum()
    # false positive.假正例
    eva["FP"] = (-(eva["y"]-1)).cumsum()
    # false negative.假负例
    eva["FN"] = P - eva["TP"]
    # ture negative.正负例
    eva["TN"] = N - eva["FP"]
    # rate of positive predictions.预测为正例比例
    eva["rpp"] = [*(eva.index+1)]
    eva["rpp"] = eva["rpp"] / eva.shape[0]
    # true positive rate/sensitivity/recall.真阳性率/灵敏度/召回率
    eva["tpr"] = eva["TP"] / P
    # false positive rate/1-specificity.假阳性率/1-特异度
    eva["fpr"] = eva["FP"] / N
    # precision/positive predictive value.精确度
    eva["ppv"] = eva["TP"] / (eva["TP"] + eva["FP"])
    # accuracy.准确率
    eva["acc"] = (eva["TP"] + eva["TN"]) / A
    # F-measure.F统计量
    eva["f"] = ((1+beta**2)*eva["ppv"]*eva["tpr"]
                ) / (beta**2 *eva["ppv"]+eva["tpr"])
    # ks statistics.ks统计量
    eva["ks"] = eva["tpr"] - eva["fpr"]
    # lift value.lift指标
    eva["lift"] = eva["ppv"] / Prevalance
    
    # calculate auc value.计算auc值
    auc0 = eva[["tpr","fpr"]].copy()
    auc0["fpr_diff"] = auc0["fpr"].diff()
    auc0.at[0,"fpr_diff"] = auc0.at[0,"fpr"]
    auc0["area"] = auc0["fpr_diff"] * auc0["tpr"]
    auc = auc0["area"].sum()
    
    # calculate optimal cutoff for given index.计算给定指标的最优阈值
    optimal_cutoff = eva.loc[eva[index].idxmax()]
    optimal_cutoff = optimal_cutoff[1:]
    cutoff = optimal_cutoff.Score
    if report:
        print(f"The optimal cutoff(for {index}) is {optimal_cutoff.Score}")
        print(f"The maximum value of {index} is: {optimal_cutoff[index].round(4)}")
        print(optimal_cutoff)
    
    # plot roc curve.绘制ROC曲线
    if plot == "roc":
        plt.figure()
        plt.plot(eva["fpr"],eva["tpr"],label=f"Area Under Curve: {auc:.2f}")
        plt.plot([0, 1], [0, 1],'r--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver operating characteristic')
        plt.legend(loc="lower right")
        plt.show()
    
    # plot ks curve.绘制KS曲线
    if plot == "ks":
        kscut = eva.loc[eva["ks"].idxmax()]
        plt.figure()
        plt.plot(eva["rpp"],eva["tpr"],label = "True Positive Rate")
        plt.plot(eva["rpp"],eva["fpr"],label = "False Positive Rate")
        plt.plot([kscut["rpp"],kscut["rpp"]],[kscut["fpr"],kscut["tpr"]],"k--")
        plt.legend(loc="lower right")
        plt.text(kscut["rpp"]-0.24,kscut["fpr"]+kscut["ks"]/2,f"max ks:{kscut.ks.round(4)}")
        plt.xlabel('rate of positive predictions')
        plt.title('K-S curve')
        plt.show()
    
    out = pd.Series({"evatable":eva,"AUC":auc,"optimal_cutoff":optimal_cutoff,
                     "cutoff":cutoff})
    return(out)
    

    
    


