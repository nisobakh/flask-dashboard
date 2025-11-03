# Flask Dashboard
# Minimal web dashboard displaying sample product metrics

from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Flask Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f9f9f9; margin: 40px; }
        h1 { color: #333; }
        table { border-collapse: collapse; width: 60%; margin-top: 20px; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background-color: #eee; }
    </style>
</head>
<body>
    <h1>Product Metrics Dashboard</h1>
    <table>
        <tr><th>Metric</th><th>Value</th></tr>
        {% for metric, value in metrics.items() %}
        <tr><td>{{ metric }}</td><td>{{ value }}</td></tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route("/")
def dashboard():
    metrics = {
        "Active Users": 1340,
        "Monthly Revenue ($)": 24800,
        "Retention Rate (%)": 87,
        "Avg. Session Duration (min)": 4.3
    }
    return render_template_string(TEMPLATE, metrics=metrics)

if __name__ == "__main__":
    app.run(debug=True)
