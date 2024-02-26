#------------------------------------------------------------
#Assignment:   Assignment 5C
#
#Program Name: Assignment_5C.rb
#
#
#Purpose:      Create a program displaying a question and asking the user to answer it. At the end calculate how many he got right and display it.
#
#
#Author:       Jairo Gutierrez
#Course:       CIS109 Spring 2024
#
#
#Created:      February 25, 2024
#
#------------------------------------------------------------
puts"Welcome to the Question-and-Answer Program"
puts"Please select the correct answer for each question"
puts
correct = 0 #Variable initialized to start at 0
puts"1.Ruby syntax is similar to Python?"
puts"(a) True"
puts"(b) False"
puts"(c) They are identical"
puts"(d) Ruby does not have syntax"
print "Your answer:\n" #Prompt user for input
answer = gets.chomp #Read user input
if answer == "a" #Decision structure to check if user input is correct
correct +=1
puts"Correct"
else
puts"Oops - the correct answer is a"
end
puts
puts"2.What text editor can you use to create a Ruby Program?"
puts"(a) Microsoft Word"
puts"(b) Microsoft Paint"
puts"(c) Rich Text Editor"
puts"(d) Komodo"
print "Your answer:\n" #Prompt user for input
answer = gets.chomp #Read user input
if answer == "d" #Decision structure to check if user input is correct
correct +=1
puts"Correct"
else
puts"Oops - the correct answer is d"
end 
puts
puts"3.In the following for loop, how many times will i love the cheese print?"
puts"for num in 0..5
        puts I love cheese
end"
puts"(a) 0"
puts"(b) 4"
puts"(c) 5"
puts"(d) 6"
print "Your answer:\n" # Prompt user for input 
answer = gets.chomp #Read user input
if answer == "d" #Decision structure to check if user input is correct
correct +=1
puts"Correct"
else
puts"Oops - the correct answer is d"
end 
puts
puts"4.Ruby allows for the if/elsif?"
puts"(a) Only if the if/else is used first"
puts"(b) Only if the if/then is used first?"
puts"(c) True"
puts"(d) False"
print"Your answer:\n" #Prompt user for input 
answer = gets.chomp #Read user input
if answer == "c" #Decission structure to check if user input is correct
correct +=1
puts"Correct"
else
puts"Oops - the correct answer is c"
end
puts
puts"5.Ruby only allows lower case variable names?"
puts"(a) True"
puts"(b) False"
print"Your answer:\n" #Prompt user for input 
answer = gets.chomp #Read user input 
if answer == "b" #Decision structure to check if user input is correct
correct +=1
puts"Correct"
else
puts"Oops - the correct answer is b"
puts
num_correct = (correct / 5.0) * 100 #Calculate the percentage of correct answers
percentage = num_correct * 100 
puts"You correclty answered #{correct} questions out of 5 which is {percentage}%"
end