#         Carrefour Data Challenge - DIO

<p align="center"><img src="./DIO.png" width="500"></p>



O desafio foi promovido pelo **Banco Carrefour** em parceria com **Digital Innovation One**.

O desafio consiste em desenvolver uma aplicação que extraia os trending topics do Twitter e os armazene em um banco de dados NoSQL.

---

### Estrutura do repositório

1. A pasta **data-challenge** contém a aplicação principal responsável por extrair os trending topics.

1. A pasta **exploratory-analysis** contém a aplicação secundária em um jupyter notebook, utilizado para realizar a análise exploratória do trending topic escolhido. Os datasets extraídos tanto pela aplicação principal quanto pela secundária também estão neste diretório. Obs:Aconselha-se abrir o arquivo no jupyter notebook para melhor visualização dos dados. 

1. A pasta **data-visualization** contém as imagens criadas para a visualização dos dados a partir de bibliotecas do **Python** e também do **MicroStrategy**.

1. Na pasta raiz temos um relatório sobre a realização do desafio. Este relatório tem o intuito de que até alguém que não tenha histórico de programação consiga compreender o objetivo da construção da aplicação e o ganho de informação com a mesma.

    ------

    

### Primeiros Passos

1. A aplicação principal já conta com as chaves da Twitter API inseridas no diretório src. Tais chaves foram obtidas apenas para o desafio através de uma conta criada para o mesmo.

2. Importe a pasta data-challenge para o seu editor de código preferencial. Inicie o arquivo `docker-compose.yml` para utilizar o MongoDB e o Mongo Express. 

3. Para iniciar a aplicação escreva no terminal `python main.py` 

4. Abra seu navegador e digite `localhost:8081` a página do Mongo Express deverá aparecer.

5. Em alguns casos a página não obtinha resposta. Esse erro era provocado pelo o Mongo Express não estar rodando de verdade, o que era constatado ao checar no Docker Desktop. Ao rodar novamente o Express, a página obtinha resposta

6. Para acessar a página da FASTAPI abra o navegador e digite `127.0.0.1:8000/docs`

7. Para utilizar a aplicação de análise exploratória, basta abrir o jupyter notebook e seguir as informações disponibilizadas no mesmo.

   ------

   ### Próximos Passos

   - Utilizar outras bibliotecas de linguagem natural e comparar os resultados
   - Após aprofundamento na documentação do **Docker**, utilizar o mesmo para a conteinerização das aplicações.

   ------

   O aprimoramento da aplicação será proporcional ao meu aprendizado. Constante

   Qualquer dúvida, informação ou sugestão, fique a vontade para entrar em contato. Ficarei muito feliz em aprender algo novo.

   rodrigomarinho.eq@gmail.com 

   linkedin.com/in/rodrigo-marinho-55a64514a/ 

   



