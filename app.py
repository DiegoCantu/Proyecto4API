from flask import Flask, request, jsonify
import predicciones_database

app = Flask(__name__)


@app.route('/predictions', methods=['POST'])
def predictions():
    return jsonify(predicciones_database.save_predictions(request.json.get('predicciones')))


@app.route('/prediction_id/<int:prediction_id>', methods=['GET'])
def prediction_by_id(prediction_id):
    return jsonify(predicciones_database.get_prediction_by_id(prediction_id))


@app.route('/predictions_date/<predictions_date>', methods=['GET'])
def predictions_by_date(predictions_date):
    return jsonify(predicciones_database.get_predictions_by_date(predictions_date))


if __name__ == '__main__':
    app.run()
