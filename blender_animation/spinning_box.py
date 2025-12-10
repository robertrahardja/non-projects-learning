import bpy

# Configuration
ANIMATION_LENGTH = 120  # Total frames (120 = 5 seconds at 24fps)
ROTATION_SPEED = 6.28   # Radians per cycle (6.28 = 360 degrees, one full spin)
CUBE_SIZE = 2           # Size of the cube
PINK_COLOR = (1.0, 0.2, 0.5)  # RGB - adjust for different shades of pink
METALLIC = 1.0          # Metallic value (0.0 = non-metallic, 1.0 = fully metallic)
ROUGHNESS = 0.1         # Roughness value (0.0 = mirror-like, 1.0 = matte)
LIGHT_STRENGTH = 1000   # Strength of the light source

# Clear default scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create a cube
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0), size=CUBE_SIZE)
cube = bpy.context.active_object
cube.name = "SpinningBox"

# Create a shiny metallic pink material
pink_material = bpy.data.materials.new(name="MetallicPinkMaterial")
pink_material.use_nodes = True

# Get the material's node tree
nodes = pink_material.node_tree.nodes
links = pink_material.node_tree.links

# Clear default nodes
nodes.clear()

# Create Principled BSDF shader (physically-based material)
principled = nodes.new(type='ShaderNodeBsdfPrincipled')
principled.location = (0, 0)

# Set pink color
principled.inputs['Base Color'].default_value = (*PINK_COLOR, 1.0)

# Set metallic properties for shininess
principled.inputs['Metallic'].default_value = METALLIC
principled.inputs['Roughness'].default_value = ROUGHNESS

# Add some specular highlight
principled.inputs['Specular IOR Level'].default_value = 0.5

# Create Material Output node
output = nodes.new(type='ShaderNodeOutputMaterial')
output.location = (200, 0)

# Connect Principled BSDF to Material Output
links.new(principled.outputs['BSDF'], output.inputs['Surface'])

# Apply material to cube
cube.data.materials.append(pink_material)

# Set up the rotation animation
# Frame 1: no rotation
cube.rotation_euler = (0, 0, 0)
cube.keyframe_insert(data_path="rotation_euler", frame=1)

# Frame ANIMATION_LENGTH: full rotation on Z axis
cube.rotation_euler = (0, 0, ROTATION_SPEED)
cube.keyframe_insert(data_path="rotation_euler", frame=ANIMATION_LENGTH)

# Configure animation settings
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = ANIMATION_LENGTH

# Set interpolation to linear for constant rotation speed
for fcurve in cube.animation_data.action.fcurves:
    for keyframe in fcurve.keyframe_points:
        keyframe.interpolation = 'LINEAR'

# Add a strong light source to showcase the metallic shininess
bpy.ops.object.light_add(type='SUN', location=(5, 5, 5))
sun_light = bpy.context.active_object
sun_light.name = "MainLight"
sun_light.data.energy = LIGHT_STRENGTH

# Rotate the light to point at the cube
sun_light.rotation_euler = (-0.785, 0, 0.785)  # 45 degrees on X and Z

# Add a secondary fill light for better highlights
bpy.ops.object.light_add(type='AREA', location=(-3, -3, 3))
fill_light = bpy.context.active_object
fill_light.name = "FillLight"
fill_light.data.energy = 300
fill_light.data.size = 5

# Point fill light at cube
fill_light.rotation_euler = (0.785, 0, -0.785)

# Add a camera for better viewing
bpy.ops.object.camera_add(location=(7, -7, 5))
camera = bpy.context.active_object
camera.name = "MainCamera"

# Point camera at cube
direction = (-7, 7, -5)
import math
camera.rotation_euler = (
    math.atan2(direction[2], math.sqrt(direction[0]**2 + direction[1]**2)) + math.pi/2,
    0,
    math.atan2(direction[0], direction[1])
)

# Set as active camera
scene.camera = camera

# Switch to Cycles render engine for better metallic rendering
scene.render.engine = 'CYCLES'
scene.cycles.samples = 128  # Good balance between quality and speed

# Enable viewport shading to see materials
for area in bpy.context.screen.areas:
    if area.type == 'VIEW_3D':
        for space in area.spaces:
            if space.type == 'VIEW_3D':
                space.shading.type = 'MATERIAL'

print(f"Shiny metallic pink box created!")
print(f"- Animation length: {ANIMATION_LENGTH} frames")
print(f"- Rotation: {ROTATION_SPEED} radians ({ROTATION_SPEED * 57.3:.0f} degrees)")
print(f"- Cube size: {CUBE_SIZE}")
print(f"- Color (RGB): {PINK_COLOR}")
print(f"- Metallic: {METALLIC}, Roughness: {ROUGHNESS}")
print(f"- Lighting: Sun ({LIGHT_STRENGTH}W) + Area fill (300W)")
print(f"- Render engine: Cycles ({scene.cycles.samples} samples)")
print("\nPress SPACEBAR in Blender to preview the animation")
print("The metallic surface will show beautiful reflections and highlights!")
