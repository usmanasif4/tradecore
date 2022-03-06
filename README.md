# TradeCore Group

# Requirements
1. Python 3.8.10

# Setup
1. Make sure python 3.8.10 is installed in the system either as default python version or through pyenv.
2. Navigate to root folder (folder containing manage.py)
3. Create a .env file in root folder (folder containing manage.py). Add the following values in .env (A sample file .env.example is provided for ease)
```
ABSTRACT_GEOLOCATION_API_KEY (Abstract API key for Geolocation)
ABSTRACT_HOLIDAYS_API_KEY (Abstract API key for Holidays)
SECRET_KEY (Secret key for JWT)
```
4. Run the following commands to get started
```
1. pipenv shell
2. pip install -r requirements.txt
3. python manage.py migrate
4. python manage.py runserver
```

### API

1. The task is implemented as a simple Django Rest Framework API.
2. The base url is ```http://127.0.0.1:8000/api```
3. API testing tools such as POSTMAN can be used to test the endpoints.

### API ENDPOINTS
1. **Sign Up**: ```http://127.0.0.1:8000/api/signup```
The endpoint accepts a POST request with the following request body and params as json.
```
{
    "email": "abc@gmail.com",
    "password": "abc123456",
    "first_name": "abc",
    "last_name": "xyz"
}
```

2. **User Data**: ```http://127.0.0.1:8000/api/user/5```
The endpoint accepts a GET request. The integer at the end is the user id. Returns the user data for given id.
3. **Login**: ```http://127.0.0.1:8000/api/login```
The endpoint accepts a POST request with the following request body and params as json.
```
{
    "email": "abc@gmail.com",
    "password": "abc123"
}
```
4. **Create Post**: ```http://127.0.0.1:8000/api/post```
The endpoint accepts a POST request with the following request body and params as json. There must be a 'Authorization' header in request with the following value ```JWT <token>```
The token can be obtained using the Login endpoint
```
{
    "title": "new title",
    "description": "new description"
}
```
5. **Get Posts**: ```http://127.0.0.1:8000/api/post```
The endpoint accepts a GET request. Returns the all the posts for the user for which the token is in the header. There must be a 'Authorization' header in request with the following value ```JWT <token>```
The token can be obtained using the Login endpoint
6. **Delete Post**: ```http://127.0.0.1:8000/api/post/2```
The endpoint accepts a DELETE request. The integer at the end is the id of the post which is to be deleted. There must be a 'Authorization' header in request with the following value ```JWT <token>```
The token can be obtained using the Login endpoint
7. **Update Post**: ```http://127.0.0.1:8000/api/post/2```
The endpoint accepts a PATCH request with the following request body and params as json. The integer at the end is the id of the post for which the data is to be updated. There must be a 'Authorization' header in request with the following value ```JWT <token>```
The token can be obtained using the Login endpoint. Any attribute of post can be updated
```
{
    "title": "updated title",
    "description": "updated description"
}
```
8. **Like/Unlike Post**: ```http://127.0.0.1:8000/api/post```
The endpoint accepts a PATCH request with the following request body and params as json. There must be a 'Authorization' header in request with the following value ```JWT <token>```
The token can be obtained using the Login endpoint. The endpoint is used to like or unlike a post. The post_id is the id of the post which is to be liked/unliked. The action can be any of the two values (like, unlike). The action is taken on the post from the user for which the token is supplied in the header.
```
{
    "post_id": "7",
    "action": "unlike"
}
```

### Testing
1. The tests are written for user as well as post
2. To run test, run the following command in root folder (folder containing manage.py)
```
python manage.py test
```

