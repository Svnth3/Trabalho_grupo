from sqlalchemy import create_engine
import pandas as pd
import numpy as np 


host = 'localhost'
user = 'root'
password = ''
database = 'bd_aula11'


try:
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

    df_basedp = pd.read_sql('basedp', engine)
    df_base_roubo_carga = pd.read_sql('basedp_roubo_carga', engine)

    # df_basedp.columns = [col.strip().replace('\ufeff', '') for col in df_basedp.columns]
    # df_base_roubo_carga.columns = [col.strip().replace('\ufeff', '') for col in df_base_roubo_carga.columns]
        
    df_novo = pd.merge(df_basedp, df_base_roubo_carga, on='cod_ocorrencia')
    
    print(df_novo.head())
except Exception as e:
    print(f'Erro: {e}')
