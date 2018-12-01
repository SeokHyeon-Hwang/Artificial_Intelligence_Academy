# -*- coding: utf-8 -*-


from flask import Flask
from flask import request
from flask import jsonify
from flask import json

app = Flask(__name__)

@app.route("/keyboard")
def keyboard():
    return jsonify(type='text')

@app.route('/message', methods=['POST'])
def message():
    data = json.loads(request.data)
    content = data['content']
    if content == '5000':
        text1 = '한식, 중식, 일식 중에 고르세요.'

    elif content == '10000':
        text1 = '한식, 중식, 일식 중에 고르세요.'

    elif content == '15000':
        text1 = '한식, 중식, 일식 중에 고르세요.'
    
    else:
        text1 = '5000, 10000, 15000 중에서 입력하세요.'


    response = {
        "message" : { 
        "text": text1
         
        }
        }
    response = json.dumps(response, ensure_ascii=False)
#    response2 = json.dumps(response2, ensure_ascii=False)
    return response #, response2        

'''        
@app.route('/message', methods=['POST'])
def message2():
    data2 = json.loads(request.data2)
    content2 = data2['content2']
    
    if content2 == str('한식'):
        food1 = '된장찌개'
    elif content2 == str('중식'):
        food1 = '짜장면'
    elif content2 == str('일식'):
        food1 = '라멘'
    else:
        food1 = '한식, 중식, 일식 중에 고르세요.'

    response2 = {
        "message2" : { 
        "food": food1
         
        }
        }
'''

    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=600)