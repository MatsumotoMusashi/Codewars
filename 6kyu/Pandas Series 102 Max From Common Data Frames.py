import pandas as pd
def max_common(df_a,df_b):
    col_a,col_b,idx=df_a.columns,df_b.columns,df_a.index
    return pd.DataFrame({col:[max(df_a.loc[i,col],df_b.loc[i,col]) for i in idx] if col in col_b else df_a[col] for col in col_a},index=idx)