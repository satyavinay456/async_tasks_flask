# async_tasks_flask

prerequests:

Install the redis server in whathever machine you use:

sudo apt-get install redis-server

sudo systemctl enable redis-server.service

# Install the required modules for this web app
=>pip3 install -r requirements.txt

run the below command to complete asynchronous jobs in reddis server(worker):

rq worker

In the root directory execute these commands:

export FLASK_APP=flaskr

export FLASK_ENV=development

Initialize db using => flask init-db

and then run the application using below command

flask run

# status
You can observe three status
1) In Queue : means the job is not submitted ( you have to start the worker using "rq worker" command)
2) running : means the job is submitted , but it is in process 
3) finished : means the job is successfully finished

