import bpy
import os

PROPS_BLEND_DIR = "/Users/sakaiss/dev/starstone-rpg/blender/props"
CHAR_BLEND_DIR = "/Users/sakaiss/dev/starstone-rpg/blender/characters"
MODELS_EXPORT_DIR = "/Users/sakaiss/dev/starstone-rpg/game/assets/models"

os.makedirs(PROPS_BLEND_DIR, exist_ok=True)
os.makedirs(CHAR_BLEND_DIR, exist_ok=True)
os.makedirs(MODELS_EXPORT_DIR, exist_ok=True)

def create_material(name, base_color, roughness=0.7, metallic=0.0, emission_color=(0,0,0,1), emission_strength=0.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = base_color
        bsdf.inputs['Roughness'].default_value = roughness
        bsdf.inputs['Metallic'].default_value = metallic
        if 'Emission Color' in bsdf.inputs:
            bsdf.inputs['Emission Color'].default_value = emission_color
            bsdf.inputs['Emission Strength'].default_value = emission_strength
    return mat

def save_and_export(name, blend_dir=PROPS_BLEND_DIR):
    blend_file = os.path.join(blend_dir, f"{name}.blend")
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
# 1. Paper Lantern (提灯ペンダントライト)
# ==========================================
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_paper = create_material("M_LanternPaper", (0.98, 0.92, 0.75, 1.0), roughness=0.6, emission_color=(1.0, 0.85, 0.5, 1.0), emission_strength=1.5)
mat_black_wire = create_material("M_LanternWire", (0.1, 0.1, 0.1, 1.0), roughness=0.5)

# Sphere body (slightly squished lantern)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.4, location=(0, 0, 0))
lantern = bpy.context.active_object
lantern.name = "PaperLantern_Body"
lantern.scale = (1.0, 1.0, 1.15)
lantern.data.materials.append(mat_paper)

# Suspension cord / ring
bpy.ops.mesh.primitive_cylinder_add(radius=0.015, depth=0.8, location=(0, 0, 0.75))
cord = bpy.context.active_object
cord.name = "Lantern_Cord"
cord.data.materials.append(mat_black_wire)

save_and_export("paper_lantern")

# ==========================================
# 2. Wooden Stool (丸スツール)
# ==========================================
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_stool = create_material("M_StoolWood", (0.46, 0.30, 0.18, 1.0), roughness=0.75)

# Round seat
bpy.ops.mesh.primitive_cylinder_add(radius=0.28, depth=0.08, location=(0, 0, 0.55))
seat = bpy.context.active_object
seat.name = "Stool_Seat"
seat.data.materials.append(mat_stool)

# 4 Legs
for i, (lx, ly) in enumerate([(-0.16, -0.16), (0.16, -0.16), (-0.16, 0.16), (0.16, 0.16)]):
    bpy.ops.mesh.primitive_cylinder_add(radius=0.035, depth=0.55, location=(lx, ly, 0.275))
    leg = bpy.context.active_object
    leg.name = f"Stool_Leg_{i}"
    leg.data.materials.append(mat_stool)

for o in [seat]:
    bev = o.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.015
    bev.segments = 2

save_and_export("wooden_stool")

# ==========================================
# 3. Workbench (木製作業机・パレット・筆立て)
# ==========================================
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_desk = create_material("M_DeskWood", (0.42, 0.26, 0.14, 1.0), roughness=0.8)
mat_ceramic = create_material("M_PotPottery", (0.85, 0.80, 0.70, 1.0), roughness=0.4)
mat_palette = create_material("M_PaletteWood", (0.65, 0.48, 0.30, 1.0), roughness=0.6)

# Table Top
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.85))
top = bpy.context.active_object
top.name = "Desk_Top"
top.scale = (2.2, 1.1, 0.1)
top.data.materials.append(mat_desk)

