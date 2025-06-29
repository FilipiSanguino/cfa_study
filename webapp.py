from flask import Flask, request, redirect, url_for, render_template_string
import tracker

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
<head>
  <meta charset='utf-8'>
  <title>CFA Study Tracker</title>
  <link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bulma@0.9.4/css/bulma.min.css'>
</head>
<body class='section'>
  <div class='container'>
    <h1 class='title'>CFA Study Tracker</h1>
    <form action='{{ url_for('add') }}' method='post' class='field has-addons'>
      <div class='control is-expanded'>
        <input name='topic' class='input' type='text' placeholder='Novo tópico'>
      </div>
      <div class='control'>
        <button type='submit' class='button is-primary'>Adicionar</button>
      </div>
    </form>
    <ul>
      {% for topic, done in tasks.items() %}
      <li class='mb-2'>
        {% if done %}
          <span class='tag is-success mr-2'>Concluído</span> {{ topic }}
        {% else %}
          <form action='{{ url_for('complete') }}' method='post' class='is-inline mr-2'>
            <input type='hidden' name='topic' value='{{ topic }}'>
            <button class='button is-small is-info'>Concluir</button>
          </form>
          {{ topic }}
        {% endif %}
      </li>
      {% else %}
      <li>Nenhum tópico cadastrado.</li>
      {% endfor %}
    </ul>
  </div>
</body>
</html>
"""

@app.route('/')
def index():
    tasks = tracker.load_data()
    return render_template_string(TEMPLATE, tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    topic = request.form.get('topic', '').strip()
    if topic:
        tasks = tracker.load_data()
        if topic not in tasks:
            tasks[topic] = False
            tracker.save_data(tasks)
    return redirect(url_for('index'))

@app.route('/complete', methods=['POST'])
def complete():
    topic = request.form.get('topic')
    tasks = tracker.load_data()
    if topic in tasks:
        tasks[topic] = True
        tracker.save_data(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
