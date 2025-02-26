from sktime.transformations.series.vmd import VmdTransformer
import numpy as np

def vmd_decomposition(data, xseq, yseq, term, k):
    # Create empty columns for storing modes and reconstruction
    mode_columns = [f'mode_{i+1}' for i in range(k)]
    for col in mode_columns:
        data[col] = np.nan  # Initialize empty mode columns

    data['vmd_recon'] = np.nan  # Final VMD reconstruction column

    for idx in data.index:
        if idx == 501: # Exclude this break point to decmopose full data
            break

        # Check for sufficient past data
        if idx - xseq + 1 < 0:
            continue
        
        # Check for sufficient future data
        if idx + xseq + yseq + term - 1 > data.index[-1]:
            break

        transformer = VmdTransformer(K=k)
        vmd_result = transformer.fit_transform(data.loc[idx:idx+xseq-1, 'price'].values)

        # Store each mode in respective columns
        for i in range(k):
            data.loc[idx:idx+xseq-1, f'mode_{i+1}'] = vmd_result[:, i]

        # Compute final VMD reconstruction (sum of all modes)
        data.loc[idx:idx+xseq-1, 'vmd_recon'] = np.sum(vmd_result, axis=1)

    return data.loc[255:500] ## Return only the decomposed data for the 255-500 rows. Exclude [255:500] to decompose full data