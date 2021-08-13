from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    personal_info = {
        'blood_type': 'O',
        'height': 180,
        'mbti': 'INTJ'
    }

    foods = ['라면', '소고기', '탕수육']
    return render_template('index.html', name='Donghun Lee', age=20, info=personal_info, foods = foods)

if __name__ == '__main__':
    app.run(debug=True)