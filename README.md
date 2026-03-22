**Projeto de Engenharia de Dados** - Pipeline Completo (Bronze, Silver e Gold)

**Aluno** - Igor Rocha Graseffi

**Matrícula** - 18106324


!!!Os dados brutos não foram incluídos no repositório devido ao seu grande volume. Eles podem ser obtidos via Kaggle em https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?resource=download!!!

\-> **Objetivo:** Construir um pipeline completo de dados utilizando uma base de e-commerce, passando pelas camadas Bronze, Silver e Gold, com foco em ingestão, tratamento, modelagem e análise de dados.



\-> **Arquitetura do Projeto**

* **Fluxo de dados:**

Fonte (CSV - Kaggle) -> Python (Pandas) -> Parquet (Silver) -> PostgreSQL (Gold)



* **Descrição**:

Os dados são ingeridos em formato CSV (Bronze)

São tratados e consolidados em um dataset analítico (Silver)

São modelados e carregados em banco relacional (Gold)



* **Camada Bronze**

  * Objetivo: Ingestão dos dados brutos.
  * Script: `bronze.py`
  * Atividades realizadas: Leitura dos arquivos CSV e Validação inicial dos dados



* **Camada Silver**

  * Objetivo: Tratamento e organização dos dados.
  * Script: `silver.py` e `graficos.py`
  * Atividades realizadas:

    * Junção das tabelas (orders, items, customers, geolocation)
    * Tratamento de valores nulos
    * Padronização de colunas
    * Remoção de duplicidades
    * Conversão de tipos (datas)
    * Exportação para formato Parquet



\-> **Análises geradas:**

\- Distribuição de preços (histograma)

\- Vendas por estado

\- Evolução temporal das vendas

\- Top cidades

\- Frete médio



* **Camada Gold**

  * Objetivo: Modelagem analítica e geração de insights.
  * Script: `gold.py`
  * Modelagem utilizada: Modelo dimensional (Star Schema)



**Tabelas:**

* **fato\_vendas**

  * order\_id
  * customer\_id
  * price
  * freight\_value
  * order\_purchase\_timestamp



* **dim\_cliente**

  * customer\_id
  * customer\_city
  * customer\_state



* **dim\_data**

  * data
  * mes
  * ano





\-> **Queries Analíticas**



**1. Receita por estado**

Descrição: Identifica os estados com maior volume de vendas.

Output: Os estados de SP, MG e RJ concentram a maior parte das vendas, com destaque absoluto para SP. A empresa possui forte concentração na região Sudeste, indicando: maior densidade de clientes, maior poder de consumo ou melhor cobertura logística.



**2. Ticket médio**

Descrição: Média de valor por pedido.

Output: A maior parte dos pedidos está concentrada em faixas de preço mais baixas, indicando que o volume de vendas ocorre principalmente em produtos de menor valor. O modelo de negócio parece ser orientado a alto volume e baixo ticket, o que pode indicar estratégia de competitividade por preço ou foco em consumo recorrente.



**3. Evolução mensal**

Descrição: Comportamento das vendas ao longo do tempo.

Output: As vendas apresentam variações ao longo do tempo, podendo indicar sazonalidade ou crescimento do negócio (mais provável dada a ascensão das vendas).



**4. Frete médio por estado**

Descrição: Comparação logística entre regiões.

Output: O valor do frete varia entre regiões, indicando diferenças logísticas e de distância. O frete pode ser um fator crítico na decisão de compra, onde fretes altos podem reduzir conversão e regiões mais caras precisam de otimização logística. Possível ação: melhorar distribuição ou negociar transportadoras.



**5. Clientes mais ativos**

Descrição: Identificação de clientes com mais compras.

Output: Grandes centros urbanos concentram maior volume de pedidos, com destaque para cidades mais populosas (provavelmente onde estão estes clientes). Isso indica que a operação está mais consolidada em áreas urbanas e a logística e marketing podem estar mais desenvolvidos nessas regiões.





\-> **Dicionário de Dados**



\## **fato\_vendas**

* order\_id = Identificador do pedido
* customer\_id = Identificador do cliente
* price = Valor do produto
* freight\_value = Valor do frete
* order\_purchase\_timestamp = Data da compra



\## **dim\_cliente**

* customer\_id = Identificador do cliente
* customer\_city = Cidade
* customer\_state = Estado



\## **dim\_data**

data = Data da compra

mes = Mês

ano = Ano





**-> Qualidade de Dados**



* **Problemas identificados:**
* **Colunas com valores nulos:**

\- `order\_approved\_at`

\- `order\_delivered\_carrier\_date`

\- `order\_delivered\_customer\_date`



* **Duplicidade em dados geográficos**

\- Alto volume de granularidade em timestamps



* **Tratamentos aplicados:**

\- Preenchimento de nulos

\- Remoção de duplicatas

\- Redução de granularidade (timestamp -> data)





\-> **Instruções de Execução**



**1. Instalar dependências**



```bash

pip install pandas sqlalchemy psycopg2-binary pyarrow matplotlib



**2. Estrutura Sugerida**



projeto\_dados/

── data/

&#x20;  ── raw/

&#x20;  ── silver/

── scripts/

&#x20;  ── bronze.py

&#x20;  ── silver.py

&#x20;  ── graficos.py

&#x20;  ── gold.py



**3. Ordem de Execução**



python bronze.py

python silver.py

python graficos.py

python gold.py



**4. Banco de Dados (PostgreSQL)**



CREATE DATABASE projeto\_dados;



**!!!Resumo Final da Interpretação dos Dados!!!**

A análise dos dados revelou que o negócio é fortemente concentrado em produtos de menor valor, com alto volume de vendas.

A região Sudeste, especialmente São Paulo, domina em termos de receita e volume, indicando maior maturidade de mercado nessa região.

Além disso, há indícios de variação temporal nas vendas, sugerindo sazonalidade ou crescimento.

O custo de frete varia entre regiões, podendo impactar a experiência do cliente e a competitividade da empresa.

NOTA: Se observa pico de vendas a partir de Novembro/2017, indicando talvez um "Boom" pós black Friday, que consolidou a marca no mercado pelo ano de 2018.

