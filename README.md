# PremierLeagueFixturesPredictions

Python app predicting all the next winners in the England Premier League Championship by using linear regression.

# Purpose of this app

Predict all the next winners in the England Premier League Championship by using linear regression.

# How to use it?

1. Download and install python 3.12.6 **_https://www.python.org/downloads/_**
2. Open your CLI by using the Win+R (or ⌘ + R on mac) key combination. Then simply enter “cmd” in the input field and press OK.
3. Trough your CLI, Clone this repo with this command **_git clone https://github.com/agahungu/PremierLeagueFixturesPredictions.git_**
4. Navigate to the directory with this command **_cd PremierLeagueFixturesPredictions_**
5. Check if python is well installed by running this command **_python --version_**
6. Install the dependencies with this command **_pip install -r requirements.txt_**
7. Run the main app with this command **_python predictNextWinners.py_**

Accuracy r2_score: 0.6156325922701607

Tech stack: Python 3.12.6, Jupyter Notebook <br><br>
Librairies: os, pandas, matplotlib.pyplot, seaborn, Scikit-Learn, joblib, csv


# Datasets

Dataset 1: Teams2425.csv

Contains insights about the teams <br><br>

Team: Name of the team <br>
Minutes: Total minutes played <br>
Goals: Number of goals scored <br>
Assists: Number of assists <br>
Penalty Shoot on Goal: Penalty shots taken on goal <br>
Penalty Shoot: Total penalty shots attempted <br>
Total Shoot: Total shots attempted <br>
Shoot on Target: Shots successfully on target <br>
Yellow Cards: Number of yellow cards received <br>
Red Cards: Number of red cards received <br>
Touches: Total ball touches <br>
Dribbles: Total dribbles attempted <br>
Tackles: Total tackles made <br>
Blocks: Total blocks <br>
Shot-Creating Actions: Actions leading to a shot attempt <br>
Goal-Creating Actions: Actions leading to a goal <br>
Passes Completed: Successful passes completed <br>
Passes Attempted: Total passes attempted <br>
Pass Completion %: Pass completion rate, expressed as a percentage (some entries have missing values here) <br>
Progressive Passes: Passes advancing the ball significantly toward the opponent’s goal <br>
Carries: Total ball carries <br>
Progressive Carries: Carries advancing the ball significantly toward the opponent’s goal <br>
Dribble Attempts: Total dribbles attempted <br>
Successful Dribbles: Total successful dribbles <br>

Raw source: Eduardo Palmieri from Kaggle <br>

Dataset 2: Fixtures2325.csv

Contains insights about the fixtures from 2023 to 2025 <br><br>

Div: E0 for Division 1 of england championship <br>
Date: Date of the match <br>
Time: Hours and mintues the match begins <br>
HomeTeam: Name of the team reciever <br>
AwayTeam: Name of the team visitor <br>
FTHG: Full time home goals <br>
FTAG: Full time away goals <br>
FTR: Full time result <br>
HTHG: Half time home goals <br>
HTAG: Half time away goals <br>
HTR: Half time result <br>
Winner: Name of the winner the match and « Draw » if no winner <br>
HREMONTADA: Home remontada <br>
AREMONTADA: Away remontada <br>
Referee: Name of the referee <br>

Raw source: https://www.football-data.co.uk/englandm.php
