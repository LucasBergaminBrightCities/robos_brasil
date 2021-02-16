from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd

anos = ["2020", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007", "2006", "2005", "2004", "2003", "2002", "2001"]
catalogo_cidades = pd.read_csv("municipio_meso_microregiao_cityId.csv", delimiter=';', encoding = 'utf-8', header = 0)
qtd = 0

HOMICIDIO_DOLOSO = []
N_DE_VITIMAS_EM_HOMICIDIO_DOLOSO= []
HOMICIDIO_DOLOSO_POR_ACIDENTE_DE_TRANSITO = []
N_DE_VITIMAS_EM_HOMICIDIO_DOLOSO_POR_ACIDENTE_DE_TRANSITO = []
HOMICIDIO_CULPOSO_POR_ACIDENTE_DE_TRANSITO	= []
HOMICIDIO_CULPOSO_OUTROS = []
TENTATIVA_DE_HOMICIDIO	= []
LESAO_CORPORAL_SEGUIDA_DE_MORTE	= []
LESAO_CORPORAL_DOLOSA = []
LESAO_CORPORAL_CULPOSA_POR_ACIDENTE_DE_TRANSITO	= []
LESAO_CORPORAL_CULPOSA_OUTRAS = []
LATROCINIO = []
N_DE_VITIMAS_EM_LATROCINIO = []
TOTAL_DE_ESTUPRO = []
ESTUPRO = []
ESTUPRO_DE_VULNERAVEL = []
TOTAL_DE_ROUBO_OUTROS = []
ROUBO_OUTROS = []
ROUBO_DE_VEICULO = []
ROUBO_A_BANCO = []
ROUBO_DE_CARGA	= []
FURTO_OUTROS = []
FURTO_DE_VEICULO = []
ANO = []
MUNICIPIO = []
ESTADO = []
MUNI_ATUAL = []
ANO_ATUAL = []

browser = webdriver.Chrome("D:\chromedriver.exe")
browser.get("http://www.ssp.sp.gov.br/estatistica/pesquisa.aspx")

element = browser.find_element_by_xpath('//*[@id="conteudo_ddlMunicipios"]')
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    MUNICIPIO.append(option.get_attribute("text"))

del MUNICIPIO[0]

btn = browser.find_element(By.ID, 'conteudo_btnMensal') #procuro o ID do botão
btn.click() #Faço ele apertar o botão.

def verificao(natureza, total):
    if natureza == "HOMICÍDIO DOLOSO (2)":
        HOMICIDIO_DOLOSO.append(total)

    elif natureza == "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)":
        N_DE_VITIMAS_EM_HOMICIDIO_DOLOSO.append(total)

    elif natureza == "HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO":
        HOMICIDIO_DOLOSO_POR_ACIDENTE_DE_TRANSITO.append(total)

    elif natureza == "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO":
        N_DE_VITIMAS_EM_HOMICIDIO_DOLOSO_POR_ACIDENTE_DE_TRANSITO.append(total)

    elif natureza == "HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO":
        HOMICIDIO_CULPOSO_POR_ACIDENTE_DE_TRANSITO.append(total)

    elif natureza == "HOMICÍDIO CULPOSO OUTROS":
        HOMICIDIO_CULPOSO_OUTROS.append(total)

    elif natureza == "TENTATIVA DE HOMICÍDIO":
        TENTATIVA_DE_HOMICIDIO.append(total)

    elif natureza == "LESÃO CORPORAL SEGUIDA DE MORTE":
        LESAO_CORPORAL_SEGUIDA_DE_MORTE.append(total)

    elif natureza == "LESÃO CORPORAL DOLOSA":
        LESAO_CORPORAL_DOLOSA.append(total)

    elif natureza == "LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO":
        LESAO_CORPORAL_CULPOSA_POR_ACIDENTE_DE_TRANSITO.append(total)

    elif natureza == "LESÃO CORPORAL CULPOSA - OUTRAS":
        LESAO_CORPORAL_CULPOSA_OUTRAS.append(total)

    elif natureza == "LATROCÍNIO":
        LATROCINIO.append(total)

    elif natureza == "Nº DE VÍTIMAS EM LATROCÍNIO":
        N_DE_VITIMAS_EM_LATROCINIO.append(total)

    elif natureza == "TOTAL DE ESTUPRO (4)":
        TOTAL_DE_ESTUPRO.append(total)

    elif natureza == "ESTUPRO":
        ESTUPRO.append(total)

    elif natureza == "ESTUPRO DE VULNERÁVEL":
        ESTUPRO_DE_VULNERAVEL.append(total)

    elif natureza == "TOTAL DE ROUBO - OUTROS (1)":
        TOTAL_DE_ROUBO_OUTROS.append(total)

    elif natureza == "ROUBO - OUTROS":
        ROUBO_OUTROS.append(total)

    elif natureza == "ROUBO DE VEÍCULO":
        ROUBO_DE_VEICULO.append(total)

    elif natureza == "ROUBO A BANCO":
        ROUBO_A_BANCO.append(total)

    elif natureza == "ROUBO DE CARGA":
        ROUBO_DE_CARGA.append(total)

    elif natureza == "FURTO - OUTROS":
        FURTO_OUTROS.append(total)

    elif natureza == "FURTO DE VEÍCULO":
        FURTO_DE_VEICULO.append(total)

def quantidade():
    if len(HOMICIDIO_DOLOSO) != len(N_DE_VITIMAS_EM_HOMICIDIO_DOLOSO):
        HOMICIDIO_DOLOSO.append("Dado faltando")

    if len(N_DE_VITIMAS_EM_HOMICIDIO_DOLOSO) != len(HOMICIDIO_DOLOSO):
        N_DE_VITIMAS_EM_HOMICIDIO_DOLOSO.append("Dado faltando")

    if len(HOMICIDIO_DOLOSO_POR_ACIDENTE_DE_TRANSITO) != len(HOMICIDIO_DOLOSO):
        HOMICIDIO_DOLOSO_POR_ACIDENTE_DE_TRANSITO.append("Dado faltando")

    if len(N_DE_VITIMAS_EM_HOMICIDIO_DOLOSO_POR_ACIDENTE_DE_TRANSITO) != len(HOMICIDIO_DOLOSO):
        N_DE_VITIMAS_EM_HOMICIDIO_DOLOSO_POR_ACIDENTE_DE_TRANSITO.append("Dado faltando")

    if len(HOMICIDIO_CULPOSO_POR_ACIDENTE_DE_TRANSITO) != len(HOMICIDIO_DOLOSO):
        HOMICIDIO_CULPOSO_POR_ACIDENTE_DE_TRANSITO.append("Dado faltando")

    if len(HOMICIDIO_CULPOSO_OUTROS) != len(HOMICIDIO_DOLOSO):
        HOMICIDIO_CULPOSO_OUTROS.append("Dado faltando")

    if len(TENTATIVA_DE_HOMICIDIO) != len(HOMICIDIO_DOLOSO):
        TENTATIVA_DE_HOMICIDIO.append("Dado faltando")

    if len(LESAO_CORPORAL_SEGUIDA_DE_MORTE) != len(HOMICIDIO_DOLOSO):
        LESAO_CORPORAL_SEGUIDA_DE_MORTE.append("Dado faltando")

    if len(LESAO_CORPORAL_DOLOSA) != len(HOMICIDIO_DOLOSO):
        LESAO_CORPORAL_DOLOSA.append("Dado faltando")

    if len(LESAO_CORPORAL_CULPOSA_POR_ACIDENTE_DE_TRANSITO) != len(HOMICIDIO_DOLOSO):
        LESAO_CORPORAL_CULPOSA_POR_ACIDENTE_DE_TRANSITO.append("Dado faltando")

    if len(LESAO_CORPORAL_CULPOSA_OUTRAS) != len(HOMICIDIO_DOLOSO):
        LESAO_CORPORAL_CULPOSA_OUTRAS.append("Dado faltando")

    if len(LATROCINIO) != len(HOMICIDIO_DOLOSO):
        LATROCINIO.append("Dado faltando")

    if len(N_DE_VITIMAS_EM_LATROCINIO) != len(HOMICIDIO_DOLOSO):
        N_DE_VITIMAS_EM_LATROCINIO.append("Dado faltando")

    if len(TOTAL_DE_ESTUPRO) != len(HOMICIDIO_DOLOSO):
        TOTAL_DE_ESTUPRO.append("Dado faltando")

    if len(ESTUPRO) != len(HOMICIDIO_DOLOSO):
        ESTUPRO.append("Dado faltando")

    if len(ESTUPRO_DE_VULNERAVEL) != len(HOMICIDIO_DOLOSO):
        ESTUPRO_DE_VULNERAVEL.append("Dado faltando")

    if len(TOTAL_DE_ROUBO_OUTROS) != len(HOMICIDIO_DOLOSO):
        TOTAL_DE_ROUBO_OUTROS.append("Dado faltando")

    if len(ROUBO_OUTROS) != len(HOMICIDIO_DOLOSO):
        ROUBO_OUTROS.append("Dado faltando")

    if len(ROUBO_DE_VEICULO) != len(HOMICIDIO_DOLOSO):
        ROUBO_DE_VEICULO.append("Dado faltando")

    if len(ROUBO_A_BANCO) != len(HOMICIDIO_DOLOSO):
        ROUBO_A_BANCO.append("Dado faltando")

    if len(ROUBO_DE_CARGA) != len(HOMICIDIO_DOLOSO):
        ROUBO_DE_CARGA.append("Dado faltando")

    if len(FURTO_OUTROS) != len(HOMICIDIO_DOLOSO):
        FURTO_OUTROS.append("Dado faltando")

    if len(FURTO_DE_VEICULO) != len(HOMICIDIO_DOLOSO):
        FURTO_DE_VEICULO.append("Dado faltando")


for muni in MUNICIPIO:
    regiao_select = Select(browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/form/div[3]/div[1]/div[2]/div[2]/div/select"))
    regiao_select.select_by_visible_text("Todos")  # Aqui eu to passando qual valor eu vou setar no select

    muni_select = Select(browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/form/div[3]/div[1]/div[3]/div[1]/div/select"))
    muni_select.select_by_visible_text(muni)  # Aqui eu to passando qual valor eu vou setar no select

    for i in anos:
        ano_select = Select(browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/form/div[3]/div[1]/div[2]/div[1]/div/select"))
        ano_select.select_by_visible_text(i)

        num = 0

        MUNI_ATUAL.append(muni)
        ANO_ATUAL.append(i)
        ESTADO.append("São Paulo")

        while num <= 25:
            num += 1
            try:
                Natureza = browser.find_element_by_xpath(f"/html/body/div[3]/div/div[1]/form/div[3]/div[2]/div/div[1]/div/table/tbody/tr[{num}]/td[1]").text
                Total = browser.find_element_by_xpath(f"/html/body/div[3]/div/div[1]/form/div[3]/div[2]/div/div[1]/div/table/tbody/tr[{num}]/td[14]").text
                verificao(Natureza, Total)
            except:
                continue
        quantidade()
        natureza_prin = pd.DataFrame({"ANO":ANO_ATUAL,
                                     "MUNICIPIO":MUNI_ATUAL,
                                     "ESTADO":ESTADO,
                                     "HOMICÍDIO DOLOSO (2)": HOMICIDIO_DOLOSO,
                                     "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO (3)": N_DE_VITIMAS_EM_HOMICIDIO_DOLOSO,
                                     "HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO": HOMICIDIO_DOLOSO_POR_ACIDENTE_DE_TRANSITO,
                                     "Nº DE VÍTIMAS EM HOMICÍDIO DOLOSO POR ACIDENTE DE TRÂNSITO": N_DE_VITIMAS_EM_HOMICIDIO_DOLOSO_POR_ACIDENTE_DE_TRANSITO,
                                     "HOMICÍDIO CULPOSO POR ACIDENTE DE TRÂNSITO": HOMICIDIO_CULPOSO_POR_ACIDENTE_DE_TRANSITO,
                                     "HOMICÍDIO CULPOSO OUTROS": HOMICIDIO_CULPOSO_OUTROS,
                                     "TENTATIVA DE HOMICÍDIO": TENTATIVA_DE_HOMICIDIO,
                                     "LESÃO CORPORAL SEGUIDA DE MORTE": LESAO_CORPORAL_SEGUIDA_DE_MORTE,
                                     "LESÃO CORPORAL DOLOSA": LESAO_CORPORAL_DOLOSA,
                                     "LESÃO CORPORAL CULPOSA POR ACIDENTE DE TRÂNSITO": LESAO_CORPORAL_CULPOSA_POR_ACIDENTE_DE_TRANSITO,
                                     "LESÃO CORPORAL CULPOSA - OUTRAS": LESAO_CORPORAL_CULPOSA_OUTRAS,
                                     "LATROCÍNIO": LATROCINIO,
                                     "Nº DE VÍTIMAS EM LATROCÍNIO": N_DE_VITIMAS_EM_LATROCINIO,
                                     "TOTAL DE ESTUPRO (4)": TOTAL_DE_ESTUPRO,
                                     "ESTUPRO": ESTUPRO,
                                     "ESTUPRO DE VULNERÁVEL": ESTUPRO_DE_VULNERAVEL,
                                     "TOTAL DE ROUBO - OUTROS (1)": TOTAL_DE_ROUBO_OUTROS,
                                     "ROUBO - OUTROS": ROUBO_OUTROS,
                                     "ROUBO DE VEÍCULO": ROUBO_DE_VEICULO,
                                     "ROUBO A BANCO": ROUBO_A_BANCO,
                                     "ROUBO DE CARGA": ROUBO_DE_CARGA,
                                     "FURTO - OUTROS": FURTO_OUTROS,
                                     "FURTO DE VEÍCULO": FURTO_DE_VEICULO})

        df_novo = pd.merge(catalogo_cidades, natureza_prin, how='left', left_on=['nome_municipio', 'nome_uf'], right_on=['MUNICIPIO', 'ESTADO'])
        df_prin = df_novo.drop(columns=['uf', 'nome_uf', 'mesorregiao_geografica', 'nome_mesorregiao', 'microrregiao_geografica', 'nome_microrregiao', 'municipio', 'codigo_municipio_sem_digito', 'cityId', 'capital', 'nome_pais', 'nome_municipio'])
        df_prin = df_prin.dropna(axis=0, how='any')
        csv = df_prin.to_csv(r"C:\Users\Bergamin\Desktop\Brigth cities\Dados\SSP\DadosSegurança.csv", sep=";")
        print(df_prin)