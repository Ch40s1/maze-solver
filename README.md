# maze-solver

## Getting started

clone the repository and add permissions of the main.sh file
if the file has execution privileges the run
```
./main.sh
```
else run
```
python src/main.py or python3 src/main.py
```

The project uses the tkinter module. It should come with your version of python
if the you get an error try installing tkinter or delete and reinstall python if you already know
you have tkinter.

When we run the file it tkinter creates a window that will hold the maze solver

### Preview
<img src="./gifs/mazegif.gif" alt="maze animation" width="500" height="300">


### Requirements
1. Python 3.12.2
2. tkinter 3.12.2

### Future ideas

* Add other solving algorithms, like breadth-first search or A*
* Make the visuals prettier, change the colors, etc
* Mess with the animation settings to make it faster/slower. Maybe make backtracking slow and blazing new paths faster?
* Add configurations in the app itself using Tkinter buttons and inputs to allow users to change maze size, speed, etc
* Make much larger mazes to solve
* Make it a game where the user chooses directions
* Allow the user to race an algorithm
* Make it 3 dimensional
* Time the various algorithms and see which ones are the fastest
