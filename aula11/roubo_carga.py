from sqlalchemy import create_engine, text

host = 'localhost'
user = 'root'
password = ''
database = 'bd_aula11'


def conecta_banco():
    try:
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

        with engine.connect() as conexao:
            query = 'SELECT * FROM basedp, basedp_roubo_carga'

            resultado = conexao.execute(text(query))

            if resultado.rowcount > 0:
                for item in resultado:
                    # print(item)
                    print(item[0], item[1], item[2])

    except Exception as e:
        print(f'Erro: {e}')