# 4 Thick Legs
for lx, ly in [(-0.95, -0.45), (0.95, -0.45), (-0.95, 0.45), (0.95, 0.45)]:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(lx, ly, 0.4))
    leg = bpy.context.active_object
    leg.scale = (0.12, 0.12, 0.8)
    leg.data.materials.append(mat_desk)

# Palette on Desk
bpy.ops.mesh.primitive_cylinder_add(radius=0.22, depth=0.02, location=(-0.3, 0.15, 0.91))
pal = bpy.context.active_object
pal.name = "Palette"
pal.scale = (1.2, 0.9, 1.0)
pal.data.materials.append(mat_palette)

# Brush Holder Pot
bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=0.18, location=(0.6, 0.25, 0.99))
pot = bpy.context.active_object
pot.name = "BrushPot"
pot.data.materials.append(mat_ceramic)

save_and_export("workbench")

# ==========================================
# 4. Pottery Shelf (飾り棚と陶器壺群)
# ==========================================
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_shelf = create_material("M_ShelfWood", (0.48, 0.32, 0.18, 1.0), roughness=0.8)
mat_pot_red = create_material("M_PotRed", (0.68, 0.28, 0.22, 1.0), roughness=0.35)
mat_pot_blue = create_material("M_PotBlue", (0.24, 0.38, 0.58, 1.0), roughness=0.35)
mat_pot_clay = create_material("M_PotClay", (0.75, 0.65, 0.52, 1.0), roughness=0.6)

# Back frame
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 1.4))
back = bpy.context.active_object
back.scale = (2.2, 0.08, 1.8)
back.data.materials.append(mat_shelf)

# 3 Shelves
for sz in [0.7, 1.4, 2.1]:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0.2, sz))
    plank = bpy.context.active_object
    plank.scale = (2.2, 0.38, 0.06)
    plank.data.materials.append(mat_shelf)

# Pots on shelves
colors = [mat_pot_red, mat_pot_blue, mat_pot_clay, mat_pot_blue, mat_pot_red]
for i, px in enumerate([-0.7, -0.35, 0.0, 0.35, 0.7]):
    bpy.ops.mesh.primitive_cylinder_add(radius=0.10, depth=0.22, location=(px, 0.2, 1.55))
    p = bpy.context.active_object
    p.name = f"Pot_Top_{i}"
    p.data.materials.append(colors[i % len(colors)])

for i, px in enumerate([-0.6, -0.2, 0.2, 0.6]):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.12, location=(px, 0.2, 0.85))
    p = bpy.context.active_object
    p.name = f"Pot_Mid_{i}"
    p.scale = (1.0, 1.0, 1.2)
    p.data.materials.append(colors[(i + 2) % len(colors)])

save_and_export("pottery_shelf")

# ==========================================
# 5. Cloth Basket (布ロールの入った木箱)
# ==========================================
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_cbox = create_material("M_ClothBox", (0.50, 0.35, 0.20, 1.0), roughness=0.85)
mat_roll_orange = create_material("M_RollOrange", (0.75, 0.40, 0.22, 1.0), roughness=0.8)
mat_roll_green = create_material("M_RollGreen", (0.35, 0.45, 0.30, 1.0), roughness=0.85)
mat_roll_linen = create_material("M_RollLinen", (0.88, 0.82, 0.70, 1.0), roughness=0.9)

# Wooden box crate
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.35))
box = bpy.context.active_object
box.scale = (1.0, 0.65, 0.7)
box.data.materials.append(mat_cbox)

# 4 Fabric rolls standing up
roll_mats = [mat_roll_orange, mat_roll_green, mat_roll_linen, mat_roll_orange]
for i, rx in enumerate([-0.3, -0.1, 0.1, 0.3]):
    bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=0.9, location=(rx, 0, 0.6))
    roll = bpy.context.active_object
    roll.rotation_euler = (0.1, 0, 0.05 * i)
    roll.data.materials.append(roll_mats[i])

