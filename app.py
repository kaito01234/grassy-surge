from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'current_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)