import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
  """This class represents the trivia test case"""

  def setUp(self):
    """Define test variables and initialize app."""
    self.app = create_app()
    self.client = self.app.test_client
    self.database_name = "trivia_test"
    self.database_path = "postgres://{}/{}".format(
        'localhost:5432', self.database_name)
    setup_db(self.app, self.database_path)

    # binds the app to the current context
    with self.app.app_context():
      self.db = SQLAlchemy()
      self.db.init_app(self.app)
      # create all tables
      self.db.create_all()
      categories = Category.query.all()
      # populate test db with categories if empty
      if len(categories) == 0:
        categories = {'1': 'Science', '2': 'Art', '3': 'Geography',
                      '4': 'History', '5': 'Entertainment', '6': 'Sports'}
        for category in categories:
          category = Category(type=categories[category])
          self.db.session.add(category)
          self.db.session.commit()
          self.db.session.close()
      # populate test db with a question if empty
      questions = Question.query.all()
      if len(questions) == 0:
        question = {
            'question': "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
            'answer': 'Maya Angelou',
            'category': 4, 'difficulty': 2
        }
        new_question = Question(question=question['question'], answer=question['answer'],
                                category=question['category'], difficulty=question['difficulty'])
        self.db.session.add(new_question)
        self.db.session.commit()
        self.db.session.close()

  def tearDown(self):
    """Executed after reach test"""
    pass

  """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

  def test_get_categories(self):
    res = self.client().get("/categories")
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertTrue(data["categories"])
    self.assertEqual(data["success"], True)

  def test_get_questions(self):
    res = self.client().get("/questions")
    data = json.loads(res.data)
    self.assertTrue(data["questions"])
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)

  def test_delete_question(self):
    question = Question.query.first()
    question_id = question.id
    res = self.client().delete("/questions/" + str(question_id))
    self.assertEqual(res.status_code, 200)

  def test_delete_question_422(self):
    res = self.client().delete("/questions/1234")
    data = json.loads(res.data)
    self.assertEqual(
        data, {'error': 422, 'message': 'Unprocessable content', 'success': False})
    self.assertEqual(res.status_code, 422)

  def test_add_question(self):
    question = {
        'question': "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
        'answer': 'Maya Angelou',
        'category': 2, 'difficulty': 1
    }
    res = self.client().post("/questions", json=question)
    self.assertEqual(res.status_code, 200)

  def test_add_question_422(self):
    # attempt to add a question with no answer or category
    question = {
        'question': "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
        'category': 2,
    }
    res = self.client().post("/questions", json=question)
    self.assertEqual(res.status_code, 422)

  def test_search_questions(self):
    search_term = {'searchTerm': 'bird'}
    res = self.client().post("/questions/search", json=search_term)
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)

  def test_search_questions_400(self):
    # attempt to search for int data type
    search_term = {'searchTerm': 1}
    res = self.client().post("/questions/search", json=search_term)
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 400)
    self.assertEqual(data["success"], False)

  def test_get_questions_by_category(self):
    res = self.client().get('/categories/4/questions')
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data["success"], True)

  def test_get_questions_by_category_422(self):
    res = self.client().get('/categories/4000/questions')
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 422)
    self.assertEqual(data["success"], False)

  def test_get_questions_for_quiz(self):
    previous_questions = [20]
    quiz_category = {'id': 0}
    mock_payload = {'previous_questions': previous_questions,
                    'quiz_category': quiz_category}
    res = self.client().post('/quizzes', json=mock_payload)
    data = json.loads(res.data)
    self.assertTrue(data['question'])
    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['success'], True)

  def test_get_questions_for_quiz_422(self):
    previous_questions = [20]
    quiz_category = {'id': 100}
    mock_payload = {'previous_questions': previous_questions,
                    'quiz_category': quiz_category}
    res = self.client().post('/quizzes', json=mock_payload)
    data = json.loads(res.data)
    self.assertEqual(res.status_code, 422)
    self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
  unittest.main()
