# Unity Game Development Course - Detailed Command Guide

## Lesson 1: Course Introduction and Overview (00:00:00)
**Topics Covered:** Course overview, what you'll learn
**No commands - introductory lesson**

---

## Lesson 2: Understanding Game Engines (00:00:52)
**Topics Covered:** Unity vs Unreal, Unity versions (Alpha, Beta, LTS, Techstream)

### Key Information:
- Unity website: unity3d.com
- Unity versions:
  - **Alpha**: Newest features, unstable, expect crashes
  - **Beta**: More stable, new features, still may crash
  - **LTS (Long-Term Support)**: Stable, supported 2-3 years, use for final game releases
  - **Techstream**: Latest stable version, 98-99% stable, what course uses
- Recommendation: Use Techstream or LTS, never Alpha/Beta for real projects

---

## Lesson 3: Installing Unity Hub and Editor (00:05:49)
**Topics Covered:** Unity Hub installation, account creation, editor installation

### Step-by-Step Commands:

1. **Download Unity Hub:**
   - Go to: `unity.com/download`
   - Click: "Download for Windows" or "Download for other versions"
   - Select your OS (Windows/Mac)
   - Click: Download button

2. **Install Unity Hub:**
   - Open downloaded installer
   - Click: Agree (license agreement)
   - Choose installation folder (use default)
   - Click: Finish
   - Allow firewall access if prompted

3. **Create Unity Account:**
   - Click: Sign up / Create account
   - Enter: Email address
   - Enter: Password (strict requirements)
   - Enter: Username
   - Enter: Full name
   - Check: Agree to terms of service
   - Complete: CAPTCHA verification
   - Confirm email via link sent to inbox
   - Click: Continue

4. **Sign into Unity Hub:**
   - Click: Sign in button
   - Allow authentication through web browser

5. **Skip Default Installation:**
   - When asked to install Unity 2021.3.16F1 (LTS)
   - Click: "Skip installation"
   - Click: "Agree and use personal license"
   - Click: "Maybe later" for light mode

6. **Install Correct Unity Version:**
   - Click: "Installs" tab (left sidebar)
   - Click: "Install Editor"
   - Select: "Official Releases" tab
   - Find: Unity 2022.2 (or newer Techstream)
   - Click: Install

7. **Select Build Modules:**
   - Leave default code editor checked
   - Check: "WebGL Build Support" (required for course)
   - Optional: Android/iOS support if needed
   - Click: Continue
   - Agree to terms
   - Click: Install
   - Wait for installation to complete

---

## Lesson 4: Creating Your First Unity Project (00:12:08)
**Topics Covered:** Project creation, template selection

### Step-by-Step Commands:

1. **Create New Project:**
   - Click: "Projects" tab (left sidebar)
   - Click: "New Project" button

2. **Select Editor Version:**
   - Check dropdown at top shows correct Unity version (2022.2+)

3. **Choose Template:**
   - Available templates explained:
     - 2D Core: Old built-in render pipeline (avoid)
     - 3D Core: Old built-in render pipeline (avoid)
     - **2D URP**: Universal Render Pipeline for 2D (SELECT THIS)
     - 3D URP: Universal Render Pipeline for 3D
     - 3D HDRP: High Definition for realistic 3D
   - Click: "2D URP"

4. **Configure Project:**
   - Project Name: Type "Alien Blasters"
   - Location: Choose/create a projects folder (e.g., C:\Projects or ~/Projects)
   - Click: "Create"
   - Wait for Unity to open project

---

## Lesson 5: Navigating the Unity Editor Interface (00:16:22)
**Topics Covered:** Editor layout, windows, basic navigation

### Editor Layout (Default):
- **Left:** Hierarchy window (lists all objects in scene)
- **Center:** Scene View (visual editor) with Game tab
- **Right:** Inspector (shows selected object properties)
- **Bottom:** Project window + Console window

### Key Commands:

1. **Reset to Default Layout:**
   - Menu: Window → Layouts → Default

2. **Open Sample Scene:**
   - Project window → Assets → Scenes
   - Double-click: "Sample Scene"
   - If prompted to save: Click "No"

3. **Hierarchy Navigation:**
   - Click arrow next to scene name to expand
   - Objects visible: Main Camera, Global Light
   - Click object to select → Inspector shows its properties

4. **Inspector Features:**
   - Click arrow next to component to collapse/expand
   - Transform: Position (X, Y, Z), Rotation, Scale
   - Camera settings: Projection (Orthographic for 2D)

5. **Multi-Select Objects:**
   - Hold Shift + click to select range
   - Hold Ctrl/Cmd + click to add to selection

6. **Important Inspector Buttons:**
   - **Lock icon** (top right): Locks inspector to current object
   - **Three dots menu**: Normal/Debug mode toggle
   - If stuck in Debug mode: Three dots → Normal

7. **Camera Background Color:**
   - Select: Main Camera
   - Find: Environment → Background Type → Solid Color
   - Click color swatch to change
   - Undo: Ctrl+Z (Cmd+Z on Mac)
   - Redo: Ctrl+Y (Cmd+Y on Mac)

---

## Lesson 6: Importing Art Assets from Kenny.nl (00:22:44)
**Topics Covered:** Downloading assets, importing into Unity

### Step-by-Step Commands:

1. **Download Art Pack:**
   - Go to: kenney.nl
   - Search for: "Platformer Pack Redux"
   - Click: Download
   - Save ZIP file

2. **Extract and Prepare Files:**
   - Open ZIP file
   - Navigate to: PNG folder
   - Inside are folders: Backgrounds, Enemies, Ground, HUD, Items, Particles, Players
   - Select ALL folders inside PNG
   - Right-click → Copy (or Ctrl+C)

3. **Create Art Folder in Unity:**
   - In Project window, go to Assets folder
   - Right-click in empty space
   - Create → Folder
   - Name: "Art"
   - Double-click to enter Art folder

