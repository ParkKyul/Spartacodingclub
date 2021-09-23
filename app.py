from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/review', methods=['POST', 'GET'])
def write_review():
    if request.method == "POST":
        title_receive = request.form['title_give']
        author_receive = request.form['author_give']
        review_receive = request.form['review_give']
        doc = {
            'title': title_receive,
            'author': author_receive,
            'review': review_receive
        }
        db.bookreview.insert_one(doc)
        return jsonify({'result': 'success', 'msg': '완료 예아'})

    elif request.method == "GET":
        reviews = list(db.bookreview.find({}, {'_id': False}))
        return jsonify({'all_reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
