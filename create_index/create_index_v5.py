#IN PROGRESS - need to still abstract into functions

import csv, itertools, string, cPickle
    
file = open("moviestats_med.csv")
reader = csv.reader(file, delimiter = ',', quotechar = '|')

generic = ["and","&","in","the","of","a"]

#Store the field names in a list
for row in itertools.islice(reader, 1):
    fields = row

movie = {}
line = []
index = {}

#Insert all the rows in the CSV file into a list
for i in reader:
    line.append(i)

line_no = 0

#Loop through all of the rows
while line_no < len(line):
    for list in line:
        i = 0
        column = 1
        cast = []
        #Read one movie into curr_movie for processing
        curr_movie = line[line_no]
        for words in curr_movie:
            if 5 <= column <= 7:
                cast.append(words)
                movie["cast"] = cast
            else:
                #Insert the dictionary key and populate with the relevant objects
                for field_name in fields:
                    if i < len(fields):
                        movie[field_name] = curr_movie[i]
                        i+=1
            print movie
            column+=1
"""
    movie_name = movie['name']
    
    #Remove any non-alphanumeric characters from the movie name and replace spaces with underscores
    for char in string.punctuation:
        movie_name = movie_name.replace(char, ' ')
        movie_name = movie_name.replace(" ", "_")
    
    #Pickle the individual movie dictionary and store it in a file named after the movie title + year
    #It is assumed that "date" is when the movie was released; therefore, re-released movies will have new dates.
    filename = movie_name + "_" + movie['date'] + ".pickle"

    file = open("data/" + filename, "w")
    cPickle.dump(movie, file)
    file.close()

    #Concatenate all the keywords (Name and Cast) for this movie into a string to enable splitting - CHANGE THIS FOR CAST
    keywords = movie['name'] + " " + movie['actor1'] + " "  + movie['actor2'] + " " + movie['actor3']
    keywords_split = str.split(keywords)
    
    #Remove generic words
    keywords_split = [text for text in keywords_split if text not in generic]
    word_no = 0
    filename_set = {filename}
    #Replace each keyword with normalised keyword
    for word in keywords_split:
        keywords_split = [x.strip() for x in keywords_split]
        keywords_split = [x.lower() for x in keywords_split]
        while word_no < len(keywords_split):
        #If key is already in the index, append the filename to current key; otherwise, create a new key and mapping.
            if keywords_split[word_no] in index:
                index[keywords_split[word_no]].add(filename)
            else:
                index[keywords_split[word_no]] = filename_set
            word_no+=1

    file = open("index.pickle", "w")
    cPickle.dump(index, file)
    file.close()

    line_no+=1
"""
