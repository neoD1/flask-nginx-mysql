from app import app
import os
import mysql.connector
from typing import List, Dict
import json



def favorite_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'core2duo',
        'host': '192.168.1.5',
        'port': '3306',
        'database': 'erp'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    return "Hey"
    return json.dumps({'favorite_colors': favorite_colors()})



'''
@app.route("/")
def index():

    # Use os.getenv("key") to get environment variables
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!!!"

    return "Hello from Flask"

'''