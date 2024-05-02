import requests
from flask import Flask
from user_agent import generate_user_agent   
app = Flask(name)       
@app.route("/hotmail=<hot>")
def hotmail(hot):
    email = hot
    try:
        r = requests.post('https://signup.live.com', headers={
            'user-agent': generate_user_agent(),
        })
        mc = r.cookies.get_dict()['amsc']
        ca = r.text.split('Canary')[4].split('","ip":"')[0].split('":"')[1].encode("ascii").decode("unicode_escape").encode("ascii").decode("unicode_escape").encode("ascii").decode("ascii")
        cookies = {
            'amsc': mc,
        }
        headers = {
            'authority': 'signup.live.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'canary': ca,
            'user-agent': generate_user_agent(),
        }

        json_data = {
            'signInName': email,
        }
        res = requests.post(
            'https://signup.live.com/API/CheckAvailableSigninNames',
            cookies=cookies,
            headers=headers,
            json=json_data,
        ).text
        if '"isAvailable":true' in res:
            return {'status': 'Available', 'Dev : @Bpv_4'}
        else:
            return {'status': 'UnAvailable', 'Dev : @Bpv_4'}
    except:
        return {'status': 'Erorr', 'Dev : @Bpv_4'}
if name == "main":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)