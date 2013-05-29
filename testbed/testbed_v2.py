import urllib, csv, itertools, string, cPickle

csv_file ='https://sites.google.com/site/info20002y13s1/project-specification/phase3/moviestats_med.csv?attredirects=0'
    
file = urllib.urlopen(csv_file)
reader = csv.reader(file, delimiter = ',', quotechar = '|')

#Store the field names in a list
for row in itertools.islice(reader, 1):
    fields = row

movie = {}
line = []
index = {}

for i in reader:
    line.append(i)

line_no = 0

while line_no < len(line):
    for list in line:
        i = 0
        curr_movie = line[line_no]
        for words in curr_movie:
            for field_name in fields:
                if i < len(fields):
                    movie[field_name] = curr_movie[i]
"""                    i+=1

    # Pickle the individual movie dictionary and store it in a file named after the movie title.
    filename = movie['name']
    for char in string.punctuation:
        filename = filename.replace(char, ' ')

    file = open(filename + ".pickle", "w")
    cPickle.dump(movie, file)
    file.close()
    line_no+=1

generic = ["and","&","in","the","of","a"]

def remove_generic(list):
    for word in list:
        if word not in generic:
            return word

def create_index():
    """
