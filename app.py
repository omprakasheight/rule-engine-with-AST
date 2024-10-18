from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule

app = Flask(__name__)


rules = []
combined_rule_ast = None

@app.route('/create_rule', methods=['POST'])
def create_rule_api():
    rule_string = request.json.get('rule')
    rule_ast = create_rule(rule_string)
    rules.append(rule_ast)
    return jsonify({"message": "Rule created", "ast": str(rule_ast)})

@app.route('/combine_rules', methods=['POST'])
def combine_rules_api():
    global combined_rule_ast
    combined_rule_ast = combine_rules([str(rule) for rule in rules])
    return jsonify({"message": "Rules combined", "ast": str(combined_rule_ast)})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_api():
    global combined_rule_ast
    data = request.json
    result = evaluate_rule(combined_rule_ast, data)
    return jsonify({"result": result})

# if __name__ == '__main__':
#     app.run(debug=True)
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

@app.route('/')
def home():
    return "Welcome to the Rule Engine!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

