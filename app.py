from flask import Flask, request, jsonify
import os

app = Flask(__name__)

PROGRAMS_DIR = 'programs'

@app.route('/add_program', methods=['POST'])
def add_program():
    data = request.get_json()
    program_name = data.get('programName')
    program_content = data.get('programContent')

    if not program_name or not program_content:
        return jsonify({'success': False, 'message': 'Invalid input'}), 400

    program_file = os.path.join(PROGRAMS_DIR, program_name)
    try:
        os.makedirs(PROGRAMS_DIR, exist_ok=True)
        with open(program_file, 'w') as file:
            file.write(program_content)
        
        index_file = 'index.html'
        with open(index_file, 'a') as file:
            file.write(f'<a href="{program_name}">{program_name}</a>\n')
        
        return jsonify({'success': True})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
