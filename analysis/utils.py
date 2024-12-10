import pandas as pd

def flag_outliers(X, lod): 
    Outlier = X.copy()
    
    for site_ in lod.index:
        Q1 = X[site_].quantile(0.25)
        Q2 = X[site_].quantile(0.5)
        Q3 = X[site_].quantile(0.75)
        IQR = Q3 - Q1   

        safe_filter = (X[site_] >= Q1 - 1.5 * IQR) & (X[site_] <= Q3 + 1.5 *IQR)
    
        Outlier[site_] = ~safe_filter
        
    return Outlier

def get_data(sheet_name, col_start, row_start, loc='../raw/DB_UVHVVR.xlsx'):
    data = pd.read_excel(loc, sheet_name=sheet_name)
    
    raw = data.iloc[row_start:,:]
    analytes = data.columns[col_start:]

    z = data.iloc[:row_start,:]
    mask = z.iloc[:,0] == 'LOD'
    lod = z[mask][analytes].max()

    return (raw, lod)