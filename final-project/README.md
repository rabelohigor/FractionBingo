# BINGO RACIONAL
#### Video Demo:  <URL HERE>

#### Description:

## Projeto final: Bingo Racional

O projeto Bingo Racional é uma aplicação web desenvolvida como parte do curso CS50 oferecido pela Universidade Harvard. A aplicação permite aos usuários gerar cartelas de bingo com números racionais e decimais. Este README fornece uma visão geral do projeto e uma explicação das escolhas de design e estrutura do código.

## Sobre o projeto

O Bingo Racional é uma aplicação web que visa criar cartelas de bingo com números racionais e decimais de forma aleatória. A aplicação é desenvolvida com o uso do framework Flask em Python e incorpora tecnologias da web, como HTML, CSS e Bootstrap. A aplicação foi criada com o objetivo de oferecer uma ferramenta educacional e lúdica que permite aos educadores e professores ensinar conceitos de números racionais de uma forma envolvente e divertida para os alunos.

A principal finalidade deste projeto é proporcionar aos professores uma ferramenta que lhes permita trabalhar o conceito de números racionais de maneira envolvente, engajadora e motivadora para os alunos. Utilizando o jogo de bingo como base, os alunos podem aprender sobre números racionais e decimais enquanto se divertem e competem por prêmios. Isso torna o processo de aprendizado mais agradável e interativo.

## Estrutura dos Arquivos

O projeto é composto por vários arquivos que desempenham funções específicas:

### app.py

Este arquivo contém a lógica principal da aplicação Flask. Ele define as rotas, gera cartelas de bingo com números racionais e decimais e renderiza as páginas HTML.

### styles.css

Um arquivo CSS que estiliza a aparência das cartelas de bingo. Ele define regras de estilo, como bordas e margens para as cartelas.

### layout.html

Este arquivo HTML define o layout principal das páginas da aplicação. Ele incorpora o Bootstrap para criar uma aparência agradável e fornece estruturas de blocos para que as páginas estendam esse layout.

### index.html

A página inicial da aplicação. Os usuários podem selecionar o tipo de cartela (racionais, decimais ou ambos) e o número de cartelas que desejam gerar. Os formulários são apresentados e processados em app.py.

### cartelas.html

A página que exibe as cartelas geradas. Ela estende o layout principal e usa estruturas de bloco para preencher o conteúdo com as cartelas geradas.

## Escolhas de Design

### Framework Flask
O projeto utiliza o framework Flask para criar a aplicação web. Flask é conhecido por sua simplicidade e é adequado para projetos menores como este.

### Bootstrap
O Bootstrap foi incorporado para melhorar a aparência e a usabilidade da aplicação. Ele fornece um estilo responsivo e agradável.

### Geração de Cartelas
As cartelas são geradas aleatoriamente com números racionais e decimais. Os usuários podem escolher o tipo de cartela e a quantidade desejada.

## Como Executar o Projeto
Para executar o projeto, certifique-se de que você possui o Python e o Flask instalados. Você pode instalar o Flask com o seguinte comando:

pip install Flask

Depois de instalar o Flask, você pode executar o projeto usando o arquivo app.py. Basta navegar até o diretório do projeto no terminal e executar:

python app.py

A aplicação será executada localmente e você poderá acessá-la em seu navegador no endereço http://localhost:5000.

## Conclusão
O projeto Bingo Racional é uma aplicação web divertida que permite gerar cartelas de bingo com números racionais e decimais. Ele demonstra o uso do Flask, Bootstrap e tecnologias da web para criar uma aplicação interativa e útil. Este README fornece uma visão geral das partes principais do projeto e das decisões de design tomadas para sua criação. A aplicação é uma adição divertida a qualquer reunião ou evento social. Divirta-se!






## Ideia principal

Criar uma página web para o professor de matemática jogar Bingo Racional com seus alunos.
- permitir que o professor escolha se as cartelas terão números fracionários (difícil), decimais (fácil), ou ambos (intermediário);
- botão para imprimir as cartelas;
- Rodar o BINGO, mantendo o registro dos números que foram sorteados;
- Permitir criar salas para que grupos menores de até 5 pessoas (1 chamador e 4 jogadores) joguem juntos;
- criar um tutorial interativo para quando a pessoa acessar pela primeira vez;

Se eu não conseguir criar tudo isso, quero que pelo menos seja possível gerar as cartelas (mesmo que sem escolher se serão números fracionários, decimais ou ambos) e que o professor consiga rodar o bingo, matendo o registro dos números sorteados.

## Funcionalidades

1. **Escolha do Tipo de Cartela:**
   - Os professores podem escolher entre três opções de cartelas:
     - Cartelas com números fracionários.
     - Cartelas com números decimais.
     - Cartelas com números fracionários e decimais.

2. **Número de Cartelas:**
   - Os professores podem especificar o número de cartelas que desejam gerar.

3. **Geração de Cartelas:**
   - Com base nas escolhas de tipo e número de cartelas, o sistema gera as cartelas de Bingo 5x5.
   - Cada cartela tem 24 números, com um espaço central vazio.

4. **Exibição das Cartelas:**
   - As cartelas geradas são exibidas na página web para que os professores possam visualizá-las.

5. **Impressão de Cartelas:**
   - Os professores podem imprimir as cartelas. São impressas seis cartelas por página no formato A4.


## Próximos Passos

- Implementar a lógica de geração de números fracionários e decimais, se necessário.
- Aperfeiçoar a formatação de impressão para atender aos requisitos específicos.

Este é um projeto em andamento e está aberto a contribuições. Se você quiser colaborar ou tiver sugestões, fique à vontade para criar problemas (issues) ou solicitações de pull (pull requests).

## Autor

Higor Rabelo da Silva

## Licença

Este projeto está sob a Licença [escolha uma licença].
