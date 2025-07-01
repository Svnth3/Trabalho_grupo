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
    
    filtro_data = df_novo['ano']
    
    df_novo2 = df_novo.groupby(['ano', 'munic']).sum(['roubo_carga']).reset_index()
    print(df_novo2)

    df_novo_filtro_data = filtro_data[df_novo['ano'].isin([2022, 2023])]

except Exception as e:
    print(f'Erro: {e}')

try:
    print("Obtendo informações do roubo de carga.")
    
    array_roubo_carga = np.array(df_novo['roubo_carga'])

    # print(filtro_data)

    media_roubo_carga = np.mean(array_roubo_carga)
    mediana_roubo_carga = np.median(array_roubo_carga)
    distancia = abs((mediana_roubo_carga) / mediana_roubo_carga)

    # print(f'media {media_roubo_carga:.2f}')
    # print(f'mediana: {mediana_roubo_carga:.2f}')
    # print(f'Distância da media e mediana: {distancia}')

    q1 = np.quantile(array_roubo_carga, 0.25, method='weibull')
    q2 = np.quantile(array_roubo_carga, 0.50, method='weibull')
    q3 = np.quantile(array_roubo_carga, 0.75, method='weibull')

    # print('Q1:', q1)
    # print('Q2:', q2)
    # print('Q3:', q3)

    maximo = np.max(array_roubo_carga)
    minimo = np.min(array_roubo_carga)
    amplitude_total = maximo - minimo

    # print('Maximo:', maximo)
    # print('Minimo:', minimo)
    # print('Amplitude:', amplitude_total)

    df_base_roubo_carga_menores = df_base_roubo_carga[df_base_roubo_carga] <M

except Exception as a:
    print(f'Erro: {a}')
