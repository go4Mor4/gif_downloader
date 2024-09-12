# `gif_downloader`

Uma biblioteca simples para busca e download de GIFs usando a API do Giphy.


## Uso

### Exemplo de uso:

```python
from gif_downloader import GifDownloader

# Parâmetros de configuração
keyword = "cats"
download_path = "/path/to/download"
api_key = "sua_giphy_api_key"

# Inicializa e executa o download
downloader = GifDownloader(key_word=keyword, 
                           download_path=download_path, 
                           api_key=api_key, 
                           limit=5)
downloader.run()
```


### Configuração

A classe `GifDownloader` necessita dos seguintes parâmetros:

- `key_word`: Termo de busca (string).
- `download_path`: Diretório de destino para salvar os GIFs.
- `api_key`: Sua chave de API do Giphy.
- `limit`: Quantidade máxima de GIFs para baixar (padrão: 5).


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues.
