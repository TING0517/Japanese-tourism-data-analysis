from django.http import JsonResponse
import pandas as pd
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import ast
import io
import requests

# 將 data 初始化為 None，不讓它在啟動時讀取
data = None

def load_data_pk():
    """負責從遠端抓取資料的函數"""
    # 建議使用不帶 token 的原始 Raw 連結
    CSV_URL = "https://raw.githubusercontent.com/TING0517/tourism-data-storage/main/app_food_pk.csv"
    
    try:
        # 使用 requests 抓取，增加 timeout 限制避免無限等待
        response = requests.get(CSV_URL, timeout=10)
        if response.status_code == 200:
            df_data_pk = pd.read_csv(io.StringIO(response.text))
            
            temp_data = {}
            for k, v in zip(df_data_pk.name, df_data_pk.value):
                try:
                    temp_data[k] = ast.literal_eval(v)
                except:
                    temp_data[k] = v # 預防轉型失敗
            
            print('✅ Load app food data success!')
            return temp_data
        else:
            print(f'❌ Failed to load CSV: Status {response.status_code}')
            return {}
    except Exception as e:
        print(f'❌ Error loading data: {e}')
        return {}

# --- 刪除原本放在最底層的 load_data_pk() 呼叫 ---

def home(request):
    return render(request, 'app_food/home.html')

@csrf_exempt
def api_get_food_data(request):
    global data
    # 只有當 data 是空的（第一次被呼叫）時，才去抓取資料
    if data is None:
        data = load_data_pk()
    
    return JsonResponse(data)

print('App food views initialized...')