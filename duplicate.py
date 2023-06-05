candidate_1 = dict()

candidate_2 = dict()
candidate_3 = dict()

candidate_1["Votes"]=int(input("enter total votes for candidate 1 "))
candidate_2["Votes"]=int(input("enter total votes for candidate 2 "))
candidate_3["Votes"]=int(input("enter total votes for candidate 3 "))

candidate_1_fct = input("is candidate 1 winner at FCT Yes/No? ").lower()
candidate_2_fct = input("is candidate 2 winner at FCT Yes/No? ").lower()
candidate_3_fct = input("is candidate 3 winner at FCT Yes/No? ").lower()

candidate_1_wins = input("did candidate 1 win two third of all states Yes/No? ").lower()
candidate_2_wins = input("did candidate 2 win two third of all states Yes/No? ").lower()
candidate_3_wins = input("did candidate 3 win two third of all states Yes/No? ").lower()

if (candidate_1.get("Votes") > candidate_3.get("Votes") and candidate_1.get("Votes") > candidate_2.get("Votes")) and (candidate_1_fct == "yes" and candidate_1_wins == "yes"):
    print("Candidate 1 is the winner of the election")

elif (candidate_2.get("Votes") > candidate_3.get("Votes") and candidate_2.get("Votes") > candidate_1.get("Votes")) and (candidate_2_fct == "yes" and candidate_2_wins == "yes"):
    print("Candidate 2 is the winner of the election")

elif (candidate_3.get("Votes") > candidate_1.get("Votes") and candidate_3.get("Votes") > candidate_2.get("Votes")) and (candidate_3_fct == "yes" and candidate_3_wins == "yes"):
    print("Candidate 3 is the winner of the election")
else:
    print("No winner")