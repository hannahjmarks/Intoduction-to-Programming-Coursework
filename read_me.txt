Introduction to Programming Coursework

By Hannah Marks
11/12/18

This project is a simple library management system. Users are able to search 
the book database, checkout and return books and weed the database.

To run the program run the 'menu' module
*running any of the other modules will run them in test mode*

Book id's are 6 digits in length and can only contain numbers 0-9

With the menu open the user must first log in using their 4 characted id in 
order to access the features of the program.
(user id's begin with 'a' for administrator or 's' for student followed by 3 numbers in 
range 1-9)

After successful log in the user can access the other modules by clicking thier 
respective buttons on the menu:


Search Module:
Users can search by title only.
The search item can be a partial title, is case insensitive and cannot contain '*'
('*' is used to split elements in the database file). If there are no search results 
or the input is invalid the user will be informed by a message pop-up. Results are 
displayed in a list showing the book id, title, author and availibility.


Checkout Module:
Users must use book id's to checkout books (as there are multiple books with the same 
title).
Book id's will be checked for validity, it will then be checked that it exists in the database
and that it is not already on loan to another user. If the book id is valid and the book 
is availible the book is checked out. The database and log files are then updated with
the new data.


Return Module:
Users must use book id's to checkout books (as there are multiple books with the same 
title).
Book id's will be checked for validity, it will then be checked that is exists in the database
and has not already been returned, it then checks that the user id that is trying to 
return the book is an administrator or matches the user id that checked the book out. If 
these conditions are met the book is returned. The database and log files are then 
updated with the new data.


Weed Module:
*Only administrators can access this feature*

To display all the books that have not been checked out in the selected timeframe select a
radio button and press the display button. (The books to be deleted are up to the users 
judgement).

Users must use book id's to checkout books (as there are multiple books with the same 
title).
Book id's will be checked for validity, it will then be checked that it exists in the database.
If the book id is valid a message is displayed asking the user to confirm deletion. The
database entry is then deleted and the database file updated.