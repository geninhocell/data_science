# Distribuições de Probabilidade

## Bernoulli
- Experimento Aleatório (Incerteza)
- Realizado Repetida vezes (Tentativas)
- Mantidas as condições
- Resultado: sucesso ou fracasso

```buildoutcfg
P(sucesso) = p

P(fracasso) = q = 1 - p

P = pᴷq¹⁻ᴷ K ∈ {0,1}
```

## Binomial
- N provas independentes
- Sucesso ou Fracasso (Bernoulli)
- P(sucesso) = P → (Constante)
```buildoutcfg
Nesta Ordem!

P = p*p*p*p*...*p*q*q*..*q

P = pᴷqᴺ⁻ᴷ

Diferentes Ordens!

K = sucessos
N = possibilidades

             N
P(X = k) = C--- * pᴷ * qᴺ⁻ᴷ
             K
            
 N         N!
--- = -----------
 K     K!(N - K)


μ = media ou esperança
n = tentativas
p = probabilidade de sucesso
q = probabilidade de fracasso
σ = variancia

μ = n * p

σ²(x) = n * p * q

Exemplo: Torno Mecânico
- 25% defeitos
- Amostra N = 16
- X = Peças defeituosas
- P(X = 4) = ?

              16       
P(X = 4) = C ---- * 0.25⁴ * 0.75¹² = 0.2252
              4
              
μ = 16 * 0.25 = 4
σ² = 16 * 0.25 * 0.75 = 3
```

## Poisson
```buildoutcfg
lim Binomial = Poisson
n → ∞
```
Hipóteses

- Eventos definidos em intervalos não sobrepostos são independentes
- β (média) é constante no intervalo estudado
```buildoutcfg
t = números de intervalo
K = número de sucessos
β = média

           e⁻ᵝᵗ * (βt)ᴷ
P(X = K) = ------------
                K!
           
Exemplo: Semáforo
- β = 4 veículos por minuto
- t = intervalo de 2 minutos
- P(X = 7) = ?

μ = β * t = 8

            e⁻⁸ * (8)⁷
P(X = 7) = ------------ = 0.1396
                7!
```

##Normal (Gaussiana)
- Teorema do limite central
    - A soma de infinitas variáveis independentes segue uma distribuição normal, variar em formato de sino.
    - As extremidades tendem a ser menos prováveis.
```buildoutcfg
μ = média
σ = desvio padrão
σ² = variancia

         1
f(x) = ------e^-(1/2)((x-μ)/σ)² , -∞ < x < +∞
        σ√2𝛑
       
x =  
     x - μ
Z = -------
       σ
       
E(Z) = 0

σ²(Z) = 1

Exemplo: Processo numa linha de montagem
- μ = 230 minutos
- σ = 15 minutos
- P(T <= 240.5) = ?

     240.5 - 230
Z = ------------ = 0.7
         15
```
Propriedades das Distribuições

0.064
0.216