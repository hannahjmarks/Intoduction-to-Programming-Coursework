'''This module contains all neccessary functions to return books to the
database. Books are returned by id code in order to distinguis between
individual books of the same title. The user id is also checked to make
sure that the books are being returned by the correct user.

Written by Hannah Marks
From 25/10/18 to 12/10/18
'''


import tkinter
import datetime


# message displayed when user is trying to return a book which is not
# on loan.
def already_checked_in():
    '''This function displays an Error message to the user stating that the
    book they are trying to return has already been returned on the system.
    '''
    already_checked_in_window=tkinter.Toplevel()
    already_checked_in_window.configure(bg='white')
    already_checked_in_window.title('Error:Invalid Book Return')
    already_checked_in_window.geometry('300x100')

    message_label=tkinter.Label(already_checked_in_window,
                                text='This Book has already been Returned\nPlease Try Again',
                                fg='black',
                                bg='white',
                                font='Ariel 10')
    message_label.pack(pady=(25,5))

    ok_button=tkinter.Button(already_checked_in_window,
                             text='Ok',
                             fg='white',
                             bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=20,
                             borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=already_checked_in_window.destroy)
    ok_button.pack()




# message displayed when the user has entered an invalid book ID code.
def book_id_error_message():
    '''This function displays an Error message to the user stating that the
    book ID code they are trying to enter is invalid.
    '''
    book_id_error_message_window=tkinter.Toplevel()
    book_id_error_message_window.configure(bg='white')
    book_id_error_message_window.title('Error:Invalid Book ID')
    book_id_error_message_window.geometry('200x100')

    message_label=tkinter.Label(book_id_error_message_window,
                                text='Invalid Book Id\nPlease Try Again',
                                fg='black',
                                bg='white',
                                font='Ariel 10')
    message_label.pack(pady=(25,5))

    ok_button=tkinter.Button(book_id_error_message_window,
                             text='Ok',
                             fg='white',
                             bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=20,
                             borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=book_id_error_message_window.destroy)
    ok_button.pack()



# message displayed during search function when there are no search results.
def no_results():
    '''This function displays an Error message to the user stating that 
    there were no results matching their search criteria.
    '''
    no_results_window=tkinter.Toplevel()
    no_results_window.configure(bg='white')
    no_results_window.title('Error:No Search Results')
    no_results_window.geometry('200x100')

    message_label=tkinter.Label(no_results_window,
                                text='No Results Found\nPlease Try Again',
                                fg='black',
                                bg='white',
                                font='Ariel 10')
    message_label.pack(pady=(25,5))

    ok_button=tkinter.Button(no_results_window,
                             text='Ok',
                             fg='white',
                             bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=20,
                             borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=no_results_window.destroy)
    ok_button.pack()


# wrong user message displayed in the bookreturn.book_id_check function 
# if the user id entered fails to meet criteria. 
def wrong_user():
    '''This function displays an Error message to the user stating that the
    user ID they have logged in with does not match the used ID used to 
    check out the book they are trying to return. In order to return this
    book they will need to log in with the correct ID.
    '''
    wrong_user_window=tkinter.Toplevel()
    wrong_user_window.configure(bg='white')
    wrong_user_window.title('Error:Invalid User')
    wrong_user_window.geometry('400x100')

    message_label=tkinter.Label(wrong_user_window,
                                text='Books must be returned by the user who checked them out\nPlease Try Again',
                                fg='black',
                                bg='white',
                                font='Ariel 10')
    message_label.pack(pady=(25,5))

    ok_button=tkinter.Button(wrong_user_window,
                             text='Ok',
                             fg='white',
                             bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=20,
                             borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=wrong_user_window.destroy)
    ok_button.pack()




# message displayed when user has successfully returned a book.
def check_in_success():
    '''This function displays a message to the user stating that they
    have successfully returned a book to the system.
    '''
    check_in_success_window=tkinter.Toplevel()
    check_in_success_window.configure(bg='white')
    check_in_success_window.title('Success')
    check_in_success_window.geometry('300x100')

    message_label=tkinter.Label(check_in_success_window,
                                text='Book was Successfully Returned',
                                fg='black',
                                bg='white',
                                font='Ariel 10')
    message_label.pack(pady=(25,5))

    ok_button=tkinter.Button(check_in_success_window,
                             text='Ok',
                             fg='white',
                             bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=20,
                             borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=check_in_success_window.destroy)
    ok_button.pack()






