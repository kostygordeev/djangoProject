from func_app.constants import API_KEY, FIRST_RES
from scipy.interpolate import UnivariateSpline
import json
import matplotlib.pyplot as plt
import seaborn
import datetime

def get_cur_inf():
    n = datetime.datetime.now()
    n_str = n.strftime("%Y-%m-%d")
    t = n - datetime.timedelta(days=90)
    t_str = t.strftime("%Y-%m-%d")
    q = "https://api.apilayer.com/fixer/timeseries?"
    q += ("start_date=" + t_str + '&')
    q += ("end_date=" + n_str + '&')
    q += "base=KZT&"
    q += "symbols=RUB&"
    q += f"apikey={API_KEY}"
    # response = requests.get(query)
    # print("\n\n", response.text, "\n\n", sep="")
    # return response.text
    return FIRST_RES

def parse_json_res_str(string=FIRST_RES):
    cur_inf = json.loads(string)
    result = dict()
    for key in cur_inf['rates'].keys():
        result[key] = cur_inf['rates'][key]['RUB']
    return result

def pred_values(days_num):
    data = get_cur_inf()
    cur_inf = parse_json_res_str(data)
    x = list([i + 1 for i in range(len(cur_inf))])
    y = list(cur_inf.values())
    spl = UnivariateSpline(x, y)
    result = []
    for i in range(days_num):
        new_value = float(spl(i + len(cur_inf)))
        result.append(new_value)
    return result

def create_pred_plot(days_num):
    data = pred_values(days_num)
    dates = []
    n = datetime.datetime.now()
    for i in range(days_num):
        n = n + datetime.timedelta(days=1)
        dates.append(n.strftime("%y/%m/%d"))
    seaborn.lineplot(x=dates, y=data)
    plt.xticks(rotation=80)
    return save_plot()


def save_plot():
    index = -1
    with open(".\\media\\index.txt", 'r') as fi:
        index = int(fi.read())
    with open(".\\media\\index.txt", 'w') as fo:
        fo.write(str(index + 1))
    filename = "plot" + str(index) + ".png"
    plt.savefig(".\\media\\" + filename)
    return filename
