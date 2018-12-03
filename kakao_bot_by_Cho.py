# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 10:01:39 2018

@author: ktm
"""

from flask import Flask
from flask import request
from flask import jsonify
from flask import json
import random

app = Flask(__name__)

# 7000원 이상 메뉴 리스트
rice7 = ["순두부찌개!", "김치찌개!", "순대국밥!", "매운갈비찜!", "연어초밥!"]
noodle7 = ["쌀국수!", "냉면!", "칼국수!", "까르보나라!"]
bread7 = ["함바그!", "피자!", "수제버거!", "돈까스!"]

# 7000원 미만 메뉴 리스트
rice6 = ["김밥?", "삼각김밥?", "돌솥비빔밥?", "한솥도시락?"]
noodle6 = ["쫄면?", "떡볶이?", "컵라면?", "잔치국수?"]
bread6 = ["써브웨이?", "뚜레쥬르?", "파리바게트?", "아티장베이커스?"]


@app.route("/keyboard")
def keyboard():
    response = {
        "type" : "buttons",
        "buttons" : ["7천원 이상", "7천원 미만"]
    }
    response = json.dumps(response, ensure_ascii=False)
    return response

@app.route("/message", methods=["POST"])
def message():
    data = json.loads(request.data)
    content = data["content"]
    if content == "처음으로 돌아가기":
        text = "예산이 7천원 이상? 미만?"
        url = "https://t1.daumcdn.net/cfile/tistory/221DDD4B53A7EFCF25"
        response = {
	      "message": {
	        "text": text,
	        "photo": {
	          "url": url,
	          "width": 640,
	          "height": 480
	        },
	        "message_button": {
	          "label": "더 알고 싶으면?",
	          "url": "https://ko.wiktionary.org/wiki/분류:한국어_음식"
	        }
	      },
	      "keyboard": {
	        "type": "buttons",
	        "buttons": [
	          "7천원 이상",
	          "7천원 미만"
	        ]
	      }
	    }
	
    elif content in ("7천원 이상", "밥!", "면!", "빵!"):
        if content == "7천원 이상":
            text = "7천원 이상인 경우만 보여드립니다"
            url = "https://t1.daumcdn.net/cfile/tistory/221DDD4B53A7EFCF25"
        elif content == "밥!":
            text = random.choice(rice7)
            url = "http://misstwinkle.co.kr/web/goods/0091_07.jpg"
        elif content == "면!":
            text = random.choice(noodle7)
            url = "http://image.aafood.co.kr/image/upload/jy/7iwfkc8c/ywli1485941447869.jpg"
        elif content == "빵!":
            text = random.choice(bread7)
            url = "http://image.aafood.co.kr/image/upload/pm/8acjweos/b7131432027899947.jpg"

        response = {
            "message": {
            "text": text,
            "photo": {
            "url": url,
            "width": 640,
            "height": 480
            },
            "message_button": {
            "label": "이게 별로라면?",
            "url": "https://www.mangoplate.com/top_lists/1896_eatdealbest5"
              }
            },
        "keyboard": {
          "type": "buttons",
          "buttons": [
          "밥!",
          "면!",
          "빵!",
          "처음으로 돌아가기"
	        ]
	      }
	    }

    else:
        if content == "7천원 미만":
            text = "7천원 미만인 경우만 보여드립니다"
            url = "https://t1.daumcdn.net/cfile/tistory/221DDD4B53A7EFCF25"
        elif content == "밥?":
            text = random.choice(rice6)
            url = "https://img.insight.co.kr/static/2016/11/12/700/G6Y1179I5ZD4I7N7D57H.jpg"
        elif content == "면?":
            text = random.choice(noodle6)
            url = "https://t1.daumcdn.net/cfile/tistory/2376D84856C6A33830"
        elif content == "빵?":
            text = random.choice(bread6)
            url = "http://gdimg.gmarket.co.kr/799899532/still/600?ver=1524208331"

        response = {
            "message": {
            "text": text,
            "photo": {
            "url": url,
            "width": 640,
            "height": 480
            },
            "message_button": {
            "label": "아직 모르겠다면?",
            "url": "https://www.mangoplate.com/mango_picks/856"
              }
            },
        "keyboard": {
          "type": "buttons",
          "buttons": [
          "밥?",
          "면?",
          "빵?",
          "처음으로 돌아가기"
	        ]
	      }
	    }

    response = json.dumps(response, ensure_ascii=False)
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # app.run(host="localhost", port=80)
    # flask 예시 : app.run(host="0.0.0.0", port=5000)