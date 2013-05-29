def show_actors(actors): #this is a list
    result = ""
    for actor in actors:
        result += '<div class="row"><span class="result">'+actor+'</span></div>'
    return result
    
def show_reviews(reviewers): #this is a dict in the form reviewers[review]
    result = ""
    for reviewer in reviewers:
        result += '<div class="row"><span class="desc">'+reviewer+'</span><span class="result">'+reviews.get(reviewer)+'</span></div>'
    return result