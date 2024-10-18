import unittest
from rule_engine import create_rule, evaluate_rule, combine_rules

class TestRuleEngine(unittest.TestCase):
    
    def test_create_individual_rule(self):
        rule_string = "(age > 30 AND department == 'Sales')"
        ast = create_rule(rule_string)
        self.assertEqual(ast.value, "AND")
        self.assertEqual(ast.left.node_type, "operand")
        self.assertEqual(ast.left.value, "age > 30")
        self.assertEqual(ast.right.node_type, "operand")
        self.assertEqual(ast.right.value, "department == 'Sales'")
    
    def test_combine_rules(self):
        rule1 = "(age > 30 AND department == 'Sales')"
        rule2 = "(salary > 50000 OR experience > 5)"
        combined_ast = combine_rules([rule1, rule2])
        self.assertEqual(combined_ast.value, "AND")
        self.assertEqual(combined_ast.left.value, "AND")
        self.assertEqual(combined_ast.right.value, "OR")
    
    def test_evaluate_rule_scenarios(self):
        rule_string = "(age > 30 AND department == 'Sales')"
        rule_ast = create_rule(rule_string)
        data1 = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        result1 = evaluate_rule(rule_ast, data1)
        self.assertTrue(result1)
        data2 = {"age": 25, "department": "Sales", "salary": 60000, "experience": 3}
        result2 = evaluate_rule(rule_ast, data2)
        self.assertFalse(result2)
        data3 = {"age": 35, "department": "Marketing", "salary": 60000, "experience": 3}
        result3 = evaluate_rule(rule_ast, data3)
        self.assertFalse(result3)

    def test_combining_additional_rules(self):
        rule1 = "(age > 30 AND department == 'Sales')"
        rule2 = "(salary > 50000 OR experience > 5)"
        combined_ast = combine_rules([rule1, rule2])
        data1 = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        result1 = evaluate_rule(combined_ast, data1)
        self.assertTrue(result1)
        data2 = {"age": 35, "department": "Sales", "salary": 40000, "experience": 2}
        result2 = evaluate_rule(combined_ast, data2)
        self.assertFalse(result2)
        data3 = {"age": 25, "department": "Marketing", "salary": 70000, "experience": 6}
        result3 = evaluate_rule(combined_ast, data3)
        self.assertFalse(result3)

if __name__ == '__main__':
    unittest.main()
