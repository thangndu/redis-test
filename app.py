#!/usr/bin/env python3
import os
import redis
import json
from flask import Flask

if 'VCAP_SERVICES' in os.environ:
    VCAP_SERVICES = json.loads(os.environ['VCAP_SERVICES'])
    CREDENTIALS = VCAP_SERVICES["rediscloud"][0]["credentials"]
    r = redis.Redis(host=CREDENTIALS["hostname"], port=CREDENTIALS["port"], password=CREDENTIALS["password"])


app = Flask(__name__)

@app.route('/')
def mainmenu():

    text = r.get("redis-key")
    
    response = """
    <html>
        <body>
            <h1>{TEXT}</h1>
            <br>
            <img src="static/piper.png">
        </body>
    </html>
    """.format(TEXT=text)

    return response

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
