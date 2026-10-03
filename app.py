from flask import Flask, jsonify, render_template_string

# Initialize the Flask application
app = Flask(__name__)

# Define the template directly for simplicity
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Python App</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        .container { border: 1px solid #ccc; padding: 20px; display: inline-block; border-radius: 8px; }
        h1 { color: #333; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Welcome to Your Python App!</h1>
        <p>This application is running successfully using Flask.</p>
        <a href="/api/status">Check API Status</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    """Renders the main home page."""
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/status')
def status():
    """Returns a simple JSON response tracking system status."""
    return jsonify({
        "status": "healthy",
"message": "The application backend is healthy and running from the merged branch!",git add app.py
git commit -m "Resolve merge conflict between main and feature branch"
git push

if __name__ == '__main__':
    # Run the application locally on port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
