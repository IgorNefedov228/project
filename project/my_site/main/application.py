
from Flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        return f'Имя: {name}, Email: {email}'
    return '''
        <form method="POST">
            <label for="name">Имя:</label>
            <input type="text" id="name" name="name" required>
            <label for="email">Электронная почта:</label>
            <input type="email" id="email" name="email" required>
            <input type="submit" value="Отправить">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
