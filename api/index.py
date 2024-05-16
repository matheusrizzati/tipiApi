from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def search():
    df = pd.read_excel('./tipi.xlsx')
    df = df.dropna(subset=['ALIQUOTA'])

    ncm = request.args.get('ncm')
    
    if ncm:
        result = df.loc[df['NCM'] == ncm].to_dict(orient='records')
    else:
        result = df.to_dict(orient='records')
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)