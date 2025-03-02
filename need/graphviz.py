from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

with PyCallGraph(output=GraphvizOutput()):


    '''
    给定一个数组depth, 从左往右扫描。
    用S记录当前的状态（未知0， 下潜1，上浮2)
    当S=0, 如果 depth[i] > depth[i+1]  修改状态为 下潜1， 否则为上浮 2
    当S=1, 如果 depth[i] < depth[i+1], 则判断为由下潜变为上浮， 此处为一个波谷（开始上浮）。
    如果该波谷比上一个rangesize范围内的波谷更低，则修改上一个波谷的值。 否则就将该波谷加入波谷列表。
    当S=2, 如果 depth[i] > depth[i+1], 则判断为由上浮变为下潜， 此处为一个波峰（开始下潜）。
    如果该波峰比上一个rangesize范围内的波峰更高，则修改上一个波谷的值。 否则就将该波峰加入波峰列表。

    :param depth:深度数据
    :param rangesize:判断的距离
    :return:波峰波谷列表，列表第三个元素status 波峰：2，波谷：1 [index,depth,status]
    '''
    depth=list()
    rangesize=2
    peaks = list()
    troughs = list()
    S = 0
    for i in range(1, len(depth) - 1):
        if S == 0:
            if depth[i] > depth[i + 1]:
                S = 1
                pass
            else:
                S = 2
                pass
            pass
        elif S == 1:
            if depth[i] < depth[i + 1]:
                S = 2  # 由下潜变为上浮
                if len(troughs):
                    (prev_i, prev_trough, prev_status) = troughs[-1]
                    if i - prev_i < rangesize:

                        if prev_trough > depth[i]:
                            troughs[-1] = (i, depth[i], 1)
                            pass
                    else:
                        troughs.append((i, depth[i], 1))

                else:
                    troughs.append((i, depth[i], 1))

        elif S == 2:
            if depth[i] > depth[i + 1]:
                S = 1  # 由上浮变为下潜
                if len(peaks):
                    prev_i, prev_peak, prev_status = peaks[-1]
                    if i - prev_i < rangesize:
                        if prev_peak < depth[i]:
                            peaks[-1] = (i, depth[i], 2)

                    else:
                        peaks.append((i, depth[i], 2))

                else:
                    peaks.append((i, depth[i], 2))

