"""
Starstone Hero 3D - 3D Asset Validator
Usage:
    blender --background <file.blend> --python pipeline/blender/validate_asset.py
"""
import sys

try:
    import bpy
except ImportError:
    print("Error: This script must be run within Blender (bpy).")
    sys.exit(1)

def validate():
    errors = []
    for obj in bpy.data.objects:
        if obj.type == 'MESH':
            # Check unapplied scale
            if any(abs(s - 1.0) > 0.001 for s in obj.scale):
                errors.append(f"Object '{obj.name}' has unapplied scale: {tuple(obj.scale)}")
            # Check missing materials
            if not obj.data.materials:
                errors.append(f"Object '{obj.name}' has no assigned materials.")
    
    if errors:
        print("[VALIDATION FAILED]")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("[VALIDATION PASSED] All meshes valid.")

if __name__ == "__main__":
    validate()
