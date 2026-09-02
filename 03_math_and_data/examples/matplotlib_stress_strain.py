"""Create a labelled stress-strain plot. Requires Matplotlib."""
from pathlib import Path
import matplotlib.pyplot as plt

strain = [0.0, 0.0005, 0.0010, 0.0015]
stress_mpa = [0.0, 100.0, 200.0, 295.0]
fig, ax = plt.subplots()
ax.plot(strain, stress_mpa, marker="o", label="Specimen A")
ax.set(xlabel="Strain (m/m)", ylabel="Stress (MPa)", title="Stress–strain measurement")
ax.grid(True)
ax.legend()
fig.tight_layout()
output_path = Path(__file__).parent / "stress_strain.png"
fig.savefig(output_path, dpi=150)
print(f"Saved: {output_path}")
