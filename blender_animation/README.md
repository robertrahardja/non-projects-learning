# Blender Animation Scripts

This project contains Python scripts for creating procedural animations in Blender.

## Projects

1. **Worm Animation** - A worm-like walking animation for an arm rig
2. **Spinning Pink Box** - A simple spinning cube with pink material

---

## Spinning Pink Box

A simple spinning cube animation demonstrating basic rotation keyframes.

### Quick Start

```bash
./run_spinning_box.sh
```

Or run manually:
```bash
blender --python spinning_box.py
```

### Features

- **Metallic Material**: Shiny, reflective surface using Principled BSDF shader
- **Dual Lighting**: Sun light + area fill light for dramatic highlights
- **Cycles Rendering**: Physically-based rendering for realistic metallic appearance
- **Auto Camera Setup**: Positioned for optimal viewing angle

### Customization

Edit these parameters in `spinning_box.py`:

```python
ANIMATION_LENGTH = 120  # Total frames (120 = 5 seconds at 24fps)
ROTATION_SPEED = 6.28   # Radians (6.28 = 360°, 12.56 = 720°)
CUBE_SIZE = 2           # Size of the cube
PINK_COLOR = (1.0, 0.2, 0.5)  # RGB values (red, green, blue)
METALLIC = 1.0          # 0.0 = plastic, 1.0 = pure metal
ROUGHNESS = 0.1         # 0.0 = mirror, 1.0 = matte
LIGHT_STRENGTH = 1000   # Brightness of main sun light
```

**Material tips:**
- Lower `ROUGHNESS` (0.0-0.2) = more mirror-like, sharp reflections
- Higher `ROUGHNESS` (0.5-1.0) = softer, more diffuse appearance
- Adjust `PINK_COLOR` RGB values between 0.0 and 1.0 for different colors

**Rotation tips:**
- Change the third value in `rotation_euler = (X, Y, Z)` to spin on different axes
- X-axis: tumble forward/backward
- Y-axis: roll left/right
- Z-axis: spin like a top (default)

### Rendering

**Single frame:**
```python
scene.render.filepath = "/tmp/spinning_box.png"
bpy.ops.render.render(write_still=True)
```

**Full animation:**
```python
scene.render.filepath = "/tmp/output_####.png"
bpy.ops.render.render(animation=True)
```

Then encode to video:
```bash
ffmpeg -framerate 24 -i /tmp/output_%04d.png -c:v libx264 output.mp4
```

---

## Worm Animation

### How to Use

#### Option 1: Run from Blender's Text Editor

1. Open Blender
2. Go to **Scripting** workspace (top menu bar)
3. Click **Open** and select `worm_animation.py`
4. Click **Run Script** button (or press Alt+P)
5. The animation will be generated automatically

#### Option 2: Run from Command Line

```bash
./run_worm_animation.sh
```

Or manually:
```bash
blender --python worm_animation.py
```

## What the Script Does

The script creates a realistic worm-like movement by:

1. **Undulating Motion**: Each bone moves in a sinusoidal wave pattern
2. **Wave Propagation**: The wave travels down the armature from head to tail
3. **Forward Movement**: The entire rig gradually moves forward
4. **Side-to-Side Sway**: Adds natural-looking side movement

## Customization

You can adjust these parameters at the top of `worm_animation.py`:

```python
ANIMATION_LENGTH = 120  # Total frames (120 = 5 seconds at 24fps)
WAVE_SPEED = 2.0        # How fast the wave travels (higher = faster)
WAVE_AMPLITUDE = 0.5    # How much vertical movement (higher = more dramatic)
FORWARD_SPEED = 0.05    # How fast it moves forward (higher = faster crawling)
```

## Animation Details

- **Frame Range**: 1-120 (5 seconds at 24 FPS)
- **Interpolation**: Bezier curves for smooth motion
- **Bone Rotation**: X-axis for vertical undulation, Z-axis for side-to-side
- **Root Movement**: Only the first bone translates forward

## Troubleshooting

**No armature found?**
- Make sure `arm.blend` is in the `assets/` folder
- Check that the blend file contains an armature object

**Animation looks wrong?**
- Try reducing `WAVE_AMPLITUDE` to 0.3 for subtler movement
- Adjust `WAVE_SPEED` to match your desired crawling pace
- Increase `ANIMATION_LENGTH` to see the full motion cycle

## Next Steps

After generating the animation:
1. Press **Spacebar** in Blender to preview
2. Scrub the timeline to see the worm motion
3. Render animation: **Render > Render Animation**
4. Export video: Set output format in **Output Properties** panel
