from func_app.constants import API_KEY, FIRST_RES
from scipy.interpolate import UnivariateSpline
import json
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
import datetime
import base64


def get_cur_inf(num_days):
    n = datetime.datetime.now()
    n_str = n.strftime("%Y-%m-%d")
    t = n - datetime.timedelta(days=num_days)
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


def pred_values(days_num, num_days):
    data = get_cur_inf(num_days)
    cur_inf = parse_json_res_str(data)
    x = list([i + 1 for i in range(len(cur_inf))])
    y = list(cur_inf.values())
    spl = UnivariateSpline(x, y)
    result = []
    for i in range(days_num):
        new_value = float(spl(i + len(cur_inf)))
        result.append(new_value)
    return result


def create_pred_plot(days_num, num_days):
    sns.set_theme(style="darkgrid")
    rcParams['figure.figsize'] = 12, 12
    data = pred_values(days_num, num_days)
    dates = []
    n = datetime.datetime.now()
    for i in range(days_num):
        n = n + datetime.timedelta(days=1)
        dates.append(n.strftime("%y/%m/%d"))
    sns.lineplot(x=dates, y=data, color='purple', dashes=True, markers=True)
    plt.fill_between(dates, data, min(data), facecolor="blue", color="green", alpha=0.3)
    plt.xlabel(
        'dates')
    plt.ylabel(
        'data')
    plt.xticks(rotation=80)
    return save_plot()

def encode_image(image_path):
    with open(image_path, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')

        return base64_message



def save_plot():
    index = -1
    with open(f"./media/index.txt", 'r') as fi:
        index = int(fi.read())
    with open(f"./media/index.txt", 'w') as fo:
        fo.write(str(index + 1))
    filename = "plot" + str(index) + ".png"
    plt.savefig(f"./media/" + filename)
    return filename
