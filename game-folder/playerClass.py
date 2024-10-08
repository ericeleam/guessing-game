class Player:
    def __init__(self, name):
        self.name = name
        self.streak = 0
        self.score = 0
        self.answer = None
        
    def get_name(self):
        return self.name
    
    def get_score(self):
        return self.score
    
    def get_streak(self):
        return self.streak
    
    def get_answer(self):
        return self.answer
    
    def set_answer(self, answer):
        self.answer = answer
    
    def wrong(self):
        self.streak = 0
        self.score -= 1
    
    def correct(self):
        self.streak += 1
        if self.streak >= 3:
            self.score += 2
            print(f"{self.name} has a streak of {self.streak}! They are gaining x2 point!")
        else:
            self.score += 1

    def __str__(self):
        return f"{self.name} has a score of {self.score} and a streak of {self.streak}."
            
