from flask import Flask, render_template,Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/requirements/')
def requirements():
    with open('requirements.txt', 'r') as file:
        content = file.read()
        content_with_newline = content + '\n'
        return Response(content_with_newline, mimetype='text/plain')






if __name__ == '__main__':
    app.run(debug=True)