4. **Import Files:**
   - Right-click Art folder → Show in Explorer/Finder
   - This opens file browser at Assets folder
   - Double-click into Art folder
   - Ctrl+V (Cmd+V) to paste
   - Return to Unity editor
   - Unity auto-imports files (progress bar appears)

5. **Verify Import:**
   - In Project window: Art folder should contain all subfolders
   - Navigate: Art → Ground → Grass to see sprites

---

## Lesson 7: Setting Up Sprites and Pixels Per Unit (00:29:36)
**Topics Covered:** Sprite settings, pixels per unit configuration

### Critical Sprite Setup:

1. **Check Sprite Resolution:**
   - Select any sprite (e.g., Art → Ground → Grass → dirt_center)
   - Look at preview (bottom right): Shows "128x128"
   - This means 128 pixels = 1 Unity unit by default

2. **Set Pixels Per Unit:**
   - With sprite selected, look at Inspector
   - Find: "Pixels Per Unit" field (default 100)
   - Change to: 128 (matches sprite resolution)
   - Click: Apply button

3. **Batch Update All Sprites:**
   - Navigate to Art folder
   - Select all subfolders: Ctrl+A
   - Or multi-select specific folders
   - In Inspector, set Pixels Per Unit: 128
   - Click: Apply
   - Repeat for each folder if needed

4. **Player Sprites (Different Size):**
   - Art → Players → 128x256 folder
   - These are 128 wide x 256 tall
   - Still use Pixels Per Unit: 128 (based on width)

---

## Lesson 8: Creating the Player and Ground Sprites (00:40:10)
**Topics Covered:** Placing sprites in scene, tiling ground

### Step-by-Step Commands:

1. **Add Ground Sprite:**
   - Navigate: Project → Art → Ground → Grass
   - Find: "grass_mid" sprite
   - Drag into Scene View
   - Position appears in scene

2. **Add Player Sprite:**
   - Navigate: Project → Art → Players → 128x256 → Blue (or your color)
   - Find: "alien_blue_front"
   - Drag into Scene View above ground

3. **Create Tiled Ground:**
   - Select ground object (grass_mid in Hierarchy)
   - Inspector → Sprite Renderer → Draw Mode
   - Change from "Simple" to "Tiled"
   - Adjust Width value (e.g., 20) to extend ground
   - Ground now tiles/repeats

4. **Fix Tiling Warning:**
   - If yellow warning appears about tiling
   - Select the sprite in Project window
   - Inspector → Mesh Type: Change to "Full Rect"
   - Click: Apply

5. **View Game:**
   - Click: Game tab (next to Scene tab)
   - Or press: Ctrl+P / Cmd+P to play
   - Press again to stop

6. **Save Scene:**
   - File → Save (Ctrl+S)
   - Or File → Save As
   - Navigate to: Assets → Scenes
   - Name: "Level One"
   - Click: Save

7. **Delete Sample Scene:**
   - Select "Sample Scene" in Project → Scenes
   - Press: Delete key
   - Confirm deletion

---

## Lesson 9: Understanding Physics and Rigidbody 2D (00:47:03)
**Topics Covered:** Physics system, Rigidbody2D component

### Step-by-Step Commands:

1. **Select Player:**
   - In Hierarchy: Click on alien sprite object
   - In Scene View: Click on player
   - Double-click to center view on player

2. **Add Rigidbody 2D:**
   - With player selected
   - Inspector → Click "Add Component"
   - Search or navigate: Physics 2D → Rigidbody 2D
   - Click to add

3. **Test Gravity:**
   - Press: Ctrl+P to play
   - Player falls down due to gravity
   - Press: Ctrl+P to stop

4. **Observe Position:**
   - While playing, watch Transform → Position → Y
   - Value decreases as player falls
   - Positive Y = up, Negative Y = down

---

## Lesson 10: Adding Colliders for Physics Interactions (00:57:07)
**Topics Covered:** Colliders, preventing fall-through

### Step-by-Step Commands:

1. **Add Player Collider:**
   - Select player object
   - Add Component → Physics 2D → Polygon Collider 2D
   - Green outline appears around sprite
   - Toggle Gizmos button to see/hide collider outline

2. **Add Ground Collider:**
   - Select ground object (grass_mid)
   - Add Component → Physics 2D → Box Collider 2D
   - Box collider is more efficient for rectangular shapes

3. **Enable Auto-Tiling for Ground Collider:**
   - Select ground object
   - Inspector → Box Collider 2D
   - Check: "Auto Tiling"
   - Collider now matches tiled width

4. **Test Collision:**
   - Press Play (Ctrl+P)
   - Player should fall and land on ground
   - Player stops when touching ground collider

5. **Freeze Player Rotation:**
   - Select player
   - Rigidbody 2D → Constraints → Freeze Rotation
   - Check: Z checkbox
   - Prevents player from tipping over

---

## Lesson 11: Introduction to Source Control with Plastic SCM (01:06:49)
**Topics Covered:** Version control concepts, why use source control

### Key Concepts:
- **Source Control Benefits:**
  - Track all code changes
  - Recover work if computer fails
  - Access project from multiple computers
  - Experiment safely (can revert changes)
  - Collaborate with others
  - Industry standard skill

- **Terminology:**
  - **Commit**: Save current state to repository
  - **Repository**: Storage for all project versions
  - **Branch**: Separate version for experiments

---

## Lesson 12: Setting Up Your First Repository (01:15:36)
**Topics Covered:** Plastic SCM setup, first commit

### Step-by-Step Commands:

1. **Open Plastic SCM:**
   - Menu: Window → Plastic SCM
   - Window appears at bottom with Project/Console

2. **Sign In:**
   - Click: "Log in" or "Sign up"
   - Choose: "Sign in with Unity ID"
   - Authenticate in browser

3. **Create Organization:**
   - Click: "Create" for new cloud organization
   - Enter name (e.g., "YourName-Courses")
   - Select region (e.g., US East)
   - Click: Create

