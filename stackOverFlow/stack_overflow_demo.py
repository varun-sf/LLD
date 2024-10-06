from stack_over_flow import StackOverFlow

class demo:
    @staticmethod
    def run():
        system = StackOverFlow()
        user = system.add_user("varun","gku@abc.com")
        question = system.create_question("science","what are dinosaurs",user)
        system.create_question("science","what is rhenopsaurus",user)
        user2 = system.add_user("varun2","gku2@abc.com")
        system.add_answer(question,"dinosaurus doesnt exist", user2)
        system.add_vote(question,1, user2)
        print(system.search_box(""))
        
        

if __name__=="__main__":
    demo.run()