# CONVERSOR PDF PARA ARQUIVO .CSV

## Este conversor extrai o conteúdo de todos arquivos *.pdf alocados na pasta */packages/orders
## referente aos pedidos do atelie do Strudel. Compila tudo em um arquivo .csv que será salvo na mesma pasta.

## Packages do projeto:
#### Conversor pdf para string:
  ##### Extrai o conteúdo do pedido (.pdf) em aloca em uma variável do tipo string
### Conversor string para list:
  ### Converte cada linha da string, informações de nome, endereço e itens comprados, retorna uma lista de strings
### Atributos dos pedidos:
  ### Extrai de cada item da lista a informação final a ser usada e retorna uma lista do pedido completo.
### Conversor csv
  Cria uma lista de listas onde cada linha é um pedido gerado pelo atributos dos pedidos. Salva em um arquivo .csv
