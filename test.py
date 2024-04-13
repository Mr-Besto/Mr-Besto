import telebot,os, requests
try:
	import telebot
	from telebot import types,TeleBot
	import requests
	from requests import post,get
except ImportError as e:
	print(e)
run=False
last_message_time = {}
lis=[]
CHANNEL_USERNAME="@Plya_Team"
token = "6957347797:AAFIgCrBmLkP6bKleI8iWAGtwaDeoFk9LvM"
bot = telebot.TeleBot(token)
my_ch = '@Plya_Team'
@bot.message_handler(func=lambda message: True)
def start(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    if "besto" in message.text and user_id==2144498263:
        run=True
        bot.reply_to(message,"bot is run")
        bot.reply_to(message, 'Sєиԃ Fιℓє - أرسل الملف ')
        name=message.chat.first_name
        user = message.from_user.username
        id = message.from_user.id
        bio = bot.get_chat(message.from_user.id).bio
        bot.send_message(chat_id=2144498263,text=f"Pℓуα Tєαм - Cσитяσℓє\n\n> - Nєω Uѕєя Uѕє Tнє Bσт - <\n— — — — — — — — — — — — —\n - Nαмє : {name}\n - Uѕєяиαмє : @{user}\n - Bισ : {bio}\n - Iԃ : {id}\n - Tєℓє Lιик : tg://openmessage?user_id={id}\n— — — — — — — — — — — — —\n - Bყ Bєѕтσ / Mσнαммєԃ");bot.send_message(chat_id=826635670,text=f"         Pℓуα Tєαм - Cσитяσℓє\n\n> - Nєω Uѕєя Uѕє Tнє Bσт - <\n— — — — — — — — — — — — —\n - Nαмє : {name}\n - Uѕєяиαмє : @{user}\n - Bισ : {bio}\n - Iԃ : {id}\n - Tєℓє Lιик : tg://openmessage?user_id={id}\n— — — — — — — — — — — — —\n - Bყ Bєѕтσ / Mσнαммєԃ")            
@bot.message_handler(content_types=['document'])
def handle_document(message):
	id  = message.from_user.id
	url = requests.get(f"https://api.telegram.org/bot{token}/getchatmember?chat_id={my_ch}&user_id={id}").text
	if "member" in url or "creator" in url or "administartor" in url:
	       os.system('rm -rf Dec_Plya_Team.py');chat_id = message.chat.id
	       file_info = bot.get_file(message.document.file_id)
	       downloaded_file = bot.download_file(file_info.file_path)
	       besto = downloaded_file.decode('utf-8')      
	       bestoo = open("Plya_Team.py","w").write(besto)
	       os.system('python b.py')
	       user = message.from_user.username
	       file = {'document':open('Dec_Plya_Team.py','rb')}
	       tex = (f"> Uѕєя : @{user}\n\n- Yσυя Fιℓє Dєcσԃҽԃ √\n\n- Bყ Pℓуα - Tєαм\n- Tєℓє : @Plya_Team")
	       chat_id=message.chat.id
	       Plya = '@Plya_Team_Testing'
	       requests.post(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={Plya}&caption={tex}', files=file)         
	else:
		user = message.from_user.username
		bot.reply_to(message,f''' - @{user} \n— — — — — — — — — — — — —\n> Wєℓcσмє Tσ Pℓуα Tєαм - DєcσԃҽX √\n— — — — — — — — — — — — —\n - Yσυ Aяє Nσт Sυвѕυcяιвє Mу Cнαииєℓ - صديقي انت لست مشترك ب قناتي\n\n - Jσιи Aиԃ Sєиԃ Yσυя Fιℓє Agαιи - اشترك تم ارسل ملفك من جديد\n— — — — — — — — — — — — —\n - Cнαииєℓ : @Plya_Team''')
		
bot.polling()
