import os
import time
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

api_url = os.environ.get('APIURL')
if api_url is None:
    api_url = "http://localhost/"
else:
    api_url = "http://" + api_url + "/"

def get_data_and_log():
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # 응답 코드가 200 이외의 경우 예외 발생
        logging.info(response.text)
    except requests.exceptions.RequestException as e:
        logging.error(f"Error occurred while fetching data: {e}")

if __name__ == "__main__":
    while True:
        get_data_and_log()
        time.sleep(10)  # 10초 대기 후 다음 요청 수행