4. **Create Workspace:**
   - Click: "Create Workspace"
   - Verify dropdown shows cloud option (not "Local")
   - Default name: "AlienBlasters@yourorg.cloud"
   - Select: "Branching, merging, push and pull"
   - Click: Create Workspace

5. **First Commit:**
   - All project files appear (400+ files)
   - Check box next to "Added" to select all
   - Enter message: "Added initial art and Level One"
   - Click: "Check-in changes"
   - If error: Click Check-in again

6. **View Commit History:**
   - Click: "Changesets" tab
   - See list of all commits with timestamps

---

## Lesson 13: Creating Your First C# Script (01:20:28)
**Topics Covered:** Creating scripts, folder organization

### Step-by-Step Commands:

1. **Create Scripts Folder:**
   - Project window → Assets folder
   - Right-click → Create → Folder
   - Name: "Scripts" (capital S)

2. **Create Player Script:**
   - Double-click Scripts folder to enter
   - Right-click → Create → C# Script
   - **IMPORTANT:** Immediately type name: "Player"
   - Press Enter
   - Do NOT click away before naming!

3. **Why Naming Matters:**
   - Class name inside script must match filename
   - If you rename later, must also change class name in code
   - Preview in Inspector shows: "public class Player"

4. **Open Script:**
   - Double-click Player script
   - Opens in Visual Studio (or configured editor)
   - Wait for solution to load

5. **Visual Studio Navigation:**
   - Left panel: Solution Explorer
   - Expand: Assembly-CSharp → Assets → Scripts
   - Double-click Player.cs to open

6. **Zoom In/Out:**
   - Hold Ctrl + mouse wheel scroll
   - Or use zoom dropdown (bottom left corner)

---

## Lesson 14: Understanding MonoBehaviour and Classes (01:31:16)
**Topics Covered:** C# basics, MonoBehaviour, Unity messages

### Code Structure Explained:

```csharp
using UnityEngine;  // Library for Unity functions

public class Player : MonoBehaviour  // Class definition
{
    // Fields (variables) go here

    void Start()  // Called once when object activates
    {

    }

    void Update()  // Called every frame
    {

    }
}
```

### Key Concepts:
- **using UnityEngine**: Imports Unity library
- **public class Player**: Defines the Player class
- **MonoBehaviour**: Base class for Unity components
- **Start()**: Runs once at beginning
- **Update()**: Runs every frame (60+ times/second)
- **void**: Method returns nothing

---

## Lesson 15: Reading Player Input for Movement (01:40:03)
**Topics Covered:** Input system, reading keyboard/controller input

### Step-by-Step Code:

1. **Delete Start Method (not needed yet):**
   - Select lines 11-15 (entire Start method)
   - Press: Delete

2. **Add Input Reading in Update:**
```csharp
void Update()
{
    var horizontal = Input.GetAxis("Horizontal");
    Debug.Log(horizontal);
}
```

3. **Test Input:**
   - Save script: Ctrl+S
   - Return to Unity
   - Press Play
   - Press A/D or Left/Right arrows
   - Check Console: Values from -1 to 1 appear
   - Controller left stick also works

4. **Understanding Input Values:**
   - Left/A key: -1 (negative)
   - Right/D key: +1 (positive)
   - No input: 0
   - Partial stick: fractional values (-0.5, 0.3, etc.)

---

## Lesson 16: Implementing Horizontal Movement (01:50:10)
**Topics Covered:** Moving player with Rigidbody2D velocity

### Step-by-Step Code:

1. **Get Rigidbody Component:**
```csharp
void Update()
{
    var horizontal = Input.GetAxis("Horizontal");

    var rb = GetComponent<Rigidbody2D>();
    var vertical = rb.linearVelocity.y;

    rb.linearVelocity = new Vector2(horizontal, vertical);
}
```

2. **Attach Script to Player:**
   - Return to Unity
   - Select Player object in Hierarchy
   - Drag Player script from Project to Inspector
   - Or: Add Component → Scripts → Player

3. **Test Movement:**
   - Press Play
   - Use A/D or arrow keys
   - Player moves left/right

4. **Add Speed Variable:**
```csharp
[SerializeField] float _horizontalVelocity = 3f;

void Update()
{
    var horizontal = Input.GetAxis("Horizontal");
    horizontal *= _horizontalVelocity;  // Multiply by speed

    var rb = GetComponent<Rigidbody2D>();
    var vertical = rb.linearVelocity.y;

    rb.linearVelocity = new Vector2(horizontal, vertical);
}
```

5. **SerializeField Explained:**
   - Makes private variable visible in Inspector
   - Can adjust value without changing code
   - Underscore prefix: naming convention for private fields

---

## Lesson 17: Adding Jump Mechanics (02:01:16)
**Topics Covered:** Jump implementation, button input

### Step-by-Step Code:

1. **Add Jump Variables:**
```csharp
[SerializeField] float _horizontalVelocity = 3f;
[SerializeField] float _jumpVelocity = 5f;
[SerializeField] float _jumpDuration = 0.5f;

float _jumpEndTime;
```

2. **Add Jump Input Check:**
```csharp
void Update()
{
    var horizontal = Input.GetAxis("Horizontal");
    horizontal *= _horizontalVelocity;

    var rb = GetComponent<Rigidbody2D>();
    var vertical = rb.linearVelocity.y;

    // Start jump when button pressed
    if (Input.GetButtonDown("Fire1"))  // Left mouse or Left Ctrl
    {
        _jumpEndTime = Time.time + _jumpDuration;
    }

    // Continue jump while button held
    if (Input.GetButton("Fire1") && Time.time < _jumpEndTime)
    {
        vertical = _jumpVelocity;
    }

    rb.linearVelocity = new Vector2(horizontal, vertical);
}
```

3. **Test Jumping:**
   - Press Play
   - Left-click or Left Ctrl to jump
   - Hold button for higher jump
   - Release for shorter jump

