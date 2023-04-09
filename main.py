# // Cricket Match Total score prediction using python

print("*******Welcome to Cricket Match Score Predictor*******")
print('''In this program you have to enter current score of a team and this
program predicts the final score of the team.''')

cricket_format_inp = int(input("Enter the cricket format you want to predict final score. \n1) T20\n2) ODI\n3) Test\n"))

if (cricket_format_inp==1):
        runs = int(input("Enter the current runs : "))
        wickets = int(input("Enter the current wickets : "))

        if wickets==0:
              wickets+=1

        if wickets>=10:
              print("Wickets cannot be 10 or 10+ !")
        else:
            balls = int(input("Enter thecurrent  balls that has been bowled (minimum 48 balls) : "))

            if balls<48:
                print("At least 48 balls must be bowled for a better prediction.")

            elif  balls>=120:
                 print("120 or More than 120 cannot be entered, Please enter less than 120 balls!")
                 
            else:
                balls_left = 120-balls
                strike_rate = runs/balls
                wicket_rate = int(balls_left/(balls/wickets))+1
                predicted_runs = runs+(strike_rate*balls_left)
                predicted_wickets = wickets+wicket_rate

                if (predicted_wickets>10):
                     wickets_left = wickets-10
                     runs_per_wickets = runs/wickets
                     predicted_runs = runs-(wickets_left*runs_per_wickets)
                     predicted_wickets = 10


                print(f"Current Score : {runs}/{wickets}")
                print(f"Predicted Final Score : {int(predicted_runs)}/{predicted_wickets}")


elif (cricket_format_inp==2):
        runs = int(input("Enter the current runs : "))
        wickets = int(input("Enter the current wickets : "))

        if wickets==0:
              wickets+=1

        if wickets>=10:
              print("Wickets cannot be 10 or 10+ !")
        else:
            balls = int(input("Enter the current  balls that has been bowled (minimum 120 balls) : "))

            if balls<120:
                print("At least 120 balls must be bowled for a better prediction.")

            elif  balls>=300:
                 print("300 or More than 300 cannot be entered, Please enter less than 300 balls!")
                 
            else:
                balls_left = 300-balls
                strike_rate = runs/balls
                wicket_rate = int(balls_left/(balls/wickets))+1
                predicted_runs = runs+(strike_rate*balls_left)
                predicted_wickets = wickets+wicket_rate

                if (predicted_wickets>10):
                     wickets_left = wickets-10
                     runs_per_wickets = runs/wickets
                     predicted_runs = runs-(wickets_left*runs_per_wickets)
                     predicted_wickets = 10


                print(f"Current Score : {runs}/{wickets}")
                print(f"Predicted Final Score : {int(predicted_runs)}/{predicted_wickets}")

else:
    runs = int(input("Enter the current runs : "))
    wickets = int(input("Enter the current wickets : "))

    if wickets==0:
        wickets+=1

    if wickets>=10:
        print("Wickets cannot be 10 or 10+ !")

    else:
        balls = int(input("Enter the current balls that has been bowled (minimum 240 balls) : "))

        if balls<240:
             print("At least 240 balls must be bowled for a better prediction.")
        else:
             
             balls_rate = balls/runs
             wickets_left = 10-wickets


             wickets_new = 1

             if wickets==0:
                wickets==1
                wickets_new = 0
                

             runs_per_wicket = round(runs/wickets)

             if wickets_left<5:
                  predicted_runs = runs+(wickets_left*(runs_per_wicket/2))

             else:
                batters_wickets_left = wickets_left-4
                batter_predicted_runs = batters_wickets_left*runs_per_wicket
                bowler_predicted_runs = 4*(runs_per_wicket/2)
                predicted_runs = round(runs+batter_predicted_runs+bowler_predicted_runs)


             predicted_balls = round(balls_rate*predicted_runs)
             
             if wickets_new==0:
                print(f"Current Score : {runs}/0")
             else:
                print(f"Current Score : {runs}/{wickets}")

             print(f"Predicted Final Score : {int(predicted_runs)}/10 in {predicted_balls} Balls")
