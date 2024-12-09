import pandas as pd
import plotly.graph_objects as go

file_path = "dataset_path"


chunksize = 10000  
required_columns = ['uid', 'Re', 'Rct']  


cycle_data = []
re_data = []
rct_data = []


for chunk in pd.read_csv(file_path, chunksize=chunksize):
    
    chunk = chunk[required_columns]

    chunk = chunk.dropna()

    cycle_data.extend(chunk['uid'].tolist())
    re_data.extend(chunk['Re'].tolist())
    rct_data.extend(chunk['Rct'].tolist())


fig = go.Figure()

fig.add_trace(go.Scatter(x=cycle_data, y=re_data, mode='lines', name='Re (Electrolyte Resistance)'))

fig.add_trace(go.Scatter(x=cycle_data, y=rct_data, mode='lines', name='Rct (Charge Transfer Resistance)'))


fig.update_layout(
    title="Battery Aging: Resistance Trends Over Cycles",
    xaxis_title="Charge/Discharge Cycle",
    yaxis_title="Resistance (Ohms)",
    legend_title="Parameter",
    template="plotly",
)


fig.show()

