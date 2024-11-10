# Carrega a biblioteca `plumber`
library(plumber)

# Configura o `plumber` para usar o arquivo `plumber.R` e inicia a API
pr <- plumb("plumber.R")
pr$run(port = 7000)
