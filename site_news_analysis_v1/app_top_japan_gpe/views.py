from django.shortcuts import render
import pandas as pd

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# load data
def load_data_topgpe():
    # read df
    df_topgpe = pd.read_csv(
        'app_top_japan_gpe/dataset/news_top_person_by_category_via_ner.csv')
    # refresh data
    global data # make data global. It can be used everywhere.
    data = {}
    for idx, row in df_topgpe.iterrows():
        data[row['category']] = eval(row['top_keys'])


# Load data first when starting server.
load_data_topgpe()


def home(request):
    return render(request, 'app_top_japan_gpe/home.html')

# csrf_exempt is used for POST
# 單獨指定這一支程式忽略csrf驗證
@csrf_exempt
def api_get_topgpe(request):

    # chart_data, wf_pairs = get_category_topkey("科技", 10) #先做簡單的測試

    cate = request.POST.get('news_category')
    topk = request.POST.get('topk')
    topk = int(topk)
    #print(cate, topk)

    chart_data, wf_pairs = get_category_topgpe(cate, topk)

    # print(chart_data)
    response = {'chart_data':  chart_data,
                'wf_pairs': wf_pairs,
                }
    return JsonResponse(response)


def get_category_topgpe(cate, topk):
    wf_pairs = data[cate][0:topk]
    words = [w for w, f in wf_pairs]
    freqs = [f for w, f in wf_pairs]
    chart_data = {
        "category": cate,
        "labels": words,
        "values": freqs}
    return chart_data, wf_pairs  # chart_data is for charting


print("app_top_japan_gpe載入成功!")