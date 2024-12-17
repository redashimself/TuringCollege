from typing import Dict

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np


class VisualizationManager:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_game_rounds_distribution(self) -> go.Figure:
        fig = px.histogram(
            self.df,
            x='sum_gamerounds',
            color='version',
            marginal='box',
            title='Distribution of Game Rounds',
            labels={'sum_gamerounds': 'Number of Game Rounds'},
            hover_data=['version']
        )

        fig.update_layout(
            title_x=0.5,
            bargap=0.1,
            height=600,
            xaxis_title="Number of Game Rounds",
            yaxis_title="Count of Players"
        )

        x_limit = np.percentile(self.df['sum_gamerounds'], 95)
        fig.update_xaxes(range=[0, x_limit])

        return fig

    def plot_treatment_effects(self, effects_data: Dict) -> go.Figure:
        metrics_df = pd.DataFrame({
            'Metric': ['1-Day Retention', '7-Day Retention'],
            'Effect': [
                effects_data['retention_1'].effect_size['absolute'],
                effects_data['retention_7'].effect_size['absolute']
            ],
            'CI_Lower': [
                effects_data['retention_1'].effect_size['confidence_interval'][0],
                effects_data['retention_7'].effect_size['confidence_interval'][0]
            ],
            'CI_Upper': [
                effects_data['retention_1'].effect_size['confidence_interval'][1],
                effects_data['retention_7'].effect_size['confidence_interval'][1]
            ]
        })

        fig = go.Figure()

        for idx in range(len(metrics_df)):
            fig.add_trace(go.Scatter(
                x=[metrics_df.iloc[idx]['Effect']],
                y=[metrics_df.iloc[idx]['Metric']],
                mode='markers',
                marker=dict(size=10)
            ))

            fig.add_trace(go.Scatter(
                x=[metrics_df.iloc[idx]['CI_Lower'], metrics_df.iloc[idx]['CI_Upper']],
                y=[metrics_df.iloc[idx]['Metric'], metrics_df.iloc[idx]['Metric']],
                mode='lines'
            ))

        fig.add_vline(x=0, line_dash="dash", line_color="gray")
        fig.update_layout(
            title='Treatment Effects and Confidence Intervals',
            xaxis_title='Effect Size (percentage points)',
            yaxis_title='Metric',
            showlegend=False
        )

        return fig