# main book return function
def check_in(user,database,log,user_input,database_file):
    ''' This function updates the database array entry with '0' in the user
    id field to show that the book has been returned and writes the updated array
    to database.txt. It also updates the log array and logfile.txt with
    the book id, user id, date and that the book was returned. If 
    check in is successful the appropriate message is displayed.
    '''
    success=False
    date=str(datetime.date.today())
    for i in range (0,len(database)):
        if user_input in database[i][0]:
            database[i][3]='0\n'
            log.append(database[i][0]+'*'+user+'*'+date+'*RETURN\n')
            check_in_success()
            success=True
            break
    if success==True:
        with open('logfile.txt','a') as logfile:
            logfile.write(database[i][0]+'*'+user+'*'+date+'*RETURN\n')
        with open(database_file,'w') as database_file:
            #writes whole updated database array to the file
            for i in range(0,len(database)):
                database_file.write(database[i][0]+'*'+database[i][1]+'*'
                                    +database[i][2]+'*'+database[i][3])


# checks the user input for invalid book id
def book_id_check(user,accept_char_lst,database,log,user_input,database_file):
    ''' This function checks that the user input is a valid book id code
    by checking the length and comparing the individual characters to the
    acceptable characters list (b). It then searches the database to check
    that a book with that id code exists and then checks if the book is on 
    loan, the user id entered during the login function is then compared to
    the user id in the database array to check that the correct user is trying
    to return the book. If the input fails to meet any of these conditions 
    the appropriate error message is displayed, otherwise the check in 
    function is run.
    '''
    book_id_error=False
    book_found=False
    index=0
    if len(user_input)!=6:
        book_id_error=True
    for i in range (0,len(user_input)):
        if user_input[i] not in accept_char_lst:
            book_id_error=True
    if book_id_error==True:
        book_id_error_message()
    else:
        for i in range (0,len(database)):
            if user_input in database[i][0]:
                book_found=True
                index=i
        if book_found==False:
            no_results()
        elif '0' in database[index][3]:
            #database[index][3] is used so that only the user id element is compared
            already_checked_in()
        elif user not in database[index][3] and user[0]!='a':
            wrong_user()
        else:
            check_in(user,database,log,user_input,database_file)



# window for book return
def check_in_window_(user,accept_char_lst,database,log,database_file):
    '''displays the check in window for the user to enter the id code of
    the book they wish to return.
    '''
    check_in_window=tkinter.Toplevel()
    check_in_window.configure(bg='white')
    check_in_window.title('Book Return')
    check_in_window.geometry('400x400')


    menu_button=tkinter.Button(check_in_window,
                               text='Main Menu',
                               fg='white',
                               bg='#5d00a0',
                               font='Ariel 10 bold',
                               width=20,
                               borderwidth=0.1,
                               activeforeground='white',
                               activebackground='#b50098',
                               command=check_in_window.destroy)
    menu_button.pack(pady=(0,100),anchor='nw')

    check_in_item_label=tkinter.Label(check_in_window,
                                      text='Please Enter the ID Number of the Book\nyou wish to Return:',
                                      fg='black',
                                      bg='white',
                                      font='Ariel 14')
    check_in_item_label.pack(pady=(0,5))

    #entry box for user to input book id, get function is used to convert
    #the input into a variable for use in other functions.
    check_in_item_input=tkinter.Entry(check_in_window,
                                      width=30,
                                      fg='black',
                                      bg='white',
                                      font='Ariel 10')
    check_in_item_input.pack(pady=5)

    check_in_item_button=tkinter.Button(check_in_window,
                                        text='Return',
                                        fg='white',
                                        bg='#5d00a0',
                                        font='Ariel 10 bold',
                                        width=25,
                                        borderwidth=0.1,
                                        activeforeground='white',
                                        activebackground='#b50098',
                                        command=lambda:book_id_check(user,
                                                                     accept_char_lst,
                                                                     database,
                                                                     log,
                                                                     check_in_item_input.get(),
                                                                     database_file))

    check_in_item_button.pack(pady=5)


if __name__=='__main__':

    #test data and test database file in order to preserve the integrity of the real database
    user = 'test'
    accept_char = ['0','1','2','3','4','5','6','7','8','9']
    database = [['000000','Test_1','Author_Test_1','test\n'],
                ['000001','Test_2','Author_Test_2','test\n'],
                ['000002','Test_3','Author_Test_3','test\n']]
    log = []
    database_file = 'database_test.txt'

    #runs check in function using the above test data
    check_in_window_ (user,accept_char,database,log,database_file)
