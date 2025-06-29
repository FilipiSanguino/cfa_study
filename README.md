# CFA Study Tracker

Aplicação simples em Python para acompanhar os estudos do CFA Level 3.

## Uso (CLI)

```bash
# Adicionar um novo tópico
python tracker.py add "Fixed Income"

# Marcar um tópico como concluído
python tracker.py complete "Fixed Income"

# Listar tópicos cadastrados
python tracker.py list
```

Os dados são armazenados no arquivo `study_data.json`. Para alterar o local do arquivo, defina a variável de ambiente `STUDY_DATA_FILE`.

## Uso (Web)

Instale o Flask e execute o servidor:

```bash
pip install flask
python webapp.py
```

Acesse `http://localhost:5000` para gerenciar os tópicos em uma interface simples baseada em Bulma.
