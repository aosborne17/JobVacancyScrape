# Job Vacancies Scrape

This project has been created to scrape Junior DevOps vacancies from the indeed job site and send them in CSV format to the user

The CSV file will then be emailed to you!!

## Prerequisites 

- Python [Here](https://www.python.org/downloads/)
- Gmail Account [Here](https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp)

## Clone the Repository

```
git clone https://github.com/aosborne17/JobVacancyScrape.git
```

## Creating a virtual environment

#### - For Windows:

```
cd JobVacancyScrape
pip install virtualenv
virtualenv venv # Create a virtual environment called 'venv'
venv\Scripts\activate # Activate the virtual environment

```

#### - For Mac:

```
cd JobVacancyScrape
sudo pip install virtualenv
virtualenv -p python3 venv # Create a virtual environment called 'venv'
source venv\Scripts\activate # Activate the virtual environment
```

## Download the required packages

```
pip install -r requirements.txt
```

## Create ENV Variables for Login

- Create an env variable for the 'EMAIL_ADDRESS' and 'EMAIL_PASSWORD in order to login to gmail

## Running the Script

```
python main.py
```

## Author

### Andrew Osborne