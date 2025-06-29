import json
import os
import importlib


def test_add_and_complete(tmp_path, capsys):
    data_file = tmp_path / 'data.json'
    os.environ['STUDY_DATA_FILE'] = str(data_file)
    tracker = importlib.import_module('tracker')

    tracker.add_task('Ethics')
    tracker.list_tasks()
    out = capsys.readouterr().out
    assert 'Ethics' in out
    assert '[✗]' in out

    tracker.complete_task('Ethics')
    tracker.list_tasks()
    out = capsys.readouterr().out
    assert '[✓]' in out

    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert data['Ethics'] is True
