# HR

Description of setup and usage of HR System.

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

You need to have `mariaDB` installed and running on port `5100` (you can change the port number from `config.py`). 


1. First you have to install the requirements:

`pip install -r requirements.txt`

2. Set app's name env. variable:

`export FLASK_APP=app`

3. Then you have to do the migrations:

`flask db upgrade`

4. Now you can run the application:

`flask run`

To run the test cases just run the following command:

`pytest app/tests`


## Customization

In order to support new File Storage options you need first to inherit from `FileHandler` class:


```
class FileHandler():
    def save():
        raise NotImplementedError()
    def retrieve():
        raise NotImplementedError()
```

```
class CustomFileHandler(FileHandler):
    def save(file, file_name):
        ...
    def retrieve(file_name):
        ...
```

Then in `config.py` override FILE_HANDLER variable:

`FILE_HANDLER = locate('path to..CutomeFileHandler')`






