import urllib
import csv
import itertools
import cPickle

csv_file ='https://sites.google.com/site/info20002y13s1/project-specification/phase3/moviestats_med.csv?attredirects=0'
    
file = urllib.urlopen(csv_file)
reader = csv.reader(file, delimiter = ',', quotechar = '|')

generic = ["and","&","in","the","of","a"]

def remove_generic(list):
    for word in list:
        if word not in generic:
            return word

for row in itertools.islice(reader, 1):
    fields = row

movie = {}
line = []

for i in reader:
    line.append(i)
    
for list in line:
    j = 0
    i = 0
    curr_movie = line[j]
    for words in curr_movie:
        for name in fields:
            if i < len(fields):
                movie[name] = curr_movie[i]
                i+=1
        #j+=1

# Pickle the individual movie dictionary and store it in a file named after the movie title.
file = open(movie['name'] + ".pickle", "w")

cPickle.dump(movie, file)
file.close()

"""for row in reader:
    print row[0]
"""

"""
for row in reader:
    i = 0
    line.append(row)
    i += 1
"""

"""
for j in line:
    for k in j:
        newline = k.split()
# print newline
        for l in k:
            keywords.append(remove_generic(newline))

for i in keywords:
"""    

"""for row in itertools.islice(reader, 3):
    i = 0
    line.append(row[0])
    print line[i]
    i += 1
"""

"""for i in range(3):
    print next(reader)
"""


#for row in reader:
    #if row[0]==movie_list[i]:
      #  print row[0]
      #  break
        #if input = "/n"
            #break


"""
pattern = re.compile("(and|&|in|the|of|a)\W", re.I)
    phrases = str
    [pattern.sub("", phrase) for phrase in phrases]
    return phrases
"""