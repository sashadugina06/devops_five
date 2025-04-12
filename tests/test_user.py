from fastapi.testclient import TestClient
from fastapi import status
from src.main import app

client = TestClient(app)

# Существующие пользователи
users = [
    {
        'id': 1,
        'name': 'Ivan Ivanov',
        'email': 'i.i.ivanov@mail.com',
    },
    {
        'id': 2,
        'name': 'Petr Petrov',
        'email': 'p.p.petrov@mail.com',
    }
]

def test_get_existed_user():
    '''Получение существующего пользователя'''
    response = client.get("/api/v1/user", params={'email': users[0]['email']})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == users[0]

def test_get_unexisted_user():
    '''Получение несуществующего пользователя'''
    response = client.get("/api/v1/user", params={'email': 'nonexistent@mail.com'})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'User not found'}

def test_create_user_with_valid_email():
    '''Создание пользователя с уникальной почтой'''
    new_user = {
        'name': 'New User',
        'email': 'new.user@mail.com'
    }
    response = client.post("/api/v1/user", json=new_user)
    assert response.status_code == status.HTTP_201_CREATED
    assert isinstance(response.json(), int)  # Возвращает ID нового пользователя

def test_create_user_with_invalid_email():
    '''Создание пользователя с почтой, которую использует другой пользователь'''
    existing_user = {
        'name': 'Duplicate User',
        'email': users[0]['email']  # Используем email существующего пользователя
    }
    response = client.post("/api/v1/user", json=existing_user)
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json() == {'detail': 'User with this email already exists'}

def test_delete_user():
    '''Удаление пользователя'''
    # Сначала создадим пользователя для теста удаления
    test_email = 'to.delete@mail.com'
    client.post("/api/v1/user", json={'name': 'To Delete', 'email': test_email})
    
    # Тестируем удаление
    response = client.delete("/api/v1/user", params={'email': test_email})
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
    # Проверяем, что пользователь действительно удален
    check_response = client.get("/api/v1/user", params={'email': test_email})
    assert check_response.status_code == status.HTTP_404_NOT_FOUND