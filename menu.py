'''This module contains the main menu portion of the program and acts as an
interface to call the other modules of the program.

Written by Hannah Marks
From 24/10/18 to 12/10/18
'''


import tkinter
import bookcheckout
import bookreturn
import bookweed
import booksearch


# this is where the user id will be stored for use throughout the program.
# initially set to 0 as no user/not logged in.
user=0



# list of acceptable characters for the user and book IDs respectively
accept_char_user_id=['1','2','3','4','5','6','7','8','9']
accept_char_book_id=['0','1','2','3','4','5','6','7','8','9']



# reads the database.txt file into a 2d array for use throughout the program.
# with function automattically closes the file when loop is broken.
database=[]
with open('database.txt','r') as f:
    for database_entry in f:
        database.append(database_entry.split('*'))
        if database_entry == '':
            break
        #loop broken when the code reads an empty line in the file



# reads the logfile.txt file into a 2d array for use in the bookweed module.
# with function automattically closes the file when loop is broken.
log=[]
with open('logfile.txt','r') as f:
    for log_entry in f:
        log.append(log_entry.split('*'))
        if log_entry == '':
            break
       #loop broken when the code reads an empty line in the file




# message displayed when the user is trying to access features without
# logging in.
def please_login():
    '''This function displays a message to the user stating that 
    they are required to log in to use the features of the program.
    '''
    please_login_window=tkinter.Toplevel()
    please_login_window.configure(bg='white')
    please_login_window.title('Error:Not Logged In')
    please_login_window.geometry('300x100')

    message_label=tkinter.Label(please_login_window,
                                text='Please Log in to access this feature',
                                fg='black',
                                bg='white',
                                font='Ariel 10')
    message_label.pack(pady=(25,5))

    ok_button=tkinter.Button(please_login_window,
                             text='Ok',
                             fg='white',
                             bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=20,
                             borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=please_login_window.destroy)
    ok_button.pack()





# message displayed when user is trying to access the book weed function
# without the correct credentials.
def please_login_admin():
    '''This function displays a message to the user stating that
    they are required to log in as an administrator to use the book
    weed feature of the program.
    '''
    please_login_admin_window=tkinter.Toplevel()
    please_login_admin_window.configure(bg='white')
    please_login_admin_window.title('Error:Not Logged in as Administrator')
    please_login_admin_window.geometry('400x100')

    message_label=tkinter.Label(please_login_admin_window,
                                text='Please Log in as an Administrator to access this feature',
                                fg='black',
                                bg='white',
                                font='Ariel 10')
    message_label.pack(pady=(25,5))

    ok_button=tkinter.Button(please_login_admin_window,
                             text='Ok',
                             fg='white',
                             bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=20,
                             borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=please_login_admin_window.destroy)
    ok_button.pack()




# run when search button is clicked in the main menu.
def login_check_search(user):
    ''' Checks that the user has logged in before granting access to the
    feature. If yes the search module is run, if no the 
    appropriate error message is displayed.
    '''
    if user==0:
        please_login()
    else:
        booksearch.search(user,
                          accept_char_book_id,
                          database,
                          log,
                          'database.txt')

# run when checkout button is clicked in the main menu.
def login_check_checkout(user):
    ''' Checks that the user has logged in before granting access to the
    rest of the program. If yes the checkout module is run, if no the 
    appropriate error message is displayed.
    '''
    if user==0:
        please_login()
    else:
        bookcheckout.checkout_window(user,
                                     accept_char_book_id,
                                     database,
                                     log,
                                     'database.txt')

# run when return button is clicked in the main menu.
def login_check_checkin(user):
    ''' Checks that the user has logged in before granting access to the
    rest of the program. If yes the return module is run, if no the 
    appropriate error message is displayed.
    '''
    if user==0:
        please_login()
    else:
        bookreturn.check_in_window_(user,
                                    accept_char_book_id,
                                    database,
                                    log,
                                    'database.txt')

# run when remove button is clicked in the main menu.
def login_check_weed(user):
    ''' Checks that the user has logged in as an administrator 
    before granting access to the rest of the program. If yes 
    the weed module is run, if no the appropriate error message 
    is displayed.
    '''
    if user==0:
        please_login()
    elif user[0]!='a':
        please_login_admin()
    else:
        bookweed.weed_window_(user,
                              accept_char_book_id,
                              database,
                              log,
                              'database.txt')



