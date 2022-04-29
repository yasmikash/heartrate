from flask import Flask, jsonify, request
import numpy as np

# Model librabries
from models.heartrate.lib.HeartRateDetector import HeartRateDetector

app = Flask(__name__)

# Keep the model initialization only at the startup
heartrate_detector = HeartRateDetector(
    sampling_rate=250,
    stride=250,
    threshold=0.05,
)

@app.route("/heartrate", methods=["POST"])
def home():
    request_data = request.json
    heartrate_signal = np.array(request_data["readings"])
    peaks = heartrate_detector.find_peaks(heartrate_signal)
    response = {
        "beats": len(peaks[0].tolist())
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)