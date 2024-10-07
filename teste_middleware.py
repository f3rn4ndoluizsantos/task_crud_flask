from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a custom middleware decorator
def my_middleware(func):
    def wrapper(*args, **kwargs):
        # Pre-processing logic
        print("Before processing the route")
        # Call the original function
        response = func(*args, **kwargs)
        # Post-processing logic
        print("After processing the route")
        return response
    return wrapper

@app.route('/specific', methods=['GET'])
@my_middleware
def specific_route():
    return jsonify(message="This is a specific route.")

@app.route('/another', methods=['GET'])
def another_route():
    return jsonify(message="This is another route.")

if __name__ == '__main__':
    app.run()
