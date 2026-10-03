import os 
 
from dotenv import load_dotenv 
from flask import Flask, jsonify, request 
 
from app.calculator import profit, total_sales 
from app.logger import get_logger 
 
load_dotenv()  # read the secret recipe from .env 
 
SHOP_NAME = os.getenv("SHOP_NAME", "My Lemonade Stand") 
PRICE = float(os.getenv("PRICE_PER_CUP", "20")) 
COST = float(os.getenv("COST_PER_CUP", "8")) 
 
log = get_logger("lemonade") 
app = Flask(__name__) 
 
 
@app.route("/") 
def home(): 
    log.info("Someone visited the home page") 
    return f"<h1>Welcome to {SHOP_NAME}!</h1><p>Try <a href='/sell?cups=5'>/sell?cups=5</a></p>" 
 
 
@app.route("/sell") 
def sell(): 
    cups_text = request.args.get("cups", "0") 
    try: 
        cups = int(cups_text) 
        result = { 
            "shop": SHOP_NAME, 
            "cups": cups, 
            "sales": total_sales(cups, PRICE), 
            "profit": profit(cups, PRICE, COST), 
        } 
        log.info(f"Sold {cups} cups, profit {result['profit']}") 
        return jsonify(result) 
    except ValueError as error: 
        log.warning(f"Bad input '{cups_text}': {error}") 
        return jsonify({"error": f"'{cups_text}' is not a valid number of cups"}), 400 
    except Exception: 
        log.exception("Something unexpected broke") 
        return jsonify({"error": "Oops! Something went wrong"}), 500 
 
 
if __name__ == "__main__": 
    port = int(os.getenv("PORT", "5000")) 
    log.info(f"{SHOP_NAME} is open on port {port}") 
    app.run(host="0.0.0.0", port=port)