save_and_export("cloth_basket")

# ==========================================
# 6. Carved Fox (キツネの木彫り人形)
# ==========================================
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_fox = create_material("M_FoxWood", (0.78, 0.42, 0.18, 1.0), roughness=0.65) # Warm terra-orange
mat_fox_white = create_material("M_FoxChest", (0.92, 0.88, 0.80, 1.0), roughness=0.65)

# Body
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.2))
fbody = bpy.context.active_object
fbody.scale = (0.22, 0.38, 0.26)
fbody.data.materials.append(mat_fox)

# Head
bpy.ops.mesh.primitive_cone_add(radius1=0.15, depth=0.25, location=(0, 0.22, 0.36))
fhead = bpy.context.active_object
fhead.rotation_euler = (1.5708, 0, 0)
fhead.data.materials.append(mat_fox)

# Ears
for ex in [-0.08, 0.08]:
    bpy.ops.mesh.primitive_cone_add(radius1=0.05, depth=0.12, location=(ex, 0.18, 0.50))
    ear = bpy.context.active_object
    ear.data.materials.append(mat_fox)

# Bushy Tail
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.14, location=(0, -0.26, 0.28))
ftail = bpy.context.active_object
ftail.scale = (0.8, 1.4, 0.8)
ftail.rotation_euler = (-0.4, 0, 0)
ftail.data.materials.append(mat_fox_white)

for o in [fbody, fhead, ftail]:
    bev = o.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.02
    bev.segments = 2

save_and_export("carved_fox")

# ==========================================
# 7. Craftsman Doll Emma (職人の少女エマ)
# ==========================================
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_eskin = create_material("M_EmmaSkin", (0.94, 0.85, 0.78, 1.0), roughness=0.55) # Porcelain skin
mat_ehair = create_material("M_EmmaHair", (0.45, 0.28, 0.18, 1.0), roughness=0.75) # Warm brown bun hair
mat_eapron = create_material("M_EmmaApron", (0.88, 0.84, 0.75, 1.0), roughness=0.85) # Linen apron
mat_esweater = create_material("M_EmmaSweater", (0.58, 0.52, 0.44, 1.0), roughness=0.85) # Wool sweater
mat_eskirt = create_material("M_EmmaSkirt", (0.24, 0.30, 0.40, 1.0), roughness=0.8)
mat_eboot = create_material("M_EmmaBoot", (0.35, 0.22, 0.14, 1.0), roughness=0.7)

# Head
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.26, location=(0, 0, 1.35))
ehead = bpy.context.active_object
ehead.data.materials.append(mat_eskin)

# Hair (Bun & Bangs)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.28, location=(0, -0.02, 1.40))
ehair = bpy.context.active_object
ehair.scale = (1.02, 1.06, 0.95)
ehair.data.materials.append(mat_ehair)

# Hair Bun at back
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.14, location=(0, -0.26, 1.40))
ebun = bpy.context.active_object
ebun.data.materials.append(mat_ehair)

# Torso (Sweater + Apron)
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.90))
etorso = bpy.context.active_object
etorso.scale = (0.42, 0.28, 0.52)
etorso.data.materials.append(mat_eapron)

# Skirt
bpy.ops.mesh.primitive_cone_add(radius1=0.32, depth=0.45, location=(0, 0, 0.55))
eskirt = bpy.context.active_object
eskirt.data.materials.append(mat_eskirt)

# Boots
for bx in [-0.12, 0.12]:
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(bx, 0, 0.18))
    boot = bpy.context.active_object
    boot.scale = (0.14, 0.20, 0.36)
    boot.data.materials.append(mat_eboot)

for o in [etorso, eskirt]:
    bev = o.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.02
    bev.segments = 2

save_and_export("craftsman_doll", blend_dir=CHAR_BLEND_DIR)

print("--- All Atelier Assets Generated Successfully! ---")
