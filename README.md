# 🚗 3D Car Model with OpenGL

A 3D interactive car model built with Python and OpenGL, featuring realistic steering physics, animated doors and hood, and an orbiting camera system.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![OpenGL](https://img.shields.io/badge/OpenGL-PyOpenGL-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## ✨ Features

- **Realistic Car Model**: Detailed 3D car with body, wheels, doors, hood, windows, and lights
- **Physics-Based Movement**: Car moves and turns based on steering wheel angle
- **Animated Components**:
  - Left and right doors that open and close smoothly
  - Hood that opens to reveal the engine bay
  - Front wheels that turn when steering
- **Interactive Camera**: 
  - Orbit around the car from any angle
  - Zoom in/out with mouse wheel
  - Camera always follows the car
- **Smooth Controls**: WASD for movement, arrow keys for camera, number keys for animations

## 🎮 Controls

### Car Movement
- **W** - Move forward (car turns if wheels are steered)
- **S** - Move backward (reverse steering)
- **A** - Turn steering wheel left (max 45°)
- **D** - Turn steering wheel right (max 45°)

### Camera Controls
- **Arrow Up/Down** - Rotate camera vertically (5° to 89°)
- **Arrow Left/Right** - Rotate camera horizontally around car
- **Mouse Wheel** - Zoom in/out (distance: 10-100 units)

### Animations
- **1** - Toggle left door (open/close)
- **2** - Toggle right door (open/close)
- **3** - Toggle hood (open/close)

## 📋 Prerequisites

- Python 3.7 or higher
- PyOpenGL
- PyOpenGL-accelerate (optional, for better performance)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/3d-car-opengl.git
cd 3d-car-opengl
```

2. Install required dependencies:
```bash
pip install PyOpenGL PyOpenGL-accelerate
```

## 🚀 Usage

Run the program:
```bash
python car_model.py
```

The window will open showing the red car model on a green ground with road markings.


## 🎨 Technical Details

### Architecture

**Rendering Pipeline**:
- Uses OpenGL fixed-function pipeline
- Double buffering for smooth rendering
- Depth testing for proper 3D occlusion
- Perspective projection with 45° FOV

**Coordinate System**:
- Car's local origin at (0, 0, 0)
- +Z axis points forward (front of car)
- +X axis points left
- +Y axis points up

**Physics Model**:
- Simple kinematic model
- Steering affects heading when moving
- Heading determines movement direction using trigonometry
- Position updated in world space

### Key Components

**Vertices**: All car parts defined as vertex arrays in local car space
- Body panels, glass, lights, bumpers, etc.
- Ground plane with road and grass

**Transformations**:
```
World Space → glTranslate(car_x, 0, car_z) → 
glRotate(car_heading) → Local Car Space
```

**Animation System**:
- State machine for door/hood animations
- 60 FPS timer callback for smooth motion
- Separate state tracking for each animated part

**Camera System**:
- Spherical coordinates (distance, angle_x, angle_y)
- Converted to Cartesian for `gluLookAt()`
- Always targets car position

## 🎯 Features Breakdown

### 1. Car Model
- **Geometry**: 20+ separate components (body, doors, hood, wheels, lights)
- **Materials**: Color-coded parts (red body, white lights, dark glass)
- **Details**: Tire panels, door handles, grill, bumpers

### 2. Movement System
- Forward/backward motion
- Turning physics based on front wheel angle
- Direction persistence (car remembers heading)
- Smooth acceleration/deceleration

### 3. Animation System
- Door opening: Rotates around vertical axis at door hinge
- Hood opening: Rotates around horizontal axis at front edge
- State machine: Closed → Opening → Open → Closing → Closed

### 4. Camera System
- Orbital camera with spherical coordinates
- Constraint: Vertical angle limited to prevent ground penetration
- Smooth zoom with distance limits
- Auto-follow: Camera position relative to car world position

## 🔍 Code Highlights

### Steering Physics
```python
if key_str == 'w':
    if abs(steer_angle) > 1.0:
        car_heading += steer_angle * 0.05
    car_x += math.sin(math.radians(car_heading)) * move_speed
    car_z += math.cos(math.radians(car_heading)) * move_speed
```

### Camera System
```python
camX = camera_distance * math.sin(math.radians(camera_angle_y)) * 
       math.cos(math.radians(camera_angle_x))
camY = camera_distance * math.sin(math.radians(camera_angle_x))
camZ = camera_distance * math.cos(math.radians(camera_angle_y)) * 
       math.cos(math.radians(camera_angle_x))

gluLookAt(car_x + camX, camY, car_z + camZ,
          car_x, 1.0, car_z,
          0.0, 1.0, 0.0)
```

## 🐛 Known Issues

- No collision detection with world boundaries
- Steering doesn't return to center automatically
- No reverse lights or brake lights
- No speedometer or UI overlay

## 🚧 Future Enhancements

- [ ] Add collision detection
- [ ] Implement automatic steering return to center
- [ ] Add working headlights and taillights
- [ ] Create a track or environment to drive around
- [ ] Add sound effects
- [ ] Implement a dashboard/HUD
- [ ] Add multiple camera views (first-person, chase, static)
- [ ] Physics improvements (acceleration, friction)
- [ ] Multiple car models/colors
- [ ] Texture mapping for more realistic appearance


## 🙏 Acknowledgments

- PyOpenGL community for excellent documentation
- OpenGL fixed-function pipeline tutorials
- Inspiration from classic car racing games


## 🎓 Learning Resources

- [PyOpenGL Documentation](http://pyopengl.sourceforge.net/documentation/index.html)
- [OpenGL Tutorial](https://www.opengl-tutorial.org/)
- [Learn OpenGL](https://learnopengl.com/)
- [3D Math Primer for Graphics](https://gamemath.com/)

---

**Made with ❤️ and OpenGL**
