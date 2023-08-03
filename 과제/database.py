import pymysql
from flask import Flask, render_template
from dotenv import load_dotenv
import os
#import timer

load_dotenv()

sensor_db = pymysql.connect(
    user = os.environ['DATABASE_USERNAME'], 
    passwd = os.environ['DATABASE_PASSWORD'], 
    host = os.environ['DATABASE_HOST'], 
    db = os.environ['DATABASE_DATABASE'], 
    charset = 'utf8'
)

#cursor = sensor_db.cursor(pymysql.cursors.DictCursor)
cursor = sensor_db.cursor()

sql = "SELECT * FROM posts"


cursor.execute(sql)


data_list = cursor.fetchall()


#Flask 객체 인스턴스 생성
app = Flask(__name__)

@app.route('/') # 접속하는 url
def index():
    
    sql = "SELECT * from posts"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    
    
    return render_template('myWeb.html',data_list=data_list)
    
if __name__=="__main__":
    #app.run(debug=True)
    # host 등을 직접 지정하고 싶다면
    app.run(host="0.0.0.0", port="3000", debug=True)