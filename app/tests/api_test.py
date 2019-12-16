import json
from datetime import datetime

def test_get_candidates_endpoint(test_client, init_db):
    response = test_client.get('candidates/')
    assert response.status_code == 403

    response = test_client.get('candidates/', headers={'X-ADMIN': 1})
    assert response.status_code == 200


def test_get_departments_endpoint(test_client, init_db):
    response = test_client.get('departments/')
    assert response.status_code == 200


def test_post_departments_endpoint(test_client, init_db, department):
    response = test_client.post('departments/', follow_redirects=True)
    assert response.status_code == 403

    response = test_client.post('departments/', json=department, follow_redirects=True, headers={'X-ADMIN': 1})
    assert response.status_code == 200

    response = test_client.get('departments/')
    departments = response.get_json()
    assert response.status_code == 200
    assert any(department["name"] == dep["name"] for dep in departments)


def test_post_candidates_endpoint(test_client, init_db, candidate):    
    response = test_client.post('candidates/', json=candidate, follow_redirects=True)
    assert response.status_code == 200
    
    response = test_client.get('candidates/', headers={'X-ADMIN': 1})
    candidates = response.get_json()
    assert response.status_code == 200
    assert any(candidate["name"] == can["name"] for can in candidates)


def test_post_get_resume_endpoint(test_client, init_db, candidate, resume):
    response = test_client.post('candidates/', json=candidate, follow_redirects=True)
    assert response.status_code == 200

    response = test_client.get('candidates/', headers={'X-ADMIN': 1})
    candidates = response.get_json()
    candidate_id = candidates[0]["id"]

    response = test_client.post('resume/{}'.format(candidate_id), 
        data={
            'file': resume,
        }, 
        follow_redirects=True,
        content_type='multipart/form-data',
    )
    assert response.status_code == 200
    
    response = test_client.get('resume/{}'.format(candidate_id), 
        follow_redirects=True,
    )
    assert response.status_code == 403

    response = test_client.get('resume/{}'.format(candidate_id), 
        follow_redirects=True,
         headers={'X-ADMIN': 1}
    )
    assert response.status_code == 200
    

def test_get_candidates_endpoint_sorted(test_client, init_db, sorted_candidates):
    response = test_client.get('candidates/', headers={'X-ADMIN': 1})
    result = response.get_json()
    assert response.status_code == 200
    assert all(sorted_candidates[i].id == can["id"] for i, can in enumerate(result))





