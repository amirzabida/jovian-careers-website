print('hello')
from flask import Flask
app=Flask(__name__)
@app.route("/")
def hello_world():
  return "Hello, Amir Zabida"

#print(__name__)
#if __name__ == '__main__':
#  print("I am inside the if now")
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