### Input Explained:
- **GetButtonDown("Fire1")**: True only on frame button pressed
- **GetButton("Fire1")**: True every frame button is held
- **Time.time**: Seconds since game started

---

## Lesson 18: Ground Detection with Raycasts (02:09:20)
**Topics Covered:** Raycasting, gizmos, ground detection

### Step-by-Step Code:

1. **Add Gizmo Visualization:**
```csharp
void OnDrawGizmos()
{
    var spriteRenderer = GetComponent<SpriteRenderer>();

    Vector2 origin = new Vector2(
        transform.position.x,
        transform.position.y - spriteRenderer.bounds.extents.y
    );

    Gizmos.color = Color.red;
    Gizmos.DrawLine(origin, origin + Vector2.down * 0.1f);
}
```

2. **Add Ground Check:**
```csharp
public bool IsGrounded;

void Update()
{
    // Get sprite renderer for bounds
    var spriteRenderer = GetComponent<SpriteRenderer>();

    Vector2 origin = new Vector2(
        transform.position.x,
        transform.position.y - spriteRenderer.bounds.extents.y
    );

    // Raycast downward
    var hit = Physics2D.Raycast(origin, Vector2.down, 0.1f);

    if (hit.collider)
    {
        IsGrounded = true;
    }
    else
    {
        IsGrounded = false;
    }

    // ... rest of movement code
}
```

3. **Require Ground for Jump:**
```csharp
if (Input.GetButtonDown("Fire1") && IsGrounded)
{
    _jumpEndTime = Time.time + _jumpDuration;
}
```

4. **View Gizmos:**
   - Scene View: Click Gizmos button (top right) to toggle
   - Red line appears at player's feet

---

## Lesson 19: Implementing Double Jump (02:21:50)
**Topics Covered:** Jump counter, multiple jumps

### Step-by-Step Code:

1. **Add Jump Counter:**
```csharp
[SerializeField] int _maxJumps = 2;
int _jumpsRemaining;
```

2. **Update Jump Logic:**
```csharp
void Update()
{
    // ... ground detection code ...

    // Reset jumps when grounded and not moving up
    if (IsGrounded && rb.linearVelocity.y <= 0)
    {
        _jumpsRemaining = _maxJumps;
    }

    // Start jump
    if (Input.GetButtonDown("Fire1") && _jumpsRemaining > 0)
    {
        _jumpEndTime = Time.time + _jumpDuration;
        _jumpsRemaining--;
    }

    // ... continue jump and movement code ...
}
```

3. **Test Double Jump:**
   - Press Play
   - Jump once from ground
   - Jump again in air (second jump)
   - Cannot jump third time until landing

---

## Lesson 20: Adding Jump Sprite Animation (02:31:30)
**Topics Covered:** Changing sprites based on state

### Step-by-Step Code:

1. **Add Jump Sprite Field:**
```csharp
[SerializeField] Sprite _jumpSprite;
Sprite _defaultSprite;
SpriteRenderer _spriteRenderer;
```

2. **Cache Components in Awake:**
```csharp
void Awake()
{
    _spriteRenderer = GetComponent<SpriteRenderer>();
    _defaultSprite = _spriteRenderer.sprite;
}
```

3. **Create Update Sprite Method:**
```csharp
void UpdateSprite()
{
    if (IsGrounded)
    {
        _spriteRenderer.sprite = _defaultSprite;
    }
    else
    {
        _spriteRenderer.sprite = _jumpSprite;
    }
}
```

4. **Call from Update:**
```csharp
void Update()
{
    // ... all other code ...

    UpdateSprite();
}
```

5. **Assign Jump Sprite in Unity:**
   - Select Player object
   - In Player component, find "Jump Sprite" field
   - Click circle icon → Search "jump"
   - Select: alien_blue_jump (from 128x256 folder)

---

## Lesson 21: Introduction to Unity Animation System (02:39:58)
**Topics Covered:** Animation window, Animator component

### Step-by-Step Commands:

1. **Create Animation Folder:**
   - Project → Assets → Right-click → Create → Folder
   - Name: "Animation"

2. **Open Animation Window:**
   - Menu: Window → Animation → Animation
   - Or press: Ctrl+6
   - Dock window at bottom with Project/Console

3. **Rename Player Object:**
   - Select alien sprite in Hierarchy
   - In Inspector, rename to "Player"
   - This affects animation file names

4. **Create First Animation:**
   - With Player selected, Animation window shows "Create" button
   - Click: Create
   - Navigate to Animation folder
   - Name: "Player_Walk"
   - Click: Save

---

## Lesson 22: Creating Walk Animation (02:54:31)
**Topics Covered:** Recording animation, sprite swapping

### Step-by-Step Commands:

1. **Add Walk Sprites:**
   - Project → Art → Players → 128x256 → Blue
   - Find: alien_blue_walk1, alien_blue_walk2
   - Select both (Shift+click)
   - Drag onto Animation timeline

2. **When Popup Appears:**
   - Choose: "Sprite Renderer" (not Player)
   - Animation now shows keyframes

3. **Adjust Animation Timing:**
   - Zoom timeline: Ctrl + mouse wheel
   - Drag second keyframe to 0:20 (0.2 seconds)
   - Select first keyframe, Ctrl+C
   - Click at 0:40, Ctrl+V (paste)
   - Animation now: walk1 → walk2 → walk1

4. **Preview Animation:**
   - Click Play button in Animation window
   - Character walks in loop

5. **Adjust Speed:**
   - Select all keyframes (Ctrl+A)
   - Drag end handle to scale timing
   - Faster = closer together

---

## Lesson 23: Setting Up Animator Controller (03:01:48)
**Topics Covered:** Animator Controller, states

### Step-by-Step Commands:

1. **Open Animator Window:**
   - Menu: Window → Animation → Animator
   - Dock next to Animation window

2. **View Controller:**
   - Select Player object
   - Animator window shows state machine
   - Orange "Entry" → "Player_Walk" state

