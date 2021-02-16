import streamlit as st
import pandas as pd
import requests
import base64
import boto3
import io
s3 = boto3.client('s3',
                    aws_access_key_id='####',
                    aws_secret_access_key='#####')

obj = s3.get_object(Bucket='bright-cities-data-lake', Key='99_documentacao/municipio_meso_microregiao_cityId.csv')
data = obj['Body'].read()
catalogo_cidades = pd.read_csv(io.BytesIO(data), delimiter=';', encoding = 'utf-8', header = 0)

login = "####"
senha = "####"

st.image("logotipo-brightcities.png", width=250)
st.title("API REQUEST SIDRA - Prototipo")

st.sidebar.markdown('**Login para acesso**')
login_acesso = st.sidebar.text_input('Digite o código para acessar', value="")
senha_acesso = st.sidebar.text_input('Digite a senha para acessar', value="", type="password")


if login_acesso == login and senha_acesso == senha:
    select_pagina = st.sidebar.selectbox("Selecione",["Fazer request", "Pegar dados"])

    if select_pagina == "Fazer request":
        num_tabela = st.text_input('Digite o número da tabela')
        if num_tabela == "":
            st.write("Por favor digite o número da tabela")
        num_indicador = st.text_input('Digite o indicador da tabela')
        if num_indicador == "":
            st.write("Por favor digite o número do indicador")

        ano_todos = st.checkbox("Todos os anos")
        ano_2020 = st.checkbox("2020")
        ano_2019 = st.checkbox("2019")
        ano_2018 = st.checkbox("2018")
        ano_2017 = st.checkbox("2017")
        ano_2016 = st.checkbox("2016")
        ano_2015 = st.checkbox("2015")
        ano_2014 = st.checkbox("2014")
        ano_2013 = st.checkbox("2013")
        ano_2012 = st.checkbox("2012")
        ano_2011 = st.checkbox("2011")
        ano_2010 = st.checkbox("2010")
        ano_2009 = st.checkbox("2009")
        ano_2008 = st.checkbox("2008")
        ano_2007 = st.checkbox("2007")
        ano_2006 = st.checkbox("2006")
        ano_2005 = st.checkbox("2005")
        ano_2004 = st.checkbox("2004")
        ano_2003 = st.checkbox("2003")
        ano_2002 = st.checkbox("2002")
        ano_2001 = st.checkbox("2001")
        ano_2000 = st.checkbox("2000")

        if st.button("Pegar o ano selecionado"):
            try:
                rename = ""
                ano = []
                if ano_todos:
                    ano = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013",
                           "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
                    rename = "todosAnos"
                if ano_2020:
                    ano.append("2020")
                if ano_2019:
                    ano.append("2019")
                if ano_2018:
                    ano.append("2018")
                if ano_2017:
                    ano.append("2017")
                if ano_2016:
                    ano.append("2016")
                if ano_2015:
                    ano.append("2015")
                if ano_2014:
                    ano.append("2014")
                if ano_2013:
                    ano.append("2013")
                if ano_2012:
                    ano.append("2012")
                if ano_2011:
                    ano.append("2011")
                if ano_2010:
                    ano.append("2010")
                if ano_2009:
                    ano.append("2009")
                if ano_2008:
                    ano.append("2008")
                if ano_2007:
                    ano.append("2007")
                if ano_2006:
                    ano.append("2006")
                if ano_2005:
                    ano.append("2005")
                if ano_2004:
                    ano.append("2004")
                if ano_2003:
                    ano.append("2003")
                if ano_2002:
                    ano.append("2002")
                if ano_2001:
                    ano.append("2001")
                if ano_2000:
                    ano.append("2000")

                df_prin = pd.DataFrame({})

                for i in range(len(ano)):
                    url = f"http://api.sidra.ibge.gov.br/values/t/{num_tabela}/n6/all/v/{num_indicador}/f/u/p/{ano[i]}"
                    base = requests.get(url)
                    df_json = pd.read_json(base.text)
                    df_json = df_json.drop([0])
                    df_json['D1C'] = df_json['D1C'].astype(int)
                    df_novo = pd.merge(catalogo_cidades, df_json[['D1C', 'V', 'D3N']], how='left',
                                       left_on=['codigo_municipio_completo'], right_on=['D1C'])
                    df_prin = pd.concat([df_prin, df_novo])

                df_prin = df_prin.drop(
                    columns=['uf', 'nome_uf', 'mesorregiao_geografica', 'nome_mesorregiao', 'microrregiao_geografica', 'nome_microrregiao', 'municipio', 'codigo_municipio_sem_digito', 'cityId', 'capital', 'nome_pais'])

                df_prin = df_prin.dropna(axis=0)

                minimo = df_prin[f'V'].min()
                maximo = df_prin[f'V'].max()
                media = df_prin[f'V'].mean()

                st.write(df_prin)

                st.text(f"Dados da tabela: Máximo: {maximo}")
                st.text(f"Dados da tabela: Minimo: {minimo}")
                st.text(f"Dados da tabela: Media:  {media}")

                st.text(f"Total de valores nulos: {df_prin.isna().sum()}")

                if rename == 'todosAnos':
                    rename += num_tabela + "_TodosAnos"

                    def download_link(object_to_download, download_filename, download_link_text):
                        if isinstance(object_to_download, pd.DataFrame):
                            object_to_download = object_to_download.to_csv(index=False)
                        b64 = base64.b64encode(object_to_download.encode()).decode()
                        return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

                    tmp_download_link = download_link(df_prin, rename, 'Baixar arquivo em csv')
                    st.markdown(tmp_download_link, unsafe_allow_html=True)
                else:
                    rename += num_tabela
                    for i in range(len(ano)):
                        rename += "_" + ano[i]

                    def download_link(object_to_download, download_filename, download_link_text):
                        if isinstance(object_to_download, pd.DataFrame):
                            object_to_download = object_to_download.to_csv(index=False)
                        b64 = base64.b64encode(object_to_download.encode()).decode()
                        return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'


                    tmp_download_link = download_link(df_prin, rename, 'Baixar arquivo em csv')
                    st.markdown(tmp_download_link, unsafe_allow_html=True)

            except KeyError:
                st.write("Por favor selecione um ano")
            except ValueError:
                st.write("Número do indicador ou da tabela incorreto")
            except:
                st.write("Verifique sua conexão com a internet")

    elif select_pagina == "Pegar dados":
        st.image("tabela_aux.PNG")
        st.write("Para mais detalhes da tabela acesse:")
        st.write("http://api.sidra.ibge.gov.br/")

else:
    st.sidebar.markdown("**Login invalido**")