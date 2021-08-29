# Medidas de posição e dispersão

- Posição central
    * média
    * moda
    * mediana
  
- Dispersão
  * amplitude
  * variância
  * assimetria
  * curtose

- Medidas de posição
  - localizar a maior concentração de valores de uma distribuição
  - sintetizar o comportamento do conjunto do qual ele é originário
  - possibilitar comparações entre séries de dados

- Média Aritmética Simples
```buildoutcfg
Xᵢ = valor observado
N = número de observações

x-barra = ∑ ᴺᵢ₌₁ Xᵢ
```

- Média Aritmética Ponderada
```buildoutcfg
- atribui um peso P

            ∑ ᴺᵢ₌₁ XᵢPᵢ
XP-barra = ------------ 
            ∑ ᴺᵢ₌₁ Pᵢ
      
Exemplo:

              Vendas        Lucro
Pregos      R$ 2500         30%
Parafuso    R$ 1500         50%
Rebite      R$ 750          40%

           2500*0.3 + 1500*0.5 + 750*0.4
XP-barra = ----------------------------- = 37.9%
                 2500 + 1500 + 750
```

- Dados agrupados
```buildoutcfg
- sem intervalo de classe

Xᵢ = valor observado
Nᵢ = número de observações por classe
N = número de observações total

           ∑ ᴺᵢ₌₁ XᵢNᵢ
X-barra = -------------
                N
                
                
Exemplo:

N° de salários     N° de funcionários
       3                  192
       4                  328
       5                  321
       6                  180
       7                  43

           3*192 + 4*328 + 5*321 + 6*180 + 7*43
X-barra = -------------------------------------- = 4.6
               192 + 328 + 321 + 180 + 43

- com intervalo de classe

           ∑ ᴺᵢ₌₁ X-barraᵢNᵢ
X-barra = -------------
                N
```

- Moda
  * Multimodal, mais de uma moda
  * Amodal, sem valor predominante
```buildoutcfg
Lᵢ = limite inferior da classe modal
d₁ = diferença entre a frequência da classe modal e a da classe imediatamente anterior
d₂ = diferença entre a frequência da classe modal e a da classe imediatamente seguinte
h = amplitude das classes

              d₁
mo = Lᵢ + --------- h
           d₁ + d₂        
```

- Mediana (M)
  * Separatriz, divide em duas partes iguais
  * Centro, da série estatística
```buildoutcfg
- impar

EMd = (n+1)/2

- par

     x(EMd) + X(EMd + 1)
Md = -------------------
            2

```

### Medidas de dispersão
- medem o grau de variabilidade em torno da média aritmética
- nível de homogeneidade ou heterogeneidade

###### amplitude
  * Xmax - Xmin
  * utilização limitada
  * pouco utilizada
  * não considera valores internos

###### variância
  * considera valores extremos e intermediários
  * relaciona os desvios em torno da média
  * média aritmética dos quadrados dos desvios
```buildoutcfg
- população

            (Xᵢ - X-barra)²
S² = ∑ᴺᵢ₌₁ -----------------
                  N
                  
- amostra

            (Xᵢ - X-barra)²
S² = ∑ᴺᵢ₌₁ -----------------
                N - 1

# dados agrupados

- população

       ∑x²nᵢ     ∑x²nᵢ  ²
S² =  ------- - -------
         N         N
         
- amostra

        ∑x²nᵢ    ∑x²nᵢ  ²
S² =  ------- - -------
        N - 1    N - 1
        
- desvio padrão 
S = √S²

- coeficiente de variação (CV)

         S
CV = ---------
      X-barra
      
- baixa dispersão CV <= 15%
- média dispersão 15% < CV < 30%
- alta dispersão CV >= 30%
```

- Curva simétrica
  * X-barra = Mo = Md
- Assimetria à direita (positiva)
  * Mo < Md < X-barra
- Assimetria à esquerda (negativa)
  * X-barra < Md < Mo