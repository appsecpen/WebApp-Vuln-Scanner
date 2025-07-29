from flask import Flask, render_template, request
from scanner import find_input_fields  # import your existing function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = ""
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            # Instead of printing, modify find_input_fields to return a string result
            results = find_input_fields(url)
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
