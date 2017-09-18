# Sudoku

## Current work
### Python
Python verison trys to crack sudoku puzzle by its basic rules. 
Initially, every empty entry has 9 possible solutions. So a 9\*9\*9 tensor is created to store the possible answers. After reading a non-empty entry, it eliminates the same number from entries on the same row, column and current 3\*3 cube. In this way the number of possible solutions on entries become fewer and fewer until the correct one remains. 

## Todo
* Test if a puzzle is valid.
* Mulitple languages
