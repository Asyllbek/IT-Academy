## IT-Academy Tests
<div align="center">
<h1 align="center">IT-Academy Tests</h1>
</div>


<!-- ABOUT THE PROJECT -->
## About The Project

### Web-based _**_Testing system_**_ built with the Django framework. This project supports full functionality for testing students of educational institutions




### Built And Work With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)






<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.



## Installation of dependencies, Project Setup & Project Start
### Important! The following command works through the pip package manager. Download the pip package manager for your system. Of course, you also need to have Python 3 (preferably higher than version 3.7) installed on your system.
* [Python](https://www.python.org/)
* [pip](https://pypi.org/project/pip/)

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

#### Important !  You need to create and activate the virtualenv before next command.
* [virtualenv](https://pypi.org/project/virtualenv/)

1. Install all required dependencies from requirements file. 
   ```sh
   pip install -r requirements.txt
   ```
   
2. Create and set your preferences in the .env file.
Important ! Create in a .env file in the root directory of the project (at the same level as the location of the manage.py file) with the values SECRET_KEY=your_secret_key
DEBUG=your_debug_status_for_example_True

You will need to generate a secret key for Django. 
You can generate manually via shell or via web service: https://djecrety.ir/  

Instructions for generating a secret key manually via shell below. (Commands in terminal)

```sh
python manage.py shell
  ```   
After, in shell
```shell
from django.core.management.utils import get_random_secret_key
```   

```shell
print(get_random_secret_key())
``` 
   ### Do not forget set your preferences in the .env file. 

3. Make migrations
   ```sh
   ./manage.py migrate
   ```

4. Create a super user
   ```sh
   ./manage.py createsuperuser
   ```
   
5. Run the project
   ```sh
   ./manage.py runserver
   ```

<!-- USAGE EXAMPLES -->
## Usage

You can see the functionality of the project by going to the url address below url in your browser.

_Django project must be running_

_URL: http://127.0.0.1:8000/admin/_

_After authentication, you can go to the following url_

_URL: http://127.0.0.1:8000/_



### After you can see a page where you will test the web application



<!-- CONTACTS -->
## Contacts

Email - asylbek1106@gmail.com





