from flask import Flask, abort, request
import json
import func

app= Flask(__name__)

app.debug = False

@app.route('/received', methods = ['POST'])
def add_earnings():
    if not request.json:
        abort(400)
    
    data = {
        'received': float(request.json['received']),
        'n_childs': int(request.json['n_childs']),
        'apply_iva': bool(request.json['apply_iva']),
        'age_of_childs': list(request.json['age_of_childs'])
    }

app.run(host='localhost', port=2556, debug=False)