from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule, sanitize_data
from flask_limiter import Limiter
from flask_caching import Cache

app = Flask(__name__)

# Set up rate limiting and caching
limiter = Limiter(app, key_func=lambda: request.remote_addr)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

rules = []  # List to store created rules
combined_rule_ast = None  # For storing the combined AST

# Home route
@app.route('/')
def home():
    return "Welcome to the Rule Engine!"

# Create individual rules
@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule')
    rule_ast = create_rule(rule_string)
    rules.append(rule_ast)
    return jsonify({"message": "Rule created", "ast": str(rule_ast)})

# Combine multiple rules
@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    global combined_rule_ast
    combined_rule_ast = combine_rules([str(rule) for rule in rules])
    return jsonify({"message": "Rules combined", "ast": str(combined_rule_ast)})

# Evaluate combined rules (cached for 60 seconds)
@cache.cached(timeout=60)
@app.route('/evaluate_rule', methods=['POST'])
@limiter.limit("10 per minute")
def evaluate_rule_api():
    global combined_rule_ast
    data = request.json
    sanitize_data(data)  # Sanitize the input data
    result = evaluate_rule(combined_rule_ast, data)
    return jsonify({"result": result})

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
