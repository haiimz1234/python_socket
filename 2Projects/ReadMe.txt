The project contains 2 projects
1 projectManyThreads
   Lets a lot of clients  to connect  but the client must make connection every query See client code.
Log Files:
In the example you have 2 log files one global , and one you can use it to every IP connection. ( If you add some simple code - you can use the code in project to set log file only to one IP).
Also at the global file I add locking between threads.
This project has an example also of an info listing.
The code use list as a stack.  
I  add Locking technique as in logging code.
The stack and log file  is basically the same in the two projects but at the other project I dont add the info message and locking nechanizim ( In the log file and stack file).

Of course, the log code can be expands

2.LessThreades_ClientMoreQuick
The CLIENT need connect one time . but the number of users is limited
I use simple list without loocking because for premative options it safe threading 
( Also in the first example you dont need  the stack code   for premative options).

  In the  first project PORT is dynamic so I print it  in a window
  You need to change it and hard coded the  IP and PORT and change the code accordingly.
 
  In the second project  the IP and PORT is hard codded and you  must change it   
