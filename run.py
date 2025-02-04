# run.py
from app import create_app  # Import the create_app function from app/__init__.py

app = create_app()  # Create the Flask application instance

if __name__ == "__main__":
    app.run(debug=True)  # Run the app in debug mode