3. **Understand States:**
   - Entry: Starting point
   - Any State: Transitions from any state
   - Player_Walk: Current animation state
   - Can add more states for idle, jump, etc.

---

## Lesson 24: Animation Parameters and Transitions (03:10:53)
**Topics Covered:** Parameters, transition conditions

### Step-by-Step Commands:

1. **Add Parameters:**
   - Animator window → Parameters tab (left side)
   - Click + button
   - Add Bool: "IsGrounded"
   - Add Float: "HorizontalSpeed"

2. **Create Idle Animation:**
   - Animation window → dropdown (shows "Player_Walk")
   - Click: "Create New Clip"
   - Name: "Player_Idle"
   - Add single sprite: alien_blue_front

3. **Create Transitions:**
   - Animator window
   - Right-click Player_Walk → Make Transition
   - Click on Player_Idle (arrow connects them)
   - Select the transition arrow
   - Inspector → Conditions → Add: HorizontalSpeed Less 0.1
   - Uncheck: "Has Exit Time"

4. **Create Return Transition:**
   - Right-click Player_Idle → Make Transition
   - Click on Player_Walk
   - Conditions: HorizontalSpeed Greater 0
   - Uncheck: "Has Exit Time"

---

## Lesson 25: Connecting Animation to Player State (03:18:29)
**Topics Covered:** Setting animator parameters from code

### Step-by-Step Code:

1. **Cache Animator:**
```csharp
Animator _animator;

void Awake()
{
    _spriteRenderer = GetComponent<SpriteRenderer>();
    _animator = GetComponent<Animator>();
    _defaultSprite = _spriteRenderer.sprite;
}
```

2. **Update Animator Parameters:**
```csharp
void UpdateSprite()
{
    _animator.SetBool("IsGrounded", IsGrounded);
    _animator.SetFloat("HorizontalSpeed", Mathf.Abs(_horizontal));

    // Flip sprite based on direction
    if (_horizontal > 0)
    {
        _spriteRenderer.flipX = false;
    }
    else if (_horizontal < 0)
    {
        _spriteRenderer.flipX = true;
    }
}
```

---

## Lesson 26: Adding Idle Animation (03:26:12)
**Topics Covered:** Idle state, animation blending

### Already covered in Lesson 24

---

## Lesson 27: Jump Animation Integration (03:31:10)
**Topics Covered:** Jump animation state

### Step-by-Step Commands:

1. **Create Jump Animation:**
   - Animation window → Create New Clip
   - Name: "Player_Jump"
   - Add sprite: alien_blue_jump (single frame)

2. **Add Transitions:**
   - Walk → Jump: Condition "IsGrounded" = false
   - Idle → Jump: Condition "IsGrounded" = false
   - Jump → Walk: Condition "IsGrounded" = true, HorizontalSpeed > 0
   - Jump → Idle: Condition "IsGrounded" = true, HorizontalSpeed < 0.1
   - All transitions: Uncheck "Has Exit Time"

---

## Lesson 28: Sprite Direction Based on Movement (03:39:55)
**Topics Covered:** Flipping sprites

### Code (from Lesson 25):
```csharp
// In UpdateSprite method
if (_horizontal > 0)
{
    _spriteRenderer.flipX = false;  // Face right
}
else if (_horizontal < 0)
{
    _spriteRenderer.flipX = true;   // Face left
}
// If horizontal == 0, keep last direction
```

---

---

## Lesson 29: Building Platforms and Obstacles (03:45:21)
**Topics Covered:** Duplicating objects, creating platforms

### Step-by-Step Commands:

1. **Duplicate Ground Platform:**
   - Select grass_mid object in Hierarchy
   - Press: Ctrl+D (Cmd+D on Mac)
   - Two objects now stacked

2. **Move Duplicated Platform:**
   - With duplicate selected
   - Press: W (move tool)
   - Hold Ctrl + drag green arrow up
   - Position at Y = -1

3. **Adjust Platform Width:**
   - Select platform
   - Sprite Renderer → Draw Mode → Tiled
   - Width: Change to 3 (smaller platform)

4. **Create Multiple Platforms:**
   - Duplicate again: Ctrl+D
   - Position higher: Y = 1 or 2
   - Create jumping challenge

---

## Lesson 30: Creating Tiled Sprites for Ground (03:50:24)
**Topics Covered:** Sprite tiling, draw modes

### Step-by-Step Commands:

1. **Enable Tiling:**
   - Select ground sprite
   - Inspector → Sprite Renderer
   - Draw Mode: Change "Simple" to "Tiled"

2. **Adjust Tile Width:**
   - Size → Width: Enter value (e.g., 20)
   - Ground now repeats horizontally

3. **Fix Tiling Issues:**
   - If warning appears in Console
   - Select sprite in Project window
   - Inspector → Mesh Type: "Full Rect"
   - Click: Apply

---

## Lesson 31-34: Level Design and Scenes
**Topics Covered:** Multiple scenes, doors, transitions

### Creating New Scene:
1. File → New Scene
2. Choose: Basic 2D (URP)
3. File → Save As → "Level Two"

### Adding Door Prefab:
1. Create Empty GameObject: Right-click Hierarchy → Create Empty
2. Name: "Door"
3. Add Sprite Renderer component
4. Assign door sprite
5. Add Box Collider 2D
6. Check: "Is Trigger"
7. Create script: "Door.cs"

### Door Script Code:
```csharp
using UnityEngine;
using UnityEngine.SceneManagement;

public class Door : MonoBehaviour
{
    [SerializeField] string _nextLevel;

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            SceneManager.LoadScene(_nextLevel);
        }
    }
}
```

### Add Scenes to Build:
1. File → Build Settings
2. Drag scenes into "Scenes In Build" list
3. Order matters (0 = first scene)

---

## Lesson 35-40: Collectibles and Hazards

### Creating Coins (Lesson 35-36):

1. **Create Coin Object:**
   - Drag coin sprite to Scene
   - Add Circle Collider 2D
   - Check: "Is Trigger"
   - Add script: "Coin.cs"

