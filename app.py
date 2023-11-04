from flask import Flask, render_template, request
app = Flask(__name__)


# Port
port = os.getenv('PORT')
file = os.getenv('LOG_FILE')

# Initialize the current line number as a global variable
current_line_number = 0

@app.route('/')
def display_code():
    global current_line_number

    # Read the code file (change the path to your file)
    with open('/var/logs/keybagd.log.0', 'r') as file:
        code_lines = file.readlines()

    # Determine the range of lines to display (100 lines at a time)
    start_line = current_line_number
    end_line = current_line_number + 100
    current_code = '\n'.join(code_lines[start_line:end_line])

    return render_template('code.html', code=current_code)

@app.route('/next')
def next_lines():
    global current_line_number
    current_line_number += 100
    return display_code()

@app.route('/previous')
def previous_lines():
    global current_line_number
    current_line_number -= 100
    if current_line_number < 0:
        current_line_number = 0
    return display_code()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=port)
