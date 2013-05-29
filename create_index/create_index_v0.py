#IN PROGRESS - need to still abstract into functions and add the index creation functionality

import csv, itertools, string, cPickle
    
file = open("moviestats_med.csv")
reader = csv.reader(file, delimiter = ',', quotechar = '|')

#Store the field names in a list
for row in itertools.islice(reader, 1):
    fields = row

movie = {}
line = []

#Insert all the rows in the CSV file into a list
for i in reader:
    line.append(i)

line_no = 0

#Loop through all of the rows
while line_no < len(line):
    for list in line:
        i = 0
        #Read one movie into curr_movie for processing
        curr_movie = line[line_no]
        for words in curr_movie:
            #Insert the dictionary key and populate with the relevant objects
            for field_name in fields:
                if i < len(fields):
                    movie[field_name] = curr_movie[i]
                    i+=1

    # Pickle the individual movie dictionary and store it in a file named after the movie title + year
    movie_name = movie['name']
    for char in string.punctuation:
        movie_name = movie_name.replace(char, ' ')
    #It is assumed that the "date" field is when the movie was released; therefore, a re-released movie will have a new date.
    file = open("data/" + movie_name + " " + movie['date'] + ".pickle", "w")
    cPickle.dump(movie, file)
    file.close()
    line_no+=1  

#To be [possibly] used for the index functionality
"""
generic = ["and","&","in","the","of","a"]

def remove_generic(list):
    for word in list:
        if word not in generic:
        return word
"""
