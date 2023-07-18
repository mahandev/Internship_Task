from django.shortcuts import render, redirect
from searcher.models import Item
import csv
import json

filename = 'static/restaurants_small.csv'

def index(request):
    i = list(Item.objects.all().values().order_by('-shop_rating'))
    # Getting information in the descending order by the rating of the shop
    print(i)
    names = []
    for p in i:
        names.append(str(p["name"]).replace("('",'').replace("',)","")  + " -- shop rating:" + str(p["shop_rating"]))
        # Formatting the data to be presented in the correct way
        
    context = {"names":names}
    return render(request, 'index.html', context)


def data_addition(request):
        resterants = []
        with open(filename, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            i = 0
            for row in datareader:
                # THe if statment is added to skip the first line that has the headings
                # to be included in the code
                if i == 0:
                    i = i + 1
                else:
                    # TEST CODE below
                    # temp_dict = {}
                    # temp_dict['id'] = row[0]
                    # temp_dict['name'] = row[1]
                    # temp_dict['location'] = row[2]
                    # temp_dict['items'] = eval(row[3])
                    # temp_dict['lat_long'] = row[4]
                    # temp_dict['details'] = row[5]
                    for j,l in eval(row[3]).items():
                        # TESTING CODE print(str(j) + str(l) + str(row[2]) + str(row[1]), eval(row[5])["user_rating"]["aggregate_rating"])

                        # This TRY line prevents any errors while adding inforamtion,
                        # as the CSV is inconsistent in it's data this line allows those riddled data to be skipped
                        # and adds 0.0 as it's rating
                        p = ""
                        p = Item(name=str(j), price=str(l), location=row[2],shop=row[1])
                        try:    
                            p.shop_rating=float(eval(row[5])["user_rating"]["aggregate_rating"])
                        except:
                            p.shop_rating=0.0
                        # p.save()
                        # ^^^^^ commented for stopping accidental data addition.
        context = {"data":resterants}
        return redirect(index)