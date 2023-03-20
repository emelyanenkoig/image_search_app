from src.functions import get_data

from config import app


@app.route("/static")
def main():
    return get_data()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
