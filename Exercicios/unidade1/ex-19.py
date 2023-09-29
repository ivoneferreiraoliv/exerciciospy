tamanhoDoArquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidadeDaInternet = float(input("Digite a velocidade da internet em Mbps: "))
tempoDeDownloadMinutos = (tamanhoDoArquivo / velocidadeDaInternet) // 60
tempoDeDownloadSegundos = (tamanhoDoArquivo / velocidadeDaInternet) % 60 
print("O tempo de download é de", tempoDeDownloadMinutos, "minutos e", tempoDeDownloadSegundos, "segundos")