import csv 
import joblib 

def searchTeamInsights(nameTeam):
    with open("datas/dataset.csv", 'r') as csvfile:
        plTeams = csv.reader(csvfile, dialect='excel', delimiter='\t')
        next(plTeams)
        teamInsights = []

        for team in plTeams:
            if(str(team[1]) == nameTeam):
                #"Team", "Progressive Carries","Successful Dribbles"
                teamInsights = [team[1], team[22], team[24]]
                break
        
        return teamInsights

def prediction (nameTeam1, nameTeam2, date):
    team1= searchTeamInsights(nameTeam1)
    team2= searchTeamInsights(nameTeam2)
    #print(str(team1)+"-"+str(team2))
    prediction_model =joblib.load('model/model_premierleague.mod')
    team1_prediction = prediction_model.predict([[team1[1], team1[2]]])
    team2_prediction = prediction_model.predict([[team2[1], team2[2]]])
    print("Match: "+str(date)+" ("+str(nameTeam1)+" VS "+str(nameTeam2)+")")
    print("   "+nameTeam1+": "+str(team1_prediction[0]))
    print("   "+nameTeam2+": "+str(team2_prediction[0]))
    print("")
    if team1_prediction>team2_prediction:
        print(nameTeam1.upper()+ " IS THE WINNER!")
    else :
        print(nameTeam2.upper()+ " IS THE WINNER!")
    print("---------------------------------------")

with open("Fixtures2325.csv", 'r') as csvfile:
        nextFixtures = csv.reader(csvfile, dialect='excel', delimiter=',')
        next(nextFixtures)
        
        for nextFixture in nextFixtures:
            if nextFixture[11]=="" and nextFixture[3]!="Leicester"   and nextFixture[3]!="Ipswich" and nextFixture[3]!="Southampton" and nextFixture[4]!="Leicester" and nextFixture[4]!="Ipswich" and nextFixture[4]!="Southampton"   :

                ####### MAIN FUNCTION #######

                #team1 (HomeTeam) - team2 (AwayTeam) - Date of the match are used in function prediction() to predict the winner
                #Another interesting variation would be to create a model to predict the percentage of victory Home and Away separetly
                prediction(str(nextFixture[3]),str(nextFixture[4]),str(nextFixture[1]))
             



