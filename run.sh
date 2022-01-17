VENV_DIR=venv
FLASK_APP=flaskapp
HOST_IP=0.0.0.0
PORT_NR=8080

. $VENV_DIR/bin/activate
export FLASK_APP=$FLASK_APP
flask run --host=$HOST_IP --port=$PORT_NR
