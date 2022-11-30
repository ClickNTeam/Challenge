from flask import Flask, render_template, jsonify, request, redirect
from flask_cors import CORS

from git_challangers.Challenge_louay66.search import find_item_list_l
from git_challangers.Challenge_cryptolake.api import preprocess
from git_challangers.Challenge_cryptolake.itemsgraph import ItemsGraph


app = Flask(__name__)


@app.route('/challange', strict_slashes=False, methods=['GET'])
def Challange():
    name = ""
    return_list = []

    return render_template('list.html', name=name, return_list=return_list)



@app.route('/challange/louay66', strict_slashes=False, methods=['GET', 'POST'])
def louay66():
    name = "louay66"
    return_list = []
    if request.method == "POST":
        return_list = find_item_list_l(request.form["id"])
        return render_template('challangel.html', name=name, return_list=return_list)
    return render_template('challangel.html', name=name, return_list=return_list)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000')
