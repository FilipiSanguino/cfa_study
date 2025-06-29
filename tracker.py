import json
import argparse
from pathlib import Path
import os

DATA_FILE = Path(os.environ.get('STUDY_DATA_FILE', 'study_data.json'))

def load_data():
    if DATA_FILE.exists():
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_task(topic):
    data = load_data()
    if topic in data:
        print(f'Tópico "{topic}" já existe.')
        return
    data[topic] = False
    save_data(data)
    print(f'Tópico "{topic}" adicionado.')

def complete_task(topic):
    data = load_data()
    if topic not in data:
        print(f'Tópico "{topic}" não encontrado.')
        return
    data[topic] = True
    save_data(data)
    print(f'Tópico "{topic}" marcado como concluído.')

def list_tasks():
    data = load_data()
    if not data:
        print('Nenhum tópico cadastrado.')
        return
    for topic, done in data.items():
        status = '✓' if done else '✗'
        print(f'[{status}] {topic}')

def main():
    parser = argparse.ArgumentParser(description='Acompanhe seus estudos para o CFA Level 3.')
    subparsers = parser.add_subparsers(dest='command')

    add_p = subparsers.add_parser('add', help='Adicionar um novo tópico')
    add_p.add_argument('topic', help='Nome do tópico a ser adicionado')

    comp_p = subparsers.add_parser('complete', help='Marcar um tópico como concluído')
    comp_p.add_argument('topic', help='Nome do tópico a ser marcado')

    subparsers.add_parser('list', help='Listar tópicos')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.topic)
    elif args.command == 'complete':
        complete_task(args.topic)
    elif args.command == 'list':
        list_tasks()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
