"""
https://pt.khanacademy.org/math/precalculus/prob-comb/combinations/v/combination-formula

Exemplo Permutação

 k     k-1   k-2   ...   k-n
--- *  --- * --- * --- * --- = k!
 1      2     3    ...    K

          n!           n!                                  números de coisas
C n,k = -------   =  --------- = coeficiente binomial  =  ------------------
        (n-k)!       k!(n-k)!                                 k lugares
        ------
          K!


4 cadeiras
6 pessoas

 6   5   4   3     Pessoas
--- --- --- ---
 1   2   3   4     Cadeiras

6! = 6 * 5 * 4 * 3 * 2 * 1  # Retirar apartir do 2!


P 6,4 = 6! / (6 - 4)!
P 6,4 = 6! / 2!
P 6,4 = 6 * 5 * 4 * 3 * 2! / 2!
P 6,4 = 6 * 5 * 4 * 3
P 6,4 = 360


"""