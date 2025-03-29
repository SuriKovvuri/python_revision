import requests

def test_get_user():
    reponse = requests.get('https://jsonplaceholder.typicode.com/users/1')
    print(reponse)
    print(reponse.status_code)
    json_data = reponse.json()
    print(json_data)

    assert reponse.status_code == 200
    print('True')
test_get_user()


def test_create_user():
    user_details = {
        'Honda' : 'Grazia',
        'Model' : 125
        }
    response = requests.post('https://jsonplaceholder.typicode.com/users', json=user_details)
    print(response)
    print(response.status_code)
    json_data = response.json()
    print(json_data)
    
    assert response.status_code == 201
    print('True')
test_create_user()




























# import requests

# # response = requests.get('https://google.com/')
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# # response = requests.get('https://github.com/SuriKovvuri')
# print(response)
# print(response.status_code)
# if response.status_code == 200:
#     print('passed')
#     data = response.json()
#     print(data)
# else:
#     print('failed')
#     # json = response.json()
#     # print(json)
    
