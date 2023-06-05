#pip install mysql-connector-python
# mysql, 파이썬 연동 라이브러리
import mysql.connector
import requests
import json
import time

try:
  connector = mysql.connector.connect(
      host='localhost', 
      port ='3306', 
      user = 'root', 
      password = '1234', 
      database = 'practice'
  )
  # 커서객체는 데이터베이스에서 쿼리의 결과를 검색하고 순회하는데 사용되는 객체
  cursor = connector.cursor() # db정보를 다 가지고 있는 쿼리 객체

except mysql.connector.Error as err:
   print(err)

while True:
  url = "https://api.binance.com/api/v3/ticker/24hr"
  response = requests.get(url)
  data_json = json.loads(response.text)

  for a in data_json:
    if a['symbol'] == 'BTCUSDT':
        data = (a['symbol'],a['lastPrice'])
        add_data = "INSERT INTO coin_price (coin_name, last_price ) VALUES(%s, %s)"
  cursor.execute(add_data, data)
  connector.commit()
  time.sleep(10)    

cursor.close()
connector.close()

