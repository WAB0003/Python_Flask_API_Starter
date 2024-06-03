from flask import Flask, request, make_response, jsonify, session
from flask_cors import CORS

from config import app
from models import Coordinate

CORS(app)

# CREATE ROUTES
@app.route('/coordinates', methods=['GET'])
def trajectories():
    if request.method == 'GET':
               # return jsonify([trajectory.to_dict() for trajectory in all_trajectories])
        return make_response([coord.to_dict() for coord in Coordinate.query.all()])



if __name__ == '__main__':
    app.run(port=5555)