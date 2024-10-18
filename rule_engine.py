class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.node_type = node_type
        self.value = value
        self.left = left
        self.right = right

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








