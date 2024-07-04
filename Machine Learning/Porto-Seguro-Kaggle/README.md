Porto Seguro Safe Driver Prediction
Descrição
Este repositório contém o código e os dados utilizados para o desafio da Porto Seguro Safe Driver Prediction no Kaggle. O desafio consistiu em prever a probabilidade de um motorista iniciar um sinistro de seguro de automóvel no próximo ano com base em uma série de características.

Objetivo
O objetivo principal deste desafio foi construir um modelo de aprendizado de máquina que pudesse prever com precisão a probabilidade de um motorista fazer uma reclamação de seguro de automóvel no próximo ano. Isso permitiria à Porto Seguro ajustar seus preços de seguro com mais precisão e potencialmente tornar o seguro de automóvel mais acessível para mais motoristas.

Métrica de Avaliação
As submissões foram avaliadas usando o Coeficiente de Gini Normalizado. Esta métrica compara a proporção acumulada de observações da classe positiva com uma proporção uniforme teórica.

Conteúdo do Repositório
train.csv: Conjunto de dados de treinamento contendo características dos motoristas e a variável alvo.
test.csv: Conjunto de dados de teste para os quais as previsões devem ser feitas.
portoseguro_safe_driver_prediction.ipynb: Jupyter Notebook contendo todo o código utilizado para explorar, limpar os dados, treinar modelos e fazer previsões.
README.md: Este arquivo, fornecendo uma visão geral do repositório, o objetivo do desafio e os resultados obtidos.
Como Usar
Clone este repositório para sua máquina local.
Abra o Jupyter Notebook portoseguro_safe_driver_prediction.ipynb.
Siga as instruções passo a passo para explorar os dados, treinar modelos e fazer previsões.
Para fazer previsões no conjunto de dados de teste, forneça o caminho do arquivo test.csv e execute as células relevantes no notebook.
Resultados
Os resultados obtidos foram avaliados com base na métrica de Coeficiente de Gini Normalizado e são documentados no notebook.

Conclusão
Este projeto demonstra a aplicação de técnicas de aprendizado de máquina para resolver um problema do mundo real na indústria de seguros de automóveis. A precisão alcançada nas previsões pode ajudar a Porto Seguro a ajustar seus preços de seguro e melhorar a acessibilidade ao seguro de automóvel para seus clientes.
