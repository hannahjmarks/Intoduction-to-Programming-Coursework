'''This module contains all the neccessary functions to weed the database.
It can only be accessed by users with an administrator login and displays
the books that have not been checked out in a selected timeframe. Books are
removed individually by book id.

Written by Hannah Marks
From 26/10/18 to 12/10/18
'''


import tkinter
import datetime


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


# user confirmation message displayed during the bookweed.weed function
# asking the user to confirm their deletion request.
def user_confirmation_weed(database,user_input,database_file):
    '''This function generates a message to the user asking them to confirm
    that they wish for the book to be removed from the database.
    '''
    user_confirmation_window=tkinter.Toplevel()
    user_confirmation_window.configure(bg='white')
    user_confirmation_window.title('Confirm')
    user_confirmation_window.geometry('350x150')

    message_label=tkinter.Label(user_confirmation_window,
                                text='Are you sure you wish to Permenantly Delete\n'+user_input+'\nfrom the Database?',
                                fg='black',
                                bg='white',
                                font='Ariel 10 bold')
    message_label.pack(pady=(20,5))

    yes_button=tkinter.Button(user_confirmation_window,
                              text='Yes',
                              fg='white',
                              bg='#5d00a0',
                              font='Ariel 10 bold',
                              width=10,
                              borderwidth=0.1,
                              activeforeground='white',
                              activebackground='#b50098',
                              command=lambda:weed(database,
                                                  user_input,
                                                  user_confirmation_window,
                                                  database_file))
    yes_button.pack(pady=5)

    no_button=tkinter.Button(user_confirmation_window,
                             text='No',
                             fg='white',
                             bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=10,
                             borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=user_confirmation_window.destroy)
    no_button.pack()




# weed success message displayed during book weed function if the user
# has successfully removed a book.
def weed_success():
    '''This function displays a message to the user stating that they
    have successfully removed a book from the system.
    '''
    weed_success_window=tkinter.Toplevel()
    weed_success_window.configure(bg='white')
    weed_success_window.title('Success')
    weed_success_window.geometry('300x100')

    message_label=tkinter.Label(weed_success_window,
                                text='Book was Successfully Removed',
                                fg='black',
                                bg='white',
                                font='Ariel 10')
    message_label.pack(pady=(25,5))

    ok_button=tkinter.Button(weed_success_window,
                             text='Ok',
                             fg='white',
                             bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=20,
                             borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=weed_success_window.destroy)
    ok_button.pack()






# main database weed function
def weed(database,user_input,user_conf_window,database_file):
    '''function that permenantly removes an item from the database and writes
    the updated database array to the database.txt file. If successful a 
    message is shown to the user.
    '''
    user_conf_window.destroy()
    success=False
    for i in range (0,len(database)):
        if user_input in database[i][0]:
            del(database[i])
            weed_success()
            success=True
            break
    if success==True:
        with open(database_file,'w') as f:
            for i in range(0,len(database)):
                f.write(database[i][0]+'*'+database[i][1]+'*'
                        +database[i][2]+'*'+database[i][3])



# function to check user input
def book_id_check(accept_char_lst,database,user_input,database_file):
    '''This function checks that the user input is a valid book id code
    by checking the length and comparing the individual characters to the
    acceptable characters list (b). It then searches the database to check
    that a book with that id code exists. If the input fails to meet any 
    of these conditions the appropriate error message is displayed, 
    otherwise the user confirmation function is run.
    '''
    book_id_error=False
    book_found=False
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
        if book_found==False:
            no_results()
        else:
            user_confirmation_weed(database,user_input,database_file)

#helper function to calculate time difference
def time_diff(logdate):
    '''function that calculates the difference in days between the date
    given in the log entry and the current date.
    '''
    current_date=datetime.date.today()
    datetimeFormat = '%Y-%m-%d'
    diff=current_date- datetime.datetime.strptime(logdate, datetimeFormat).date()
    diff_days=diff.days
    return diff_days


# main time checking function
def time_check(database,log,timeframe,output_listbox):
    ''' This function is used to help advise the user of which books they may
    wish to weed from the database by displaying the length of time it has
    been since it was last checked out. It first generates a list of all the
    checkout log entries from the log array, then 
    '''
    log_checkout=[]
    log_results=[]
    database_results=[]
    in_use=[]
    is_in_use=False
    for i in range(0,len(log)-1):
        if 'CHECKOUT' in log[i][3]:
            log_checkout.append(log[i])
    output_listbox.delete(0,'end')
    output_listbox.insert(0,'%-6s'%'ID'+'|'+'%-125s'%'Title'+'|'
                 +'%-40s'%'Author(s)')
    i=len(log_checkout)-1

    if timeframe=='0':
        while i>-1:
            logdate=log_checkout[i][2]
            if time_diff(logdate)<90:
                in_use.append(log_checkout[i])
            i-=1
        for k in range(0,len(log_checkout)):
            for j in range(0,len(in_use)):
                if log_checkout[k][0] in in_use[j][0]:
                    is_in_use=True
                    break
                else:
                    is_in_use=False
            if is_in_use==False:
                log_results.append(log_checkout[k])

    elif timeframe=='1':
         while i>-1:
            logdate=log_checkout[i][2]
            if time_diff(logdate)<180:
                in_use.append(log_checkout[i])
            i-=1
         for k in range(0,len(log_checkout)):
             for j in range(0,len(in_use)):
                 if log_checkout[k][0] in in_use[j][0]:
                     is_in_use=True
                     break
                 else:
                     is_in_use=False
             if is_in_use==False:
                 log_results.append(log_checkout[k])

    else:
         while i>-1:
            logdate=log_checkout[i][2]
            if time_diff(logdate)<365:
                in_use.append(log_checkout[i])
            i-=1
         for k in range(0,len(log_checkout)):
             for j in range(0,len(in_use)):
                 if log_checkout[k][0] in in_use[j][0]:
                     is_in_use=True
                     break
                 else:
                     is_in_use=False
             if is_in_use==False:
                 log_results.append(log_checkout[k])


    for k in range (0,len(log_results)):
        for j in range(0,len(database)):
            if log_results[k][0] in database[j][0]:
                database_results.append(database[j])
                break
    for k in range (0,len(database_results)):
        output_listbox.insert('end','%-6s'%database_results[k][0]+'|'
                              +'%-125s'%database_results[k][1]+'|'
                              +'%-40s'%database_results[k][2])






