from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route('/<int:num>',methods= ['GET'] )
def square(num):
    return jsonify({'data':num**2})


if __name__=='__main__':
    app.run(host='0.0.0.0')
