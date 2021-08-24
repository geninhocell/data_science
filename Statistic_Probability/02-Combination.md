# Análise Combinatória 

4 quadros

a b c d

a b d c

a c b d

a c d b

a d b c

a d c b

Total de 6 combinações com quadro a na primeira posição.

Logo 4 quadros * 6 = 24 combinações ou **4!**

Permutação = n!

Com repetição

a b b d

a b d b 

a b b d

a b d b 

a d b b 

a d b b 

Cai pela metade as combinações.

```
     4!
P = ---- = 12
     2
     
             n!
P = n1 n = ------
             n1!
```
Exemplo 1.

###### Quantos anagramas existem da palavra BORBOLETÁRIO?

Temos 12 Letras.

B repete 2 vezes.

O repete 3 vezes.

R repete 2 vezes.
```buildoutcfg
                12!
P 2,3,2 12 = -------- = 19,958,400
              2!3!2!
```
Exemplo 2.

###### Cinco candidatos e três vagas, quantas combinações?

```buildoutcfg
# Onde a ordem importa
 5   4   3
--- --- ---

5 * 4 * 3 = 60 arranjos onde a ordem importa
n: número de pessoas
p: número de vagas

            n!
A n,p = ---------   
         (n - p)!
         
# Onde a ordem não importa
             n!
C n,p = ------------
         p!(n - p)!
         
             5!         5 * 4 * 3!     5 * 4
C n,p = ------------ = ------------ = ------- = 10
         3!(5 - 3)!      3! * 2!       2 * 1
```

