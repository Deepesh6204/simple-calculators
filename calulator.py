from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():

    result = "0"
    expression = ""

    if request.method == "POST":

        expression = request.form["expression"]
        operation = request.form["operation"]

        try:

            if operation == "sqrt":

                result = math.sqrt(float(expression))

            else:

                expression = expression.replace("×", "*")
                expression = expression.replace("÷", "/")

                result = eval(expression)

            if isinstance(result, float) and result.is_integer():
                result = int(result)

        except:

            result = "Error"

    return render_template(
        "index.html",
        result=result,
        expression=expression
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)