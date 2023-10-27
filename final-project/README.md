[EN]
# RATIONAL BINGO
#### Video Demo: <URL HERE>

#### Description:

## Final project: Rational Bingo
The Bingo Racional project is a web application developed as part of the CS50 course offered by Harvard University. The application allows users to generate bingo cards with rational and decimal numbers or both. This README provides an overview of the project and an explanation of the design choices and code structure.

## About the project
Bingo Racional is a web application that aims to create bingo cards with rational numbers, decimal numbers or both at random. The application is developed using the Flask framework in Python and incorporates web technologies such as HTML, CSS, JavaScript and Bootstrap. The application was created with the aim of offering an educational and playful tool that allows educators and teachers to teach rational number concepts in an engaging and fun way for students.

The main purpose of this project is to provide teachers with a tool that allows them to work on the concept of rational numbers in an engaging, engaging and motivating way for students. Using the game of bingo as a base, students can learn about rational numbers and decimals while having fun and competing for prizes. This makes the learning process more enjoyable and interactive.

## Summary of features
- Home page with an explanation of Bingo and how to use the site to play;
- Register, log in and log out;
- Button to create game (the user must choose a name);
- Once the user chooses the name of the game, they will have access to the page to choose how many cards the user wants to generate, as well as the type of cards (decimal, fractional or both);
- Once the cards are generated, they will be displayed on a page with the option of pressing a button to generate a PDF for download;
- Generate PDF for download;
- Access the Draw page and choose which game you want to draw;
- Carry out the draw.

## File Structure
The project is made up of several files that perform specific functions:

### app.py
This file contains the main logic of the Flask application. It defines the routes, generates bingo cards with rational and decimal numbers, generates PDFs of the cards for download, renders the HTML pages, and carries out the draw.

### styles.css
A CSS file that styles the appearance of bingo cards. It defines style rules, such as borders and margins for the cards.

### layout.html
This HTML file defines the main layout of the application pages. It incorporates Bootstrap to create a nice look and feel and provides block structures for pages to extend this layout.

### index.html
The application home page. This page explains what Bingo Racional is and how to use the site to play.

### geracao.html
On this page, users can select the type of card (rational, decimal or both) and the number of cards they want to generate. Forms are presented and processed in app.py. Once the choices have been made, the cards will be displayed on the cards.html page.

### cartelas.html
The page that displays the generated cards. It extends the main layout and uses block structures to fill the content with the generated cards.

## Design Choices

### Framework Flask
The project uses the Flask framework to create the web application. Flask is known for its simplicity and is suitable for smaller projects like this.

### Bootstrap
Bootstrap has been incorporated to improve the appearance and usability of the application. It provides responsive and pleasant styling.

## How to Execute the Project
To run the project, make sure you have Python and Flask installed. You can install Flask with the following command:

pip install Flask

After installing Flask, you can run the project using the app.py file. Just navigate to your project directory in the terminal and run:

python app.py

The application will run locally and you can access it in your browser at http://localhost:5000.

## Next steps
- The logic for registering, logging in and logging out is not working yet. I'm working on it.
- Implement a functionality so that the user can save the game, that is, the numbers that were used to generate the cards. This way, he will have enough time to print and cut out all the cards. When finished, you can return to the website, log in and access the same game that generated the cards. This way, it will be possible to guarantee that the draw will take place with the same numbers that were used to generate the cards.

This is an ongoing project and is open to contributions. If you want to collaborate or have suggestions, please let me know.

## Conclusion
The Bingo Racional project is a fun web application that allows you to generate bingo cards with rational and decimal numbers. It demonstrates the use of Flask, Bootstrap, and web technologies to create an app

[PT-BR]
# BINGO RACIONAL
#### Video Demo:  <URL HERE>

#### Description:

## Projeto final: Bingo Racional

O projeto Bingo Racional é uma aplicação web desenvolvida como parte do curso CS50 oferecido pela Universidade Harvard. A aplicação permite aos usuários gerar cartelas de bingo com números racionais e decimais ou ambos. Este README fornece uma visão geral do projeto e uma explicação das escolhas de design e estrutura do código.

## Sobre o projeto

O Bingo Racional é uma aplicação web que visa criar cartelas de bingo com números racionais, decimais ou ambos de forma aleatória. A aplicação é desenvolvida com o uso do framework Flask em Python e incorpora tecnologias da web, como HTML, CSS, javascript e Bootstrap. A aplicação foi criada com o objetivo de oferecer uma ferramenta educacional e lúdica que permite aos educadores e professores ensinar conceitos de números racionais de uma forma envolvente e divertida para os alunos.

