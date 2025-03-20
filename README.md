# Simple Task API

Uma API REST simples para gerenciamento de tarefas construída com Flask.

## Funcionalidades

- Criar, ler, atualizar e deletar tarefas (CRUD completo)
- Filtragem de tarefas por status (completas/incompletas)
- Persistência de dados em arquivo JSON
- Suporte a CORS para integração com frontend

## Requisitos

- Python 3.6+
- Flask
- Flask-CORS

## Instalação

1. Clone este repositório:
```bash
https://github.com/Qualificando/API-REST-com-Flask
cd simple-task-api
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como usar

1. Inicie o servidor:
```bash
python app.py
```

2. O servidor estará rodando em `http://localhost:5000`

## Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET    | /tasks   | Listar todas as tarefas |
| POST   | /tasks   | Criar uma nova tarefa |
| GET    | /tasks/{id} | Obter detalhes de uma tarefa específica |
| PUT    | /tasks/{id} | Atualizar uma tarefa |
| DELETE | /tasks/{id} | Deletar uma tarefa |
| GET    | /tasks/status/{true\|false} | Filtrar tarefas por status |

## Exemplo de Uso

### Criar uma tarefa
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar Python", "description": "Aprender Flask e APIs REST"}'
```

### Listar todas as tarefas
```bash
curl http://localhost:5000/tasks
```

### Atualizar uma tarefa (marcar como completa)
```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Estudar Python", "description": "Aprender Flask e APIs REST", "completed": true}'
```

## Estrutura do Projeto
```
simple-task-api/
├── app.py           # Arquivo principal da aplicação
├── tasks.json       # Arquivo de armazenamento de dados
├── requirements.txt # Dependências do projeto
├── LICENSE          # Licença MIT
└── README.md        # Este arquivo
```

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
