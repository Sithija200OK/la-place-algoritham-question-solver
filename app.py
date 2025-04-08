from flask import Flask, render_template, request
import sympy as sp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    steps = None
    expression = ""
    transform_type = "laplace"

    if request.method == 'POST':
        expression = request.form.get('expression')
        transform_type = request.form.get('transform_type')

        try:
            # Declare symbols
            t, s = sp.symbols('t s')

            # Parse the input expression using sympy
            func = sp.sympify(expression)

            # Compute Laplace or Inverse Laplace Transform based on user choice
            if transform_type == "laplace":
                result = sp.laplace_transform(func, t, s)
                steps = f"Step-by-step calculation: {result}"
            elif transform_type == "inverse":
                result = sp.inverse_laplace_transform(func, s, t)
                steps = f"Step-by-step calculation: {result}"
        except Exception as e:
            result = f"Error in calculation: {e}"

    return render_template('index.html', result=result, steps=steps, expression=expression, transform_type=transform_type)

if __name__ == "__main__":
    app.run(debug=True)
