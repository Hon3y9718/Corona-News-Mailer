import bs4, requests, lxml
import smtplib, ssl, schedule
from time import sleep

class CoronaVirusNews():
    def __init__(self):
        self.res = requests.get('https://www.worldometers.info/coronavirus/country/india/')
        self.soup = bs4.BeautifulSoup(self.res.text, 'lxml')
        self.tag = self.soup.find_all('div', id = 'maincounter-wrap')
        for i in self.tag:
            if 'Cases' in i.get_text():
                self.Cases = i.get_text()
            elif 'Recovered' in i.get_text():
                self.Recovered = i.get_text()
            elif 'Deaths' in i.get_text():
                self.Deaths = i.get_text()

    def Display(self):
        print(self.Cases, self.Recovered, self.Deaths)

    def Send_Email(self):
        Server = smtplib.SMTP('smtp.gmail.com', 587)
        Server.ehlo()
        Server.starttls(context=ssl.create_default_context())
        Server.ehlo()

        Server.login('uk481281@gmail.com', 'Hon3y.me2000')

        Subject = 'Daily Corona Updates in India!'
        body = f'Today in India \n{self.Cases}\n{self.Recovered}\n{self.Deaths}\nCheck the link : https://www.worldometers.info/coronavirus/country/india/'
        msg = f'Subject: {Subject}\n\n{body}'

        Server.sendmail('CoronaVirus', 'umeshkumar.80244@gmail.com', msg)
        print('EmailSent')
        Server.quit()

job = CoronaVirusNews()
job.Display()

def Job():
    job.Send_Email()

schedule.every().day.at('09:00').do(Job)

while True:
    schedule.run_pending()
    sleep(1)
