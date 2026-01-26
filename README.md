# Projeto de Controle de Qualidade — Logística (Power BI)

## 1. Contexto do Projeto

### 1.1 Objetivo Principal
Averiguar o cumprimento de prazos (**SLA**) e o monitoramento de qualidade nas entregas.

### 1.2 O que o Projeto Não Cobrirá
- **Custos detalhados**
  - Frete por quilômetro
  - Margem por cliente
- **Segmentação por produtos e categorias**
  - Eletrônicos
  - Alimentos

### 1.3 Perguntas de Negócio
- As entregas estão sendo feitas no prazo?
- Onde ocorrem mais falhas de qualidade?
- Quais transportadoras têm pior desempenho?
- A qualidade está melhorando ou piorando ao longo do tempo?

---

## 2. Análises

### 2.1 Análises Gerais
- Entregas com **1 (uma) ou mais ocorrências registradas** superaram as entregas feitas no prazo em **3,27%**.
- A transportadora com o **menor tempo médio de entrega** é:
  - **Sudeste e Cargas Logística** — **5d5h**.
- As regiões com **maiores concentrações de ocorrências** foram:
  - **Sudeste** — cidades do interior de São Paulo e Rio de Janeiro
  - **Nordeste** — litoral nordestino
  - **Norte** — principalmente Belém/PA

### 2.2 Entregas
- No ano de **2024**, o número de entregas realizadas **decaiu 3,95%** em comparação com **2023**.
- No **1º trimestre de 2024**, foi registrada uma queda de **15,56%** no número de entregas realizadas em comparação ao mesmo período do ano anterior.
- O **maior número de entregas registradas em um único mês** foi de **59 entregas**.

### 2.3 Ocorrências
- O tipo de ocorrência mais frequente é **"Extravio"**, com **147 ocorrências**.
  - Transportadoras com maior número de registros:
    - **Litoral Sul Logística** — 17 ocorrências
    - **NorteVeloz Cargas** — 17 ocorrências
- Em **2024**, as entregas com ocorrências tiveram uma **diminuição de 1,42%** em relação ao ano anterior.
  - Esse comportamento é esperado devido à queda no volume de entregas realizadas.
- O período com a **menor taxa de entregas realizadas no prazo** foi o **1º trimestre de 2023**, com **21,52%** das entregas.
  - Nesse mesmo período, foi registrado o **maior número de ocorrências do tipo "Avaria"**, totalizando **21 ocorrências**.
- O **3º trimestre de 2023** foi o período com o **maior número de entregas com ocorrências**, atingindo **38,67%**.
  - Apesar disso, o **tempo médio de entrega** nesse período foi apenas **3 horas maior** que a média de todo o período analisado.

### 2.4 Transportadoras
- A transportadora com o **melhor índice de entregas no prazo por entregas com ocorrência(s) (EPEC)** é:
  - **BrasilFlex Logística** — **1,29**
- O estado com a maior quantidade de ocorrências do **tipo "Atraso"** é o **Pará (PA)**. Curiosamente, as transportadoras situadas na **região Nordeste são as principais responsáveis** desse número. Enquanto, as transportadoras localizadas em regiões afastadas possuem um desempenho melhor.

---

## 3. Conclusões

### 3.1. A existência de ocorrências **não é o fator mais impactante** no aumento do tempo médio de uma entrega. Assim, é possível que as operações internas das transportadoras são fatores mais agravantes nas demoras das entregas.
### 3.2. Em períodos onde as ocorrências do tipo "Avaria" são muito frequentes que as demais, a tendência é de que a **quantidade de entregas realizadas no prazo seja menor.**
### 3.3. Existe a possibilidade de transportadoras sediadas em cidades **mais distantes do local de destino** cumpram suas entregas no prazo mais do que transportadora localizadas próximas ao local destino.
