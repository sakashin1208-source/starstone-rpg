import bpy
import os

ENV_BLEND_DIR = "/Users/sakaiss/dev/starstone-rpg/blender/environments"
MODELS_EXPORT_DIR = "/Users/sakaiss/dev/starstone-rpg/game/assets/models"

os.makedirs(ENV_BLEND_DIR, exist_ok=True)
os.makedirs(MODELS_EXPORT_DIR, exist_ok=True)

def create_material(name, base_color, roughness=0.75, metallic=0.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = base_color
        bsdf.inputs['Roughness'].default_value = roughness
        bsdf.inputs['Metallic'].default_value = metallic
    return mat

def save_and_export(name):
    blend_file = os.path.join(ENV_BLEND_DIR, f"{name}.blend")
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
# 1. Elder's House (長老の家 - 赤屋根・煙突・小窓)
# ==========================================
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_plaster = create_material("M_PlasterWall", (0.86, 0.82, 0.74, 1.0), roughness=0.8)
mat_red_roof = create_material("M_ElderRoof", (0.75, 0.26, 0.18, 1.0), roughness=0.65)
mat_door = create_material("M_WoodDoor", (0.38, 0.22, 0.12, 1.0), roughness=0.85)
mat_chimney = create_material("M_BrickChimney", (0.58, 0.32, 0.25, 1.0), roughness=0.9)

# Main House Body
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 1.8))
body = bpy.context.active_object
body.name = "Elder_Body"
body.scale = (5.6, 4.4, 3.6)
body.data.materials.append(mat_plaster)

# Triangular Roof
bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=3.8, depth=2.4, location=(0, 0, 4.6))
roof = bpy.context.active_object
roof.name = "Elder_Roof"
roof.rotation_euler = (0, 0, 0.785398) # 45 deg
roof.scale = (1.05, 0.85, 1.0)
roof.data.materials.append(mat_red_roof)

# Door
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 2.22, 1.1))
door = bpy.context.active_object
door.name = "Elder_Door"
door.scale = (1.2, 0.1, 2.1)
door.data.materials.append(mat_door)

# Windows (Left & Right)
for x in [-1.6, 1.6]:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(x, 2.22, 2.0))
    win = bpy.context.active_object
    win.name = f"Elder_Win_{x}"
    win.scale = (0.9, 0.08, 0.9)
    win.data.materials.append(mat_door)

# Chimney
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(1.8, -1.0, 5.0))
chimney = bpy.context.active_object
chimney.name = "Elder_Chimney"
chimney.scale = (0.7, 0.7, 2.0)
chimney.data.materials.append(mat_chimney)

for o in [body, roof, door, chimney]:
    bev = o.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.04
    bev.segments = 2

save_and_export("doll_house_elder")

# ==========================================
# 2. Weapon Shop (武器屋 - 青屋根・木板・看板・庇)
# ==========================================
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_timber = create_material("M_ShopTimber", (0.50, 0.35, 0.22, 1.0), roughness=0.85)
mat_blue_roof = create_material("M_ShopRoof", (0.22, 0.38, 0.62, 1.0), roughness=0.6)
mat_sign = create_material("M_ShopSign", (0.75, 0.60, 0.35, 1.0), roughness=0.7)

# Main Body
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 1.8))
sbody = bpy.context.active_object
sbody.name = "Shop_Body"
sbody.scale = (6.0, 4.6, 3.6)
sbody.data.materials.append(mat_timber)

# Blue Roof
bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=4.0, depth=2.2, location=(0, 0, 4.5))
sroof = bpy.context.active_object
sroof.name = "Shop_Roof"
sroof.rotation_euler = (0, 0, 0.785398)
sroof.scale = (1.08, 0.88, 1.0)
sroof.data.materials.append(mat_blue_roof)

# Awning (庇)
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 2.8, 2.3))
awning = bpy.context.active_object
awning.name = "Shop_Awning"
awning.rotation_euler = (0.25, 0, 0)
awning.scale = (3.6, 1.2, 0.15)
awning.data.materials.append(mat_blue_roof)

# Signboard (木製看板)
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(2.2, 2.5, 3.0))
sign = bpy.context.active_object
sign.name = "Shop_Signboard"
sign.scale = (1.2, 0.1, 0.7)
sign.data.materials.append(mat_sign)

for o in [sbody, sroof, awning, sign]:
    bev = o.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.04
    bev.segments = 2

save_and_export("doll_house_shop")

# ==========================================
# 3. Village Inn (宿屋 - 緑屋根・広め・木造テラス)
# ==========================================
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_stone_base = create_material("M_InnStone", (0.58, 0.58, 0.55, 1.0), roughness=0.8)
mat_green_roof = create_material("M_InnRoof", (0.24, 0.44, 0.28, 1.0), roughness=0.65)
mat_balcony = create_material("M_InnWood", (0.45, 0.30, 0.18, 1.0), roughness=0.85)

# Main Body
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 2.0))
ibody = bpy.context.active_object
ibody.name = "Inn_Body"
ibody.scale = (6.4, 5.0, 4.0)
ibody.data.materials.append(mat_stone_base)

# Green Roof
bpy.ops.mesh.primitive_cone_add(vertices=4, radius1=4.4, depth=2.4, location=(0, 0, 5.0))
iroof = bpy.context.active_object
iroof.name = "Inn_Roof"
iroof.rotation_euler = (0, 0, 0.785398)
iroof.scale = (1.1, 0.9, 1.0)
iroof.data.materials.append(mat_green_roof)

# Balcony / Porch
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 2.8, 1.5))
balcony = bpy.context.active_object
balcony.name = "Inn_Balcony"
balcony.scale = (4.8, 1.2, 0.2)
balcony.data.materials.append(mat_balcony)

for o in [ibody, iroof, balcony]:
    bev = o.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.04
    bev.segments = 2

save_and_export("doll_house_inn")

print("--- All Buildings Generated Successfully! ---")
