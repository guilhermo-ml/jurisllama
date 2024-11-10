# Carrega as bibliotecas necessárias
library(plumber)
library(tjsp)
library(parallel)
library(tools)

#* Busca processos de primeiro grau com um termo específico, com tempo limite
#* @param termo Termo de busca para processos
#* @param diretorio Diretório para salvar os arquivos
#* @param timeout Tempo máximo para o download em segundos (padrão: 300 segundos)
#* @post /buscar
function(termo, diretorio, timeout = 10) {
  timeout <- as.numeric(timeout)
  
  # Verifica se o diretório existe, caso contrário, cria o diretório
  if (!dir.exists(diretorio)) {
    dir.create(diretorio)
  }
  
  # Inicia o processo de download em paralelo
  download_process <- mcparallel({
    tjsp_baixar_cjpg(livre = termo, diretorio = diretorio)
  })
  
  # Espera o processo terminar ou o timeout ser atingido
  result <- mccollect(download_process, wait = FALSE, timeout = timeout)
  
  # Verifica se o processo foi concluído ou se houve timeout
  if (is.null(result)) {
    # Mata o processo se o timeout foi atingido
    pskill(download_process$pid)
    return(list(mensagem = "Tempo limite excedido para a busca", diretorio_salvo = diretorio))
  } else {
    return(list(mensagem = "Busca concluída", diretorio_salvo = diretorio))
  }
}

#* Lista todos os arquivos HTML no diretório especificado
#* @param diretorio Diretório onde os arquivos HTML estão salvos
#* @get /listar_arquivos
function(diretorio) {
  if (!dir.exists(diretorio)) {
    return(list(erro = "Diretório não encontrado"))
  }
  
  arquivos <- list.files(path = diretorio, pattern = "\\.html$", full.names = FALSE)
  return(list(arquivos = arquivos))
}

#* Baixa um arquivo HTML específico do diretório
#* @param diretorio Diretório onde o arquivo HTML está salvo
#* @param arquivo Nome do arquivo HTML a ser baixado
#* @get /download_arquivo
#* @serializer contentType list(type="application/octet-stream")
function(diretorio, arquivo) {
  file_path <- file.path(diretorio, arquivo)
  
  if (file.exists(file_path)) {
    readBin(file_path, "raw", n = file.info(file_path)$size)
  } else {
    res$status <- 404
    return(list(erro = "Arquivo não encontrado"))
  }
}
