import requests, json

PARAMETERS = {
    "amount": 10,
    "category": 18,
    "difficulty": "easy",
    "type":"boolean"
}
def get_questions():
    response = requests.get(url="https://opentdb.com/api.php", params=PARAMETERS)
    questions = response.json()
    question_data = questions["results"]
    return question_data
    
    



