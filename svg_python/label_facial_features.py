"""
Script to add clear labels/IDs to facial features in girl.svg for animation purposes.
This will identify and label eyes, eyelids, and mouth elements.
"""

import re
from pathlib import Path

def add_facial_feature_ids(input_svg_path, output_svg_path):
    """
    Add IDs to facial features for easier animation.

    The eyelids are the dark paths around the eyes (fill="#150B0B" or fill="#3E0E18")
    that are positioned near the eye elements.
    """

    with open(input_svg_path, 'r') as f:
        svg_content = f.read()

    # Track line numbers for context
    lines = svg_content.split('\n')

    # We'll identify eyelids by their position relative to already-labeled eyes
    # Right eye is around line 7-10, left eye around line 54-56

    # Add ID to right eyelid (the dark path just before the right eye)
    # Line 7: <path fill="#150B0B" ...> before eye-right
    svg_content = re.sub(
        r'<path fill="#150B0B" d="M541\.048 399\.398.*?Z"/>',
        r'<path id="eyelid-right" fill="#150B0B" d="M541.048 399.398C544.214 401.911 546.68 403.866 549.595 406.696C550.229 407.312 554.515 411.82 554.702 411.962C559.346 420.947 560.063 429.673 556.949 439.363C556.72 440.074 556.479 440.782 556.228 441.486C546.855 460.597 534.461 459.536 521.702 444.49C521.703 444.492 520.752 442.559 520.804 442.635C517.83 438.341 517.804 430.32 516.509 426.927C516.937 423.94 517.411 420.961 517.931 417.989L518.453 417.19C527.347 416.046 529.38 414.827 535.918 409.039C539.005 408.191 540.307 402.321 541.048 399.398Z"/>',
        svg_content,
        count=1
    )

    # Add ID to left eyelid (line 54-55)
    svg_content = re.sub(
        r'<path fill="#150B0B" d="M330\.272 434\.745.*?Z"/>',
        r'<path id="eyelid-left" fill="#150B0B" d="M330.272 434.745C310.684 418.747 342.443 386.779 356.384 410.549C360.455 406.724 365.24 409.59 368.256 413.157C374.241 420.236 378.338 431.098 379.92 440.111L380.235 441.941C381.226 445.852 380.71 464.513 381.929 465.478C382.993 466.32 383.743 466.816 384.119 468.188C383.591 471.257 379.578 478.983 377.77 481.135L377.27 481.992C376.249 483.773 375.88 484.591 375.735 486.678C376.466 487.839 375.941 487.513 377.249 487.813C377.916 487.334 382.645 480.415 383.143 479.268L383.384 479.47C382.515 483.284 376.139 491.043 372.619 492.835C358.595 499.976 345.11 499.502 332.984 489.838C329.085 486.8 325.601 481.965 323.573 477.49C320.056 469.733 319.318 466.709 322.023 458.784C320.85 453.836 320.601 444.926 321.38 439.864C322.085 434.467 323.889 434.252 328.744 435.703L330.272 434.745Z"/>',
        svg_content,
        count=1
    )

    # The existing labels are already good:
    # - eye-right-white (highlight/glint on right eye)
    # - eye-right (right eye white)
    # - eye-left (left eye white)
    # - eye-left-highlight (highlight/glint on left eye)
    # - mouth

    # Let's also add IDs for the pupils/irises (the darker inner parts)
    # Right pupil is line 6
    svg_content = re.sub(
        r'(<path fill="#3E0E18" d="M485\.806 395\.593.*?466\.064 421\.677.*?Z"/>)',
        lambda m: m.group(0).replace('<path fill="#3E0E18"', '<path id="pupil-right" fill="#3E0E18"', 1),
        svg_content,
        count=1
    )

    # Left eye area - line 51
    svg_content = re.sub(
        r'(<path fill="#3E0E18" d="M315\.798 414\.639.*?315\.798 414\.639.*?Z"/>)',
        lambda m: m.group(0).replace('<path fill="#3E0E18"', '<path id="pupil-left" fill="#3E0E18"', 1),
        svg_content,
        count=1
    )

    # Save the modified SVG
    with open(output_svg_path, 'w') as f:
        f.write(svg_content)

    print(f"✓ Created labeled SVG: {output_svg_path}")
    print("\nLabeled elements for animation:")
    print("  Eyes:")
    print("    - #eye-right (right eye white)")
    print("    - #eye-right-white (right eye highlight/glint)")
    print("    - #pupil-right (right pupil/iris)")
    print("    - #eye-left (left eye white)")
    print("    - #eye-left-highlight (left eye highlight/glint)")
    print("    - #pupil-left (left pupil/iris)")
    print("  Eyelids:")
    print("    - #eyelid-right (right eyelid)")
    print("    - #eyelid-left (left eyelid)")
    print("  Mouth:")
    print("    - #mouth (mouth/lips)")
    print("\nYou can now animate these elements using CSS, JavaScript, or SMIL animations!")
    print("\nExample CSS animation:")
    print("""
    /* Blink animation */
    #eyelid-right, #eyelid-left {
        animation: blink 3s infinite;
    }

    @keyframes blink {
        0%, 96%, 100% { transform: scaleY(1); }
        98% { transform: scaleY(0.1); }
    }

    /* Talking animation */
    #mouth {
        animation: talk 0.5s infinite;
    }

    @keyframes talk {
        0%, 100% { transform: scaleY(1); }
        50% { transform: scaleY(1.3); }
    }
    """)

if __name__ == "__main__":
    input_path = Path("assets/girl.svg")
    output_path = Path("assets/girl_labeled.svg")

    if not input_path.exists():
        print(f"Error: {input_path} not found!")
    else:
        add_facial_feature_ids(input_path, output_path)
