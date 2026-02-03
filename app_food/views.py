from django.http import JsonResponse
import pandas as pd
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import ast
def load_data_pk():
    # Read data from csv file
    CSV_URL ="https://raw.githubusercontent.com/TING0517/tourism-data-storage/refs/heads/main/app_food_pk.csv"
    df_data_pk = pd.read_csv(CSV_URL)
    
    global data
    data={}
    for k,v in zip(df_data_pk.name, df_data_pk.value):
        data[k]=ast.literal_eval(v)
    
    # 沒用到的變數刪除之
    del df_data_pk

# load pk data
load_data_pk()

def home(request):
    return render(request,'app_food/home.html')

# csrf_exempt is used for POST
# 單獨指定這一支程式忽略csrf驗證
@csrf_exempt
def api_get_food_data(request):
    return JsonResponse(data)

print('Load app food leaderboard...')
