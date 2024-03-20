from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/calculate", methods=["POST"])
def calculate():
    now_num = float(request.form["name"])
    date = request.form["date1"]

    # Define a dictionary to store the annual inflation rates for each year
    annual_inflation_rates = {
        "2018": 33.8343,
        "2019": -22.4046,
        "2020": 49.943,
        "2021": 44.5261,
        "2022": 33.965,
        "2023": 32.017
    }

    # Calculate the cumulative inflation rate for the selected year
    years = list(annual_inflation_rates.keys())
    years = sorted(annual_inflation_rates.keys(), reverse=True)  # Sort years in descending order
    inflation_rate = 0
    for year in years:
        inflation_rate += annual_inflation_rates[year]
        if year == date:
            break

    # Calculate future value using the formula (consider error handling)
    try:
        # Calculate future value
        future_value = now_num * (1 + inflation_rate / 100)

        # Extract and format the decimal part
        future_value_decimal = f"{future_value:.2f}"  # Format to two decimal places

    except ZeroDivisionError:
        future_value_decimal = "Error: Inflation rate cannot be zero."
    except ValueError:
        future_value_decimal = "Error: Invalid input. Please enter a valid number."
    except TypeError:
        future_value_decimal = "Error: Invalid year. Please select a valid year."
    return render_template('index.html', result=future_value_decimal)

if __name__ == "__main__":
    app.run(debug=True)
