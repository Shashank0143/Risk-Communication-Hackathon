from flask import Flask, request
import dill
from requests import get

app = Flask(__name__)

@app.route('/',methods=['POST'])
def foo():
    sender = request.form.to_dict()['data'][25:38]      #25 to 38 signifies the length of a phone number with 234, example; 2348033880659
    reply(sender)
    print("This is awesome")
    return "dope"

def reply(sender):
    url = "https://panel.apiwha.com/send_message.php"
    querystring = {"apikey":"LLRFNP1BRVGDDUM6R1KW","number":sender,"text":"Your query is acknowledged, you would get an answer shortly"}
    get(url, params=querystring)

if __name__ == '__main__':
   app.run()

"""
The next time you are working on this, change the ngroc url on the whatsapp service apiwha
"""