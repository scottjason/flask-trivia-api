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

Then run:

`psql trivia < trivia.psql`

Next in a second terminal window, navigate to the frontend directory and run: 

```
npm install
```

Start a postgreSQL server and create two databases, one called `trivia` and another called `trivia_test`.


## Running the app
To start the app, run `npm start` in one terminal window in the frontend directory, then in the another terminal window, while under the backend directory, run `flask run`.

## API

### `GET /categories`

- Fetches a dictionary of categories with key as id and value as the category name.
- Request Arguments: None
- Returns: An object with a key, categories, and key / value pairs of id and category name.

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

### `GET /categories`

- Fetches a dictionary of categories with key as id and value as the category name.
- Request Arguments: None
- Returns: An object with a key, categories, and key / value pairs of id and category name.

#### Example Response:
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

### `GET /questions`

- Fetches a dictionary of questions for the page the user is on, categories, total pages and current category. 
- Request Arguments: None
- Returns: An object containing an array of objects of questions, categories, total questions and current_category as the other keys. The current_category should be null for this response.

#### Example Response:
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    ...
  ],
  "total_questions": 20
}
```

### `POST /questions`
- Creates a new trivia question which includes the answer, category and difficulty level.
- Request Arguments: post body contains `question` and `answer`, both of type string as well as `category` and `difficulty`, both of type int.
Returns `{ success: true }`


### `DELETE /questions/<question_id>`
- Deletes a question by id.
- Request Arguments: `question_id` in the path, data type int.
Returns `{ success: true }`

### `POST questions/search`
- Searches for trivia questions that partially match the search term.
- Request Arguments: post body contains `searchTerm` of type string.
- Returns: An array of objects containing questions that partially match the search term as well as categories, total questions and current_category, which should be null for this response.

#### Example Response:
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    ...
  ],
  "total_questions": 20
}
```

### `GET categories/<category_id>/questions`
- Fetches questions by category.
- Request Arguments: the path contains the category id of type int representing the category of questions to return.
- Returns: An array of objects including questions associated with the category selected as well as categories, total questions and current_category.

#### Example Response:
```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": "Science",
  "questions": [
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    ...
  ],
  "total_questions": 7
}
```

### `POST /quizzes`
- Fetches a random question from one category or all categories, depending on which the user selects.
- Request Arguments: post body includes previous_questions, an array of question ids of questions that have already been asked as well as a quiz_category object which contains the category id selected by the user as well as the category type.
- Returns: an object containing the question and answer both of type string as well as the category id, the id of the question and difficulty level of type int.

#### Example Response:
```
{
  "answer": "Jackson Pollock",
  "category": 2,
  "difficulty": 2,
  "id": 19,
  "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
}
```
