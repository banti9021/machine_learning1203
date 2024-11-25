from flask import Flask
from src.machine_learning1.logger import logging
from src.machine_learning1.exception import CustomException
import os,sys

app=Flask(__name__,)
@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("we testing")
    except Exception  as e:
        ml=CustomException(e,sys)
        logging.info(ml.error_message)
        logging.info("we testing")

        return "we"


if __name__=="__main__":
    app.run(debug=True)