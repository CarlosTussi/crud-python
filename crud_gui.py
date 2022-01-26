from tkinter import *

master = Tk(className=' Movie DB')
master.geometry("800x500")
master.resizable(False, False)

#DataBase variables (Change to a class later one ?)
#Movie Table
movie_db_title = None
movie_db_director = None
movie_db_country = None
movie_db_year = None
movie_db_genre = None

#Actors Table
actor_db_first_name = None
actor_db_last_name = None
actor_db_gender = None

#Cast Table
cast_db_role = None


#Creating label
#Main labels
movie_label = Label(master, text = "Movie")
cast_label = Label(master, text ="Cast")

#Arrange main labels in the grid layout
movie_label.grid(row= 0, column = 1, columnspan= 3)
cast_label.grid(row= 6, column = 1, columnspan= 3)

#Input labels
#Movie labels
movie_label_title = Label(master, text = "Title")
movie_label_director = Label(master, text = "Director")
movie_label_country = Label(master, text = "Label")
movie_label_year = Label(master, text = "Year")
movie_label_genre = Label(master, text = "Genre")

#Cast labels
cast_label_first_name = Label(master, text = "First Name")
cast_label_last_name = Label(master, text = "Last Name")
cast_label_gender = Label(master, text = "Gender")
cast_label_role = Label(master, text = "Role")


#Arrange input labels in the grid
#Movie labels
movie_label_title.grid(row=1, column=0, sticky= W, pady= 2, padx= 10)
movie_label_director.grid(row=2, column=0, sticky= W, pady= 2, padx= 10)
movie_label_country.grid(row=3, column=0, sticky= W, pady= 2, padx= 10)
movie_label_year.grid(row=4, column=0, sticky= W, pady= 2, padx= 10)
movie_label_genre.grid(row=5, column=0, sticky= W, pady= 2, padx= 10)


#Cast labels
cast_label_first_name.grid(row = 7, column= 0, sticky = W, pady = 2, padx= 10)
cast_label_last_name.grid(row = 8, column= 0, sticky = W, pady = 2, padx= 10)
cast_label_gender.grid(row = 9, column= 0, sticky = W, pady = 2, padx= 10)
cast_label_role.grid(row = 10, column= 0, sticky = W, pady = 2, padx= 10)


#Get input from user
#Movie input
movie_input_title = Entry(master)
movie_input_director = Entry(master)
movie_input_country = Entry(master)
movie_input_year = Entry(master)
movie_input_genre = Entry(master)

#Cast input
cast_input_first_name = Entry(master)
cast_input_last_name = Entry(master)
cast_input_gender = Entry(master)
cast_input_role = Entry(master)

#Arrange input box in the grid layout
#Movie input
movie_input_title.grid(row = 1, column= 2, sticky = W, pady = 2)
movie_input_director.grid(row = 2, column= 2, sticky = W, pady = 2)
movie_input_country.grid(row = 3, column= 2, sticky = W, pady = 2)
movie_input_year.grid(row = 4, column= 2, sticky = W, pady = 2)
movie_input_genre.grid(row = 5, column= 2, sticky = W, pady = 2)

#Cast input
cast_input_first_name.grid(row = 7, column= 2, sticky = W, pady = 2)
cast_input_last_name.grid(row = 8, column= 2, sticky = W, pady = 2)
cast_input_gender.grid(row = 9, column= 2, sticky = W, pady = 2)
cast_input_role.grid(row = 10, column= 2, sticky = W, pady = 2)


string_text = ""
###############
##Bind testing#
###############
def testing(event):
    global string_text
    string_text = string_text + event.char
    
    ##For REAL-TIME update
    #Erase whatever is writted
    result_db_panel.delete('1.0',END)
    #Write the new content
    result_db_panel.insert(END, string_text)

    print(string_text)

cast_input_first_name.bind('<Key>', testing)
###############
##Bind testing#
###############



#Adds button to the interface
def addNewMovieEntry():
    #Movie Table
    movie_db_title = movie_input_title.get()
    movie_db_director = movie_input_director.get()
    movie_db_country = movie_input_country.get()
    movie_db_year = movie_input_year.get()
    movie_db_genre = movie_input_genre.get()


    print(movie_db_title)
    print(movie_db_director)
    print(movie_db_country)
    print(movie_db_year)
    print(movie_db_genre)
 

submit_button = Button(master, text ="Submit New Entry", command = addNewMovieEntry)



def addNewCastMember():
    #Actor Table
    actor_db_first_name = cast_input_first_name.get()
    actor_db_last_name = cast_input_last_name.get()
    actor_db_gender = cast_input_gender.get()

    
    #Cast Table
    cast_db_role = cast_input_role.get()

    print(actor_db_first_name)
    print(actor_db_last_name)
    print(actor_db_gender)
    print(cast_db_role)


add_cast_member_button = Button(master, text = "Add", command = addNewCastMember)

add_cast_member_button.grid(row = 11, column = 1, columnspan= 3)
submit_button.grid(row = 15, column = 1, columnspan=3)

#############################
#############################
######### CANVAS ############
#############################
#############################

result_db_panel = Text(master, height=35, width = 67)
result_db_panel.grid(row=1, rowspan= 15, column=7, padx= (20, 20), pady= (2, 10))



print(master.grid_size())

master.mainloop()