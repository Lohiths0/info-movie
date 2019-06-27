from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/namemovie/test', methods=['GET', 'POST'])
def moviePageDisplay():
    
    result = "invalid movie"
    if request.method == 'POST' or request.method == 'GET':
        result = request.form['nameMovie']
    
    return result




if __name__ == '__main__':
   app.run(debug = True)