import smtplib
import ssl
import logging
import requests
from bs4 import BeautifulSoup

url = ["https://www.amazon.in/Apple-iPhone-15-128-GB/dp/B0CHX1W1XY/",
       "https://www.amazon.in/Apple-iPhone-Plus-128GB-Starlight/dp/B0BDJFTGK6/",
       "https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4?pid=MOBGTAGPTB3VS24W&lid=LSTMOBGTAGPTB3VS24WVZNSC6&marketplace=FLIPKART&q=iphone+15&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_1_8_na_na_na&fm=search-autosuggest&iid=c0f297c7-3aec-41d0-9da8-40a52832b1ed.MOBGTAGPTB3VS24W.SEARCH&ppt=sp&ppn=sp&ssid=hdtmipn9s00000001723967692730&qH=2f54b45b321e3ae5",
       "https://www.flipkart.com/apple-iphone-14-starlight-128-gb/p/itm3485a56f6e676"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,en;q=0.8",
}


def send_email(subject, body, to_email):
    port = 465  # For SSL
    password = "ppjv tfqu wrmh pmnk"
    email = "smarthomie780@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(email, password)
        server.sendmail(
            email,
            to_email,
            f"Subject: {subject}\n\n{body}"
        )


def fetch_price():
    logging.basicConfig(
        filename='../logs/iphone_price_log.txt',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    response = requests.get(url[0], headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        try:
            price = soup.find("span", {"class": "a-price-whole"}).text.strip()
            price1 = int(float(price.replace(",", "")))
            print(f"Price on Amazon iphone15: Rs. {price}")
            if price1 < 75000:
                send_email("Price Alert!!!", f"Price on Amazon iphone15 is below Rs. 75000", "karmadebjit@gmail.com")
                logging.info(f"Price on Amazon iphone15 is Rs. {price1} within budget")
            else:
                print("Price on Amazon iphone15 is not Rs. 75000")
                logging.info("Overpriced!!!")
        except AttributeError as e:
            logging.error(f'Could not find the price on the page: {str(e)}')
            print("Could not find the price on the page")
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)

    response = requests.get(url[1], headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        try:
            price = soup.find("span", {"class": "a-price-whole"}).text.strip()
            price1 = int(float(price.replace("₹", "").replace(",", "").replace("Rs.", "")))
            print(f"Price on Amazon iphone14: Rs. {price}")
            if price1 <= 60000:
                send_email("Price Alert!!!", f"Price on Amazon iphone14 is below Rs. 60000", "karmadebjit@gmail.com")
                logging.info(f"Price on Amazon iphone14 is Rs. {price1} within budget")
            else:
                print("Price on Amazon iphone14 is not Rs. 60000")
                logging.info("Overpriced!!!")
        except AttributeError:
            logging.error(f'Could not find the price on the page: {str(e)}')
            print("Could not find the price on the page.")

    response = requests.get(url[2], headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        try:
            price = soup.find("div", {"class": "Nx9bqj CxhGGd"}).text.strip()
            price1 = int(float(price.replace("₹", "").replace(",", "")))
            print(f"Price on Flipkart Iphone15: {price}")
            if int(price1) <= 70000:
                send_email("Price Alert!!!", f"Price on Flipkart iphone15 is below Rs. 75000", "karmadebjit@gmail.com")
                logging.info(f"Price on Flipkart iphone15 is Rs. {price1} within budget")
            else:
                print("Price on Flipkart iphone15 is not Rs. 75000")
                logging.info("Overpriced!!!")
        except AttributeError:
            logging.error(f'Could not find the price on the page: {str(e)}')
            print("Could not find the price on the page.")

    response = requests.get(url[3], headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "lxml")
        try:
            price = soup.find("div", {"class": "Nx9bqj CxhGGd"}).text.strip()
            price1 = int(float(price.replace("₹", "").replace(",", "")))
            print(f"Price on Flipkart Iphone14: {price}")
            if price1 < 60000:
                send_email("Price Alert!!!", f"Price on Flipkart iphone14 is below Rs. 60000", "karmadebjit@gmail.com")
                logging.info(f"Price on Flipkart iphone14 is Rs. {price1} within budget")
            else:
                print("Price on Flipkart iphone14 is not Rs. 60000")
                logging.info("Overpriced!!!")
        except AttributeError:
            logging.error(f'Could not find the price on the page: {str(e)}')
            print("Could not find the price on the page.")


if __name__ == '__main__':
    fetch_price()
