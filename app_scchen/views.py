from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd

def load_data_scchen():
    # Read data from csv file
    CSV_URL ="https://raw.githubusercontent.com/TING0517/tourism-data-storage/refs/heads/main/app_scchen_data.csv"
    df_data = pd.read_csv(CSV_URL,sep=',')
    global response
    response = dict(list(df_data.values))
    del df_data

# load data
load_data_scchen()

#print(response)

def home(request):
    return render(request,'app_scchen/home.html', response)

print('app_scchen was loaded!')
