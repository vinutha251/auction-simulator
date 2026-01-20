from flask import Flask, render_template, request
from auction_simulator import Bidder, english_auction, first_price_sealed_bid, second_price_auction
import io
import sys

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        # Read all bidder names and values as lists
        names = request.form.getlist("name")
        values = request.form.getlist("value")

        # Build list of Bidder objects
        bidders = []
        for n, v in zip(names, values):
            if n.strip() and v.strip():
                bidders.append(Bidder(n.strip(), int(v)))

        # Check if any bidder exists
        if not bidders:
            result = "No bidders provided!"
        else:
            # Capture auction output
            buffer = io.StringIO()
            sys.stdout = buffer

            auction_type = request.form.get("auction_type")
            if auction_type == "english":
                english_auction(bidders)
            elif auction_type == "first_price":
                first_price_sealed_bid(bidders)
            elif auction_type == "second_price":
                second_price_auction(bidders)

            sys.stdout = sys.__stdout__
            result = buffer.getvalue()

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
