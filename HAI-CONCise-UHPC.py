#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import pickle
from PIL import Image, ImageOps, ImageTk
import webbrowser
import os
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import xgboost as xgb
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from scipy.interpolate import make_interp_spline
from resources.optimized_hyperparameters_hybrid_ML_USED import *
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    buf = figure_canvas_agg.buffer_rgba()
    image = Image.frombuffer('RGBA', (buf.shape[1], buf.shape[0]), buf, 'raw', 'RGBA', 0, 1)
    photoimage = ImageTk.PhotoImage(image=image)
    canvas.create_image(0, 0, image=photoimage, anchor=tk.NW)
    return photoimage
def delete_figure_agg(canvas, figure_agg):
    canvas.delete("all")
response_groups = [(0, 5), (6, 6), (7, 16), (17, 17), (18, 18)]
with open('resources/min_max_values.pkl', 'rb') as file:
    min_max_values = pickle.load(file)
ranges = {param: [round(min_max_values[param][0], 4), round(min_max_values[param][1], 4)] for param in min_max_values}
def normalize(input_df, min_max_values):
    normalized_data = input_df.copy()
    for column in input_df.columns:
        min_val = min_max_values[column][0]
        max_val = min_max_values[column][1]
        normalized_data[column] = (input_df[column] - min_val) / (max_val - min_val)
    return normalized_data
def denormalize(predictions, feature_name, min_max_values):
    min_val = min_max_values[feature_name][0]
    max_val = min_max_values[feature_name][1]
    return predictions * (max_val - min_val) + min_val
def calculate_final_prediction(xgb_pred, gb_pred, rf_pred, gb_weight):
    rf_weight = 1.0 - gb_weight
    final_pred = xgb_pred + gb_weight * gb_pred + rf_weight * rf_pred
    return final_pred
with open('resources/resp.pkl', 'rb') as file:
    resp = pickle.load(file)
def calculate_sr(row):
    peak_sr = row['ecc']
    ultimate_sr = row['ecu']
    fractions_before_peak = np.linspace(0.4, 0.9, 6) * peak_sr
    points_before_peak_sr = fractions_before_peak
    fractions_after_peak = np.linspace(1, 10, 10) * (ultimate_sr - peak_sr) / 10 + peak_sr
    points_after_peak_sr = fractions_after_peak
    sr_values = pd.Series(points_before_peak_sr.tolist() + [peak_sr] + points_after_peak_sr.tolist())
    return sr_values    
left_col = [
    [sg.Text("Enter Vf:"), sg.InputText(key='-VF-')],
    [sg.Text("Enter fy:"), sg.InputText(key='-FY-')],
    [sg.Text("Enter fco:"), sg.InputText(key='-FCO-')],
    [sg.Text("Enter rohsy:"), sg.InputText(key='-ROHSY-')],
    [sg.Button("Predict and Plot")]
]
right_col = [
    [sg.Canvas(key='-CANVAS-', size=(450, 340))]  # Adjust size as needed
]
parameters = ['Vf', 'fy', 'fco', 'rohsy']
import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')
def check_value(value, range):
    try:
        float_value = float(value)
        if range[0] <= float_value <= range[1]:
            return True
    except ValueError:
        pass
    return False
def OpenLink(url):
    webbrowser.open_new(url)

def create_link_label(text, url):
    root = tk.Tk()
    root.withdraw()
    label = tk.Label(root, text=text, fg="blue", cursor="hand2")
    label.pack()
    label.bind("<Button-1>", lambda event: handle_link_click(url))
    return label    
