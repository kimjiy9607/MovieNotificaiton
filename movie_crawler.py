import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = '1093019925:AAFk7CcBa2uqEuR8yz0ndSQvAU0jB5tz6_c')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theaterCode=0074&date=20200317'

def job_function():
	html = requests.get(url)
	soup = BeautifulSoup(html.text, 'html.parser')
	imax = soup.select_one('span.imax')
	if(imax):
		imax = imax.find_parent('div', class_='col-times')
		title = imax.select_one('div.info-movie > a > strong').text.strip()
		bot.sendMessage(chat_id=1067964999, text=title + 'IMAX is now available.')
		sced.pause()
		#print(title + 'IMAX is now available.')
#	else:
#		bot.sendMessage(chat_id=1067964999, text='IMAX is not available.')
		#print('IMAX is not available.')


sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()
