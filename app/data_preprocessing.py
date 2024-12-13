import pandas as pd

def preprocess_data(posts):
    
    df = pd.DataFrame(posts)
 
    print("Columns in DataFrame:", df.columns.tolist())
    
    df.fillna('', inplace=True)  

    if 'user_id' not in df.columns or 'post_id' not in df.columns:
        print("Required columns 'user_id' or 'post_id' are missing.")
        return pd.DataFrame()  
    
    return df