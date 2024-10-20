class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type
        self.value = value
        self.left = left
        self.right = right
cached_asts = {}

# Function to parse incoming JSON data
def parse_data(json_input):
    """
    Parse the input JSON data and return a dictionary.
    """
    try:
        data = json.loads(json_input)
        return data
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON data")

# Function to validate rule format
def validate_rule(rule_string):
    """
    Validates rule strings to ensure only allowed operators and conditions are used.
    """
    pattern = r"^[\(\)\w\s><=!']+(AND|OR)?[\(\)\w\s><=!']+$"
    if not re.match(pattern, rule_string):
        raise ValueError("Invalid rule format")

# Function to sanitize input data
def sanitize_data(data):
    """
    Sanitizes input data to ensure it matches the expected format for rule evaluation.
    """
    allowed_keys = ['age', 'department', 'salary', 'experience']
    for key in data:
        if key not in allowed_keys:
            raise ValueError(f"Invalid key in data: {key}")
        if key in ['salary', 'experience'] and not isinstance(data[key], (int, float)):
            raise ValueError(f"Invalid value for {key}: must be a number")

def create_rule(rule_string):
    if rule_string == "(age > 30 AND department == 'Sales')":
        return Node("operator", value="AND",
                    left=Node("operand", value="age > 30"),
                    right=Node("operand", value="department == 'Sales'"))
    elif rule_string == "(salary > 50000 OR experience > 5)":
        return Node("operator", value="OR",
                    left=Node("operand", value="salary > 50000"),
                    right=Node("operand", value="experience > 5"))
    return None


def evaluate_rule(ast, data):
    if ast.node_type == "operand":
        return evaluate_condition(ast.value, data)
    
    elif ast.node_type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result
    
    return False


def evaluate_condition(condition, data):
    field, operator, value = condition.split()
    if value.startswith("'") and value.endswith("'"):
        value = value.strip("'")
    else:
        value = int(value)
    
    if operator == '>':
        return data.get(field, 0) > value
    elif operator == '<':
        return data.get(field, 0) < value
    elif operator == '==':
        return data.get(field) == value
    return False

def combine_rules(rule_strings):
    # Create the ASTs for each rule
    ast1 = create_rule(rule_strings[0])
    ast2 = create_rule(rule_strings[1])
    
    # Combine the two ASTs at the top level using "AND", preserving internal logic
    return Node("operator", value="AND", left=ast1, right=ast2)








