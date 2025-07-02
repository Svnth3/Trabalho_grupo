from sqlalchemy import create_engine
import pandas as pd
import numpy as np 


host = 'localhost'
user = 'root'
password = ''
database = 'bd_aula11'


try:
    engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    
    query = 'SELECT b.ano, b.munic, b.cod_ocorrencia, r.roubo_carga FROM basedp b JOIN basedp_roubo_carga r ON b.cod_ocorrencia = r.cod_ocorrencia WHERE b.ano IN (2022, 2023)'

    df_roubo = pd.read_sql(query, engine)

    df_ocorrencia_roubo = df_roubo.groupby('munic')['roubo_carga'].sum().reset_index()

   
    print(df_ocorrencia_roubo)


except Exception as e:
    print(f'Erro: {e}')

try:
    print("Obtendo informações do roubo de carga.")
    
    array_roubo_carga = np.array(df_roubo['roubo_carga'])

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

    # df_base_roubo_carga_menores = df_base_roubo_carga[[df_base_roubo_carga] < q1]
    # df_base_roubo_carga_maiores = df_base_roubo_carga[[df_base_roubo_carga] < q3]

    variancia = np.var(array_roubo_carga)
    distancia_variancia_media = variancia / (media_roubo_carga **2)
    desvio_padrao = np.std(array_roubo_carga)
    coeficiente_variação = desvio_padrao / media_roubo_carga
    
except Exception as a:
    print(f'Erro: {a}')

