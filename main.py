from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

# --- Variabel Global yang Relevan untuk Penggambaran Model ---
movement = 0.0 # Digunakan untuk menggerakkan mobil pada sumbu Z

def init():
    """Inisialisasi pengaturan OpenGL."""
    # Ini harus dipanggil jika ingin menjalankan kode ini sebagai script mandiri
    # di luar konteks GLUT lengkap untuk inisialisasi GL.
    # Namun, karena bagian ini tidak mendefinisikan geometri, saya tetap memasukkannya
    # untuk kepatuhan, tetapi perlu diingat bahwa GL_DEPTH_TEST penting.
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)


# --- Definisi Geometri Mobil (Vertices) ---
# Koordinat untuk berbagai bagian mobil.
# Hanya menyertakan bagian mobil, menghilangkan 'ground'
frontBody = [
    [2.8,1.0,10.5], [3.0,1.0,8.0], [2.8,3.5,10.5], [3.0,4.0,8.0],
    [0.0,3.5,10.7], [0.0,4.0,8.0], [-2.8,3.5,10.5], [-3.0,4.0,8.0],
    [-2.8,1.0,10.5], [-3.0,1.0,8.0], [0.0,1.1,10.7], [0.0,1.1,8.0],
    [2.8,1.0,10.5], [3.0,1.0,8.0],
]
grill = [
    [2.8,1.0,10.5], [2.8,3.5,10.5], [0.0,1.1,10.7], [0.0,3.5,10.7],
    [-2.8,1.0,10.5], [-2.8,3.5,10.5],
]
frontLight = [
    [2.6,3.2,10.55], [1.6,3.2,10.6], [1.6,2.7,10.6], [2.6,2.7,10.55],
    [-2.6,3.2,10.55], [-1.6,3.2,10.6], [-1.6,2.7,10.6], [-2.6,2.7,10.55],
]
hood = [
    [3.0,4.0,8.0], [3.0,4.0,4.0], [-3.0,4.0,4.0], [-3.0,4.0,8.0],
]
leftTirePanel = [
    [-3.0,1.0,8.0], [-3.0,4.0,8.0], [-3.0,2.5,7.0], [-3.0,4.0,6.0],
    [-3.0,2.5,5.0], [-3.0,4.0,4.0], [-3.0,1.0,4.0],
]
rightTirePanel = [
    [3.0,1.0,8.0], [3.0,4.0,8.0], [3.0,2.5,7.0], [3.0,4.0,6.0],
    [3.0,2.5,5.0], [3.0,4.0,4.0], [3.0,1.0,4.0],
]
frontGlassRim = [
    [-3.0,4.0,4.0], [3.0,4.0,4.0], [3.0,6.0,1.0], [-3.0,6.0,1.0],
]
frontGlass = [
    [-2.8,4.0,4.08], [2.8,4.0,4.08], [2.8,5.9,1.14], [-2.8,5.9,1.14],
]
roof = [
    [-3.0,6.0,1.0], [3.0,6.0,1.0], [3.0,6.0,-3.0], [-3.0,6.0,-3.0],
]
rightBody = [
    [-3.0,6.0,-2.0], [-3.0,6.0,-3.0], [-3.0,4.5,-5.0], [-3.0,2.5,-5.0], [-3.0,1.0,-4.0], 
    [-3.0,1.0,-3.0], [-3.0,1.0,-2.0],
]
rightDoorPanel = [
    [-3.0,4.0,4.0], [-3.0,6.0,1.0], [-3.0,6.0,-2],
    [-3.0,1.0,-2], [-3.0,1.0,4.0],
]
leftBody = [
    [3.0,6.0,-2.0], [3.0,6.0,-3.0], [3.0,4.5,-5.0], [3.0,2.5,-5.0],[3.0,1.0,-4.0], 
    [3.0,1.0,-3.0], [3.0,1.0,-2.0]
]
leftDoorPanel = [
    [3.0,4.0,4.0], [3.0,6.0,1.0], [3.0,6.0,-2.0], 
    [3.0,1.0,-2], [3.0,1.0,4.0],
]
bottom = [
    [-3.0,1.0,4.0], [3.0,1.0,4.0], [3.0,1.0,-4.0], [-3.0,1.0,-4.0],
]
rightGlassOne = [
    [-3.1,4.0,3.5], [-3.1,5.8,0.8], [-3.1,5.8,-0.8], [-3.1,4.0,-0.8],
]
leftGlassOne = [
    [3.1,4.0,3.5], [3.1,5.8,0.8], [3.1,5.8,-1.0], [3.1,4.0,-1.0],
]
rightHandle = [
    [3.1,3.5,0.0], [3.1,3.5,0.8], [3.1,3.2,0.8], [3.1,3.2,0.0],
]
leftHandle = [
    [-3.1,3.5,0.0], [-3.1,3.5,0.8], [-3.1,3.2,0.8], [-3.1,3.2,0.0],
]
backGlass = [
    [-2.8,5.9,-3.3], [2.8,5.9,-3.3], [2.8,4.5,-5.0], [-2.8,4.5,-5.0],
]
backGlassRim = [
    [-3.0,6.0,-3.0], [3.0,6.0,-3.0], [3.0,4.5,-5.0], [-3.0,4.5,-5.0],
]
backTirePanel = [
    [3.0,2.5,-5.0], [3.0,2.5,-7.5], [3.0,4.5,-5.0], [3.0,4.0,-7.0],
    [-3.0,4.5,-5.0], [-3.0,4.0,-7.0], [-3.0,2.5,-5.0], [-3.0,2.5,-7.5],
    [3.0,2.5,-5.0], [3.0,2.5,-7.5],
]
backBody = [
    [3.0,1.0,-8.0], [3.0,1.5,-10.0], [3.0,4.0,-7.0], [3.0,4.5,-10.5],
    [-3.0,4.0,-7.0], [-3.0,4.5,-10.5], [-3.0,1.0,-8.0], [-3.0,1.5,-10.0],
    [3.0,1.0,-8.0], [3.0,1.5,-10.0],
]
bumper = [
    [-3.0,1.5,-10.0], [3.0,1.5,-10.0], [3.0,4.5,-10.5], [-3.0,4.5,-10.5],
]
backLight = [
    [-2.6,3.5,-10.4], [-1.2,3.5,-10.4], [-1.2,4.2,-10.5], [-2.6,4.2,-10.5],
    [2.6,3.5,-10.4], [1.2,3.5,-10.4], [1.2,4.2,-10.5], [2.6,4.2,-10.5],
]


