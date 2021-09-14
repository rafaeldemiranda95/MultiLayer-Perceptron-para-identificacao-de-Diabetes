# MultiLayer Perceptron para identificação de Diabetes

Este software utiliza multilayer perceptrons para identificar, a partir de uma combinação de fatores, qual o risco do usuário desenvolver diabetes nos próximos cinco anos. Desenvolvido por Luís Roberto Weck e Rafael de Miranda

## Sumário

- [Problema](#problema)
- [Dataset](#dataset)
- [Técnica](#tecnica)
- [Ferramentas](#ferramentas)
- [Instruções de uso](#instrucoes)

### [Problema](#problema)

Identificar usando técnicas de inteligência computacional a probabilidade de que uma pessoa desenvolva diabetes em até cinco anos após data da aferição. A probabilidade é calculada utilizando um modelo de perceptron de multi-camadas, que analisam os seguintes parâmetros: concentração de glucose no plasma, pressão arterial diastólica, espessura da pele no tríceps, nível de insulina, IMC, função diabetes (quando existem casos de diabéticos na família), idade e número de gravidezes.

Todos estes parâmetros encontram-se no dataset de treinamento em formato numérico. Estes foram usados para treinar o perceptron de multi-camadas. Para a utilização do software, é necessário que o usuário informe um valor para cada um dos parâmetros.

A função diabetes foi utilizada diretamente do artigo [Using the ADAP Learning Algorithm to Forecast the Onset of Diabetes Mellitus](https://europepmc.org/backend/ptpmcrender.fcgi?accid=PMC2245318&blobtype=pdf), de Smith, J.W. et al. É dada calculada pelo dataset. Consiste na seguinte função:

![DPF = \frac{\sum_{i}K_i(88-ADM_i)+20}{\sum_{j}K_j(ALC_j-14)+50}](<https://latex.codecogs.com/svg.latex?DPF&space;=&space;\frac{\sum_{i}K_i(88-ADM_i)+20}{\sum_{j}K_j(ALC_j-14)+50}>)

Onde, de acordo com o autor do artigo:

- i -> abrange todos os parentes que desenvolveram diabetes na data do exame do sujeito;
- j -> abrange todos os parentes, que NÃO desenvolveram diabetes na data do exame do sujeito;
- Kx -> é a porcentagem de genes compartilhados pelo parente, e:
  - é igual a 0.500 quando o parente x é um pai ou irmão;
  - é igual a 0.250 quando o parente x é meio-irmão, avô, tia ou tio;
  - é igual a 0.125 quando o parente x é meia tia, meio tio ou primo de primeiro grau;
- ADM_i -> é a idade, em anos, do parente i em que o diabetes foi diagnosticado;
- ACL_j -> é a idade em anos do parente j no último exame não diabético (antes da data do exame do sujeito);
- Constantes
  - As constantes 88 e 14 representam, com raras exceções, as idades máxima e mínima em que os parentes dos sujeitos deste estudo desenvolveram diabetes.
  - As constantes 20 e 50 foram escolhidas de forma que:
    1. Um sujeito sem parentes teria um valor DPF ligeiramente inferior à média
    2. O valor do DPF diminuiria de forma relativamente lenta à medida que parentes jovens livres de diabetes ingressassem no banco de dados
    3. O valor DPF aumentaria relativamente rápido, pois parentes conhecidos desenvolveram diabetes

Smith ainda define diabetes como uma concentração de glucose no plasma acima de 200 mg/dL duas horas após a ingestão de 75 gramas de uma solução de carboidratos.
Para a solução do perceptron, o valor de glucose no plasma já esta no dataset de treinamento, e, portanto, faz parte das informações que o usuário precisa informar para obter um resultado válido.

### [Dataset](#dataset)

O dataset utilizado é o [Pima Indians Diabetes Database](https://www.kaggle.com/uciml/pima-indians-diabetes-database).

Com base nestes dados, é criado um modelo usando os perceptrons de multi-camadas. No dataset, não existem entradas de pacientes que registrem o valor necessário para ser considerado portador de diabetes. Isto se deve ao fato de que Smith et al. realizaram um trabalho preditivo sobre os dados coletados.

Para os casos que desenvolveram diabetes dentro de 5 anos, e foram classificados como positivos, tem seu "Outcome" como positivo.

Casos onde o usuário não possuia diabetes no momento do testes, mas o desenvolveu dentro de um ano, foram excluidos do dataset pelo próprio autor, para que, em suas palavras, fossem removidos os casos que são fáceis de predizer.

Distribuição dos atributos do dataset:
<img src="https://github.com/lrweck/proj_ia/blob/main/images/dist.png">

### [Técnica](#tecnica)

A partir da leitura do dataset, foram definidas duas camadas ocultas, de 32 e 26 neurônios. Utilizando o modelo de regressão do algoritmo _Limited-memory Broyden–Fletcher–Goldfarb–Shanno_. Este é um algoritmo de otimização (_optimizer_), cujo objetivo é minimizar <img src="https://render.githubusercontent.com/render/math?math=f(x)"> sobre valores irrestritos do vetor real <img src="https://render.githubusercontent.com/render/math?math=x"> onde <img src="https://render.githubusercontent.com/render/math?math=f"> é uma função escalar diferenciável

As entradas da rede neural serão os valores encontrados no dataset. O usuário deverá informar cada um dos valores para que o perceptron calcule a probabilidade do usuário desenvolver diabetes dentro de cinco anos. A saída do software é um valor absoluto, onde "1" significa, de acordo com os dados de treinamento, que o usuário vai desenvolver diabetes em até cinco anos.

Neste trabalho foi utilizada a biblioteca Python [sciki-learn](https://scikit-learn.org/stable/).

Foram realizados testes de acurácia com uma e duas camadas de até 32 neurônios. O teste pode ser visualizado
<a href="https://github.com/lrweck/proj_ia/blob/main/hidden_layers.ods">clicando aqui.</a>

<img src="https://github.com/lrweck/proj_ia/blob/main/images/dataset_acuracia.png">

### [Ferramentas](#ferramentas)

- Python 3
- Pandas
- Numpy
- Scikit-learn
- Weka

### [Instruções de uso](#instrucoes)

Para utilizar o projeto, será necessário executar os seguintes comandos:

- pip install numpy
- pip install pandas
- pip install scikit-learn

Para executar o software, utilize o comando python3 Main.py

O sistema solicitará informações ao usuário para realizar a predição:
<img src="https://github.com/lrweck/proj_ia/blob/main/images/predicao.png">