2. **Coin Script:**
```csharp
using UnityEngine;

public class Coin : MonoBehaviour
{
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            // Add to score here
            gameObject.SetActive(false);
        }
    }
}
```

### Adding Sound Effects (Lesson 37):

1. **Import Audio:**
   - Create folder: Assets → Audio
   - Drag .wav files into folder

2. **Add Audio Source:**
   - Select object
   - Add Component → Audio Source
   - Drag clip to AudioClip field
   - Uncheck: "Play On Awake"

3. **Play Sound in Code:**
```csharp
AudioSource _audioSource;

void Awake()
{
    _audioSource = GetComponent<AudioSource>();
}

void PlaySound()
{
    _audioSource.Play();
}
```

### Creating Spring Pads (Lesson 38-39):

1. **Spring Setup:**
   - Create sprite object
   - Add Box Collider 2D (trigger)
   - Add script: "Spring.cs"

2. **Spring Script:**
```csharp
[SerializeField] float _bounceForce = 15f;

void OnTriggerEnter2D(Collider2D other)
{
    var rb = other.GetComponent<Rigidbody2D>();
    if (rb != null)
    {
        rb.linearVelocity = new Vector2(rb.linearVelocity.x, _bounceForce);
    }
}
```

### Creating Spike Hazards (Lesson 40):

1. **Spike Setup:**
   - Add spike sprite
   - Add Polygon Collider 2D (trigger)
   - Add script: "DamagePlayer.cs"

2. **DamagePlayer Script:**
```csharp
[SerializeField] float _damage = 1f;
[SerializeField] float _knockbackForce = 5f;

void OnTriggerEnter2D(Collider2D other)
{
    if (other.CompareTag("Player"))
    {
        var player = other.GetComponent<Player>();
        player.TakeDamage(_damage, transform.position, _knockbackForce);
    }
}
```

---

## Lesson 41-44: Cinemachine Camera System

### Installing Cinemachine (Lesson 41):
1. Window → Package Manager
2. Change dropdown: "Unity Registry"
3. Search: "Cinemachine"
4. Click: Install

### Setting Up Virtual Camera (Lesson 42):

1. **Add Cinemachine Brain:**
   - Select Main Camera
   - Add Component → Cinemachine Brain

2. **Create Virtual Camera:**
   - GameObject → Cinemachine → 2D Camera
   - Or: Right-click Hierarchy → Cinemachine → 2D Camera

3. **Configure Follow:**
   - Select CinemachineCamera object
   - Tracking Target → Target: Drag Player object
   - Body: "Framing Transposer" (for 2D)
   - Aim: "Do Nothing"

### Camera Settings (Lesson 43):
- **Dead Zone:** Area where player can move without camera moving
  - Width: 0.1-0.3
  - Height: 0.1-0.2
- **Soft Zone:** Camera accelerates to follow
- **Damping:** Smoothness of camera movement (0.5-2)

### Camera Bounds (Lesson 44):
1. Create Empty GameObject: "CameraBounds"
2. Add Component: Polygon Collider 2D
3. Edit collider to match level bounds
4. On Virtual Camera:
   - Add Extension → Cinemachine Confiner 2D
   - Bounding Shape 2D: Assign CameraBounds collider

---

## Lesson 45-50: Water and Climbing Systems

### Water Implementation (Lesson 45-47):

1. **Create Water Object:**
   - Create sprite for water
   - Add Box Collider 2D
   - Check: "Is Trigger"
   - Set Layer: "Water" (create new layer)

2. **Add Buoyancy Script:**
```csharp
using UnityEngine;

public class Water : MonoBehaviour
{
    [SerializeField] float _density = 0.1f;
    [SerializeField] float _surfaceLevel;

    void Start()
    {
        _surfaceLevel = transform.position.y +
            GetComponent<Collider2D>().bounds.extents.y;
    }
}
```

3. **Modify Player for Swimming:**
```csharp
bool _isInWater;

void OnTriggerEnter2D(Collider2D other)
{
    if (other.GetComponent<Water>())
    {
        _isInWater = true;
    }
}

void OnTriggerExit2D(Collider2D other)
{
    if (other.GetComponent<Water>())
    {
        _isInWater = false;
    }
}
```

### Ladder System (Lesson 49-50):

1. **Create Ladder:**
   - Add ladder sprite
   - Add Box Collider 2D (trigger)
   - Set Layer: "Ladder"

2. **Ladder Climbing Code:**
```csharp
bool _isOnLadder;
bool _isClimbing;

void Update()
{
    if (_isOnLadder)
    {
        float vertical = Input.GetAxis("Vertical");
        if (Mathf.Abs(vertical) > 0.1f)
        {
            _isClimbing = true;
            _rb.gravityScale = 0;
            _rb.linearVelocity = new Vector2(_rb.linearVelocity.x, vertical * _climbSpeed);
        }
    }
}
```

---

## Lesson 51-55: Advanced Player Mechanics

### Ducking/Crouching (Lesson 51-52):

1. **Add Colliders:**
   - Standing Collider: Capsule Collider 2D (full height)
   - Ducking Collider: Capsule Collider 2D (half height, disabled by default)

2. **Ducking Code:**
```csharp
[SerializeField] CapsuleCollider2D _standingCollider;
[SerializeField] CapsuleCollider2D _duckingCollider;
bool _isDucking;

void Update()
{
    if (Input.GetButtonDown("Fire2")) // Right mouse or Ctrl
    {
        _isDucking = true;
        _standingCollider.enabled = false;
        _duckingCollider.enabled = true;
    }
    if (Input.GetButtonUp("Fire2"))
    {
        _isDucking = false;
        _standingCollider.enabled = true;
        _duckingCollider.enabled = false;
    }
}
```

### Surface Effects (Lesson 54-55):

1. **Tag Surfaces:**
   - Select snow ground
   - Inspector → Tag → Add Tag → "Snow"
   - Apply tag to snow objects

