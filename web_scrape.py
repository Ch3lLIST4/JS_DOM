import requests
import bs4

def print_menu():
	print('='*30)
	print('''
This is a Web Scraping Program


Where do you want me to extract data?
1. R6 Tracker
2. Facebook
3. Youtube
4. Let me decide the URL

5. Quit
		''')
	print('='*30)


def extract_data_r6_Tracker():
	char_name = input('Enter target character_name:')
	if char_name=='':
		char_name = 'BigSadDolan'

	res = requests.get('https://r6.tracker.network/profile/pc/'+char_name)

	soup = bs4.BeautifulSoup(res.text, 'lxml')

	defstat_name = soup.findAll("div", {"class": "trn-defstat__name"})
	defstat_value = soup.findAll("div", {"class": "trn-defstat__value"})

	for name,value in zip(defstat_name,defstat_value):
		line = '{}:{}'.format(name.getText(), value.getText())
		print(line.strip())


def extract_data_Facebook():
	username = input("Enter user's profile username: ")
	if username=='':
		username = 'hoangtv1204'

	res = requests.get('https://facebook.com/'+ username + '/')

	soup = bs4.BeautifulSoup(res.text, 'lxml')


def extract_data_Youtube():
	username = input("Enter user's profile username: ")
	if username=='':
		username = 'chelgaming'

	res = requests.get('https://facebook.com/'+ username + '/')

	soup = bs4.BeautifulSoup(res.text, 'lxml')


def extract_data_custom():
	url = input("Enter the url you want to extract the data from: ")

	res = requests.get(url)

	soup = bs4.BeautifulSoup(res.text, 'lxml')


def main():	
	key_input = 'Y'
	while (key_input == 'y' or key_input == 'Y'):
		print_menu()

		option = input('Choose one of the above:').strip()

		if(option == '1'):
			extract_data_r6_Tracker()
		elif(option == '2'):
			extract_data_Facebook()
		elif(option == '3'):
			extract_data_Youtube()
		elif(option == '4'):
			extract_data_custom()
		else:
			break

		key_input = input('Do you wanna continue? (Y/N)')

	print('Exiting the Program!!!')


if __name__ == "__main__":
    main()

