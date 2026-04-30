#Exercise 4 - Primitive Quiz
#Marionne Jizella E. Centeno

answer = input("What is the capital of France?")

if answer.lower() == "Paris":
    print("Correct!")
else:
    print("Wrong answer.")

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United Kingdom": "London",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Austria": "Brussels",
    "Portugal": "Lisbon",
    "Greece": "Athens",
}

score = 0

print("--- European Capitals Quiz ---")

for country, capital in capitals.items():
    answer = input(f"What is the capital of {country}?")
    if answer.strip().lower() == capital.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong. The correct answer is {capital}.")

print(f"\nQuiz Finished! Your final score is {score}/{len(capitals)}.")