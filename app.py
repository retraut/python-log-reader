from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Port
port = os.getenv('PORT')
log_file = os.getenv('LOG_FILE')

# Initialize the current page number and lines per page as global variables
current_page_number = 1
lines_per_page = 100

@app.route('/')
@app.route('/page/<int:page_number>')
def display_code(page_number=1):
    global current_page_number
    current_page_number = page_number

    # Read the code file (change the path to your file)
    with open(log_file, 'r') as file:
        code_lines = file.readlines()

    # Determine the range of lines to display based on the current page
    start_line = (current_page_number - 1) * lines_per_page
    end_line = start_line + lines_per_page
    current_code = '\n'.join(code_lines[start_line:end_line])

    return render_template('code.html', code=current_code, current_page_number=current_page_number)

@app.route('/next')
def next_lines():
    global current_page_number
    current_page_number += 1
    return redirect(url_for('display_code', page_number=current_page_number))

@app.route('/previous')
def previous_lines():
    global current_page_number
    current_page_number = max(1, current_page_number - 1)
    return redirect(url_for('display_code', page_number=current_page_number))

@app.route('/end')
def to_the_end():
    global current_page_number
    with open(log_file, 'r') as file:
        code_lines = file.readlines()
        max_pages = (len(code_lines) - 1) // lines_per_page + 1
    current_page_number = max_pages
    return redirect(url_for('display_code', page_number=current_page_number))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)
