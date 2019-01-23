from flask import Flask, jsonify
app = Flask(__name__)
#app.run(debug=True)
stores = [{
    'name': 'My Store',
    'items': [{'name':'my item', 'price': 15.99 }]
}]


@app.route('/')
def index():
    jsinData = {
                'ddddd' : '1',
                'ffffff' : '2',
                }
    return jsonify(jsinData)

@app.route('/hello')
def hello():
    return jsonify(stores)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

if __name__ == '__main__': 
    app.run(debug=True)  # important to mention debug=True
