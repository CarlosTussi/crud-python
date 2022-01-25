from tkinter import *

master = Tk()


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
movie_label_title.grid(row=1, column=0, sticky= W, pady= 2)
movie_label_director.grid(row=2, column=0, sticky= W, pady= 2)
movie_label_country.grid(row=3, column=0, sticky= W, pady= 2)
movie_label_year.grid(row=4, column=0, sticky= W, pady= 2)
movie_label_genre.grid(row=5, column=0, sticky= W, pady= 2)


#Cast labels
cast_label_first_name.grid(row = 7, column= 0, sticky = W, pady = 2)
cast_label_last_name.grid(row = 8, column= 0, sticky = W, pady = 2)
cast_label_gender.grid(row = 9, column= 0, sticky = W, pady = 2)
cast_label_role.grid(row = 10, column= 0, sticky = W, pady = 2)


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


#Adds button to the interface
def buttonPressed():
   print("Button pressed")

submit_button = Button(master, text ="Submit", command = buttonPressed)

submit_button.grid(row = 11, column = 1, columnspan=3)


master.mainloop()