# run during login function to verify user id
def user_id_error_check(user_input,accept_char_lst,output_msg,login_window):
    '''function that checks that the user input fulfills the criteria for 
    the user id. If yes the user is logged in and the user id stored as 
    the variable user, if no the appropriate error message is displayed.
    '''
    user_id_error=False
    global user
    if len(user_input)!=4:
        user_id_error=True
    elif user_input[0]!='a'and user_input[0]!='s':
        user_id_error=True
    for i in range(1,len(user_input)):
            if user_input[i]not in accept_char_lst:
                user_id_error=True
    if user_id_error==True:
        output_msg.configure(text='Invalid User ID')
        user=0
    else:
        user=user_input
        login_window.destroy()
                

# user log in window
def login():
    '''generates the login window allowing the user to input thier 4 digit
    id, then runs the user_id_error_check function on button press.
    '''
    login_window=tkinter.Toplevel()
    login_window.title('Login')
    login_window.configure(bg='white')
    login_window.geometry('250x350')

    message=tkinter.Label(login_window,text='Please Enter Your\nUser ID',
                          fg='black',bg='white',font='Ariel 10')
    message.pack(pady=(100,10),anchor='center')


    user_id=tkinter.Entry(login_window,
                          fg='black',bg='#ffd1f7',
                          font='Ariel 10',width=28)
    user_id.pack(pady=(0,30))



    login_accept_button=tkinter.Button(login_window,text='Login',
                                       fg='white',bg='#5d00a0',
                                       font='Ariel 10 bold',
                                       width=25,borderwidth=0.1,
                                       activeforeground='white',
                                       activebackground='#b50098',
                                       command=lambda:user_id_error_check(user_id.get(),
                                                                          accept_char_user_id,
                                                                          output_message,
                                                                          login_window))
    login_accept_button.pack()

    output_message=tkinter.Label(login_window,text='',
                                fg='#b50098',bg='white',
                                font='Ariel 10')
    output_message.pack(pady=5)
    







# main menu for entire program.
main = tkinter.Tk()

main.title('Main Menu')
main.configure(bg='white')
main.geometry('500x500')



# login button opens login window on press
login_button=tkinter.Button(main,text='Login',
                            fg='white',bg='#5d00a0',
                            font='Ariel 10 bold',
                            width=20,borderwidth=0.1,
                            activeforeground='white',
                            activebackground='#b50098',
                            command=login)
login_button.pack(anchor='ne',pady=(0,140))


# runs login_check_search on press
search_button=tkinter.Button(main,text='Search',
                             fg='white',bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=30,borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=lambda:login_check_search(user))
search_button.pack(pady=(0,25))


# runs login_check_checkout on press
checkout_button=tkinter.Button(main,text='Chekout Books',
                               fg='white',bg='#5d00a0',font='Ariel 10 bold',
                               width=30,borderwidth=0.1,
                               activeforeground='white',
                               activebackground='#b50098',
                               command=lambda:login_check_checkout(user))
checkout_button.pack(pady=(0,25))


# runs login_check_checkin on press
check_in_button=tkinter.Button(main,text='Return Books',
                               fg='white',bg='#5d00a0',
                               font='Ariel 10 bold',
                               width=30,borderwidth=0.1,
                               activeforeground='white',
                               activebackground='#b50098',
                               command=lambda:login_check_checkin(user))
check_in_button.pack(pady=(0,25))



admin_label=tkinter.Label(main,text='Administrator Use Only',
                          fg='black',bg='white',
                          font='Ariel 10 bold')
admin_label.pack(pady=(25,0))


# runs login_check_weed on press
remove_button=tkinter.Button(main,text='Remove Books',
                             fg='white',bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=30,borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=lambda:login_check_weed(user))
remove_button.pack()


# exits the program
quit_button=tkinter.Button(main,text='Quit',
                           fg='white',bg='#5d00a0',
                           font='Ariel 10 bold',
                           width=20,borderwidth=0.1,
                           activeforeground='white',
                           activebackground='#b50098',
                           command=main.destroy)
quit_button.pack(side='bottom',anchor='se')



main.mainloop()

