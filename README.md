# Detector Automático de COH-PIAH

Este é um detector automático de COH-PIAH, uma sigla fictícia utilizada para referir-se a um conjunto de sintomas que podem indicar um problema de escrita. Este detector analisa características linguísticas de textos fornecidos e determina qual deles está mais próximo de uma assinatura típica de um aluno infectado com COH-PIAH.

## Como Utilizar

Para utilizar este detector, siga as instruções abaixo:

1. Execute o código Python fornecido.
2. Será solicitado que você forneça uma assinatura típica de um aluno infectado. Você precisará inserir os seguintes valores:
   - Tamanho médio de palavra
   - Relação Type-Token
   - Razão Hapax Legomana
   - Tamanho médio de sentença
   - Complexidade média da sentença
   - Tamanho médio de frase

3. Após inserir a assinatura típica, você será solicitado a fornecer textos para análise. Insira os textos um por um, pressionando Enter após cada texto. Quando terminar de inserir os textos, pressione Enter sem digitar nada para finalizar.

4. O programa irá determinar qual texto está mais próximo da assinatura típica de um aluno infectado e informará o número do texto.

## Funções Principais

### `le_assinatura()`

Esta função solicita ao usuário que insira os valores da assinatura típica de um aluno infectado com COH-PIAH e retorna esses valores como uma lista.

### `le_textos()`

Esta função solicita ao usuário que insira os textos para análise e retorna esses textos como uma lista.

### `calcula_assinatura(texto)`

Esta função recebe um texto como entrada e calcula a assinatura linguística desse texto, retornando-a como uma lista.

### `avalia_textos(textos, ass_cp)`

Esta função avalia uma lista de textos em relação à assinatura típica de um aluno infectado. Ela determina qual texto está mais próximo da assinatura e o imprime na tela, além de retornar o número do texto.

## Sobre o Código

Este código foi desenvolvido em Python e utiliza expressões regulares para separar sentenças e frases, além de outras funções para análise linguística.

## Requisitos

Este código requer Python 3.x para ser executado.

## Contribuições

Contribuições são bem-vindas. Sinta-se à vontade para abrir problemas ou solicitações de envio (pull requests) para melhorias.