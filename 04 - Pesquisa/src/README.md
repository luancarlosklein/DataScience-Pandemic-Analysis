## Instruções para a execução do projeto

- Descompactar a pasta "SRAGHospitalizado_2020_12_07"

- Executar o arquivo get_fyles.py:
	- Roda o script para pegar todos as bases de dados;

- Executar o jupyter SRAG *:
	- Faz a união e ajustes dos dados de mortalidade (para gerar o "mortalidade_idades.csv", caso já tiver, não é necessário esse passo);
	- * Como esse processo pode demorar, colocamos o arquivo gerado por ele na pasta: "mortalidade_idades", basta descompata-lo e ir para o próximo passo, sem necessidade de executar o SRAG; 

- Executar o jupyter Mortalidade:
	- Calcula a mortalidade ajustada das cidades brasileiras;

- Executar o jupyter main:
	- Executa o código principal;