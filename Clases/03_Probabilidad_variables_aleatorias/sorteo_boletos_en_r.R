boletos = 1:10
resultados = replicate(1000000, sample(boletos,1))
sum(resultados %% 3 == 0)

1000000*0.3