# window for database weeding
def weed_window_(user,accept_char_lst,database,log,database_file):
    '''displays the book weed window for an administrator user to enter the id
    codes of the books they wish to remove from the database. It also allows
    the user to check if books have not been checked out for a user specified
    amount of time.
    '''
    weed_window=tkinter.Toplevel()
    weed_window.configure(bg='white')
    weed_window.title('Remove Book')
    weed_window.geometry('1500x550')


    menu_button=tkinter.Button(weed_window,
                               text='Main Menu',
                               fg='white',
                               bg='#5d00a0',
                               font='Ariel 10 bold',
                               width=20,
                               borderwidth=0.1,
                               activeforeground='white',
                               activebackground='#b50098',
                               command=weed_window.destroy)
    menu_button.pack(pady=(0,5),anchor='nw')


    last_checkout=tkinter.Label(weed_window,
                                text='Display all books not checked out in the last:',
                                fg='black',
                                bg='white',
                                font='Ariel 10')

    last_checkout.pack(padx=(75,0),pady=5,anchor='w')


    timeframe=tkinter.StringVar(weed_window)
    timeframe.set(0)

    three_month_radbutton=tkinter.Radiobutton(weed_window,
                                          text='3 months',
                                          fg='#b50098',
                                          bg='white',
                                          font='Ariel 10 bold',
                                          activeforeground='#5d00a0',
                                          activebackground='white',
                                          variable=timeframe,
                                          value=0)
    three_month_radbutton.pack(padx=75,pady=1,anchor='w')

    six_month_radbutton=tkinter.Radiobutton(weed_window,
                                          text='6 months',
                                          fg='#b50098',
                                          bg='white',
                                          font='Ariel 10 bold',
                                          activeforeground='#5d00a0',
                                          activebackground='white',
                                          variable=timeframe,
                                          value=1)
    six_month_radbutton.pack(padx=75,pady=1,anchor='w')

    twelve_month_radbutton=tkinter.Radiobutton(weed_window,
                                          text='12 months',
                                          fg='#b50098',
                                          bg='white',
                                          font='Ariel 10 bold',
                                          activeforeground='#5d00a0',
                                          activebackground='white',
                                          variable=timeframe,
                                          value=2)
    twelve_month_radbutton.pack(padx=75,pady=1,anchor='w')

    display_button=tkinter.Button(weed_window,
                                  text='Display Books',
                                  fg='white',
                                  bg='#5d00a0',
                                  font='Ariel 10 bold',
                                  width=20,
                                  borderwidth=0.1,
                                  activeforeground='white',
                                  activebackground='#b50098',
                                  command=lambda:time_check(database,
                                                            log,
                                                            timeframe.get(),
                                                            timeframe_results_list))
    display_button.pack(padx=75,pady=1,anchor='w')


    weed_frame=tkinter.Frame(weed_window,
                             borderwidth=0.1,
                             height=50)

    timeframe_results_list=tkinter.Listbox(weed_frame,
                                           width=10,
                                           fg='black',
                                           bg='white',
                                           font='Consolas 10')

    results_scrollbar_y=tkinter.Scrollbar(weed_frame,
                                          orient='vertical',
                                          command=timeframe_results_list.yview)

    results_scrollbar_x=tkinter.Scrollbar(weed_frame,
                                          orient='horizontal',
                                          command=timeframe_results_list.xview)


    results_scrollbar_y.pack(side='right',fill='y')
    results_scrollbar_x.pack(side='bottom',fill='x')
    timeframe_results_list.pack(side='left',fill='both',expand=True)


    weed_frame.pack(padx=75,pady=(0,5),
                    fill='x',anchor='nw')





    weed_item_label=tkinter.Label(weed_window,
                                      text='Please Enter the ID Number of the Book\nyou wish to Remove:',
                                      fg='black',
                                      bg='white',
                                      font='Ariel 10')
    weed_item_label.pack(pady=10)

    weed_item_input=tkinter.Entry(weed_window,
                                  width=30,
                                  fg='black',
                                  bg='white',
                                  font='Ariel 10')
    weed_item_input.pack(pady=(0,10))


    weed_item_button=tkinter.Button(weed_window,
                                    text='Remove',
                                    fg='white',
                                    bg='#5d00a0',
                                    font='Ariel 10 bold',
                                    width=25,
                                    borderwidth=0.1,
                                    activeforeground='white',
                                    activebackground='#b50098',
                                    command=lambda:book_id_check(accept_char_lst,
                                                                 database,
                                                                 weed_item_input.get(),
                                                                 database_file))

    weed_item_button.pack(pady=(0,10))
    
if __name__=='__main__':

    #test data and test database file in order to preserve the integrity of the real database
    user = 'test'
    accept_char = ['0','1','2','3','4','5','6','7','8','9']
    database = [['000000','Test_1','Author_Test_1','test\n'],
                ['000001','Test_2','Author_Test_2','test\n'],
                ['000002','Test_3','Author_Test_3','test\n']]
    log = []
    database_file = 'database_test.txt'

    #runs weed function using the above test data
    weed_window_ (user,accept_char,database,log,database_file)
 
