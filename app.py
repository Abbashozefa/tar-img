from flask import Flask,request,jsonify


app=Flask(__name__)


@app.route('/')
def get_service_name():
    return jsonify({'name':'AUSF_NEWIMG'})


if __name__=='__main__':
    app.run()

