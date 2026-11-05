import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    target_zip = request.args.get("zip", "81123")
    target_loc = request.args.get("loc", "San Luis Valley / Blanca Corridor")
    return f'''
    <div style="font-family: monospace; background: #0a0a0a; color: #0f0; padding: 25px; min-height: 90vh;">
        <div style="border: 2px solid #0f0; padding: 15px; background: #111; margin-bottom: 20px;">
            <h2 style="margin: 0; color: #0f0;">[D2 / D3 / D5: UNIFIED SALES MOCK BOARD]</h2>
            <p style="margin: 5px 0 0 0; color: #ff0;"><b>Target Zone:</b> {target_loc} (ZIP: {target_zip})</p>
        </div>
        <h3>Active Prospect Presentation Views:</h3>
        <ul style="line-height: 1.8;">
            <li><b>D2 Mock:</b> Spatial Lead Marketplace & Hazard Volume Preview</li>
            <li><b>D3 Mock:</b> Field Trial Queue & 3-Lead Preview for ZIP {target_zip}</li>
            <li><b>D5 Mock:</b> Estimator & Neighbor Scan Preview</li>
        </ul>
        <p><i>Append <code>?zip=XXXXX&loc=CityName</code> to dynamically control this board live on a call.</i></p>
    </div>
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
