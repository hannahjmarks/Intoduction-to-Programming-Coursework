'''This module contains the neccessary functions to search the database by
book title and display the results in the user interface.

Written by Hannah Marks
From 24/10/18 to 12/10/18
'''


import tkinter
import bookcheckout

#message window indicating that the user has entered an invalid input.
def title_input_error():
    '''This function shows a pop-up message window telling the user that
    the input they have entered is invalid.
    '''
    title_error_window=tkinter.Toplevel()
    title_error_window.configure(bg='white')
    title_error_window.title('Error:Invalid Input')
    title_error_window.geometry('200x100')

    message_label=tkinter.Label(title_error_window,
                                text='Invalid Search Item\nPlease Try Again',
                                fg='black',
                                bg='white',
                                font='Ariel 10')
    message_label.pack(pady=(25,5))

    ok_button=tkinter.Button(title_error_window,
                             text='Ok',
                             fg='white',
                             bg='#5d00a0',
                             font='Ariel 10 bold',
                             width=20,
                             borderwidth=0.1,
                             activeforeground='white',
                             activebackground='#b50098',
                             command=title_error_window.destroy)
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

# main search function
def title_search(database,search_item,results_listbox):
    ''' function that searches the database array for titles containing
    the search item the user inputs into the entry box and displays the
    results in the listbox. If there are no results the appropriate 
    error message windoow is displayed.
    '''
    search_results=[]
    # generates an empty list for the search results to prevent the 
    # database array being altered during the search process
    availibility=False
    for i in range(0,len(database)):
        if search_item in database[i][1]:
            search_results.append(database[i])
        elif search_item in database[i][1].lower():
            search_results.append(database[i])
    # database[i][1] is the location of the title element of the list element
    # with index i.
    if search_results==[]:
        results_listbox.delete(0,'end')
        no_results()
    else:
        results_listbox.delete(0,'end')
        results_listbox.insert(0,'%-6s'%'ID'+'|'+'%-125s'%'Title'+'|'
                 +'%-40s'%'Author(s)'+'|'+'Availibility')
        for entry in range(0,len(search_results)):
            if '0'in search_results[entry][3]:
                availibility='Availible'
                results_listbox.insert('end',search_results[entry][0]+'|'
                                       +'%-125s'%search_results[entry][1]+'|'
                                       +'%-40s'%search_results[entry][2]
                                       +'|'+availibility)
            else:
                availibility='On Loan'
                results_listbox.insert('end',search_results[entry][0]+'|'
                                       +'%-125s'%search_results[entry][1]+'|'
                                       +'%-40s'%search_results[entry][2]
                                       +'|'+availibility)

#function to check that user input is valid
def input_check(database,search_input,results_listbox):
    '''This function checks that the user has entered a search item and that
    that item does not contain '*'. If it does an error message is shown, if
    not the search function is run.
    '''
    input_error=False
    if search_input=='':
        input_error=True
    elif '*' in search_input:
        input_error=True
    if input_error==True:
        title_input_error()
    else:
        title_search(database,
                     search_input,
                     results_listbox)



# generates search window for user input
def search(user,accept_char_book_id,database,log,database_file):
    ''' opens the search window for the user to input search term and display
    results in a formatted listbox.
    a = user
    b = accept_char_book_id
    c = database array
    d = log array
    '''
    search_window=tkinter.Toplevel()
    search_window.configure(bg='white')
    search_window.title('Search')
    search_window.geometry('1500x750')


    menu_button=tkinter.Button(search_window,
                               text='Main Menu',
                               fg='white',
                               bg='#5d00a0',
                               font='Ariel 10 bold',
                               width=20,
                               borderwidth=0.1,
                               activeforeground='white',
                               activebackground='#b50098',
                               command=search_window.destroy)
    menu_button.pack(pady=(0,50),anchor='nw')

    search_item_label=tkinter.Label(search_window,
                                    text='Please Enter a Search Item:',
                                    fg='black',
                                    bg='white',
                                    font='Ariel 14')
    search_item_label.pack(padx=75,pady=(15,5),anchor='nw')

    message_label=tkinter.Label(search_window,
                                text='*Warning Books are Searched by Title Only*',
                                fg='#b50098',
                                bg='white',
                                font='Ariel 10')
    message_label.pack(padx=75,pady=5,anchor='nw')

    search_item_input=tkinter.Entry(search_window,
                                    fg='black',
                                    bg='white',
                                    font='Ariel 10')
    search_item_input.pack(padx=75,pady=5,fill='x',anchor='nw')

    # runs title_search function on press
    search_button=tkinter.Button(search_window,
                                 text='Search',
                                 fg='white',
                                 bg='#5d00a0',
                                 font='Ariel 10 bold',
                                 width=20,
                                 borderwidth=0.1,
                                 activeforeground='white',
                                 activebackground='#b50098',
                                 command=lambda:input_check(database,
                                                            search_item_input.get(),
                                                            search_results_list))

    search_button.pack(padx=75,pady=5,anchor='nw')



    search_frame=tkinter.Frame(search_window,
                               borderwidth=0.1)

    search_results_list=tkinter.Listbox(search_frame,
                                        width=10,
                                        fg='black',
                                        bg='white',
                                        font='Consolas 10')

    results_scrollbar_y=tkinter.Scrollbar(search_frame,
                                          orient='vertical',
                                          command=search_results_list.yview)

    results_scrollbar_x=tkinter.Scrollbar(search_frame,
                                          orient='horizontal',
                                          command=search_results_list.xview)


    results_scrollbar_y.pack(side='right',fill='y')
    results_scrollbar_x.pack(side='bottom',fill='x')
    search_results_list.pack(side='left',fill='both',expand=True)


    search_frame.pack(padx=75,pady=(0,50),fill='both',expand=True,anchor='nw')


    # opens checkout window on press for ease of use
    check_out_button=tkinter.Button(search_window,
                                    text='Checkout',
                                    fg='white',
                                    bg='#5d00a0',
                                    font='Ariel 10 bold',
                                    width=20,
                                    borderwidth=0.1,
                                    activeforeground='white',
                                    activebackground='#b50098',
                                    command=lambda:bookcheckout.checkout_window(user,
                                                                                accept_char_book_id,
                                                                                database,
                                                                                log,
                                                                                database_file))

    check_out_button.pack(side='left',anchor='sw')


if __name__=='__main__':

    #test data
    user = 'test'
    accept_char = []
    database = [['000000','Test_1','Author_Test_1','0'],
                ['000001','Test_2','Author_Test_2','0'],
                ['000002','Test_3','Author_Test_3','0']]
    log = []
    database_file = 'database_test.txt'

    #runs search function using the above test data
    search (user,accept_char,database,log,database_file)
