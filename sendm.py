import smtplib
import re
import urllib.request

def connectionon():
	
	r1=get_status('http://google.com')
	r2 = get_status('http://yahoo.com')
	if r1 and r2:
		return True
	else:
		return False

def get_status(url):
	try:
		r=urllib.request.urlopen(url).code
		if r in (200,302):
			return True
		else:
			return False
	except:
		return False
def normalize(url):	
	if not re.match('^http[s]?://',url):
		url = 'http://' + url
	return url
	
def email_alert(text):
	sender = 'sender@domain.com'
	receiver = 'receiver@domain.com'
	message = '''
	From: sender
	To: receiver
	Subject: SITE STATUS

	''' + text
	try:
		#gmail uses port 587 with tls
		server = smtplib.SMTP('smtp.domain.com',587)
		server.starttls()
		server.login(sender,'PASSWORD')
		server.sendmail(sender,receiver,message)
		server.quit()
	except smtplib.SMTPException:
		print("error")
def test(url):
	url2 = normalize(url)
	if connectionon():
		if get_status(url2):
			print("Site is up")
		else:
			print("Site is down")
			email_alert(url + " is down")
	else:
		print("Please Check Your INTERNET Connection!")


test('https://www.google.co.in/')