layout = [
    [sg.Text('Define the input parameters', text_color='blue', font=(''))],
    [
        sg.Column(layout=[
            [sg.Frame(layout=[
                [sg.Text('Compressive strength of unconfined UHPC, fco (MPa)', size=(38, 1)), sg.Input(key='-FCO-', size=(15, 1), enable_events=True)],
                [sg.Text('Fiber volumetric ratio, vf (%)', size=(38, 1)), sg.Input(key='-VF-', size=(15, 1), enable_events=True)],
                [sg.Text('Spiral reinforcement ratio, ρs (%)', size=(38, 1)), sg.Input(key='-ROHSY-', size=(15, 1), enable_events=True)],
                [sg.Text('Yield strength of spiral reinforcement, fy (MPa)', size=(38, 1)), sg.Input(key='-FY-', size=(15, 1), enable_events=True)]],
            title='Input parameters')], 
        ], justification='left'),

        sg.Column(layout=[
            [sg.Frame(layout=[
                [sg.Text(f'{ranges["fc"][0]} ≤ fco (MPa) ≤ {ranges["fc"][1]}')],
                [sg.Text(f'{ranges["vf"][0]} ≤ vf (%) ≤ {ranges["vf"][1]}')],
                [sg.Text(f'{ranges["roh_t (%)"][0]} ≤ ρs (%) ≤ {ranges["roh_t (%)"][1]}')],
                [sg.Text(f'{ranges["fy"][0]} ≤ fy (MPa) ≤ {ranges["fy"][1]}')]],                  
            title='Range of applications of the model')],             
        ], justification='center')
    ],
    [
        sg.Button('Predict and Plot'), sg.Button('Export to Excel'),sg.Button('Cancel')             
    ],
    [sg.Text('')],    
    
    [sg.Text('Predicted stress-strain response of confined UHPC', text_color='blue', font=('Helvetica', 11))],
    [

        sg.Column(layout=[
            [sg.Canvas(key='-CANVAS-', size=(450, 262))],          
            
        ]
                  , justification='center'
                 )
    ],
]
img2 = Image.open('resources/image2.png')
img3 = Image.open('resources/image3.png')
img4 = Image.open('resources/image4.png')
widths = [img2.width, img4.width]
heights = [img2.height,  img4.height]
min_width = min(widths)
min_height = min(heights)
img2 = ImageOps.fit(img2, (min_width, min_height))
img3 = ImageOps.fit(img3, (min_width, min_height))
img4 = ImageOps.fit(img4, (min_width, min_height))
scale_factor = 0.25
img2 = img2.resize((int(min_width * scale_factor), int(min_height * scale_factor)))
img3 = img3.resize((int(min_width * scale_factor), int(min_height * scale_factor)))
img4 = img4.resize((int(min_width * scale_factor), int(min_height * scale_factor)))
img2.save('image22.png')
img3.save('image33.png')
img4.save('image44.png')
fig2 = sg.Image(filename='image22.png', key='-fig2-', size=(min_width * scale_factor, min_height * scale_factor))
fig3 = sg.Image(filename='image33.png', key='-fig3-', size=(min_width * scale_factor, min_height * scale_factor))
fig4 = sg.Image(filename='image44.png', key='-fig4-', size=(min_width * scale_factor, min_height * scale_factor))
layout += [
    [sg.Text('')],
    [sg.Column([
    [sg.Text('Authors: Wakjira T., Abushanab A., and Alam M.'+ '\n'
             '             The University of British Columbia, Okanagan')],
    [
     sg.Button('www.tadessewakjira.com/Contact', key='WEBSITE', button_color=('white', 'gray')),
     sg.Button('https://alams.ok.ubc.ca', key='WEBSITE', button_color=('white', 'gray')),
    ]
    ],
    element_justification='left'
    ),
        sg.Column(
            [   [fig2,
                 fig3,
                fig4,
                ],
            ],
            element_justification='center'
        ),
    ],

    [sg.Text("   If you utilize this software for your work, we kindly request that you cite the corresponding paper as a reference.", 
             size=(90, 1), 
             border_width=1, 
             relief=sg.RELIEF_SUNKEN, 
             background_color='white',
             text_color='black',
             font=('Helvetica', 8, 'bold'))],
]
window = sg.Window('HAI-CONCise-UHPC: Hybrid Artificial Intelligence-based CONstitutive model for Confined UHPC', layout)
predictions_made = False
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Predict and Plot':
        input_data1 = np.array([
            float(values['-VF-']),
            float(values['-FY-']),
            float(values['-FCO-']),
            float(values['-ROHSY-'])
        ]).reshape(1, -1)
        input_data = pd.DataFrame(input_data1, columns=['vf', 'fy', 'fc', 'roh_t (%)'])
        input_data = normalize(input_data, min_max_values)
        all_predictions = []
        for group_index, (start_col, end_col) in enumerate(response_groups):
            xgb_params = {key: eval(f"xgb_{key}_group{group_index + 1}") for key in ['n_estimators', 'max_depth', 'learning_rate', 'subsample', 'colsample_bytree', 'random_state']}
            gb_params = {key: eval(f"gb_{key}_group{group_index + 1}") for key in ['n_estimators', 'max_depth', 'learning_rate', 'subsample', 'random_state']}
            rf_params = {key: eval(f"rf_{key}_group{group_index + 1}") for key in ['n_estimators', 'max_depth', 'random_state']}
            gb_weight = eval(f"gb_weight_group{group_index + 1}")
            for col in range(start_col, end_col + 1):
                with open(f'resources/xgb_model_group{group_index + 1}_col{col}.pkl', 'rb') as file:
                    xgb_model = pickle.load(file)
                with open(f'resources/gb_model_group{group_index + 1}_col{col}.pkl', 'rb') as file:
                    gb_model = pickle.load(file)
                with open(f'resources/rf_model_group{group_index + 1}_col{col}.pkl', 'rb') as file:
                    rf_model = pickle.load(file)                
                xgb_pred = xgb_model.predict(input_data)
                gb_pred = gb_model.predict(input_data)
                rf_pred = rf_model.predict(input_data)
                final_pred = calculate_final_prediction(xgb_pred, gb_pred, rf_pred, gb_weight)
                all_predictions.append(final_pred[0])
        denormalized_predictions = [denormalize(pred, resp.columns[i], min_max_values) for i, pred in enumerate(all_predictions)]
        denormalized_predictions = pd.DataFrame(denormalized_predictions).T
        denormalized_predictions.columns = resp.columns 
        new_sr = 100*denormalized_predictions.apply(calculate_sr, axis=1).values[0]
        new_ss = denormalized_predictions.drop(['ecc', 'ecu'], axis=1).values[0]       
        zero_four_peak_sr = new_sr[0]
        xnew = np.linspace(zero_four_peak_sr, new_sr[-1], 300)
        spl = make_interp_spline(new_sr, new_ss, k=3)
        smooth_ss = spl(xnew)
        fc_value = f"f$_{{co}}$ = {input_data1[0][2]} MPa"
        vf_value = f"v$_f$ = {input_data1[0][0]}%"
        roh_t_value = f"ρ$_s$ = {input_data1[0][3]:.3f}%"
        fy_value = f"f$_y$ = {input_data1[0][1]} MPa"
        fig, ax = plt.subplots(figsize=(5, 3.85))
        ax.plot(xnew, smooth_ss, linestyle='-', color='red')
        ax.plot([0, zero_four_peak_sr], [0, new_ss[0]], linestyle='-', color='red')
        ax.set_xlim(0, xnew[-1])
        ax.set_ylim(0, np.ceil(max(new_ss) / 50) * 50)
        ft=14
        ax.set_ylabel('Stress (MPa)', fontsize=ft)
        ax.set_xlabel('Strain (%)', fontsize=ft)
        ax.text(0.4, 0.6, fc_value, transform=ax.transAxes, ha='left', fontsize=ft)
        ax.text(0.4, 0.5, vf_value, transform=ax.transAxes, ha='left', fontsize=ft)
        ax.text(0.4, 0.42, roh_t_value, transform=ax.transAxes, ha='left', fontsize=ft)
        ax.text(0.4, 0.32, fy_value, transform=ax.transAxes, ha='left', fontsize=ft)
        ax.tick_params(axis='both', which='major', labelsize=ft)
        ax.grid(True, linestyle='--')
        plt.tight_layout()    
        predictions_made = True 
        if 'figure_canvas_agg' in globals():
            delete_figure_agg(window['-CANVAS-'].TKCanvas, figure_canvas_agg)
        figure_canvas_agg = draw_figure(window['-CANVAS-'].TKCanvas, fig)
    elif event == 'Export to Excel':
        if predictions_made:
            new_sr = np.insert(new_sr, 0, 0)
            new_ss = np.insert(new_ss, 0, 0)
            data_to_save = pd.DataFrame({'Strain (%)': new_sr, 'Stress (MPa)': new_ss})                   
            filename = sg.popup_get_file('Save to Excel file', save_as=True, default_extension='.xlsx', file_types=(("Excel Files", "*.xlsx"),))           
            if filename:
                if not filename.endswith('.xlsx'):
                    filename += '.xlsx'
                data_to_save.to_excel(filename, sheet_name='Predicted Data', index=False, engine='openpyxl')
                sg.popup('Data successfully saved!')
            else:
                sg.popup('No file selected. Data was not saved.')
        else:
            sg.popup('Please predict data first before exporting.')

