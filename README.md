# Detecção de autoria


Diferentes pessoas possuem diferentes estilos de escrita; por exemplo, algumas pessoas preferem sentenças mais curtas, outras preferem sentenças mais longas. Utilizando diversas estatísticas do texto, é possível identificar aspectos que funcionam como uma “assinatura” do seu autor e, portanto, é possível detectar se dois textos dados foram escritos por uma mesma pessoa. Ou seja, essa “assinatura” pode ser utilizada para detecção de plágio, evidência forense ou, neste caso, para diagnosticar a grave doença COH-PIAH.


## Traços linguísticos

Neste exercício utilizaremos as seguintes estatísticas para detectar a doença:

* Tamanho médio de palavra: Média simples do número de caracteres por palavra.

* Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.

* Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.

* Tamanho médio de sentença: Média simples do número de caracteres por sentença.

* Complexidade de sentença: Média simples do número de frases por sentença.

* Tamanho médio de frase: Média simples do número de caracteres por frase.



## Funcionamento do programa

A partir da assinatura conhecida de um portador de COH-PIAH, seu programa deverá receber diversos textos e calcular os valores dos diferentes traços linguísticos desses textos para compará-los com a assinatura dada. Os traços linguísticos que seu programa deve utilizar são calculados da seguinte forma:

* Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.

* Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 4 diferentes (o, gato, caçava, rato). Nessa frase, a relação Type-Token vale =0.8

* Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras. Por exemplo, na frase "O gato caçava o rato", temos 5 palavras no total (o, gato, caçava, o, rato) mas somente 3 que aparecem só uma vez (gato, caçava, rato). Nessa frase, a relação Hapax Legomana vale = 0.6

* Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças (os caracteres que separam uma sentença da outra não devem ser contabilizados como parte da sentença).

* Complexidade de sentença é o número total de frases divido pelo número de sentenças.

* Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto  (os caracteres que separam uma frase da outra não devem ser contabilizados como parte da frase).
