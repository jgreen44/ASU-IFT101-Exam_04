#   Filename:           Exam 4
#   Created by:         jasongreen
#   Date:               Sunday, February 17, 2019
#   Time of Creation:   14:13
#   ---

# wages = []
# gender = []
# counter = 0
# total_male = 0
# average_male = 0
# total_female = 0
# average_female = 0
#
# while counter < 10:
#     wages.append(int(input("What is your wage? ")))
#     gender.append(input("What is your gender? (type m/f) "))
#     counter += 1
#
# for i in range(len(wages)):
#     if gender[i] == "m":
#         total_male = total_male + wages[i]
#         average_male = total_male / gender.count("m")
#     elif gender[i] == "f":
#         total_female = total_female + wages[i]
#         average_female = total_female / gender.count("f")
#
# if gender.count("m") > 0:
#     print("The average wages for males is ${:.2f}.".format(average_male))
#     # print(gender.count("m"))
# else:
#     print("No males reported wages!")
#
# if gender.count("f") > 0:
#     print("The average wages for females is ${:.2f}.".format(average_female))
#     # print(gender.count("f"))
# else:
#     print("No females reported wages!")

# ratings = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 5, 4, 4, 4, 4, 3, 4, 5, 5, 5, 5, 5]
#
# # do not need to close txt file when using WITH
# with open("ratings.txt", "w") as ratings_file:
#     for i in ratings:
#         print(i, file=ratings_file)


total = 0
counter = 0
ratings = []
with open("ratings.txt", "r") as ratings_file:
    for i in ratings_file:
        ratings.append(i.strip('\n'))
        counter += 1
        total = total + int(i)

print("The average ratings is {}.".format(total / counter))



