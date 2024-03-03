# ps: ირაკლი, დავალებაში ეწერა, რომ იგივე ფაილში ჩაგვეწერა, მაგრამ თვალსაჩინოებისთვის ახალი ჯეისონი შევქმენი და 
# იქ ჩავყარე მხოლოდ დასააფდეითებელი მონაცემები. ასე გადაჩეკვა უფრო მარტივი იყო:)

import json

class movies:
    def __init__(self, page, results, total_pages, total_results):
        self.page = page
        self.results = results
        self.total_pages = total_pages
        self.total_results = total_results


def deserialized_custom(json_obj):
    return movies(json_obj['page'],
                  json_obj['results'],
                   json_obj['total_pages'],
                    json_obj['total_results'] )


with open("movies.json", "r") as movies_json:
    data = json.load(movies_json)

movies_list = [deserialized_custom(obj) for obj in data]

movies_list_update = []
for moviesx in movies_list:

        for i in moviesx.results:
            
            #get year
            release_date = i.get("release_date")
            year_str = release_date[:4]
            year_int = int(year_str)

            #check genre
            genre_lst = i.get("genres")

            #crime, drama
            isCrime = False
            isDrama = False

            for items in genre_lst:
                if items == "Crime":
                    isCrime = True

            
            for items in genre_lst:
                if items == "Drama":
                    isDrama = True
                
            #1 check
            if year_int > 2000 and isCrime:
                crime_index= i.get("genres").index("Crime")
                i.get("genres")[crime_index] = "New_Crime"

                movies_list_update.append(i)
              
            #2 check
            if year_int < 2000 and isDrama:
                drama_index= i.get("genres").index("Drama")
                i.get("genres")[drama_index] = "Old_Drama"

                movies_list_update.append(i)           


            #3 check
            if year_int==2000:
                i.get("genres").append("New_Century")       
                movies_list_update.append(i)

json_string = json.dumps(movies_list_update)

with open("movies_update.json", "w") as json_file:
    json.dump(movies_list_update, json_file, indent = 4)
