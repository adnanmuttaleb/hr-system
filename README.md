# HR

Describtion of setup and usage of HR System.

## Usage
This system has the following resources:

1. `...candidates/` with *POST* and *GET* endpoints. 
2. `...departments/` with *POST* and *GET* endpoints. 
3. `...resume/<candidate_id>` with *POST* and *GET* endpoints. 

For complete example:

1. Perform *POST* `...departments/` with `{"name": "IT"}` as payload and `X-ADMIN=1` as header.
2. Perform *POST* `...candidates/` with `{"name": "khaled", "birth_date": "12/3/1970", "years_of_exp": 10, "department": 1}` as payload.
3. Perform *POST* `...resume/1` with a file atteched.

---

## Setup

You need to have `mariaDB` installed and running on port 5100 (you can change the port number from `config.py`). 

First you have to install the requirements:

`pip install -r requirements.txt`

Then you have to do the migrations:

`flask db upgrade`

Now you can run the application:

`flask run`

to run the tests:

`pytest app/tests`



## Customization

In order to support 








