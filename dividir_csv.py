import pandas as pd

# Cargar el archivo CSV
file_path = "fraudTrain.csv"
chunk_size = 150000  # Número de filas por archivo (ajusta según sea necesario)

for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size)):
    chunk.to_csv(f"parte_{i+1}.csv", index=False)
