import numpy as np
import trimesh

# Parameters for the catenoid
R = 1.0  # neck radius
z_max = 1.5  # height from center
n_u = 100  # angular resolution
n_v = 100  # vertical resolution

u = np.linspace(0, 2 * np.pi, n_u)
v = np.linspace(-z_max, z_max, n_v)
u, v = np.meshgrid(u, v)

# Parametric equations for catenoid
x = R * np.cosh(v / R) * np.cos(u)
y = R * np.cosh(v / R) * np.sin(u)
z = v

# Stack into vertices
vertices = np.stack([x, y, z], axis=-1).reshape(-1, 3)

# Build faces
faces = []
for i in range(n_v - 1):
    for j in range(n_u - 1):
        idx = i * n_u + j
        faces.append([idx, idx + 1, idx + n_u])
        faces.append([idx + 1, idx + n_u + 1, idx + n_u])

faces = np.array(faces)

# Create mesh
mesh = trimesh.Trimesh(vertices=vertices, faces=faces)

# Export to STL
mesh.export('catenoid.stl')