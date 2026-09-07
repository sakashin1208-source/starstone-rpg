"""
Starstone Hero 3D - Blender to GLB Exporter
Usage:
    blender --background <file.blend> --python pipeline/blender/export_glb.py -- <output.glb>
"""
import sys
import os

try:
    import bpy
except ImportError:
    print("Error: This script must be run within Blender (bpy).")
    sys.exit(1)

def export_active_scene_to_glb(output_path):
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    bpy.ops.export_scene.gltf(
        filepath=output_path,
        export_format='GLB',
        use_selection=False,
        export_apply=True,
        export_yup=True
    )
    print(f"[SUCCESS] Exported GLB to: {output_path}")

if __name__ == "__main__":
    args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    if not args:
        print("Usage: blender --background <file.blend> --python export_glb.py -- <output_path.glb>")
        sys.exit(1)
    export_active_scene_to_glb(args[0])
