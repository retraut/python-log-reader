from flask import Flask, render_template, request
import os
app = Flask(__name__)


# Port
port = os.getenv('PORT')
log_file = os.getenv('LOG_FILE')

# Initialize the current line number as a global variable
current_line_number = 0

# Read the code file (change the path to your file)
with open(log_file, 'r') as file:
    code_lines = file.readlines()
    max_code_lines = len(code_lines)

@app.route('/')
def display_code():
    global current_line_number

    # Determine the range of lines to display (100 lines at a time)
    if current_line_number > 0:
        start_line = current_line_number
        end_line = current_line_number + 100
        current_code = '\n'.join(code_lines[start_line:end_line])
    else:
        current_code = '\n'.join(code_lines[-100:])
    return render_template('code.html', code=current_code, current_line_number=current_line_number)

@app.route('/next')
def next_lines():
    global current_line_number
    current_line_number += 100
    if current_line_number >= max_code_lines:
       message = "the end of file, see the last 100 strings"
       current_line_number = max_code_lines - 100
    return display_code()

@app.route('/previous')
def previous_lines():
    global current_line_number
    current_line_number -= 100
    if current_line_number < 0:
        current_line_number = 0
    return display_code()

@app.route('/end')
def to_the_end():
    global current_line_number
    global max_code_lines
    current_line_number = max_code_lines - 100
    return display_code()

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=port)
