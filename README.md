# Rule Engine with Abstract Syntax Tree (AST)

## Overview

This project implements a **Rule Engine** using an **Abstract Syntax Tree (AST)** to represent and evaluate user-defined rules. The engine allows the creation, combination, and evaluation of dynamic rules based on attributes such as age, department, income, and other user data.

### Features:
- **Create and Evaluate Rules**: Define rules as strings and convert them into an AST for structured evaluation.
- **Combine Multiple Rules**: Combine rules using logical operators (`AND`, `OR`).
- **Real-Time Evaluation**: Dynamically evaluate rules against incoming data.
- **Modular Design**: The core logic is in `rule_engine.py` for easy extensibility and maintenance.

## Project Structure

```
rule-engine/
├── src/
│   ├── rule_engine.py        # Core rule engine logic for AST generation, combination, and evaluation
├── tests/
│   ├── test_rule_engine.py   # Unit tests for rule engine
├── Dockerfile                # Dockerfile for containerized setup
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── ...
```

## Installation

### Prerequisites:
- **Python 3.9+**
- **Docker** (for containerized execution)

### Steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/diomate/rule-engine.git
   cd rule-engine
   ```

2. **Install dependencies**:
   Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   You can run the application directly with:
   ```bash
   python3 src/app.py
   ```

4. **Run with Docker (Optional)**:
   You can also run the application inside a Docker container:
   
   ```bash
   docker build -t rule-engine .
   docker run -it -p 8090:5000 rule-engine
   ```

   Access the application at:
   ```
   http://localhost:8090
   ```

## Usage

### Creating and Combining Rules:
Use the provided `create_rule` and `combine_rules` functions to generate and combine rules:

1. **Create Rule**:
   ```python
   from src.rule_engine import create_rule
   rule = "(age > 30 AND department == 'Sales')"
   ast = create_rule(rule)
   ```

2. **Combine Rules**:
   ```python
   from src.rule_engine import combine_rules
   rule1 = "(age > 30 AND department == 'Sales')"
   rule2 = "(salary > 50000 OR experience > 5)"
   combined_ast = combine_rules([rule1, rule2])
   ```

3. **Evaluate Rule**:
   ```python
   from src.rule_engine import evaluate_rule
   data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
   result = evaluate_rule(combined_ast, data)
   print(result)  # True or False
   ```

## Testing

The project includes unit tests to ensure the correctness of the rule engine.

1. **Run Tests**:
   Use `unittest` to run all tests:
   ```bash
   python3 -m unittest discover tests
   ```

2. **Test Coverage**:
   - Rule creation and AST generation.
   - Rule combination with logical operators.
   - Rule evaluation against different user data.

## Dependencies

The project requires the following dependencies:

- **Flask** (for the web server)
- **pytest** (for testing)
- Any other dependencies listed in `requirements.txt`.

You can install these using:
```bash
pip install -r requirements.txt
```

## Future Enhancements

- **Support for more complex conditions**: Add support for `NOT` operators or nested conditions.
- **Improved Error Handling**: Add better error handling for invalid rule formats or missing attributes in the evaluation data.
- **User-defined Functions**: Allow users to define custom functions that can be used in rules.

## Non-Functional Enhancements

### Security Enhancements

- **Input Validation**: User inputs, such as rule strings and evaluation data, are validated to prevent injection attacks and invalid formats.
- **Rate Limiting**: To protect the application from abuse, API requests are limited to 10 per minute per IP address using Flask-Limiter.
- **Data Sanitization**: Inputs are sanitized before being processed to ensure safety from malicious data or injection attacks.

### Performance Optimizations
- **Caching**: Frequently evaluated rules are cached to reduce redundant calculations, improving the overall performance.
- **Efficient Data Parsing**: Data parsing is optimized for handling large JSON inputs with minimal performance overhead.
- **Reuse of ASTs**: The Abstract Syntax Tree (AST) for frequently used rules is cached to prevent redundant calculations and improve speed.

### Deployment and Scalability

- **Docker Containerization**: The project is containerized using Docker, which makes deployment easier and ensures scalability across different environments.


## Conclusion

This project provides a flexible and dynamic **Rule Engine** using AST for decision-making based on user-defined conditions. It is easily extendable for real-world applications, such as user eligibility evaluations, business logic enforcement, or other rule-based systems.

