# Aula de API com Flask
Este repositorio foi criado para dar uma introdução ao Flask, criando uma API simples para introdução dos Alunos aos conceitos de API e  MicroServiço

## Estrutura do Projeto

```
/
├── microFlask.py
└── Readme.md
```

## Configuração e Execução

1. **Instalar Dependências**: Certifique-se de que você tem o Flask instalado. Você pode instalar o Flask usando `pip`:

```sh
pip install Flask
```

2. **Rodar a API**: Navegue até o diretório onde o arquivo `microFlask.py` está localizado e execute o seguinte comando para iniciar o servidor Flask:

```sh
python microFlask.py
```

3. **Acessar a API**: A API estará disponível em `http://127.0.0.1:5000`.

## Endpoints

### Listar Todos os Produtos

- **URL**: `/produtos`
- **Método**: `GET`
- **Descrição**: Retorna uma lista de todos os produtos.
- **Exemplo de `curl`**:
  ```sh
  curl -X GET http://127.0.0.1:5000/produtos
  ```

### Obter Detalhes de um Produto

- **URL**: `/produtos/<int:produto_id>`
- **Método**: `GET`
- **Descrição**: Retorna os detalhes de um produto específico.
- **Exemplo de `curl`**:
  ```sh
  curl -X GET http://127.0.0.1:5000/produtos/1
  ```

## Propósito

Esta API foi desenvolvida para fins educacionais, como parte de uma aula de introdução a microserviços utilizando Flask. Ela demonstra como criar endpoints simples para listar e obter detalhes de produtos.

```
Sinta-se à vontade para modificar e expandir esta API conforme necessário para atender aos requisitos da sua aula ou projeto.
```
