"""
Create an HTML demo with properly grouped eyes for realistic blinking
"""

from pathlib import Path

# Read the grouped SVG file
svg_path = Path("assets/girl_grouped.svg")
with open(svg_path, 'r') as f:
    svg_content = f.read()

# Remove XML declaration if present
svg_content = svg_content.replace('<?xml version=\'1.0\' encoding=\'utf-8\'?>', '').strip()

# Create the HTML with embedded SVG
html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Girl SVG - Realistic Blinking Animation</title>
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

        button.active {{
            background: #3E0E18;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);
        }}

        .animation-group {{
            margin: 10px 0;
        }}

        .animation-group label {{
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }}

        /* Realistic blinking animation - animates the entire eye group */
        .blink #eye-right-complete,
        .blink #eye-left-complete {{
            animation: blink 3s infinite ease-in-out;
            transform-origin: center 400px; /* Approximate vertical center of eyes */
        }}

        @keyframes blink {{
            0%, 90%, 100% {{
                transform: scaleY(1);
            }}
            94%, 96% {{
                transform: scaleY(0.05);
            }}
        }}

        /* Wink animation - only left eye */
        .wink #eye-left-complete {{
            animation: wink 4s infinite ease-in-out;
            transform-origin: center 440px;
        }}

        @keyframes wink {{
            0%, 80%, 100% {{
                transform: scaleY(1);
            }}
            85%, 90% {{
                transform: scaleY(0.05);
            }}
        }}

        /* Sleepy/tired animation - slower, heavier blinks */
        .sleepy #eye-right-complete,
        .sleepy #eye-left-complete {{
            animation: sleepy 4s infinite ease-in-out;
            transform-origin: center 400px;
        }}

        @keyframes sleepy {{
            0%, 70%, 100% {{
                transform: scaleY(1);
            }}
            75%, 95% {{
                transform: scaleY(0.3);
            }}
        }}

        /* Surprised - eyes wide open */
        .surprised #eye-right-complete,
        .surprised #eye-left-complete {{
            animation: surprised 2s ease-out forwards;
            transform-origin: center 400px;
        }}

        @keyframes surprised {{
            0% {{
                transform: scaleY(1);
            }}
            50% {{
                transform: scaleY(1.3);
            }}
            100% {{
                transform: scaleY(1.2);
            }}
        }}

        /* Talking animation for mouth */
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

        .info-box {{
            margin-top: 20px;
            padding: 15px;
            background: #e8f4f8;
            border-radius: 5px;
            border-left: 4px solid #5E1122;
        }}

        .info-box h3 {{
            margin-top: 0;
        }}

        code {{
            background: #fff;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }}
    </style>
</head>
<body>
    <h1>Realistic Blinking Animation</h1>

    <div class="container">
        <div id="svg-container">
{svg_content}
        </div>

        <div class="controls">
            <div class="animation-group">
                <label>Eye Animations:</label>
                <button onclick="toggleAnimation('blink', this)">Blink</button>
                <button onclick="toggleAnimation('wink', this)">Wink</button>
                <button onclick="toggleAnimation('sleepy', this)">Sleepy</button>
                <button onclick="toggleAnimation('surprised', this)">Surprised</button>
            </div>

            <div class="animation-group">
                <label>Mouth Animations:</label>
                <button onclick="toggleAnimation('talk', this)">Talk</button>
            </div>

            <div class="animation-group">
                <label>Reset:</label>
                <button onclick="resetAnimations()">Clear All</button>
            </div>
        </div>

        <div class="info-box">
            <h3>How it works:</h3>
            <p>The entire eye (eyelids, whites, pupils, highlights) is now grouped together in:</p>
            <ul>
                <li><code>#eye-right-complete</code> - Complete right eye</li>
                <li><code>#eye-left-complete</code> - Complete left eye</li>
                <li><code>#mouth</code> - Mouth</li>
            </ul>
            <p>When you blink, the entire eye group scales vertically (<code>scaleY</code>) to create a realistic eyelid closing effect!</p>
        </div>
    </div>

    <script>
        let activeButton = null;

        function toggleAnimation(className, button) {{
            const container = document.getElementById('svg-container');

            // Remove all animation classes
            container.className = '';

            // Remove active state from all buttons
            document.querySelectorAll('button').forEach(btn => {{
                btn.classList.remove('active');
            }});

            // If clicking the same button, just turn it off
            if (activeButton === button) {{
                activeButton = null;
                return;
            }}

            // Apply the new animation
            container.classList.add(className);
            if (button) {{
                button.classList.add('active');
                activeButton = button;
            }}
        }}

        function resetAnimations() {{
            const container = document.getElementById('svg-container');
            container.className = '';
            document.querySelectorAll('button').forEach(btn => {{
                btn.classList.remove('active');
            }});
            activeButton = null;
        }}
    </script>
</body>
</html>
'''

# Write the output file
output_path = Path("blink_demo.html")
with open(output_path, 'w') as f:
    f.write(html_content)

print(f"✓ Created: {output_path}")
print("This demo shows realistic blinking where the ENTIRE eye closes!")
print("Open it in your browser to see the effect.")
