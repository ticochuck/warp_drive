import base64
from io import BytesIO
from django_pandas.io import read_frame

import matplotlib.pyplot as plt
# import seaborn as sns
from matplotlib.text import get_rotation


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(results):
    x = [x.rotation for x in results]
    x.sort()
    y = [y.blade_count for y in results]
    y.sort()
    plt.switch_backend('AGG')
    plt.figure(figsize=(6,5))
    plt.title('Blade Count vs Rotation')
    plt.plot(x,y)
    # plt.xticks(rotation=45)
    plt.xlabel('Rotation')
    plt.ylabel('Blade Count')
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_plot2(results):

    data = read_frame(results)

    x = data['blade_count'].value_counts()
    y = [y.blade_count for y in results]
    plt.switch_backend('AGG')
    plt.figure(figsize=(6,5))
    plt.title('Blade Count')
    plt.plot(x,y)
    # plt.xticks(rotation=45)
    plt.xlabel('Rotation')
    plt.ylabel('Blade Count')
    plt.tight_layout()
    graph = get_graph()
    return graph
