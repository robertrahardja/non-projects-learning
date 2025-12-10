"""
Blender Python Script: Worm-like Walking Animation for Arm Rig
This script creates an undulating, worm-like movement animation.
"""

import bpy
import math

# Configuration
BLEND_FILE = "/Users/robertrahardja/Projects/Trial/blender_animation/assets/arm.blend"
ANIMATION_LENGTH = 120  # frames
FPS = 24
WAVE_SPEED = 2.0  # How fast the wave travels
WAVE_AMPLITUDE = 0.5  # How much each bone moves up/down
FORWARD_SPEED = 0.05  # How fast the worm moves forward

def setup_scene():
    """Load the blend file and prepare the scene"""
    # Clear existing scene
    bpy.ops.wm.read_factory_settings(use_empty=True)

    # Load the arm.blend file
    bpy.ops.wm.open_mainfile(filepath=BLEND_FILE)

    # Set frame range
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = ANIMATION_LENGTH
    bpy.context.scene.render.fps = FPS

    print("Scene setup complete")

def get_armature_and_bones():
    """Find the armature object and its bones"""
    armature_obj = None

    # Find armature object
    for obj in bpy.data.objects:
        if obj.type == 'ARMATURE':
            armature_obj = obj
            break

    if not armature_obj:
        print("ERROR: No armature found in the file!")
        return None, []

    # Deselect all objects first
    bpy.ops.object.select_all(action='DESELECT')

    # Set as active object and select it
    bpy.context.view_layer.objects.active = armature_obj
    armature_obj.select_set(True)

    # Use override context to ensure we can change modes
    with bpy.context.temp_override(active_object=armature_obj, object=armature_obj):
        # Switch to pose mode
        bpy.ops.object.mode_set(mode='POSE')

    # Get all pose bones sorted by their hierarchy
    pose_bones = armature_obj.pose.bones

    print(f"Found armature: {armature_obj.name}")
    print(f"Number of bones: {len(pose_bones)}")
    for bone in pose_bones:
        print(f"  - {bone.name}")

    return armature_obj, pose_bones

def create_worm_animation(armature_obj, pose_bones):
    """Create undulating worm-like animation"""

    # Clear existing animation data
    if armature_obj.animation_data:
        armature_obj.animation_data_clear()

    # Get bones as a list for indexing
    bone_list = list(pose_bones)
    num_bones = len(bone_list)

    if num_bones == 0:
        print("ERROR: No bones to animate!")
        return

    print(f"\nCreating worm animation with {num_bones} bones...")

    # Animate each frame
    for frame in range(1, ANIMATION_LENGTH + 1):
        bpy.context.scene.frame_set(frame)

        # Calculate time for wave propagation
        time = frame / FPS

        # Animate each bone with a wave pattern
        for i, bone in enumerate(bone_list):
            # Phase offset based on bone position in chain
            phase = (i / max(num_bones - 1, 1)) * 2 * math.pi

            # Sinusoidal wave for vertical movement (worm undulation)
            vertical_offset = WAVE_AMPLITUDE * math.sin(WAVE_SPEED * time * 2 * math.pi - phase)

            # Apply vertical movement (Z-axis rotation creates arc motion)
            bone.rotation_euler[0] = vertical_offset  # X-axis rotation
            bone.rotation_euler[2] = math.sin(WAVE_SPEED * time * 2 * math.pi - phase + math.pi/2) * 0.3  # Z-axis for side-to-side

            # Forward movement (translate the root/first bone)
            if i == 0:
                bone.location[1] = FORWARD_SPEED * frame  # Y-axis forward movement
                bone.location[2] = abs(vertical_offset) * 0.5  # Slight vertical bounce

            # Insert keyframes
            bone.keyframe_insert(data_path="rotation_euler", frame=frame)
            if i == 0:
                bone.keyframe_insert(data_path="location", frame=frame)

    print(f"Animation complete! {ANIMATION_LENGTH} frames animated.")
    print("Tip: Press spacebar in Blender to play the animation")

def smooth_animation(armature_obj):
    """Make the animation smoother by setting interpolation"""
    if not armature_obj.animation_data or not armature_obj.animation_data.action:
        print("No animation data to smooth")
        return

    for fcurve in armature_obj.animation_data.action.fcurves:
        for keyframe in fcurve.keyframe_points:
            keyframe.interpolation = 'BEZIER'
            keyframe.handle_left_type = 'AUTO_CLAMPED'
            keyframe.handle_right_type = 'AUTO_CLAMPED'

    print("Animation curves smoothed")

def main():
    """Main execution function"""
    print("=" * 50)
    print("WORM ANIMATION GENERATOR")
    print("=" * 50)

    # Setup
    setup_scene()

    # Get armature and bones
    armature_obj, pose_bones = get_armature_and_bones()

    if not armature_obj:
        print("Failed to find armature. Exiting.")
        return

    # Create animation
    create_worm_animation(armature_obj, pose_bones)

    # Smooth it out
    smooth_animation(armature_obj)

    # Save as a new file
    output_file = "/Users/robertrahardja/Projects/Trial/blender_animation/assets/arm_worm_animation.blend"
    bpy.ops.wm.save_as_mainfile(filepath=output_file)
    print(f"\nAnimation saved to: {output_file}")

    print("\n" + "=" * 50)
    print("ANIMATION READY!")
    print("=" * 50)
    print("\nNext steps:")
    print("1. Press SPACEBAR to preview the animation")
    print("2. Go to Render > Render Animation to export")
    print("3. Adjust WAVE_SPEED, WAVE_AMPLITUDE, or FORWARD_SPEED at the top of the script to tune the motion")
    print(f"4. Your animation is saved at: {output_file}")

# Run the script
if __name__ == "__main__":
    main()
