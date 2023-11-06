# Trivia App

## Installation
Open a new terminal window then navigate to the `backend` directory. Create and source a virtual environment in the `backend` directory like so:

```
python -m venv venv
source venv/bin/activate
```

Then install the dependencies:

```
pip install -r requirements.txt
```

Then in a second terminal window, navigate to the frontend directory and run: 
```
npm install
```

Start a postgreSQL server and create two databases, one called `trivia` and another called `trivia_test`.

## Running the app
To start the app, run `npm start` in the frontend directory, then in the first terminal window, while under the backend directory, run `flask run`.

## API
`GET /categories`

Fetches a dictionary of categories with key as id and value as the category name.
Request Arguments: None
Returns: An object with a key, categories, and key / value pairs of id and category name.

```
categories: {
  "1": "Science",
  "2": "Art",
  "3": "Geography",
  "4": "History",
  "5": "Entertainment",
  "6": "Sports"
}
```