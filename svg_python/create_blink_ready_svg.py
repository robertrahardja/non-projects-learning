"""
Create an SVG with eye elements properly grouped for blinking animation.
Each complete eye (eyelids, whites, pupils, highlights) will be in a <g> group.
"""

import xml.etree.ElementTree as ET
from pathlib import Path

def create_blink_ready_svg():
    # Parse the SVG
    svg_path = Path("assets/girl.svg")
    tree = ET.parse(svg_path)
    root = tree.getroot()

    # Define namespace
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    ET.register_namespace('', 'http://www.w3.org/2000/svg')
    ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')

    # Find all path elements
    paths = list(root.findall('.//svg:path', ns))

    # We'll collect paths that belong to each eye based on their fill colors and coordinates
    # Right eye area: paths around coordinates 500-580 x, 380-480 y
    # Left eye area: paths around coordinates 280-390 x, 380-500 y

    right_eye_paths = []
    left_eye_paths = []
    other_paths = []

    for path in paths:
        d = path.get('d', '')
        fill = path.get('fill', '')
        path_id = path.get('id', '')

        # Check if this path is part of the right eye
        if any(keyword in path_id for keyword in ['eye-right', 'pupil-right']) or \
           (('M5' in d[:10] or 'M4' in d[:10]) and any(coord in d for coord in ['399', '409', '411', '417', '426', '437', '441'])):
            if fill in ['#3E0E18', '#150B0B', 'white', 'url(#gradient'] or 'eye' in path_id:
                right_eye_paths.append(path)
                continue

        # Check if this path is part of the left eye
        if any(keyword in path_id for keyword in ['eye-left', 'pupil-left']) or \
           (('M3' in d[:10] or 'M2' in d[:10]) and any(coord in d for coord in ['414', '434', '441', '462', '472'])):
            if fill in ['#3E0E18', '#150B0B', 'white', '#9D99A5'] or 'eye' in path_id:
                left_eye_paths.append(path)
                continue

        other_paths.append(path)

    # Remove the eye paths from root
    for path in right_eye_paths + left_eye_paths:
        root.remove(path)

    # Create groups for eyes
    right_eye_group = ET.Element('g', {'id': 'eye-right-complete'})
    for path in right_eye_paths:
        right_eye_group.append(path)

    left_eye_group = ET.Element('g', {'id': 'eye-left-complete'})
    for path in left_eye_paths:
        left_eye_group.append(path)

    # Find a good position to insert the eye groups (after background, before other facial features)
    # Insert after the first few paths
    insert_position = 5
    root.insert(insert_position, right_eye_group)
    root.insert(insert_position + 1, left_eye_group)

    # Write the output
    output_path = Path("assets/girl_grouped.svg")
    tree.write(output_path, encoding='utf-8', xml_declaration=True)

    print(f"✓ Created {output_path}")
    print(f"\nRight eye group: {len(right_eye_paths)} paths")
    print(f"Left eye group: {len(left_eye_paths)} paths")
    print("\nUse #eye-right-complete and #eye-left-complete for blinking animations!")

if __name__ == "__main__":
    create_blink_ready_svg()
