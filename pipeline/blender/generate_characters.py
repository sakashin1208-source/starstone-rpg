import bpy
import os

CHAR_BLEND_DIR = "/Users/sakaiss/dev/starstone-rpg/blender/characters"
MODELS_EXPORT_DIR = "/Users/sakaiss/dev/starstone-rpg/game/assets/models"

os.makedirs(CHAR_BLEND_DIR, exist_ok=True)
os.makedirs(MODELS_EXPORT_DIR, exist_ok=True)

def create_material(name, base_color, roughness=0.5, metallic=0.0, transmission=0.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = base_color
        bsdf.inputs['Roughness'].default_value = roughness
        bsdf.inputs['Metallic'].default_value = metallic
        if 'Transmission Weight' in bsdf.inputs:
            bsdf.inputs['Transmission Weight'].default_value = transmission
        elif 'Transmission' in bsdf.inputs:
            bsdf.inputs['Transmission'].default_value = transmission
    return mat

def save_and_export(name):
    blend_file = os.path.join(CHAR_BLEND_DIR, f"{name}.blend")
    glb_file = os.path.join(MODELS_EXPORT_DIR, f"{name}.glb")
    
    bpy.ops.wm.save_as_mainfile(filepath=blend_file)
    bpy.ops.export_scene.gltf(
        filepath=glb_file,
        export_format='GLB',
        export_apply=True,
        export_yup=True
    )
    print(f"[GENERATED] {name} -> Blend: {blend_file}, GLB: {glb_file}")

# ==========================================
# 1. Doll Slime (ドール風フォレストスライム)
# ==========================================
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_slime = create_material("M_SlimeJelly", (0.18, 0.82, 0.42, 0.9), roughness=0.15, transmission=0.4)
mat_white = create_material("M_EyeWhite", (0.98, 0.98, 0.98, 1.0), roughness=0.2)
mat_black = create_material("M_EyeBlack", (0.08, 0.08, 0.08, 1.0), roughness=0.1)

# Body Sphere
bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3, radius=0.5, location=(0, 0, 0.35))
body = bpy.context.active_object
body.name = "Slime_Body"
body.scale = (1.0, 1.0, 0.75)
body.data.materials.append(mat_slime)

# Eyes (Left & Right)
for x in [-0.15, 0.15]:
    # White base
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.08, location=(x, 0.42, 0.4))
    eye_w = bpy.context.active_object
    eye_w.name = f"EyeWhite_{x}"
    eye_w.data.materials.append(mat_white)
    # Pupil
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.045, location=(x, 0.48, 0.41))
    pupil = bpy.context.active_object
    pupil.name = f"Pupil_{x}"
    pupil.data.materials.append(mat_black)

save_and_export("doll_slime")

# ==========================================
# 2. Doll Hero Leon (ドール調主人公レオン)
# ==========================================
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_skin = create_material("M_DollSkin", (0.92, 0.82, 0.72, 1.0), roughness=0.6) # Ceramic skin
mat_hair = create_material("M_HeroHair", (0.75, 0.45, 0.20, 1.0), roughness=0.7) # Auburn hair
mat_tunic = create_material("M_HeroTunic", (0.22, 0.38, 0.65, 1.0), roughness=0.8) # Blue cloth
mat_belt = create_material("M_HeroLeather", (0.35, 0.20, 0.12, 1.0), roughness=0.75) # Leather
mat_cape = create_material("M_HeroCape", (0.80, 0.25, 0.22, 1.0), roughness=0.85) # Red cape

# Head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.28, location=(0, 0, 1.45))
head = bpy.context.active_object
head.name = "Hero_Head"
head.data.materials.append(mat_skin)

# Hair (Cap)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.30, location=(0, -0.02, 1.50))
hair = bpy.context.active_object
hair.name = "Hero_Hair"
hair.scale = (1.02, 1.05, 0.9)
hair.data.materials.append(mat_hair)

# Torso (Tunic)
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.95))
torso = bpy.context.active_object
torso.name = "Hero_Torso"
torso.scale = (0.45, 0.30, 0.55)
torso.data.materials.append(mat_tunic)

# Belt
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.72))
belt = bpy.context.active_object
belt.name = "Hero_Belt"
belt.scale = (0.48, 0.32, 0.10)
belt.data.materials.append(mat_belt)

# Legs / Boots
for x in [-0.14, 0.14]:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(x, 0, 0.35))
    leg = bpy.context.active_object
    leg.name = f"Hero_Leg_{x}"
    leg.scale = (0.18, 0.22, 0.70)
    leg.data.materials.append(mat_belt)

# Cape (Back)
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, -0.22, 0.85))
cape = bpy.context.active_object
cape.name = "Hero_Cape"
cape.rotation_euler = (0.15, 0, 0)
cape.scale = (0.50, 0.08, 0.75)
cape.data.materials.append(mat_cape)

for o in [torso, belt, cape]:
    bev = o.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.02
    bev.segments = 2

save_and_export("doll_hero_leon")

print("--- All Characters Generated Successfully! ---")
