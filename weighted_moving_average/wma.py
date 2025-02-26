import pandas as pd

def wma_cal(data, weight):
    data.reset_index(drop=True, inplace=True)
    wma_list = []
    wma_list = data.loc[:weight-2, 'price'].to_list()

    for i in range(weight-1, len(data)):
        weighted_sum = 0
        total_weight = 0

        for j in range(weight):
            weight_for_point = j + 1
            weighted_sum += data.loc[i-j, 'price'] * weight_for_point
            total_weight += weight_for_point

        wma = weighted_sum / total_weight
        wma_list.append(wma)
    
    data['wma'] = wma_list

    return data