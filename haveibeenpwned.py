import requests
from dotenv import load_dotenv
import os
import time
import csv
import datetime
from bs4 import BeautifulSoup

class HaveIBeenPwned:
    def __init__(self):
        self.API_KEY = os.environ.get('HAVE_I_BEEN_PWNED_API_KEY')
        self.mailservers = ['gmx.at', 'gmx.de', 'gmx.net', 'gmail.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'yahoo.com', 'yahoo.de', 'web.de', 'mail.ru', 'magenta.de', 't-mobile.de', 'vodafone.de', 'vodafonemail.de', 'aol.at', 'aon.at', 'aol.de', 'a1.at', 'drei.at', 'magenta', 'kabelplus.at', 'kabsi.at', 'bnet.at', 'liwest.at', 'upc.at', 'mail.de']

    def get_email_combinations(self, email_address):
        username = email_address.split('@')[0]
        combinations = [email_address]
        combinations.extend([f'{username}@{mailserver}' for mailserver in self.mailservers])
        if '.' in email_address:
            new_username = username.split('.')[0][0] + '.' + username.split('.')[1]
            combinations.extend([f'{new_username}@{mailserver}' for mailserver in self.mailservers])
        return combinations
    
    def check_for_breaches(self, email_address):
        url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{email_address}?truncateResponse=false'
        headers = {'hibp-api-key': self.API_KEY}
        while True:
            response = requests.get(url, headers=headers)
            time.sleep(5/6)
            if response.status_code == 429:
                print('[-] Rate limit exceeded. Retrying in 1 seconds.')
                time.sleep(1)
            break
        

        results = []
        if response.status_code == 200:
            for breach in response.json():
                results.append({
                    'Email': email_address,
                    'Name': breach['Name'],
                    'Domain': breach['Domain'],
                    'BreachDate': breach['BreachDate'],
                    'Description': BeautifulSoup(breach['Description'], 'html.parser').text,
                    'Data': ', '.join(breach['DataClasses']),
                    'Verified': breach['IsVerified'],
                    'Sensitive': breach['IsSensitive']
                })
        return results

if __name__ == '__main__':
    load_dotenv()
    service = HaveIBeenPwned()
    filename = input('Enter the name of the CSV file containing the email addresses: ')
    reader = csv.reader(open(filename, 'r'))
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H%M%S')
    writer = csv.DictWriter(open(f'results-{time_now}.csv', 'a+'), fieldnames=['Email', 'Name', 'Domain', 'BreachDate', 'Description', 'Data', 'Verified', 'Sensitive'])
    writer.writeheader()

    def process_email(email_address):
        email_combinations = service.get_email_combinations(email_address)
        for email in email_combinations:
            results = service.check_for_breaches(email)
            print(email, results)
            writer.writerows(results)

    n = 0
    for row in reader:
        process_email(row[0])