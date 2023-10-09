from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')

def work():
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)