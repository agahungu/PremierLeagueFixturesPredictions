# PremierLeagueFixturesPredictions

Python app predicting all the next winners in the England Premier League Championship by using linear regression.

Purpose of this app :

Predict all the next winners in the England Premier League Championship by using linear regression.

How to use it?

1. Trough your CLI, Clone this repo with this command git clone https://github.com/agahungu/PremierLeagueFixturesPredictions.git
2. Navigate to the directory with this command **_Cd PremierLeagueFixturesPredictions_**
3. Run the main app with this command **_python predictNextWinners.py_**

Tech stack : Python 3.10, Jupyter Notebook
Librairies : os, pandas, matplotlib.pyplot, seaborn, Scikit-Learn, joblib, csv

Datasets :

Dataset 1 : Teams2425.csv

Contains insights about the teams

Team : Name of the team
Minutes: Total minutes played
Goals: Number of goals scored
Assists: Number of assists
Penalty Shoot on Goal: Penalty shots taken on goal
Penalty Shoot: Total penalty shots attempted
Total Shoot: Total shots attempted
Shoot on Target: Shots successfully on target
Yellow Cards: Number of yellow cards received
Red Cards: Number of red cards received
Touches: Total ball touches
Dribbles: Total dribbles attempted
Tackles: Total tackles made
Blocks: Total blocks
Shot-Creating Actions: Actions leading to a shot attempt
Goal-Creating Actions: Actions leading to a goal
Passes Completed: Successful passes completed
Passes Attempted: Total passes attempted
Pass Completion %: Pass completion rate, expressed as a percentage (some entries have missing values here)
Progressive Passes: Passes advancing the ball significantly toward the opponent’s goal
Carries: Total ball carries
Progressive Carries: Carries advancing the ball significantly toward the opponent’s goal
Dribble Attempts: Total dribbles attempted
Successful Dribbles: Total successful dribbles

Raw source : Eduardo Palmieri from Kaggle

Dataset 2 : Fixtures2325.csv

Contains insights about the fixtures from 2023 to 2025
Div : E0 for Division 1 of england championship
Date : Date of the match
Time : Hours and mintues the match begins
HomeTeam : Name of the team reciever
AwayTeam : Name of the team visitor
FTHG : Full time home goals
FTAG : Full time away goals
FTR : Full time result
HTHG : Half time home goals
HTAG: Half time away goals
HTR : Half time result
Winner : Name of the winner the match and « Draw » if no winner
HREMONTADA : Home remontada
AREMONTADA : Away remontada
Referee : Name of the referee

Raw source : https://www.football-data.co.uk/englandm.php
