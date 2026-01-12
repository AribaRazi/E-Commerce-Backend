from flask import Flask,jsonify
from routes.product_routes import product_bp
from routes.order_routes import order_bp
from routes.user_routes import user_bp
from routes.payment_routes import payment_bp

app=Flask(__name__)

app.register_blueprint(product_bp)
app.register_blueprint(order_bp)
app.register_blueprint(user_bp)
app.register_blueprint(payment_bp)
@app.route("/")
def home():
    return {"message":"hello welcome to my e commerce backend"}
@app.route("/data")
def database():
    return {"hello data":"ariba razi"}

# global error handler

@app.errorhandler(Exception)
def handle_global_exception(error):
    return jsonify({
        "success": False,
        "data": None,
        "error": str(error)
    }), 500
if __name__ =="__main__":
    app.run(debug=True)
