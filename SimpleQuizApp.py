print("Hello.  You are about to take a 5-question quiz.")

score = 0

answer_1 = input("1) What is the capital of France? ").lower().strip()
if answer_1 == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect.  The answer is \"Paris\".")

answer_2 = input("How many planets are in our solar system?"
                 " (Enter your answer as an integer) ").lower().strip()
if answer_2 == "8":
    print("Correct!")
    score += 1
else:
    print("Incorrect.  The answer is 8.")

answer_3 = input("What year did World War II end?"
                     " (Enter your answer as an integer.) ").strip()
if answer_3 == "1945":
    print("Correct!")
    score += 1
else:
    print("Incorrect.  The answer is 1945.")

answer_4 = input("What is the largest ocean on Earth? ").lower().strip()
if answer_4 == "pacific" or answer_4 == "pacific ocean":
    print("Correct!")
    score += 1
else:
    print("Incorrect.  The answer is \"Pacific\".")

answer_5 = input("How many sides does a hexagon have?"
                 " (Enter your answer as an integer) ").strip()
if answer_5 == "6":
    print("Correct!")
    score += 1
else:
    print("Incorrect.  The answer is 6.")

print(f"You scored {score} out of 5 ({(score/5) * 100:.0f}%) on the quiz.")



