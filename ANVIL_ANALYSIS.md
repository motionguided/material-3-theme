# Anvil Material 3 Theme - Analysis & Getting Started Guide

## What I Learned About Anvil.works

### Core Concepts
- **Anvil** is a full-stack web development platform where you build everything in Python
- No HTML, CSS, or JavaScript required - it's all Python
- Uses a drag-and-drop visual designer for UI
- Has built-in database (Data Tables), hosting, and deployment
- Supports client-side Python (runs in browser) and server-side Python (runs on Anvil servers)

### Key Features
1. **Component System**: Custom components can be created and shared
2. **Dependencies**: Apps can depend on other Anvil apps (like this Material 3 theme)
3. **GitHub Integration**: Full version control with Git
4. **Package System**: Code is organized into packages/modules
5. **Theme System**: CSS and styling can be packaged as themes

### Material 3 Theme
- This repo is a **theme library**, not a standalone app
- It provides Material Design 3 components for use in other Anvil apps
- Components follow Google's Material 3 design specifications
- Can be added as a dependency (ID: `4UK6WHQ6UX7AKELK`) to any Anvil app

## Repository Structure Analysis

### Directory Structure
```
_M3/
├── client_code/          # Client-side Python code
│   ├── _Components/      # All Material 3 components
│   │   ├── Button/       # Each component has its own folder
│   │   ├── Card/
│   │   ├── TextInput/
│   │   └── ...           # ~30+ components
│   ├── _utils/           # Utility functions (FloatingUI, properties)
│   ├── components/       # Public API - exports all components
│   ├── InitModule.py     # Initialization code
│   └── Layouts/          # Layout forms (NavigationDrawer, NavigationRail)
├── server_code/          # Server-side code (minimal in this theme)
├── theme/                # CSS, assets, theme configuration
│   ├── assets/          # CSS files, icons, JavaScript libraries
│   ├── parameters.yaml  # Theme parameters
│   └── templates.yaml   # Form templates
├── anvil.yaml           # Main app configuration
├── README.md
└── CONTRIBUTING.md
```

### Component Architecture

Each component follows this pattern:
1. **Folder Structure**: `_Components/ComponentName/`
   - `__init__.py` - Python class definition
   - `form_template.yaml` - HTML template and component definition

2. **Component Class**: Inherits from a template class
   - Uses `@anvil_prop` decorator for properties
   - Implements Material 3 styling via CSS classes
   - Handles events and interactions

3. **Key Technologies**:
   - **FloatingUI**: JavaScript library for positioning menus/dropdowns
   - **Material Symbols**: Google's icon font
   - **Custom CSS**: Material 3 compliant styling in `theme/assets/`

### Available Components

**Typography**: Text, Heading, Link
**Buttons**: Button, IconButton, ToggleIconButton, ButtonMenu, IconButtonMenu
**Form Inputs**: TextBox, TextArea, Checkbox, RadioButton, Switch, Slider, DropdownMenu, FileLoader
**Display**: Card, InteractiveCard, Avatar, AvatarMenu, Divider, SidesheetContent
**Feedback**: LinearProgressIndicator, CircularProgressIndicator
**Navigation**: NavigationLink, NavigationDrawerLayout, NavigationRailLayout
**Menus**: Menu, MenuItem

## The Error & Fix

### Problem
The `anvil.yaml` file had a reference to a non-existent test form:
```yaml
startup: {module: _TestForms.ButtonMenuFUI, type: form}
```

This was a leftover from development/testing. The `_TestForms` module doesn't exist in the public repository.

### Solution
I removed the `startup` line from `anvil.yaml`. Since this is a theme library (meant to be used as a dependency), it doesn't need a startup form. The `startup_form: null` setting is appropriate.

**Fixed**: The app should now load without errors in Anvil.

## How to Get Started

### 1. Understanding the Purpose
This is a **component library/theme**, not a standalone application. It's designed to:
- Be added as a dependency to other Anvil apps
- Provide Material 3 components for building UIs
- Serve as a reference implementation

