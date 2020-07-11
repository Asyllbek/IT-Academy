## It's Django project

Do you want to run my project ?
Do this instruction below in your terminal.

#### 1-st step
Clone with HTTPS from GitHub
```
git clone https://github.com/Asyllbek/It_academy_tests.git
```
#### 2-nd step
Go to the bent directory. Install and activate the virtual environment.
Install all packages in  requirement.txt

```
pipenv install -r requirements.txt
```
then activate env
```
pipenv shell
```
#### 3-th step
Read env_example and add your SECRET_KEY and DEBUG status

#### 4-th step
Make migrations steps
1-st
```
./manage.py makemigrations classroom
```
2-nd
```
./manage.py migrate classroom
```
then 
```
./manage.py migrate 

```
#### 5-th step
Create a super user
```
./manage.py createsuperuser
```
### Finally step
Run the project

```
./manage.py runserver
```



