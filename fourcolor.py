import geopandas as gpd
import networkx as nx


shapefile_path = "India_State_Boundary.shp"
world = gpd.read_file(shapefile_path)

G = nx.Graph()


for idx, state in world.iterrows():
    G.add_node(idx, name=state["State_Name"])  

for idx, state in world.iterrows():
    for neighbor_idx, neighbor in world.iterrows():
        if idx != neighbor_idx and state.geometry.touches(neighbor.geometry):
            G.add_edge(idx, neighbor_idx)

print("\nAdjacency List:")
for node in G.nodes:
    print(f"{world.loc[node, 'State_Name']} -> {[world.loc[n, 'State_Name'] for n in G.neighbors(node)]}")
