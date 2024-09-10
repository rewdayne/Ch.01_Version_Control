'''
1.0 Jedi Training (17pts)  Name:Dayne Rew


1. Define Forking (1pt): 
The act of copying someone elses code from their
repository and pasting it into your own on GitHub.

2. Define Cloning (1pt): 
Download a copy to my local machine to code in it.

3. Define Branching (1pt):
Makes a clone of a code all in ONE file and allows you to "test out"
possible changes to your code that you might add.

4. Define Committing (1pt): 
Sends a message to the repository to save the changes made to the code and makes
sure you dont lose progress

5. Define Merging (1pt): 
takes code that you made within a branch and adds it to the "master branch"...
Need to make sure your on the branch you want to add the code to in order
 for it to add the new code you want.

6. Define Pushing (1pt):
Pushing adds and collects al of your commits or changes onto your "remote"
repository on GitHub.

7. Define Pull Request (1pt):
Sends a request to add code onto a shared repository ( in this case its on the origional repository "CSP-UHS").
makes sure you dont have conflicting code that will interfere with overall code


8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle
t=turtle.Turtle()
t.speed(250)
turtle.bgcolor('black')
colors = ['pink','blue']
for number in range(400):
    t.forward(number+1)
    t.left(122)
    t.pencolor(colors[number%2])
    "percent symbol means it switches colors every time it changes directions"


t.write('Dayne Rew',font=("times new roman", 16, "normal")) # signs your name to your art
turtle.done()
