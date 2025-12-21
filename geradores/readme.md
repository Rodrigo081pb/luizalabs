O que são geradores

são tipos especiais de iteradores que ao contrário das listas ou outros iteráveis, eles não armazenam todos os seus valores em memória.

São definidos usando funções regulares, mas ao invés de retornar valores usando "return", utilizam o yield

# Característica

** Uma ve que um item gerado é consumido, ele é esquecido e não pode ser acessado novamente

** O estado interno de um gerador é mantido entre chamadas


------------------

User case :

Recuperando dados de uma API

- Solicitar dados por páginas
- Fornecer um produto por vez entre as chamadas
- Quando todos os produtos de uma página forem retornados, verificar se tem mais páginas
- tratar o consumo da API como uma lista python