import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd


#https://dash.plotly.com/canvas
import dash
import dash_html_components as html
from dash_canvas import DashCanvas
import numpy as np
import pydicom
import cv2
import os
import imageio
#dataset = pydicom.dcmread('./data/DICOM/I0')
inputdir = './data/DICOM/'
outdir = './assets/'

test_list = [ f for f in  os.listdir(inputdir)]
if(True):
    for f in test_list:   
        ds = pydicom.read_file(inputdir + f, force=True) # read dicom image
        img = ds.pixel_array # get image array
        cv2.imwrite(outdir + f + ".png" ,img) # write png image
        #imageio.imwrite(outdir + f.replace('.dcm','.jp2'), img)

app = dash.Dash(__name__)

filename = " http://127.0.0.1:8050/"+'ID_0060_AGE_0080_CONTRAST_0_CT.dcm.png'
filename_s = 'ID_0060_AGE_0080_CONTRAST_0_CT.dcm.png'
canvas_width = 500


app.layout = html.Div([
    #html.Img(src=app.get_asset_url(filename_s)),
    
    DashCanvas(id='canvas_image',
               tool='line',
               lineWidth=5,
               lineColor='red',
               filename=app.get_asset_url(filename_s),
               width=canvas_width)
    ])


if __name__ == '__main__':
    app.run_server(debug=True)