### 2. Testing the Theme
To test that everything works:
1. The app should now load in Anvil without the error
2. You can browse the components in the Toolbox (left sidebar)
3. Components are organized into sections: Common, Typography, Buttons, etc.

### 3. Making It Your Own

#### Option A: Use as Dependency (Recommended)
1. Create a new Anvil app (or use existing)
2. Go to Settings → Dependencies
3. Add this app as a dependency
4. Use `m3.components` in your code

#### Option B: Customize This Repo
If you want to modify/extend the theme:

1. **Add New Components**:
   - Create folder: `client_code/_Components/YourComponent/`
   - Add `__init__.py` with component class
   - Add `form_template.yaml` with HTML template
   - Export in `client_code/components/__init__.py`
   - Add to toolbox in `anvil.yaml`

2. **Modify Existing Components**:
   - Edit files in `client_code/_Components/ComponentName/`
   - Update CSS in `theme/assets/anvil-m3/`
   - Test changes in Anvil designer

3. **Create Demo/Test Forms**:
   - Create a new Form in Anvil designer
   - Add it to a new module (e.g., `client_code/Demo/`)
   - Set it as startup form in `anvil.yaml` if you want to test

### 4. Recommended First Steps

1. **Explore Components**:
   - Open each component in the designer
   - Check their properties
   - Look at the code to understand structure

2. **Study Key Files**:
   - `client_code/_Components/Button/__init__.py` - Simple component example
   - `client_code/_Components/ButtonMenu/__init__.py` - More complex with menu
   - `client_code/_utils/properties.py` - Property system
   - `client_code/_utils/fui.py` - FloatingUI integration

3. **Create a Test Form**:
   - In Anvil, create a new Form
   - Add various M3 components
   - Test interactions and styling

4. **Read Anvil Documentation**:
   - [Anvil Docs](https://anvil.works/docs)
   - [Anvil API Reference](https://anvil.works/docs/api)
   - [Material 3 Theme Docs](https://anvil.works/docs/ui/app-themes/material-3)

## Key Code Patterns

### Component Property Definition
```python
@anvil_prop
@property
def text(self, value) -> str:
    """The text displayed on the Button"""
    # Property setter logic here
    self.menu_button.text = value
```

### Component Initialization
```python
class ButtonMenu(MenuMixin, ButtonMenuTemplate):
    def __init__(self, **properties):
        self.tag = ComponentTag()
        self._props = properties
        # Setup DOM nodes, event listeners
        self.init_components(**properties)
```

### Using FloatingUI for Menus
```python
from .._utils.fui import auto_update

# In component initialization
cleanup = auto_update(
    reference_el=self._btn_node,
    floating_el=self._menu_node,
    placement="bottom"
)
```

## Architecture Insights

1. **Package System**: Components are in `_Components/`, exported via `components/__init__.py`
2. **Template System**: Each component uses `form_template.yaml` for HTML structure
3. **CSS Organization**: Material 3 CSS is in `theme/assets/anvil-m3/` with one file per component type
4. **Designer Integration**: Components have special methods for Anvil's visual designer
5. **Property System**: Uses custom `@anvil_prop` decorator for reactive properties

## Next Steps

1. ✅ **Fixed the error** - Removed startup form reference
2. **Load in Anvil** - Should work now without errors
3. **Explore** - Browse components, understand structure
4. **Create** - Build your own components or modify existing ones
5. **Test** - Create demo forms to test components
6. **Contribute** - If you make improvements, consider contributing back!

## Resources

- **Anvil Documentation**: https://anvil.works/docs
- **Anvil Forum**: https://anvil.works/forum
- **Material 3 Specs**: https://m3.material.io/
- **GitHub Repo**: https://github.com/anvil-works/material-3-theme-2

## Notes

- This theme is still in **beta** - some components may be missing or have bugs
- The codebase is well-structured and follows Anvil best practices
- Most Anvil team members work on this, so it's a great learning resource
- Components use modern web technologies (FloatingUI, Material Symbols, CSS Grid/Flexbox)

---

**Status**: ✅ Error fixed - Ready to explore and customize!

