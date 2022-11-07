Handout criado por Pedro Andrade, Willian Kenzo e Thiago Kawahara 

Algoritmo de Programação Dinâmica para o Problema da Quebra em Palavras
===

Problema
---

**Qual a o problema?**

O problema da quebra em palavras consiste em dado um conjunto de palavras sem espaço, descobrir se esse mesmo conjunto de palavras pode ser separado por espaços ou não.

**Onde se encontra?**

Nas ferramentas de busca da internet e entrevistas de emprego de grandes empresas de tecnologia, como por exemplo a Google.

**Qual a importância de solucionar esse problema?**

??? Exercício 1

Entre no site da Amazon e busque por "tvplasma".
Depois entre no site da Americanas e faça a mesma busca.
Há diferença entre as respostas?

::: Gabarito
No site da Amazon é devolvido os resultados para "tv plasma", já no site da Americanas não é encontrado nenhum resultado.
:::

???

Isso é um problema visto que se você fosse comprar uma tv de plasma na Americanas, e escrevesse "tvplasma" na ferramenta de busca, o site não te retornaria nenhum resultado. Dando a entender que a Americanas não vende tvs de plasma (o que não é verdade) e a empresa perderia a venda.

Implementação
---

**O que é dado?**

* Uma string (conjunto de palavras sem espaço).
* Uma lista de palavras existentes (banco de dados).

**O que fazer?**

Fazer um algoritmo para descobrir se a string pode ser segmentada em espaços ou não.

**O que retornar?**

Um boolean:

* Se a string pode ser segmentada em espaços, retorna {green}(True).

* Se a string não pode ser segmentada em espaços, retorna {red}(False).

!!! Aviso
Por simplicidade iremos retornar apenas um boolean, mas facilmente poderiamos alterar o código para retornar a string segmentada em espaços.
!!!

**Prática**

Dado a seguinte lista de palavras:
``` py
[de, garrafa, agua, monitor, camisa, bordada]
```

E as seguintes strings:
``` py
"garrafadeagua"
"camisaxadrez"
"monitor"
"camisabordada"
```

??? Exercício 2

O que o algoritmo retornaria?

::: Gabarito
``` py
True 
False 
True
True
``` 

"garrafadeagua" retorna {green}(True), pois no banco de dados há "garrafa", "de" e "agua".

O mesmo para "monitor" e "camisabordada".

"camisaxadrez" retorna {red}(False), pois no banco de dados não há a palavra "xadrez", apesar de ter "camisa".
:::

???

RASCUNHO - EXPLICAR RECURSAO
---

Agora que já sabemos as entradas e as saídas do algoritmo, vamos ver como ele funciona.



RASCUNHO - EXPLICAR PROGRAMAÇAO DINAMICA
---

RASCUNHO - COMPLEXIDADE
---

RASCUNHO - DESAFIO: MUDAR O CODIGO PARA IMPRIMIR AS STRINGS SEGMENTAS
---










--APAGAR--APAGAR--APAGAR--APAGAR--APAGAR--APAGAR--APAGAR--APAGAR--APAGAR

Subtítulo
---------

Para criar um parágrafo, basta escrever um texto contínuo, sem pular linhas.

Você também pode criar

1. listas;

2. ordenadas,

assim como

* listas;

* não-ordenadas

e imagens. Lembre que todas as imagens devem estar em uma subpasta *img*.

![](logo.png)

Para tabelas, usa-se a [notação do
MultiMarkdown](https://fletcher.github.io/MultiMarkdown-6/syntax/tables.html),
que é muito flexível. Vale a pena abrir esse link para saber todas as
possibilidades.

| coluna a | coluna b |
|----------|----------|
| 1        | 2        |

Ao longo de um texto, você pode usar *itálico*, **negrito**, {red}(vermelho) e
[[tecla]]. Também pode usar uma equação LaTeX: $f(n) \leq g(n)$. Se for muito
grande, você pode isolá-la em um parágrafo.

$$\lim_{n \rightarrow \infty} \frac{f(n)}{g(n)} \leq 1$$

Para inserir uma animação, use `md :` seguido do nome de uma pasta onde as
imagens estão. Essa pasta também deve estar em *img*.

:bubble

Você também pode inserir código, inclusive especificando a linguagem.

``` py
def f():
    print('hello world')
```

``` c
void f() {
    printf("hello world\n");
}
```

Se não especificar nenhuma, o código fica com colorização de terminal.

```
hello world
```


!!! Aviso
Este é um exemplo de aviso, entre `md !!!`.
!!!


??? Exercício

Este é um exemplo de exercício, entre `md ???`.

::: Gabarito
Este é um exemplo de gabarito, entre `md :::`.
:::

???
