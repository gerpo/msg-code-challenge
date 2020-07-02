import os

import numpy as np
import plotly.graph_objects as go


def _get_location_scatter(locations):
    return go.Scattergeo(
        locationmode='ISO-3',
        lon=[x.longitude for x in locations],
        lat=[x.latitude for x in locations],
        hoverinfo='text',
        text=[x.name for x in locations],
        mode='markers',
        marker={'size': 5, 'color': 'rgb(255, 0, 0)', 'line': {'width': 3, 'color': 'rgba(68, 68, 68, 0)'}})


def _get_animation_frames(locations, order):
    frames = []
    frame_data = []
    for i in range(0, len(order) - 1):
        start_location = locations[order[i]]
        end_location = locations[order[i + 1]]

        frame_data.append(go.Scattergeo(
            locationmode='ISO-3',
            lon=[start_location.longitude, end_location.longitude],
            lat=[start_location.latitude, end_location.latitude],
            text=f'Section {i}',
            mode='lines+markers',
            line={'width': 1, 'color': 'red'},
        ))
        frames.append(go.Frame(data=frame_data))

    return frames


def _get_all_traces(locations, order):
    traces = []
    for i in range(0, len(order) - 1):
        start_location = locations[order[i]]
        end_location = locations[order[i + 1]]

        traces.append(go.Scattergeo(
            locationmode='ISO-3',
            lon=[start_location.longitude, end_location.longitude],
            lat=[start_location.latitude, end_location.latitude],
            text=f'Section {i}',
            mode='lines+markers',
            line={'width': 1, 'color': 'red'},
        ))
    return traces


def _get_base_layout(sub_title: str = None) -> dict:
    title = f'msg Locations TSP <br><sub>{sub_title}</sub>' if sub_title else 'msg Locations TSP'
    return {'title_text': title,
            'showlegend': False,
            'geo': {'scope': 'europe', 'projection_type': 'mercator', 'showland': True,
                    'lataxis': {'range': [46, 56]}, 'lonaxis': {'range': [2, 19]}, 'landcolor': 'rgb(243, 243, 243)',
                    'countrycolor': 'rgb(204, 204, 204)'}}


def visualize(locations: list, order: np.ndarray, options: dict) -> None:
    show_visualization = options.get('show_visualization', True)
    sub_title = options.get('sub_title', None)
    animate = options.get('animate_visualization', True)
    export_as_image = options.get('export_as_image', False)
    export_name = options.get('export_name', 'solution')

    location_scatter = _get_location_scatter(locations)
    plot_data = [location_scatter]
    frames = []
    layout = _get_base_layout(sub_title)

    if animate and show_visualization:
        plot_data = [location_scatter] * (len(locations) + 1)
        frames = _get_animation_frames(locations, order)
        layout['updatemenus'] = [
            {'type': "buttons", 'buttons': [{'label': "Play", 'method': "animate", 'args': [None]}]}]
    else:
        plot_data = plot_data + _get_all_traces(locations, order)

    fig = go.Figure(data=plot_data, frames=frames, layout=layout)

    if show_visualization:
        fig.show()

    if export_as_image:
        image_export_dir = os.path.join('results', 'images')
        image_export_file = os.path.join(image_export_dir, f'{export_name}.svg')
        if not os.path.exists(image_export_dir):
            os.mkdir(image_export_dir)

        fig.write_image(image_export_file)
