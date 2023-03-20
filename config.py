from flask import Flask

app = Flask(__name__)

# Буфер недавних ссылок
recent_images = []
