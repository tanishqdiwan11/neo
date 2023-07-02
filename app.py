from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    # Run the neofetch command and capture its output
    output = subprocess.check_output(['neofetch', '--stdout'])

    # Convert the output to a string and pass it to the template
    return render_template('index.html', system_info=output.decode('utf-8'))

if __name__ == '__main__':
    app.run()
