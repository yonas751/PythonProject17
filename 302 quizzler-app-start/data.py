import requests
question_data =requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean").json()
# print(question_data)
data=question_data["results"]
# question_data.raise_for_status()
# data=question_data.json()
# print(data)