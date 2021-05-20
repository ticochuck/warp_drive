import base64
from io import BytesIO

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
    x = [x.engine_id for x in results]
    y = [y.reduction_ratio_rename_to_red_drive_name for y in results]
    plt.switch_backend('AGG')
    plt.figure(figsize=(6,5))
    plt.title('Engines and Red Rates')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Engines')
    plt.ylabel('Reduction Rates')
    plt.tight_layout()
    graph = get_graph()
    return graph

