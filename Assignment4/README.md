# README
## Introduction to Multimedia Technology HW4

---

### Q1. Bezier curve (1.py)
- a. plot curve
    - slide p.17
    - use 4 points as the a set of control_points and pass the parameter t
    - return P(t), the point on the Bezier curve corresponding to the parameter value t.
    ```python
    def bezier_curve(control_points, t):
    n = len(control_points) - 1
    result = 0
    for i in range(n + 1):
        coefficient = np.math.comb(n, i) * (t ** i) * ((1 - t) ** (n - i))
        result += coefficient * control_points[i]
    return result
    ```

- b. scale up the image by 4 and plot
    - use nearest_neighbor_interpolation(img, 4) to scale image by 4
    - scale the coordinates of the curve (before drawn)
    - plot high detail curve

### Q2. 3D Models (2.ipynb)
- a. shift the center to (0, 0, 0)
    ```python
    # Calculate the necessary shifts to move the center to the origin
    shifts = [-current_center[0], -current_center[1], -current_center[2]]

    # Apply the shifts to each vertex   
    x_shifted = [coord + shifts[0] for coord in x]
    y_shifted = [coord + shifts[1] for coord in y]
    z_shifted = [coord + shifts[2] for coord in z]
    ```
- b. rotate the bunny to face the screen
    ```python
    theta = np.pi / 2
    # Rotation matrix for a 90-degree rotation around the x-axis
    Rx = np.array([
    [1, 0, 0],
    [0, np.cos(theta), -np.sin(theta)],
    [0, np.sin(theta), np.cos(theta)]
    ])
    ```    
    - creates rotation matrices ‘Rx’, ‘Ry’, and ‘Rz’ for 90-degree rotations around the x-axis, y-axis, and z-axis, respectively.
- c. put a cubic under the foot of the bunny
    - use the position of bunny to define the vertices of the cubic, so that the cubic will be under the foot of the bunny.
    ```python
    centerX = (max(x_rotated)+min(x_rotated))/2
    centerY = (max(y_rotated)+min(y_rotated))/2
    centerZ = min(z_rotated)
    cube_x = [centerX-1, centerX+1, centerX+1, centerX-1, 
          centerX-1, centerX+1, centerX+1, centerX-1]  
    cube_y = [centerY-1, centerY-1, centerY+1, centerY+1, 
          centerY-1, centerY-1, centerY+1, centerY+1]  
    cube_z = [centerZ, centerZ, centerZ, centerZ, centerZ-1, centerZ-1, centerZ-1, centerZ-1]    
    ```
- d. try different ambient strength, diffuse strength, and specular strength
    - modify the setting of lighting
    ```python
    fig.add_trace(
    go.Surface(z=Z, colorscale='Viridis', lighting=dict(ambient=0.1, diffuse=0.8, specular=0.05)),
    row=1, col=1)

    fig.add_trace(
    go.Surface(z=Z, colorscale='Viridis', lighting=dict(ambient=0.9, diffuse=0.8, specular=0.05)),
    row=1, col=2)
    ```
