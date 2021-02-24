# Hash tables are implimented in Python through disctionaries

# Voting Register example: Grokking Algorithums

voted = {}
def check_voted(name):
    if voted.get(name):
        print("Kick ",name," out!")
    else:
        voted[name] = True
        print("Let ",name," vote!")

check_voted("Tom")

check_voted("Chris")

check_voted("Tom")
