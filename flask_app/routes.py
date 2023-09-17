from flask import Flask, request, jsonify
from flask_cors import cross_origin, CORS
from fi_calculator import FICalculator

app = Flask(__name__, static_url_path='')
cors = CORS(app, resources={r'/*': {"origins": '*'}})

fi_calc = FICalculator()

@app.route('/get_personal_details', methods=["GET"])
def get_personal_details():
    personal_details = fi_calc.get_personal_details()

    return jsonify({"status": "success", "msg": "Personal details fetched", "data": personal_details})

@app.route('/set_personal_details', methods=["POST"])
def set_personal_details():
    current_age = request.form.get("current_age")
    fi_age = request.form.get("fi_age")
    lifespan = request.form.get("lifespan")
    
    status = fi_calc.get_personal_details()
    if status == -1:
        return jsonify({'status': 'failed', 'msg': 'Personal details could not be updated'})
    else:
        return jsonify({'status': 'success', 'msg': 'Personal details updated'})

@app.route('/get_market_expectations', methods=["GET"])
def get_market_expectations():
    market_expectations = fi_calc.get_market_expectations()

    return jsonify({"status": "success", "msg": "Personal details fetched", "data": market_expectations})

@app.route('/set_market_expectations', methods=["POST"])
def set_market_expectations():
    inflation = request.form.get("inflation")
    asset_classes = eval(request.form.get("asset_classes"))
    
    status = fi_calc.set_market_expectations(inflation, asset_classes)
    if status == -1:
        return jsonify({'status': 'failed', 'msg': 'Market expectations could not be updated'})
    else:
        return jsonify({'status': 'success', 'msg': 'Market expectations updated'})