# --- Fungsi Penggambaran (Drawing Functions) ---

def draw_geometry(vertices, gl_mode, color=None):
    """Fungsi helper untuk menggambar geometri dari list vertex."""
    global movement
    glBegin(gl_mode)
    for i, v in enumerate(vertices):
        # Penentuan warna
        if color:
            glColor3f(color[0], color[1], color[2])
        # Hilangkan bagian 'ground' dari logika pewarnaan
        elif vertices is frontLight:
            glColor3f(1.0, 1.0, 1.0) # Putih
        elif vertices is backLight:
            glColor3f(1.0, 0.0, 0.0) # Merah
        elif vertices is frontGlass:
            glColor3f(0.317, 0.309, 0.301) # Kaca
        elif vertices is roof:
            glColor3f(0.913, 0.494, 0.047) # Atap
        elif vertices is backGlassRim:
            glColor3f(0.956, 0.560, 0.145) # Rangka Kaca Belakang
        elif vertices is grill:
            glColor3f(0.964, 0.639, 0.298) # Grill``
        elif vertices is hood:
            glColor3f(0.956, 0.541, 0.101) # Kap Mesin
        elif vertices is leftDoorPanel :
            glColor3f(1, 1, 1) # Pintu
        elif vertices is rightDoorPanel :
            glColor3f(1, 1, 1) # Pintu
        elif vertices is leftBody or vertices is rightBody:
            glColor3f(0.960, 0.6, 0.219) # Pintu
        elif vertices is backBody:
            glColor3f(0.964, 0.6, 0.215) # Body Belakang
        elif vertices is bumper:
            glColor3f(0.964, 0.631, 0.274) # Bumper
        elif vertices in (rightGlassOne, leftGlassOne, backGlass, rightHandle, leftHandle):
            glColor3f(0.317, 0.309, 0.301) # Kaca Samping/Belakang & Handle
        else:
            glColor3f(0.956, 0.592, 0.203) # Warna body utama (default)

        # Apply movement
        glVertex3f(v[0], v[1], v[2] + movement)
    glEnd()

