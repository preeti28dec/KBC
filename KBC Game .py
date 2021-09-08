que_list=["Who Invented computer","Who invented Internet","When was python developed","what is the fullform of Www."]
opt_list=[["Vint cerf","Mark Jukerberg","Charls babbage","Robert Vintage"],["Vint cerf","vinton cerf", "Guido","John babbage"],["21 feb","20 feb","20 march","19 jan"],["world web wide","world wide web","world web webside","world wide webside"]]
ans_list=[3,1,2,2]
fifty_list=[["Charls babbage","Robert Vintage"],["vint cef","guido"],["21 feb","20 feb"],["world web wide","world wide web"]]
sol_list=[1,1,2,2]
def option():
    index=0
    count=0
    while index<len(que_list):
        print(index+1,que_list[index])
        j=0
        while j<len(ans_list):
            print(j+1,opt_list[index][j])
            j+=1
        user=int(input("enter your option , for lifeline 5050="))
        print("..........")
        if user==ans_list[index]:
            print("congractulation")
        elif user==5050:
            if count==0:
                i=0
                while i<len(fifty_list[i]):
                    print(i+1,fifty_list[index][i])
                    i+=1
                count+=1
                answer=int(input("enter your option="))
                if answer==sol_list[index]:
                    print("Congractualtion")
                else:
                    print("Wrong :(")
                    break
            else:
                print("you Already used your 5050 life line")
            
        else:
            print("You Loose :(")
            break
        index+=1

option()


#that is the final code KBC 
# que=int(input("enter your question number 1 to 3="))
# question = ["How many continents are there?",  "What is the capital of India?",    
#     "NG mei kaun se course padhaya jaata hai?"]
# option= [["Four", "Nine", "Seven", "Eight"],
#     ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
#     ["Counseling", "Software Engineering", "Tourism", "Agriculture"]]
# lenght=len(question[0])
# num=0
# i=0
# while i<3:
#     print(question[i])
#     print(option[i])
#     answer=int(input("enter your answer number 0 to 3="))
#     i=i+1
#     if i==1:
#         if answer==3:
#             print("right answer",option[0][answer])
#         else:
#             print("oppss,wrong answer")
#             break 
#         print()
#     elif i==2:
#         if answer==3:
#             print("right answer",option[1][answer])
#         else:
#             print("wrong,now you are out of game")
#             print("you are now out of game try again")
#             break
#         print()
#     else:
#         if answer==1:
#             print("right answer",option[2][answer])
#             print()
#             print("congratulations you won the game")
#         else:
#             print("wrong,now you are out of game")
#             break