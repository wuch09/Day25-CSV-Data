from turtle import Screen, Turtle
import pandas

score =0
screen = Screen()
screen.setup(725, 491)
screen.title("US States Quiz Game")
screen.bgpic("blank_states_img.gif")

us_data = pandas.read_csv("50_states.csv")
all_state = us_data.state.to_list()
guessed_state = []
while len(guessed_state) < 50:
    user_guess = screen.textinput(f"{score}/50", "Please Input the State Name")
    if user_guess == "Exit":
        missing_state = [state for state in all_state if state not in guessed_state]
        missing_data = pandas.DataFrame(missing_state)
        missing_data.to_csv("states_to_learn.csv")


        break
    if user_guess in all_state:
        guessed_state.append(user_guess)
        score +=1
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = us_data[us_data.state == user_guess]

        # print(f"state location : ({state_data.x},{state_data.y})")
        t.goto(int(state_data.x), int(state_data.y))

        t.write(f"{user_guess}", align="center", font= ("Arial", 10, "normal"))
csv_data = pandas.DataFrame(guessed_state)
csv_data.to_csv("user_guessed.csv")
#save the current data to csv file

screen.exitonclick()
#
# print(us_data.state)
# game_is_on = True
# #
# # while game_is_on:
# #     user_guess = screen.textinput(f"{score}/50" ,"Please Input the State Name")
# #     print(user_guess)
#
#
# screen.exitonclick()
#

# pen = Turtle()
# pen.color("pink")
# pen.penup()
# pen.goto(-38, -106)
# pen.fillcolor("pink")

#input: "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
#output : "squirrel_count.csv"
# find from "Primary Fur Color" "count"
#output :
#         Fur Color  Count
#    0      grey      2473
#    1      red       392
#    2      black     103
# example : how to transit dict to csv

# data_dict = {
# 	"Students" : ["Amy", "James", "Angela"],
# 	"Scores" : [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# import pandas
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# output = []
# gray_Squirrel =data[data["Primary Fur Color"] == "Gray"]
# red_Squirrel =data[data["Primary Fur Color"] == "Cinnamon"]
# black_Squirrel =data[data["Primary Fur Color"] == "Black"]
#
# num_of_gray = len(gray_Squirrel)
# num_of_red = len(red_Squirrel)
# num_of_black = len(black_Squirrel)
# data_dict = []
# data_dict.append(["gray","red","black"])
#
# data_dict ={"Fur Color": ["gray", "red", "black"],
#             "Count": [num_of_gray,num_of_red, num_of_black]}
# print(data_dict)
# output_data= pandas.DataFrame(data_dict)
# output_data.to_csv("new_data.csv")

# data_dict["gray"] = num_of_gray
# data_dict["red"] = num_of_red
# data_dict["black"] = num_of_black

# print(data_dict)
















#monday = data[data.day == "Monday"]

# print(monday.temp *1.8 + 32)

# print(data[data.temp == data.temp.max()])

# mean = data["temp"].mean()
# max = data["temp"].max()
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())

# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature .append(row[1])
#     print(temperature)