2. **Check Surface in Raycast:**
```csharp
bool _isOnSnow;

void CheckGround()
{
    var hit = Physics2D.Raycast(origin, Vector2.down, 0.1f, _layerMask);
    if (hit.collider)
    {
        IsGrounded = true;
        _isOnSnow = hit.collider.CompareTag("Snow");
    }
}

void ApplyMovement()
{
    float speedMultiplier = _isOnSnow ? 0.5f : 1f;  // Slower on snow
    // Apply to movement
}
```

---

## Lesson 61-68: Enemy Systems

### Basic Enemy Setup (Lesson 61-63):

1. **Create Enemy Prefab:**
   - Drag enemy sprite to scene
   - Add Rigidbody 2D
   - Add Capsule Collider 2D
   - Create script: "Enemy.cs"
   - Drag to Prefabs folder

2. **Patrol AI:**
```csharp
[SerializeField] float _speed = 2f;
[SerializeField] Transform _leftPoint;
[SerializeField] Transform _rightPoint;

Transform _target;
SpriteRenderer _spriteRenderer;

void Start()
{
    _spriteRenderer = GetComponent<SpriteRenderer>();
    _target = _rightPoint;
}

void Update()
{
    // Move toward target
    transform.position = Vector2.MoveTowards(
        transform.position,
        _target.position,
        _speed * Time.deltaTime
    );

    // Switch direction at endpoints
    if (Vector2.Distance(transform.position, _target.position) < 0.1f)
    {
        _target = (_target == _rightPoint) ? _leftPoint : _rightPoint;
        _spriteRenderer.flipX = !_spriteRenderer.flipX;
    }
}
```

### Enemy Collision (Lesson 64):
```csharp
void OnCollisionEnter2D(Collision2D collision)
{
    if (collision.gameObject.CompareTag("Player"))
    {
        var player = collision.gameObject.GetComponent<Player>();
        player.TakeDamage(1f, transform.position, 5f);
    }
}
```

### Shooting Enemy (Lesson 66-67):
```csharp
[SerializeField] GameObject _projectilePrefab;
[SerializeField] Transform _firePoint;
[SerializeField] float _fireRate = 2f;

float _nextFireTime;

void Update()
{
    if (Time.time >= _nextFireTime)
    {
        Fire();
        _nextFireTime = Time.time + _fireRate;
    }
}

void Fire()
{
    Instantiate(_projectilePrefab, _firePoint.position, Quaternion.identity);
}
```

---

## Lesson 69-76: Combat System

### Player Health (Lesson 69-70):
```csharp
[SerializeField] int _maxHealth = 3;
int _currentHealth;
bool _isInvincible;
float _invincibilityDuration = 1.5f;

void Start()
{
    _currentHealth = _maxHealth;
}

public void TakeDamage(float damage, Vector3 damageSource, float knockback)
{
    if (_isInvincible) return;

    _currentHealth--;
    StartCoroutine(InvincibilityFrames());

    // Knockback
    Vector2 knockbackDir = (transform.position - damageSource).normalized;
    _rb.linearVelocity = knockbackDir * knockback;

    if (_currentHealth <= 0)
    {
        Die();
    }
}

IEnumerator InvincibilityFrames()
{
    _isInvincible = true;
    // Flash sprite
    for (int i = 0; i < 6; i++)
    {
        _spriteRenderer.enabled = !_spriteRenderer.enabled;
        yield return new WaitForSeconds(_invincibilityDuration / 6);
    }
    _spriteRenderer.enabled = true;
    _isInvincible = false;
}
```

### Blaster Weapon (Lesson 71-73):
```csharp
// Player.cs
[SerializeField] GameObject _blasterShotPrefab;
[SerializeField] Transform _firePoint;

void Update()
{
    if (Input.GetButtonDown("Fire1"))
    {
        Shoot();
    }
}

void Shoot()
{
    var shot = Instantiate(_blasterShotPrefab, _firePoint.position, Quaternion.identity);
    shot.GetComponent<BlasterShot>().Launch(_facingDirection);
}

// BlasterShot.cs
[SerializeField] float _speed = 10f;
[SerializeField] float _lifetime = 2f;
Vector2 _direction;

public void Launch(Vector2 direction)
{
    _direction = direction;
    Destroy(gameObject, _lifetime);
}

void Update()
{
    transform.Translate(_direction * _speed * Time.deltaTime);
}

void OnCollisionEnter2D(Collision2D collision)
{
    var damageable = collision.gameObject.GetComponent<ITakeDamage>();
    if (damageable != null)
    {
        damageable.TakeDamage();
    }
    gameObject.SetActive(false);
}
```

### ITakeDamage Interface (Lesson 74):
```csharp
// ITakeDamage.cs
public interface ITakeDamage
{
    void TakeDamage();
}

// Enemy.cs - implement interface
public class Enemy : MonoBehaviour, ITakeDamage
{
    public void TakeDamage()
    {
        gameObject.SetActive(false);
    }
}
```

### Impact Explosions (Lesson 76):
```csharp
[SerializeField] GameObject _impactExplosion;

void OnCollisionEnter2D(Collision2D collision)
{
    // Spawn explosion at contact point
    var explosion = Instantiate(
        _impactExplosion,
        collision.contacts[0].point,
        Quaternion.identity
    );
    Destroy(explosion, 0.9f);  // Destroy after animation

    gameObject.SetActive(false);
}
```

---

## Lesson 77-82: Local Multiplayer

### Player Input System (Lesson 77-78):

1. **Install Input System:**
   - Window → Package Manager
   - Search: "Input System"
   - Install

2. **Create Input Actions:**
   - Right-click Project → Create → Input Actions
   - Name: "PlayerControls"
   - Double-click to open editor
   - Add Action Map: "Player"
   - Add Actions: Move, Jump, Fire

3. **Player Input Component:**
   - Select Player prefab
   - Add Component: Player Input
   - Actions: Assign PlayerControls asset
   - Default Map: Player

