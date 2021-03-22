from factory import create_app

if __name__ == "__main__":
    app = create_app("db.db")
    app.run(debug=True, ssl_context="adhoc")