def draw_tires():
    """Menggambar keempat ban dengan transformasi yang benar."""
    global movement
    # Ban digambar menggunakan Solid Torus (Donat)
    glColor3f(0.1, 0.1, 0.1) # Warna ban

    # Ban Kanan Depan (Tire Front Right)
    glPushMatrix()
    glTranslatef(3.0, 1.0, 6.0 + movement)
    glRotatef(90, 0, 1, 0)
    glutSolidTorus(0.75, 0.75, 10, 10)
    glPopMatrix()
    
    # Ban Kiri Depan (Tire Front Left)
    glPushMatrix()
    glTranslatef(-3.0, 1.0, 6.0 + movement) 
    glRotatef(90, 0, 1, 0)
    glutSolidTorus(0.75, 0.75, 10, 10)
    glPopMatrix()

    # Ban Kiri Belakang (Tire Back Left)
    glPushMatrix()
    glTranslatef(-3.0, 1.0, -6.0 + movement) 
    glRotatef(90, 0, 1, 0)
    glutSolidTorus(0.75, 0.75, 10, 10)
    glPopMatrix()

    # Ban Kanan Belakang (Tire Back Right)
    glPushMatrix()
    glTranslatef(3.0, 1.0, -6.0 + movement) 
    glRotatef(90, 0, 1, 0)
    glutSolidTorus(0.75, 0.75, 10, 10)
    glPopMatrix()

def draw_car_model():
    """Fungsi untuk menggambar model mobil."""
    # --- Menggambar Geometri Mobil ---
    # Hilangkan draw_geometry(ground, GL_QUADS)
    draw_geometry(frontBody, GL_QUAD_STRIP)
    draw_geometry(grill, GL_QUAD_STRIP)
    draw_geometry(frontLight, GL_QUADS)
    draw_geometry(hood, GL_QUADS)
    draw_geometry(leftTirePanel, GL_TRIANGLE_STRIP)
    draw_geometry(rightTirePanel, GL_TRIANGLE_STRIP)
    draw_geometry(frontGlassRim, GL_QUADS)
    draw_geometry(frontGlass, GL_QUADS)
    draw_geometry(roof, GL_QUADS)
    draw_geometry(leftBody, GL_TRIANGLE_FAN)
    draw_geometry(leftDoorPanel, GL_TRIANGLE_FAN)
    draw_geometry(rightDoorPanel, GL_TRIANGLE_FAN)
    draw_geometry(rightBody, GL_TRIANGLE_FAN)
    draw_geometry(bottom, GL_QUADS)
    draw_geometry(rightGlassOne, GL_QUADS)
    draw_geometry(leftGlassOne, GL_QUADS)
    draw_geometry(rightHandle, GL_QUADS)
    draw_geometry(leftHandle, GL_QUADS)
    draw_geometry(backGlass, GL_QUADS)
    draw_geometry(backGlassRim, GL_QUADS)
    draw_geometry(backTirePanel, GL_QUAD_STRIP)
    draw_geometry(backBody, GL_QUAD_STRIP)
    draw_geometry(bumper, GL_QUADS)
    draw_geometry(backLight, GL_QUADS)

    # Ban
    draw_tires()


# --- Contoh fungsi display untuk melihat mobil secara terisolasi ---

def display_car_only():
    """Contoh fungsi display untuk merender hanya mobil."""
    global spin_x, spin_y, Zoom
    # Anda perlu mendefinisikan spin_x, spin_y, Zoom
    # atau menghapusnya dan mengatur sudut pandang secara manual
    
    spin_x = 35 # Contoh nilai default
    spin_y = 25 # Contoh nilai default
    Zoom = 1.0  # Contoh nilai default

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Transformasi Viewport (Diadaptasi dari kode asli, diatur untuk tampilan mobil)
    # Geser ke belakang (-Z) untuk melihat objek, dan sedikit geser ke bawah (-Y)
    glTranslatef(0.0, -3.0, -40.0) 
    
    # Rotasi untuk sudut pandang
    glRotatef(spin_x, 0.0, 1.0, 0.0)
    glRotatef(spin_y, 1.0, 0.0, 0.0) # Mengubah sumbu rotasi untuk spin_y

    glScalef(Zoom, Zoom, Zoom)

    draw_car_model()

    glutSwapBuffers()

# Catatan: Untuk menjalankan fungsi display_car_only() ini, Anda tetap memerlukan 
# setup dasar GLUT, reshape, dan init.