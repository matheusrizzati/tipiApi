from flask import Flask, jsonify, request
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
excel_file_path = os.path.join(BASE_DIR, 'tipi.xlsx')

CORS(app)

@app.route('/')
def search():
    df = pd.read_excel(excel_file_path)
    df = df.dropna(subset=['ALIQUOTA'])

    ncm = request.args.get('ncm')
    
    if ncm:
        result = df.loc[df['NCM'] == ncm].to_dict(orient='records')
    else:
        result = df.to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)