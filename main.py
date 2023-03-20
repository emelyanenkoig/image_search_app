from src.functions import get_categories, get_list_of_links, remove_one_show, get_data
from flask import Flask, render_template
import random
from config import app


@app.route("/static")
def main():
    return get_data()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
