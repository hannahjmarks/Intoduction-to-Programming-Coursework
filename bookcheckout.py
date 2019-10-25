'''This module contains all neccessary functions to checkout books from the
database. Books are checked out by id code in order to distinguis between
individual books of the same title.

Written by Hannah Marks
From 25/10/18 to 12/10/18
'''


import tkinter
import datetime

# message displayed when the user is trying to check out a book that has
# already been checkked out.
def book_not_availible():
    '''This function displays an Error message to the user stating that the
    book they are trying to check out has already been checked out by another 
    user.
    '''
    book_not_availible_window=tkinter.Toplevel()
    book_not_availible_window.configure(bg='white')
    book_not_availible_window.title('Error:Invalid Book')
    book_not_availible_window.geometry('300x100')

    message_label=tkinter.Label(book_not_availible_window,
                                text='This Book has already been Checked Out\nPlease Try Again',
                                fg='black',
                                bg='white',
                                font='Ariel 10')
    message_label.pack(pady=(25,5))

    ok_button=tkinter.Button(book_not_availible_window,
                             text='Ok',
                             fg='white',
                             bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=20,
                             borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=book_not_availible_window.destroy)
    ok_button.pack()



# message displayed when the user has successfully checked out a book.
def checkout_success():
    '''This function displays a message to the user stating that they
    have successfully checked a book out of the system.
    '''
    checkout_success_window=tkinter.Toplevel()
    checkout_success_window.configure(bg='white')
    checkout_success_window.title('Success')
    checkout_success_window.geometry('300x100')

    message_label=tkinter.Label(checkout_success_window,
                                text='Book was Successfully Checked Out',
                                fg='black',
                                bg='white',
                                font='Ariel 10')
    message_label.pack(pady=(25,5))

    ok_button=tkinter.Button(checkout_success_window,
                             text='Ok',
                             fg='white',
                             bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=20,
                             borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=checkout_success_window.destroy)
    ok_button.pack()


# message displayed during search function when there are no search results.
def no_results():
    '''This function displays an Error message to the user stating that 
    there were no results matching their search criteria.
    '''
    no_results_window=tkinter.Toplevel()
    no_results_window.configure(bg='white')
    no_results_window.title('Error:No Results Found')
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



# main book checkout function
def checkout(user,database,log,user_input,database_file):
    ''' This function updates the database array entry with the user id to
    show that the book has been checked out and writes the updated array
    to database.txt. It also updates the log array and logfile.txt with
    the book id, user id, date and that the book was checked out. If 
    checkout is successful the appropriate message is displayed.
    '''
    success=False
    date=str(datetime.date.today())
    for i in range (0,len(database)):
        if user_input in database[i][0]:
            database[i][3]=user+'\n'
            log.append(database[i][0]+'*'+user+'*'+date+'*CHECKOUT\n')
            checkout_success()
            success=True
            break
    if success==True:
        with open('logfile.txt','a') as logfile:
            logfile.write(database[i][0]+'*'+user+'*'+date+'*CHECKOUT\n')
        with open(database_file,'w') as database_file:
            #writes the whole updated database array to the file
            for i in range(0,len(database)):
                database_file.write(database[i][0]+'*'+database[i][1]+'*'
                                    +database[i][2]+'*'+database[i][3])


# checks user input for invalid book id
def book_id_check(user,accept_char_lst,database,log,user_input,database_file):
    ''' This function checks that the user input is a valid book id code
    by checking the length and comparing the individual characters to the
    acceptable characters list (b). It then searches the database to check
    that a book with that id code exists and then checks if the book is
    availible to be checked out. If the input fails to meet any of these 
    conditions the appropriate error message is displayed, otherwise the 
    checkout function is run.
    '''
    book_id_error=False
    book_found=False
    book_availible=True
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
                if '0' not in database[i][3]:
                    book_availible=False


        if book_found==False:
            no_results()
        elif book_found==True and book_availible==False:
            book_not_availible()
        else:
            checkout(user,database,log,user_input,database_file)



# displays checkout window
def checkout_window(user,accept_char_lst,database,log,database_file):
    '''displays the checkout window for the user to enter the id code of
    the book they wish to checkout.
    '''
    check_out_window=tkinter.Toplevel()
    check_out_window.configure(bg='white')
    check_out_window.title('Checkout')
    check_out_window.geometry('400x400')


    menu_button=tkinter.Button(check_out_window,
                               text='Main Menu',
                               fg='white',
                               bg='#5d00a0',
                               font='Ariel 10 bold',
                               width=20,
                               borderwidth=0.1,
                               activeforeground='white',
                               activebackground='#b50098',
                               command=check_out_window.destroy)
    menu_button.pack(pady=(0,100),anchor='nw')

    checkout_item_label=tkinter.Label(check_out_window,
                                      text='Please Enter the ID Number of the Book\nyou wish to Checkout:',
                                      fg='black',
                                      bg='white',
                                      font='Ariel 14')
    checkout_item_label.pack(pady=(0,5))

    #entry box for user input, the get command is used to convert the
    #input to a variable for use in other functions.
    checkout_item_input=tkinter.Entry(check_out_window,
                                      width=30,
                                      fg='black',
                                      bg='white',
                                      font='Ariel 10')
    checkout_item_input.pack(pady=5)

    checkout_item_button=tkinter.Button(check_out_window,
                                        text='Checkout',
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
                                                                     checkout_item_input.get(),
                                                                     database_file))

    checkout_item_button.pack(pady=5)


if __name__=='__main__':

    #test data and test database file in order to preserve the integrity of the real database
    user = 'test'
    accept_char = ['0','1','2','3','4','5','6','7','8','9']
    database = [['000000','Test_1','Author_Test_1','0\n'],
                ['000001','Test_2','Author_Test_2','0\n'],
                ['000002','Test_3','Author_Test_3','0\n']]
    log = []
    database_file = 'database_test.txt'

    #runs checkout function using the above test data
    checkout_window (user,accept_char,database,log,database_file)

