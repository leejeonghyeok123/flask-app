from flask import Flask , Blueprint , jsonify


app = Flask(__name__)

app_api = Blueprint('api_v1', __name__, url_prefix='/api/v1')


@app_api.route('/health')
def health():
    response_data = {'message': 'true'}
    return jsonify(response_data) , 200

if __name__ == '__main__':
    # 블루프린트 등록
    app.register_blueprint(app_api)
    app.run(host='0.0.0.0', port=5000, debug=True)