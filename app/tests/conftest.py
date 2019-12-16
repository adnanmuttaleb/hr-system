import io
import random
import pytest

from .. import create_app, db
from ..models import Candidate


@pytest.fixture(scope='session')
def test_client():

    flask_app = create_app('test_config.py')
    testing_client = flask_app.test_client()
 
    ctx = flask_app.app_context()
    ctx.push()
 
    yield testing_client
 
    ctx.pop()


@pytest.fixture(scope='session')
def init_db():
    db.create_all()
    yield db  
    db.drop_all()


@pytest.fixture
def department():
    return {
        "name": 'IT',
    }

@pytest.fixture
def candidate():
    return {
        "name": random.choice(("salem", "ad", "moh", "khaled", "raed")),
        "birth_date": "12/3/1970",
        "years_of_exp": 20,
        "department": 1
    }


@pytest.fixture
def resume():
    return (io.BytesIO(b"Senior Software developer"), 'resume.pdf')

@pytest.fixture
def sorted_candidates(test_client, init_db):
    return  Candidate.get_candidates()
    