from typing import List


# 从A[x_0,y_0]点到B[x_n,y_n]点有一条路，一辆车从这条路上开过三次，每隔1分钟记录一次当前经纬度，如何用这些记录的点
# [
# [[x_0,y_0,t_10],...,[x_1i,y_1i,t_1i],...,[x_n,y_n,t_1']],
# [[x_0,y_0,t_20],...,[x_2j,y_2j,t_2j],...,[x_n,y_n,t_2']],
# [[x_0,y_0,t_30],...,[x_3k,y_3k,t_3k],...,[x_n,y_n,t_3']]]
# 尽量还原道路形状[[x_0,y_0],...,[x_n,y_n]]

def reconstruct_road(start: List[float], end: List[float], samplings: List[List[List[float]]]) -> List[List[float]]:
    def dist(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    road = [start]
    for i in samplings:
        i.reverse()
    while samplings:
        temp = 0
        min_dist = float('inf')
        for i in range(len(samplings)):
            if dist(road[-1], samplings[i][-1]) < min_dist:
                temp = i
                min_dist = dist(road[-1], samplings[i][-1])
        road.append(samplings[temp][0])
        samplings[temp].pop()
        if not samplings[temp]:
            samplings.pop(temp)
    return road + [end]
