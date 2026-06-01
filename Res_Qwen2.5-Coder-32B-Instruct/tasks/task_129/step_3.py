import json

print("Parsing the JSON response...")
data = json.loads('{"response_code":0,"results":[{"type":"boolean","difficulty":"easy","category":"Entertainment: Film","question":"Matt Damon played an astronaut stranded on an extraterrestrial planet in both of the movies Interstellar and The Martian.","correct_answer":"True","incorrect_answers":["False"]}]}')
question = data['results'][0]['question']
print(f"Random Trivia Question: {question}")