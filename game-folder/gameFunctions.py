import random

def rules():
    print("The rules are simple.")
    print("You will be prompted a series of multiple choice questions and you will have to vote on what you think the majority of players in the game would pick.")
    print("Players who pick the question with the most votes gain a point, the ones who chose the answers with the minorty will lose one.")
    print("If there is a tie in answers eveyrone will gain a point.")
    print("If a player gets 3 or more questions in a row correct, they will gain 2 points instead of 1.")
    print("Answer all question by using numberpad.")
    print("The player with the most points at the end of the game wins!")

def separator():
    print("-------------------------------------------------")

def getQuestion():
    question = [
        "Who would survive the longest on a deserted island?",
        "Who is most likely to become a superhero?",
        "Who would win in a dance-off?",
        "Who has the most outrageous fashion sense?",
        "Who is the biggest drama queen?",
        "Who would accidentally start a fire while cooking?",
        "Who is most likely to forget their own birthday?",
        "Who is the best at telling terrible jokes?",
        "Who would bring a pet rock to a party?",
        "Who is most likely to accidentally text the wrong person?",
        "Who would be the first to get lost in a familiar place?",
        "Who has the best collection of weird socks?",
        "Who is most likely to wear mismatched shoes?",
        "Who would try to sell ice to an Eskimo?",
        "Who is the best at making up silly songs on the spot?",
        "Who is most likely to break into song at any moment?",
        "Who has the weirdest talent?",
        "Who would get caught talking to themselves in public?",
        "Who is most likely to create a ridiculous conspiracy theory?",
        "Who would forget how to use a fork?",
        "Who is the biggest liar?"
    ]
    randQuestion = random.choice(question)
    print(randQuestion)

def getAnswers(players):
    answers = []
    for player in players:
        print(f"{player.get_name()}, it's your time to answer!")
        for index, other_player in enumerate(players):
            print(f"Press: {index + 1} to vote {other_player.get_name()}")
        separator()
        answer = int(input("Enter your choice: ")) - 1
        answer = verifyInput(answer, players)
        player.set_answer(answer)
        answers.append(answer)
    
    answer_counts = [answers.count(answer) for answer in set(answers)]
    highestVoteFreq = max(answer_counts)
    # Check how many answers have the highest frequency
    if answer_counts.count(highestVoteFreq) > 1:
    # There is a tie
        return -1
    else:
        # Return the index of the most voted answer
        return max(answers, key=answers.count)

 

def verifyInput(answer, players):
    while True:
        try:
            if answer < 0 or answer >= len(players):
                raise ValueError
            break
        except ValueError:
            print("Invalid input! Please try again.")
            answer = int(input("Enter your choice: ")) - 1
    return answer

def revealResults(players, answerIDX):
    print("The results are in!")
    print("The majority of players voted for:") 
    separator()
    if answerIDX != -1:
        mostVoted = players[answerIDX]
        print(f"{mostVoted.get_name()}!!!")
        separator()
        for player in players:
            if player.get_answer() == answerIDX: 
                player.correct()
                print(f"{player.get_name()} has gained a point!")
            else:
                player.wrong()
                print(f"{player.get_name()} has lost a point!")
    else:
        print("No majority vote. Everyone gains a point!")
        separator()
        for player in players:
            player.correct()
            print(f"{player.get_name()} has gained a point!")

def quitGame(players):
    print("Do you want to quit the game?")
    print("Enter 1 for Yes")
    print("Enter 2 for No")
    choice = int(input("Enter your choice: "))
    if choice < 1 or choice > 2:
        print("Invalid input! Please try again.")
        quitGame(players)
    if choice == 1:
        winner(players)

def printScores(players):
    for player in players:
        print(player.__str__())

def winner(players):
    scores = []
    for player in players:
        scores.append(player.get_score())
    highestScore = max(scores)
    separator()
    if scores.count(highestScore) > 1:
        print("There is a tie!")
        print(f"There are multiple winners with a score of {highestScore}!")
        exit()
    else:
        print(f"{players[scores.index(highestScore)].get_name()} has won the game with a score of {players[scores.index(highestScore)].get_score()}!")
        print("Congratulations!")
        exit()
    

def limitedMode(players, rounds):
    for i in range(rounds):
        print(f"Round {i + 1}!")
        separator()
        getQuestion()
        answerIDX = getAnswers(players)
        revealResults(players, answerIDX)
        separator()
        printScores(players)
        input("Press Enter to continue")
        separator()
    winner(players)


def endlessMode(players):
    rounds = 0
    while True:
        rounds += 1
        print(f"Round {rounds}!")
        separator()
        getQuestion()
        answerIDX = getAnswers(players)
        revealResults(players, answerIDX)
        separator()
        printScores(players)
        quitGame(players)
        separator()
        