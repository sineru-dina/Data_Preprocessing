import numpy as np
import visualize

def boxcox_transformation(data_vol, lambdas):
    transformed_data = []
    for lam in lambdas:
        if lam == 0:
            transformed_data.append(np.log(data_vol))  # Log transformation when lambda=0
        else:
            transformed_data.append((data_vol**lam - 1) / lam)
    
    visualize.data_plot(transformed_data, lambdas, simple=False, sub=True, hist=False)
    return transformed_data