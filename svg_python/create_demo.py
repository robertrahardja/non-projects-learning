"""
Create an HTML demo with the SVG embedded directly to avoid CORS issues
"""

from pathlib import Path

# Read the SVG file
svg_path = Path("assets/girl_labeled.svg")
with open(svg_path, 'r') as f:
    svg_content = f.read()

# Remove XML declaration if present
svg_content = svg_content.replace('<?xml version="1.0" encoding="utf-8"?>', '').strip()

# Create the HTML with embedded SVG
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Girl SVG - Animated Facial Features</title>
    <style>
        body {{
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            font-family: Arial, sans-serif;
            background: #f0f0f0;
        }}

        h1 {{
            color: #333;
        }}

        .container {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            max-width: 600px;
        }}

        #svg-container svg {{
            max-width: 100%;
            height: auto;
        }}

        .controls {{
            margin-top: 20px;
            padding: 15px;
            background: #f9f9f9;
            border-radius: 5px;
        }}

        button {{
            margin: 5px;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            background: #5E1122;
            color: white;
            cursor: pointer;
            font-size: 14px;
        }}

        button:hover {{
            background: #7B2C3E;
        }}

        button:active {{
            background: #3E0E18;
        }}

        .animation-group {{
            margin: 10px 0;
        }}

        .animation-group label {{
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }}

        /* CSS Animations */
        .blink #eyelid-right,
        .blink #eyelid-left {{
            animation: blink 3s infinite;
            transform-origin: center;
        }}

        @keyframes blink {{
            0%, 92%, 100% {{
                transform: scaleY(1) translateY(0);
            }}
            96% {{
                transform: scaleY(0.1) translateY(-20px);
            }}
        }}

        .talk #mouth {{
            animation: talk 0.4s infinite;
            transform-origin: center;
        }}

        @keyframes talk {{
            0%, 100% {{
                transform: scaleY(1);
            }}
            50% {{
                transform: scaleY(1.4);
            }}
        }}

        .look-left #pupil-right,
        .look-left #pupil-left {{
            animation: lookLeft 2s infinite;
            transform-origin: center;
        }}

        @keyframes lookLeft {{
            0%, 100% {{
                transform: translateX(0);
            }}
            50% {{
                transform: translateX(-15px);
            }}
        }}

        .look-right #pupil-right,
        .look-right #pupil-left {{
            animation: lookRight 2s infinite;
            transform-origin: center;
        }}

        @keyframes lookRight {{
            0%, 100% {{
                transform: translateX(0);
            }}
            50% {{
                transform: translateX(15px);
            }}
        }}

        .happy #mouth {{
            transform: rotate(-5deg) scaleX(1.2);
            transform-origin: center;
            transition: all 0.3s ease;
        }}

        .wink #eyelid-left {{
            animation: wink 3s infinite;
            transform-origin: center;
        }}

        @keyframes wink {{
            0%, 85%, 100% {{
                transform: scaleY(1) translateY(0);
            }}
            90%, 95% {{
                transform: scaleY(0.1) translateY(-20px);
            }}
        }}
    </style>
</head>
<body>
    <h1>Animated Girl SVG</h1>

    <div class="container">
        <div id="svg-container">
{svg_content}
        </div>

        <div class="controls">
            <div class="animation-group">
                <label>Eye Animations:</label>
                <button onclick="toggleAnimation('blink')">Toggle Blink</button>
                <button onclick="toggleAnimation('wink')">Toggle Wink</button>
                <button onclick="toggleAnimation('look-left')">Look Left</button>
                <button onclick="toggleAnimation('look-right')">Look Right</button>
            </div>

            <div class="animation-group">
                <label>Mouth Animations:</label>
                <button onclick="toggleAnimation('talk')">Toggle Talk</button>
                <button onclick="toggleAnimation('happy')">Toggle Happy</button>
            </div>

            <div class="animation-group">
                <label>Reset:</label>
                <button onclick="resetAnimations()">Clear All Animations</button>
            </div>
        </div>

        <div style="margin-top: 20px; padding: 15px; background: #e8f4f8; border-radius: 5px;">
            <h3>Available IDs for Animation:</h3>
            <ul style="column-count: 2; font-size: 14px;">
                <li><code>#eye-right</code></li>
                <li><code>#eye-left</code></li>
                <li><code>#eye-right-white</code></li>
                <li><code>#eye-left-highlight</code></li>
                <li><code>#pupil-right</code></li>
                <li><code>#pupil-left</code></li>
                <li><code>#eyelid-right</code></li>
                <li><code>#eyelid-left</code></li>
                <li><code>#mouth</code></li>
            </ul>
        </div>
    </div>

    <script>
        function toggleAnimation(className) {{
            const container = document.getElementById('svg-container');
            if (container.classList.contains(className)) {{
                container.classList.remove(className);
            }} else {{
                container.classList.add(className);
            }}
        }}

        function resetAnimations() {{
            const container = document.getElementById('svg-container');
            container.className = '';
        }}
    </script>
</body>
</html>
'''

# Write the output file
output_path = Path("animation_demo_embedded.html")
with open(output_path, 'w') as f:
    f.write(html_content)

print(f"✓ Created: {output_path}")
print("This version has the SVG embedded directly, so it works without a web server!")
