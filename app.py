from flask import Flask
from threading import Thread
import requests
from requests import post as pp
from user_agent import generate_user_agent as gg
from random import choice as cc
from random import randrange as rr
import re
import os

Besto_H = 'azertyuiopmlkjhgfdsqwxcvbn'
app = Flask(__name__)

@app.route("/email=<email>")
def Gmail(email):
    try:
        n1 = ''.join(cc(Besto_H) for i in range(rr(6, 9)))
        n2 = ''.join(cc(Besto_H) for i in range(rr(3, 9)))
        host = ''.join(cc(Besto_H) for i in range(rr(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-YE,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
            "sec-ch-ua-arch": "\"\"",
            "sec-ch-ua-bitness": "\"\"",
            "sec-ch-ua-full-version": "\"116.0.5845.72\"",
            "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-model": "\"ANY-LX2\"",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-ch-ua-platform-version": "\"13.0.0\"",
            "sec-ch-ua-wow64": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
            "x-client-data": "CJjbygE=",
            "x-same-domain": "1",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            'user-agent': str(gg()),
        }

        res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {'__Host-GAPS': host}
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
            'user-agent': gg(),
        }
        data = {
            'f.req': '["' + tok + '","' + n1 + '","' + n2 + '","' + n1 + '","' + n2 + '",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = pp(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        
        if '@' in email:
            email = str(email).split('@')[0]

            cookies = {'__Host-GAPS': host}
            headers = {
                'authority': 'accounts.google.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'google-accounts-xsrf': '1',
                'origin': 'https://accounts.google.com',
                'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL=' + tl,
                'user-agent': gg(),
            }
            params = {'TL': tl}
            data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A' + tl + '%22%2C%22' + email + '%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
            response = pp(
                'https://accounts.google.com/_/signup/usernameavailability',
                params=params,
                cookies=cookies,
                headers=headers,
                data=data,
            )
            if '"gf.uar",1' in response.text:
                return {'Good': 'Gmail', 'Dev > @Bpv_4'}
            elif '"gf.uar",2' in response.text:
                return {'Bad': 'Gmail', 'Dev > @Bpv_4'}
            elif '"er",null,null,null,null,400' in str(response.text):
                return {'status': 'Erorr', 'Dev > @Bpv_4'}
            else:
                return {'status': 'Erorr', 'Dev > @Bpv_4'}
    except:
    	return {'status': 'Error', 'Dev > @Bpv_4'}
    	pass
    	
                
def run():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

  
def keep_alive():
  t = Thread(target=run)
  t.start()
  
if __name__ == "__main__":
	keep_alive()