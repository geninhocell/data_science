

###### Experimento Aleatório
Definição Frequencialista
```buildoutcfg
m = número de sucessos
n = número de experimentos

         m
p = lim ---, n → ∞
         n
    
# Definição clássica
P = Probabilidade
M = Número de sucessos
N = Número de possibilidades

     M
P = ---
     N
```
###### Espaço Amostral (S)
Conjunto de todos os possíveis resultados desse experimento.

Lançamento de moeda.
```buildoutcfg
# Uma moeda, 2 eventos
S = {cara, coroa}

# Duas moedas, 4 eventos
S = {(c,k), (c,c), (k,c), (k,k)}
```

###### Eventos Aleatórios (E)
Qualquer subconjunto de um espaço amostral.

Resultado possível em experimentos aleatórios e que não é previsível.

Lançamento de moeda.
```buildoutcfg
# Uma moeda
S = {C,K}
E = K
P(E) = ?

# Duas moedas
S = {(c,k), (c,c), (k,c), (k,k)}
E = K,K
P(E) = ?
```
Propriedades
- 0 <= P(E) <= 1
- P(S) = 1

###### Evento Complementar
Se o evento A não ocorreu, Ã

###### Evento Equiprovável
Cada ponto do espaço amostral tem a mesma probabilidade de ocorrer.

###### Eventos Mutuamente Excludentes
Se acontece o evento A, B não ocorre e também ao contrário.

###### Operações Entre Eventos
União A U B, ocorreu A ou B

Intersecção A ∩ B, ocorreu A e B

###### Axiomas da Probabilidade
1. Conjunto Ø (evento impossível)
```buildoutcfg
P(Ø) = 0

P(A ∩ B) = 0, significa que são mutuamente excludentes
```
2. Teorema do Evento Complementar: se Ã é o complemento de A então:
```buildoutcfg
P(Ã) = 1 - P(A)
```
3. Teorema da Soma: se A e B são dois eventos quaisquer então:
```buildoutcfg
# quando soma a P(A) com a P(B), a intersecção fica duplicada, então subtrai uma.
P(A U B) = P(A) + P(B) - P(A ∩ B)

# mas se são mutuamente exlusivos, não há intersecção, sendo A ∩ B = Ø, então P(A ∩ B) = 0
P(A U B) = P(A) + P(B) - 0

# 3 eventos
P(A U B U C) = P(A) + P(B) + P(C) - P(A ∩ B) - P(A ∩ C) - P(B ∩ C) + P(A ∩ B ∩ C)
```

###### Teoria da Contagem
```
Evento 1, m possibilidades
Evento 2, n possibilidades
m*n possibilidades
```

###### Teoremas de Probabilidade
Probabilidade Condicional
```buildoutcfg
# Probabilidade de A, dado que B aconteceu
          P(A ∩ B)
P(A|B) = ----------
            P(B)
           

```
Teorema do Produto
```buildoutcfg
          P(A ∩ B)
P(A|B) = ---------- → P(A ∩ B) = P(B) * P(A|B)
            P(B)
            
          P(A ∩ B)
P(B|A) = ---------- → P(A ∩ B) = P(A) * P(B|A)
            P(A)
```

###### Eventos Independentes
```buildoutcfg
P(A|B) = P(A)

P(A ∩ B) = P(A) * P(B)
```

