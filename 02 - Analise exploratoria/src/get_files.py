import requests
from requests.auth import HTTPBasicAuth
import json
import csv

urls = [
##	{'url': "https://gitlab.procc.fiocruz.br/mave/repo/-/raw/master/Dados/InfoGripe/dados_semanais_faixa_etaria_sexo_virus_sem_filtro_febre.csv", 
##	'name': "Dados_InfoGripe_dados_semanais_faixa_etaria_sexo_virus_sem_filtro_febre.csv",
##	'auth': None},

	{'url': "https://raw.githubusercontent.com/otaviobertucini/data/master/dataset-codigos-ibge.csv", 
	'name': "dataset-codigos-ibge.csv",
	'auth': None},

	{'url': "https://www.ipea.gov.br/ipeageo/arquivos/bases/IDH_2010.xls", 
	'name': "IDH_2010.xls",
	'auth': None}	

]

for url in urls:	
	req = requests.get(url['url'], auth=url['auth'])
	url_content = req.content
	csv_file = open(url['name'], 'wb')
	csv_file.write(url_content)
	csv_file.close()

def get_internacoes(url, au):
        req=requests.get(url,auth=au)
        url_content=json.loads(req.content)
        saida = []
        lista = url_content["hits"]["hits"]
        for i in lista:
                a = json.dumps(i["_source"])
                a = json.loads(a)
                saida.append(a)
        with open("dataset-inter.csv","w",newline="") as f:
                title = "estado,estadoSigla,municipio,cnes,nomeCnes,dataNotificacaoOcupacao,ofertaRespiradores,ofertaHospCli,ofertaHospUti,ofertaSRAGCli,ofertaSRAGUti,ocupHospCli,ocupHospUti,ocupSRAGCli,ocupSRAGUti,altas,obitos,ocupacaoInformada,algumaOcupacaoInformada".split(",")
                cw = csv.DictWriter(f,title,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                cw.writeheader()
                cw.writerows(saida)

def get_casos(download_address):
    r = requests.get(download_address)
    r = json.loads(r.content)
    nextAdress = r['next']
    data = r['results']
    with open("dataset-covid19.csv","w",newline="") as f:
        title = "city,city_ibge_code,date,epidemiological_week,estimated_population,estimated_population_2019,is_last,is_repeated,last_available_confirmed,last_available_confirmed_per_100k_inhabitants,last_available_date,last_available_death_rate,last_available_deaths,new_confirmed,new_deaths,order_for_place,place_type,state".split(",") # quick hack
        cw = csv.DictWriter(f,title,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        cw.writeheader()
        cw.writerows(data)
    print ("Dados coletados e salvos com sucesso!")
    

get_internacoes("https://elastic-leitos.saude.gov.br/leito_ocupacao/_search?size=10000", HTTPBasicAuth('user-api-leitos', 'aQbLL3ZStaTr38tj'))
get_casos("https://brasil.io/api/v1/dataset/covid19/caso_full/data/?is_last=True&page_size=10000")


