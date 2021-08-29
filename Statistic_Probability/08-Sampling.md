# Amostragem — Conceitos Fundamentais
- Amostragem
- Amostra
- Amostragem probabilística e não probabilísticas

### Método Estatístico
- Coleta
- Organização
- Apresentação
- Análise
- Interpretação
- O seu objetivo é o estudo dos parâmetros de uma população

### Amostragem
- Censo: Todos os elementos da população
- Amostragem: Seleção de alguns elementos
    - Pesquisas podem ser feitas pelo estudo dos elementos de uma amostra
    - Amostra é extraída da população que se pretende estudar
    - Amostragem é o processo de escolha da amostra

### Amostragem não probabilística
- Amostras intencionais
- Escolha deliberada dos elementos
- Não garantem a representatividade
- Não são generalizáveis
- Tipos
  * Conveniência (Acidental)
    * formada por elementos conforme vão aparecendo
    * elementos são os possíveis de se obter
    * encerra quando completar o número da amostra
    * exemplo: pessoas transitando por determinada avenida
  * Julgamento (Intencional)
    * formada por elementos seguindo algum critério
    * intencionalmente escolhidos
    * exemplo: especialista em algum assunto
  * Por quotas (Proporcionalidade)
    * Classificação de acordo com propriedades
    * determinação da proporcionalidade da população para cada propriedade
    * seleção não aleatória

### Amostragem probabilística
- Cada elemento possuí probabilidade conhecida de ser escolhida
- Usualmente a probabilidade é a mesma entre os elementos
- exemplo: população n elementos, cada elemento tem 1/n, oportunidades de participar
- pode-se realizar inferência sobre uma população a partir dos parâmetros de uma amostra
- são generalizáveis
- Tipos
    * Amostragem aleatória simples
        * seleção de amostras de tamanho K dentre número(n) de unidades da população
        * amostragem realizada sem reposição
        * número de amostras possíveis:
        ```buildoutcfg
                         n!
        C (n / k) = -----------
                     k!(n - k)!
        ```
        * as unidades da população são numeradas de 1 até n
        * escolhem se k números compreendidos de 1 até n
        * equivale a um sorteio
    * Amostragem aleatória estratificada
      * separando as unidades em grupos não superpostos
      * usando amostragem aleatória simples em cada estrato
      ```buildoutcfg
      N = N° de unidades da população
      n = N° de unidades das amostras
      Na = N° de unidades do estrato A
      na = N° de amostras de A
      
       Na     na             n
      ---- = ---- → na = Na ----
       N      n              N
      
      Sexo          População   10%     N° de amostras
      ------------------------------------------------
      Masculino         52      5.2             5
      Feminino          38      3.8             4
      Total             90      9.0             9
      ```
    * Amostragem sistemática
      * elementos ordenados
      * seleção obedece um intervalo
      * N -K <= N/n
      * fácil, menos erros do entrevistador
      * proporciona mais informações por custo unitário do que aleatória simples
      ```buildoutcfg
      N = n° de elementos
      n = n° de amostras
      K = intervalo
      
           N 
      K = ---, arrendondar para inteiro menor
           n
      ```
    * Amostragem por conglomerado
      * especificar conglomerados apropriados
      * todos os elementos fazem parte de uma amostra
      * elementos tendem a ter características similares
      * n° de elementos deve ser pequeno
      * o n° do conglomerado deve ser razoavelmente grande
      ```buildoutcfg
      # levantamento de uma população de uma cidade
      - mapa indicando cada quarteirão
      - seleciona amostras dos quarteirões
      - realiza a contagem completa de todos que residem nos quarterões sorteados
      ```