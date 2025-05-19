import plotly.express as px

def plot_tourism_trends(df):
    fig = px.line(df, x="Month", y="Tourists", title="Tourism Trends")
    return fig
