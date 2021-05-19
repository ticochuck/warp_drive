import base64
from io import BytesIO

import matplotlib.pyplot as plt


def get_image():
    # create bytes in memory buffer for image to save
    buffer = BytesIO()
    # create plot using BytesIO object as its 'file'
    plt.savefig(buffer, format='png')
    # set cursor at the begining of the stream
    buffer.seek(0)
    # retrive the entire content of the file
    image_png = buffer.getvalue() 
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    #free the memory of the buffer
    buffer.close()

    return graph

def simple_plot(*args, **kwargs):
    
    plt.switch_backend('AGG')
    fig_bar = plt.figure(figsize=(10,4))
    fig_line = plt.figure(figsize=(10,4))
    
    x = kwargs.get('x')
    y = kwargs.get('y')
    # data = kwargs.get('data')
    # df = kwargs.get('df')
    

    plt.title('Test Plot')
    plt.bar(x,y)
    plt.tight_layout()    

    graph = get_image()
    return graph

