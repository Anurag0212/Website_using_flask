from flask import Flask, render_template

app =Flask(__name__)

@app.route('/')
def Assignment1():
    return render_template('Assignment1.html')

@app.route('/Menu/')
def Menu():
    return render_template('Menu.html')

@app.route('/orderOnline/')
def orderOnline():
    return render_template('orderOnline.html')


@app.route('/about/')
def About_Us():
    return render_template('About_Us.html')

if __name__ == "__main__":
    app.run(debug=True)
