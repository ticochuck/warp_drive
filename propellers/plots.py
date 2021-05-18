import base64
from io import BytesIO

import matplotlib.pyplot as plt


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64decode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()


def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,8))
    plt.title('Engines and Red Rates')
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel('Engines')
    plt.ylabel('Reduction Rates')
    plt.tight_layout()
    graph = get_graph()
    return graph
