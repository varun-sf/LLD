

class Voteable():
  
    def __init__(self):
      self.votes = []
 
    def add_vote(self, vote):
        self.votes.append(vote)
  
    def get_total_votes(self):
        positive=0
        negative=0
        for vote in self.votes:
            if vote.value ==1:
                positive+=1
            else:
                negative+=1
        return f"Total positive votes- {positive} & negative votes - {negative}"