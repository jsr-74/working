from flask import Flask, render_template, request
import urllib.parse

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    qr_url = None

    # Read data from GET parameters
    upi = request.args.get("upi")
    name = request.args.get("name")
    amount = request.args.get("amount")

    if upi and name and amount:
        # Create UPI string
        upi_data = f"upi://pay?pa={upi}&pn={name}&am={amount}&cu=INR"
        upi_encoded = urllib.parse.quote(upi_data)  # Encode for URL

        api = "https://api.qrserver.com/v1/create-qr-code/"
        qr_url = f"{api}?data={upi_encoded}&size=300x300"

    return render_template("index.html", qr_url=qr_url)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)