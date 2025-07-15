<h2>API_Workstation</h2>
<br>
<div>
<b>This project provides an API service that allows users to have a look at work of basic API</b>
<br><br>
<h6>API can:</h6>
<ul>

<li>Returns data in both HTML and JSON formats.</li>
<li>Integrates with a PostgreSQL database.</li>
<li>Keep you informed about forecast :partly_sunny:</li>
</ul>
</div>
<br>
:sparkles:<b>Tech Stack</b>:sparkles:<br>
FastApi, PostgreSQL, Docker, Docker-Compose, Nginx
<hr> 
<div>
<h3>Docker Deploy</h3>

```commandline
git clone https://github.com/735Andrew/API_Workstation    
```
<br>
Create a <b>.env</b> file in the root directory with the following variables: <br>
<b>/API_Workstation/.env</b>

```commandline 
POSTGRES_USER = <USER_VARIABLE>
POSTGRES_PASSWORD = <PASSWORD_VARIABLE>
POSTGRES_DB = <DB_VARIABLE>
POSTGRESQL_DATABASE_URL = postgresql://<USER_VARIABLE>:<PASSWORD_VARIABLE>@db:5432/<DB_VARIABLE>
```
<br>
Open a terminal in the root directory and run the following command: 

```commandline
docker-compose up -d 
```
</div>
<hr>
<h3>Work example of API</h3>

```bash
cd API_Workstation
python3 -m venv venv 
venv\Scripts\activate 
(venv) pip install -r requirements.txt
(venv) python 
>>> import requests as r
>>>
>>> response = r.get("http://localhost:80/list")
>>> response.text
"[(1, 'London', 20), (2, 'Paris', 10)]"
>>>
>>> data = {"city":"Moscow","temperature":30}
>>> response = r.post("http://localhost:80/forecast", json=data)
>>> respose.json()
{'success': 'Forecast has been added.'}
>>>
>>> response = r.get("http://localhost:80/list")
>>> response.text
"[(1, 'London', 20), (2, 'Paris', 10), (3, 'Moscow', 30)]"
```