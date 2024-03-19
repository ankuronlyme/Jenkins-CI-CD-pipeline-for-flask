from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! My Jenkins CI/CD pipeline for flask application.'

if __name__ == '__main__':
    app.run(debug=True)
