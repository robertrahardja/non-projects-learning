"""
Create an SVG with properly grouped eye elements for realistic blinking
Each eye will be wrapped in a <g> tag so the entire eye (including eyelids,
whites, pupils, highlights) can be animated as a unit.
"""

import re
from pathlib import Path

def create_grouped_svg():
    # Read the original SVG
    with open("assets/girl.svg", 'r') as f:
        svg_content = f.read()

    lines = svg_content.split('\n')
    output_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]

        # Right eye group starts around line 6-7 (pupil and eyelid areas)
        # We need to group lines 6-11 approximately (the right eye area)
        if i == 6 and 'fill="#3E0E18"' in line and 'M485.806' in line:
            output_lines.append('  <g id="eye-right-group">')
            output_lines.append('    <!-- Right eye pupil -->')
            output_lines.append('    ' + line)
            i += 1
            # Add next lines (eyelid, whites, highlights) until we're past the eye
            while i <= 11:
                if i == 7:
                    output_lines.append('    <!-- Right eyelid -->')
                elif i == 9:
                    output_lines.append('    <!-- Right eye white -->')
                elif i == 10:
                    output_lines.append('    <!-- Right eye highlight -->')
                output_lines.append('    ' + lines[i])
                i += 1
            output_lines.append('  </g>')
            continue

        # Left eye group starts around line 51-56
        # Check for the left eye pupil area
        if i == 52 and 'fill="#3E0E18"' in line and 'M315.798' in line:
            output_lines.append('  <g id="eye-left-group">')
            output_lines.append('    <!-- Left eye pupil area -->')
            output_lines.append('    ' + line)
            i += 1
            # Continue through the left eye elements
            while i <= 73:
                if i == 55 and 'fill="#150B0B"' in line:
                    output_lines.append('    <!-- Left eyelid -->')
                elif i == 69 and 'fill="white"' in line and 'M330.272' in line:
                    output_lines.append('    <!-- Left eye white -->')
                elif i == 72 and 'fill="white"' in line and 'M352.247' in line:
                    output_lines.append('    <!-- Left eye highlight -->')
                output_lines.append('    ' + lines[i])
                i += 1
            output_lines.append('  </g>')
            continue

        output_lines.append(line)
        i += 1

    # Write the new SVG
    with open("assets/girl_grouped.svg", 'w') as f:
        f.write('\n'.join(output_lines))

    print("✓ Created assets/girl_grouped.svg with grouped eyes")
    print("\nEye groups created:")
    print("  - #eye-right-group (all right eye elements)")
    print("  - #eye-left-group (all left eye elements)")
    print("\nThese groups can now be animated together for realistic blinking!")

if __name__ == "__main__":
    create_grouped_svg()
