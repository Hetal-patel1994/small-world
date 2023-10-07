# small-world
Designed and implemented an algorithm related to strings.


Problem definition: 
An algorithm that calculates the shortest connection between movie casts. 
The first two casts on the list are the most important, such that if there is at least one string in common, the shortest connection is 1. 
If those two casts have no strings in common, then look for another cast in the list of casts that has a string in common, and the shortest connection is 2. 
Otherwise, the shortest connection is more than 2 or there is no connection.

Algorithm:
- Input the name of the file that contains the CAST. CAST is in a text file where every line in the file is a cast
- Initialize a casts list which contains a list of casts
- Read the file line-by-line.
  - Strip the newline and split every line by a comma(,)
  - For each actor in the list of actor
    - Strip leading and trailing whitespaces from it
    - append it to the actors list
  - append the actors list to the casts list
- if casts list is empty or length of casts < 2 then
  - print Number of casts must be greater than 2
  - exit the execution
- else
  - find common actor between the first cast and second cast
  - if common actor is found then
    - print Shortest connection = 1
  - else
    - for every cast j in casts
      - find a common actor between cast j and first cast and find a common actor between cast j and second cast
      - if found:
        - print Shortest connection = 2
      - else
        - print Shortest connection > 2 or no connection

Execution of code:
You need to have Python3 installed to run this code. Please execute this code by running the main.py file.
Type the command:
```
python3 main.py
```

You will see an input to enter the filename. 
Please enter the filename from any of the files contained in our folder(e.g. Test1.txt). You will see the output on the console for the respective. 
To test for other cases, please create a file and pass the name of the file while running the main.py file.

The format of the file will be as follows:
- number of casts(eg. 4)
- 1st cast
- 2nd cast
- 3rd cast
- 4th cast

For eg. The file Test1.txt contains.

> 4<br>Carrie-Anne Moss,Gloria Foster,Hugo Weaving,Joe Pantoliano,Keanu Reeves,Laurence Fishburne,Marcus Chong 
> <br>Andre Braugher,Beau Garrett,Chris Evans, Doug Jones, Ioan Gruffudd,Jessica Alba,Julian McMahon,Kerry Washington,Laurence Fishburne,Michael Chiklis 
> <br>Ewan McGregor, Ian McDiarmid, Jake Lloyd, Liam Neeson, Natalie Portman<br>Angela Bassett,Chadwick Boseman,Danai Gurira,Daniel Kaluuya,Forest Whitaker,Letitia Wright,Lupita Nyong'o,Martin Freeman,Michael B. Jordan,Sterling K. Brown, Winston Duke
