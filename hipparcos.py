'''
In dit programma hipparcos.py gaan we het HR-diagram plotten aan de hand van
data van 118 duizend sterren, direct uit de ESA Hipparcos satelliet (1989–1993)

Zie bijbehorend document met alle uitleg.

Hugo van der Linde.
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Laad de dataset
bestand = "hipparcos.csv"
df = pd.read_csv(bestand)

# Selecteer en filter alleen rijen met geldige gegevens
# Vmag = visuele magnitude, Plx = parallax, (V-I)red = kleurindex
filtered = df[['Vmag', 'Plx', '(V-I)red']].dropna()
filtered = filtered[filtered['Plx'] > 0]  # Alleen sterren met positieve parallax

# Bereken afstand in parsecs
filtered['Distance_pc'] = 1000 / filtered['Plx']

# Bereken absolute magnitude
filtered['AbsMag'] = filtered['Vmag'] - 5 * np.log10(filtered['Distance_pc'] / 10)

# Plot het HR-diagram
plt.figure(figsize=(10, 8))
plt.scatter(filtered['(V-I)red'], filtered['AbsMag'], s=1, color='black')
plt.gca().invert_yaxis()  # Helderdere sterren bovenaan
plt.xlabel('V−I (kleurindex)')
plt.ylabel('Absolute magnitude (M)')
plt.title('Hertzsprung–Russell diagram (Hipparcos)')
plt.grid(True)
plt.show()
