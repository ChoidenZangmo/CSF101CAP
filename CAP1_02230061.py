####################################
#Choiden Zangmo
#First Year Electrical Department
#02230061
####################################
#References
#Chatgpt and Copilot
#(n.d.). Python read a file. Youtube. https://www.youtube.com/watch?v=LpZmZs2_BC4
####################################
#Solution
#My solution Score: 50029 


def read_input(): #For reading the input text file
    input_data = []  # empty list
    with open('C:\\Users\\Lenovo\\OneDrive\\Desktop\\CSF101\\CSF101CAP\\input_1_cap1.txt', 'r') as file: #copied my given input_1_cap1 as a path and used doubleslashes to interpret it as literal characters not escape characters
        lines = file.readlines()#To read all the lines from file
        for line in lines:
            my_move, desired_outcome = line.strip().split() # to make it easier to process the data accurately by removing unnnessary space and to separate diff. parts of string
            input_data.append((my_move, desired_outcome))
    return input_data
 # To calculate score
def calculate_score(input_data):
    total_score = 0               #MOVES And OUTCOME:  (A:Rock, B:Paper, C:Scissors; X:lost, Y:Draw, Z:win)
                                  #SCORE: (A = 1, B = 2, C = 3; X = 0, Y = 3, Z = 6)
    for my_move, desired_outcome in input_data: # Summing the move and outcome's score in simple
        if desired_outcome == 'X': #To Lose
            if my_move == 'A': #Rock
                total_score += 1 + 0
            elif my_move == 'B': #Paper
                total_score += 2 + 0
            elif my_move == 'C': #Scissors
                total_score += 3 + 0
        elif desired_outcome == 'Y': #To Draw
            if my_move == 'A': #Rock
                total_score += 1 + 3
            elif my_move == 'B': #Paper
                total_score += 2 + 3
            elif my_move == 'C': #Scissors
                total_score += 3 + 3
        elif desired_outcome == 'Z': #To Win
            if my_move == 'A':#Rock
                total_score += 1 + 6
            elif my_move == 'B':#Paper
                total_score += 2 + 6
            elif my_move == 'C':#Scissors
                total_score += 3 + 6

    return total_score
#Calling function and to calculate final score based on the input data
input_data = read_input()
final_score = calculate_score(input_data)
print("Final Score is:", final_score) #Printing the final score