A principal finalidade deste projeto é proporcionar aos professores uma ferramenta que lhes permita trabalhar o conceito de números racionais de maneira envolvente, engajadora e motivadora para os alunos. Utilizando o jogo de bingo como base, os alunos podem aprender sobre números racionais e decimais enquanto se divertem e competem por prêmios. Isso torna o processo de aprendizado mais agradável e interativo.

## Resumo das funcionalidades
- Página inicial com a explicaçao do Bingo e de como usar o site para jogar;
- Se cadastrar, fazer login e logout;
- Botão para criar jogo (o usuário deve escolher um nome);
- Uma vez que o usuário escolher o nome do jogo, terá acesso a página para escolher quantas cartelas o usuário quer gerar, bem como o tipo de cartelas (decimal, fracionárias ou ambas);
- Uma vez que as cartelas forem geradas, serão exibidas numa página com a opção de apertar um botão para gerar um PDF para download;
- Gerar PDF para download;
- Acessar a página de Sorteio e escolher qual jogo ele quer sortear;
- Realizar o sorteio.

## Estrutura dos Arquivos

O projeto é composto por vários arquivos que desempenham funções específicas:

### app.py

Este arquivo contém a lógica principal da aplicação Flask. Ele define as rotas, gera cartelas de bingo com números racionais e decimais, gera o pdf das cartelas para download, renderiza as páginas HTML, realiza o sorteio.

### styles.css

Um arquivo CSS que estiliza a aparência das cartelas de bingo. Ele define regras de estilo, como bordas e margens para as cartelas.

### layout.html

Este arquivo HTML define o layout principal das páginas da aplicação. Ele incorpora o Bootstrap para criar uma aparência agradável e fornece estruturas de blocos para que as páginas estendam esse layout.

### index.html

A página inicial da aplicação. Essa página explica o que é o Bingo Racional e como usar o site para jogar.

### geracao.html
Nessa página, os usuários podem selecionar o tipo de cartela (racionais, decimais ou ambos) e o número de cartelas que desejam gerar. Os formulários são apresentados e processados em app.py. Uma vez realizada as escolhas, as cartelas serão exibidas na página cartelas.html.

### cartelas.html

A página que exibe as cartelas geradas. Ela estende o layout principal e usa estruturas de bloco para preencher o conteúdo com as cartelas geradas.

## Escolhas de Design

### Framework Flask
O projeto utiliza o framework Flask para criar a aplicação web. Flask é conhecido por sua simplicidade e é adequado para projetos menores como este.

### Bootstrap
O Bootstrap foi incorporado para melhorar a aparência e a usabilidade da aplicação. Ele fornece um estilo responsivo e agradável.

## Como Executar o Projeto
Para executar o projeto, certifique-se de que você possui o Python e o Flask instalados. Você pode instalar o Flask com o seguinte comando:

pip install Flask

Depois de instalar o Flask, você pode executar o projeto usando o arquivo app.py. Basta navegar até o diretório do projeto no terminal e executar:

python app.py

A aplicação será executada localmente e você poderá acessá-la em seu navegador no endereço http://localhost:5000.

## Próximos Passos
- A lógica para fazer cadastro, login e logout ainda não está funcionando. Estou trabalhando nisso.
- Implementar uma funcionalidade para que o usuário salve o jogo, ou seja, os números que foram usados para gerar as cartelas. Assim, ele terá tempo suficiente para imprimir e recortar todas as cartelas. Quando ele terminar, pode retornar ao site, fazer login e acessar aquele mesmo jogo que gerou as cartelas. Assim, será possível garantir que o sorteio acontecerá com os mesmos números que foram usados para gerar as cartelas.

Este é um projeto em andamento e está aberto a contribuições. Se você quiser colaborar ou tiver sugestões, por favor me avise.

## Conclusão
O projeto Bingo Racional é uma aplicação web divertida que permite gerar cartelas de bingo com números racionais e decimais. Ele demonstra o uso do Flask, Bootstrap e tecnologias da web para criar uma aplicação interativa e útil. Este README fornece uma visão geral das partes principais do projeto e das decisões de design tomadas para sua criação. A aplicação é uma adição divertida a qualquer reunião ou evento social. Divirta-se!

## Autor

Higor Rabelo da Silva

## Licença

Este projeto está sob a Licença [escolha uma licença].
