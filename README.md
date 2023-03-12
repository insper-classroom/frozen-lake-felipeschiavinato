[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10442743&assignment_repo_type=AssignmentRepo)
# Projeto para testar uma implementação para o FrozenLake 8x8

Considere o ambiente FrozenLake 8x8 versão não-determinística. Implemente um agente capaz de chegar ao objetivo final em pelo menos 80% das vezes. Para implementar este agente você pode utilizar o algoritmo *Q-Learning* ou *Sarsa* com os hiperparâmetros que você considerar melhor. 

Você deve adicionar neste projeto e fazer o commit dos seguintes artefatos: 

* o arquivo `q-table.csv` dentro do diretório `data`. Já existe um arquivo q-table neste projeto, mas ele é para a versão do ambiente 4x4. Quando você executar o arquivo `test_frozenlake.py` usando o comando `pytest`irá ocorrer um erro de `IndexError`. Você deve substituir este arquivo pelo arquivo gerado pelo seu agente durante o período de treinamento; 

* depois de substituir o arquivo `data/q-table.csv`, você poderá executar os testes e verificar se o mesmo é aprovado em todos os testes. São quatro testes: o primeiro executa o ambiente 1000 vezes e verifica se o agente conseguiu chegar ao final em no mínimo 700 vezes. Os outros 3 testes fazem exatamente a mesma coisa: executam o agente no ambiente 1000 vezes e verificam se o agente conseguiu chegar ao final em no mínimo 800 vezes;

* você também deve adicionar a sua implementação no diretório raiz deste projeto, e;

* alterar este arquivo README.md informando os hiperparâmetros utilizados para o treinamento. 

* (critério para A+) apresentar um gráfico comparando a curva de aprendizagem de diversas abordagens utilizadas durante o treinamento. 

## Algoritmo e hiperparâmetros utilizados para o treinamento

| Atributo        |  Valor     |
|:----------------|:----------:|
| Algoritmo       |            |
| alpha           |            |
| gamma           |            |
| epsilon         |            |
| epsilon_dec     |            |
| epsilon_min     |            |
| qtd_episodios   |            |


## Comparação entre abordagens

O Q-learning foi o algorítimo escolhido por ser de característica off-policy, atualizando seu resultado de acordo com a política ótima e por se tratar de um ambiente estocástico. Vamos aprofundar o processo de ajuste dos hiperparâmetros do algoritmo Q-learning para melhorar seu desempenho na resolução do ambiente FrozenLake. Primeiramente foram fixados os seguintes parametros:


* $\alpha = 0.1$

* $\gamma = 0.99$

* $\epsilon = 0.9999$

* $\epsilon_{min} = 0.0001$

* $E = 100000$

Em seguida, um gráfico foi plotado de modo a vizualizar o decaimento do parametro $\epsilon$ para diferentes $\epsilon_{dec}$ ao longo dos episodios de treinamento.

![alt text](results/epsilon_per_episodes.png "Epsilon x Episodes")

<!-- O gráfico ajuda a visualizar o efeito de diferentes valores de epsilon na compensação exploration-explotation durante o processo de Q-learning. Um valor mais alto de epsilon significa que o algoritmo tem mais chances de explorar o ambiente selecionando ações aleatórias, enquanto um valor mais baixo de epsilon significa que o algoritmo tem mais chances de explorar os valores Q aprendidos selecionando a ação com o valor Q mais alto.

Além disso, mostra que, à medida que o epsilon diminui ao longo do tempo, o algoritmo se concentra mais em explorar os valores Q aprendidos, o que pode levar a um desempenho melhor na tarefa. No entanto, um valor baixo de epsilon pode fazer com que o algoritmo fique preso em um ótimo local e perca o ótimo global. Portanto, é essencial equilibrar a exploração e a "exploitação" escolhendo um valor apropriado de $\epsilon_{dec}$. -->

O grafico nos permite vizualizar para varios valores de $\epsilon_{dec}$, qual a curva que controla a diminuiçao da probailidade de exploração, para valores menores de $\epsilon_{dec}$, a diminuição é brusca, fazendo com que durante o treinamento, o modelo pare de explorar logo nos primeiros episodios, e conforme $\epsilon_{dec}$ aumenta, o decaimento de $\epsilon$ fica gada vez mais gradual.

### Treinamento




