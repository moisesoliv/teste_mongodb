# MongoDB + Flask = <3

Codigo desenvolvido para ser um gerenciador de noticias de um blog em python utilizando flask e o banco de dados MongoDB.

O programa deve receber requisições responsáveis por criar, editar, excluir e exectar buscas na base de dados.

Para executar o programa primeiro devemos instalar as dependências `pip install -r requirements.txt` e executar utilizando o comando `python app.py`

Cada uma das requisições é listada a seguir:

# buscar todos os artigos

Retorna um json com todas as noticias cadastradas.

**URL** : `/articles/`

**Método** : `GET`

## buscar um artigo específico pelo ID

Retorna somente a noticia com id = <article_id>

**URL** : `/article/<article_id>`

**Método** : `GET`

## Adicionar um artigo

Adiciona um novo artigo à base de dados.
Todos os campos são obrigatórios e o campo texto é ilimitado.

**URL** : `/articles`

**Método** : `POST`

**Exemplo de dados**
```json
{
    "title": "titulo", 
    "text": "texto",
    "author": "moises"
}
```

## Editar um artigo

Edita um artigo na base de dados.
é preciso fazer uma busca na base para encontrar a ID a ser editada e adicionad à URL.

**URL** : `/articles/<article_id>`

**Método** : `PUT`

**Exemplo de dados**
```json
{
    "title": "titulo edited", 
    "text": "texto edited",
    "author": "moises edited"
}
```
## Excluir um artigo pelo ID

Exclui o artigo com id = <article_id>

**URL** : `/article/<article_id>`

**Método** : `DELETE`

## Buscar um artigo por palavra chave
Retorna todos os artigos que contenham a palavra buscada(<keyword>).
A busca é feita nos campos título, texto e autor.

**URL** : `/article/<keyword>`

**Método** : `GET`
