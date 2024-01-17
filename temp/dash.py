# Import required libraries
import pandas as pd

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("data/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

launch_sites = spacex_df['Launch Site'].unique()

options = [{'label': 'All Sites', 'value': 'ALL'}]

for site in launch_sites:
    options.append({'label': site, 'value': site})


def get_graph(entered_site):
    filtered_df = spacex_df
    if entered_site == 'ALL':
        print(filtered_df.shape)
    else:
        filtered_df = spacex_df.groupby('class')['Launch Site' == entered_site]
        print(filtered_df.shape)


get_graph(launch_sites[0])