### Split Screen Setup (Lesson 79):

1. **Camera Per Player:**
   - Each player prefab has own Camera + Cinemachine
   - Main Camera settings:
     - Viewport Rect: X=0, Y=0, W=0.5, H=1 (left half)
   - Second camera:
     - Viewport Rect: X=0.5, Y=0, W=0.5, H=1 (right half)

### Target Group Camera (Lesson 81-82):

1. **Create Target Group:**
   - GameObject → Cinemachine → Target Group
   - Add both players to targets list
   - Weight: 1 each, Radius: 1 each

2. **Virtual Camera Settings:**
   - Tracking Target: Target Group object
   - Body: Framing Transposer
   - Adjusts zoom to keep both players in view

---

## Lesson 116-120: Object Pooling

### Pool Manager Setup:
```csharp
public class PoolManager : MonoBehaviour
{
    public static PoolManager Instance;

    [System.Serializable]
    public class Pool
    {
        public string tag;
        public GameObject prefab;
        public int size;
    }

    [SerializeField] List<Pool> _pools;
    Dictionary<string, Queue<GameObject>> _poolDictionary;

    void Awake()
    {
        Instance = this;
        _poolDictionary = new Dictionary<string, Queue<GameObject>>();

        foreach (Pool pool in _pools)
        {
            Queue<GameObject> objectPool = new Queue<GameObject>();
            for (int i = 0; i < pool.size; i++)
            {
                GameObject obj = Instantiate(pool.prefab);
                obj.SetActive(false);
                objectPool.Enqueue(obj);
            }
            _poolDictionary.Add(pool.tag, objectPool);
        }
    }

    public GameObject SpawnFromPool(string tag, Vector3 position, Quaternion rotation)
    {
        if (!_poolDictionary.ContainsKey(tag)) return null;

        GameObject obj = _poolDictionary[tag].Dequeue();
        obj.SetActive(true);
        obj.transform.position = position;
        obj.transform.rotation = rotation;

        _poolDictionary[tag].Enqueue(obj);
        return obj;
    }
}

// Usage:
// Instead of: Instantiate(bulletPrefab, position, rotation);
// Use: PoolManager.Instance.SpawnFromPool("Bullet", position, rotation);
```

---

## Lesson 121-128: Tile Maps

### Creating Tile Palette (Lesson 122-123):

1. **Open Tile Palette:**
   - Window → 2D → Tile Palette

2. **Create New Palette:**
   - Click: "Create New Palette"
   - Name: "EnvironmentPalette"
   - Save in: Assets/Tiles

3. **Add Tiles:**
   - Select sprites in Project
   - Drag onto Tile Palette
   - Creates tile assets automatically

### Painting Tiles:
- **B** - Brush (paint tiles)
- **E** - Eraser
- **G** - Fill bucket
- **I** - Eyedropper (pick tile)
- **S** - Selection tool

### Tile Map Collider (Lesson 124):
1. Select Tilemap object (under Grid)
2. Add Component: Tilemap Collider 2D
3. Optional: Add Composite Collider 2D for optimization
   - On Tilemap Collider 2D: Check "Used By Composite"
   - Add Rigidbody 2D (set Body Type: Static)

### One-Way Platforms (Lesson 128):
1. Create separate Tilemap for platforms
2. Add: Tilemap Collider 2D
3. Add: Platform Effector 2D
4. On Collider: Check "Used By Effector"

---

## Lesson 140-144: Performance Optimization

### Using Profiler (Lesson 140-141):
1. Window → Analysis → Profiler
2. Enable: Deep Profile (for detailed code analysis)
3. Press Play
4. Click on frames to analyze
5. Hierarchy view: Sort by "Time ms"
6. Look for: GC Alloc (garbage collection)

### Non-Allocating Raycast (Lesson 142):
```csharp
// AVOID (allocates memory):
RaycastHit2D[] hits = Physics2D.RaycastAll(origin, direction, distance);

// USE (pre-allocated array):
RaycastHit2D[] _results = new RaycastHit2D[10];

void Update()
{
    int hitCount = Physics2D.Raycast(
        origin,
        direction,
        new ContactFilter2D { layerMask = _layerMask },
        _results,
        distance
    );

    for (int i = 0; i < hitCount; i++)
    {
        // Process _results[i]
    }
}
```

### Caching Components (Lesson 143-144):
```csharp
// AVOID:
void Update()
{
    GetComponent<Rigidbody2D>().linearVelocity = ...;  // Called every frame!
}

// USE:
Rigidbody2D _rb;

void Awake()
{
    _rb = GetComponent<Rigidbody2D>();  // Called once
}

void Update()
{
    _rb.linearVelocity = ...;
}
```

---

# Quick Reference: Common Unity Hotkeys

| Action | Windows | Mac |
|--------|---------|-----|
| Play/Stop | Ctrl+P | Cmd+P |
| Save Scene | Ctrl+S | Cmd+S |
| Undo | Ctrl+Z | Cmd+Z |
| Redo | Ctrl+Y | Cmd+Y |
| Duplicate | Ctrl+D | Cmd+D |
| Delete | Delete | Delete |
| Move Tool | W | W |
| Rotate Tool | E | E |
| Scale Tool | R | R |
| Pan View | Middle Mouse | Middle Mouse |
| Zoom | Scroll Wheel | Scroll Wheel |
| Focus Object | F | F |

# Quick Reference: Common Code Patterns

## Get Component
```csharp
var rb = GetComponent<Rigidbody2D>();
```

## Serialize Field
```csharp
[SerializeField] float _speed = 5f;
```

## Input
```csharp
Input.GetAxis("Horizontal");     // -1 to 1
Input.GetButtonDown("Fire1");    // True on press frame
Input.GetButton("Fire1");        // True while held
```

## Physics
```csharp
Physics2D.Raycast(origin, direction, distance);
```

## Debug
```csharp
Debug.Log("Message");
```
