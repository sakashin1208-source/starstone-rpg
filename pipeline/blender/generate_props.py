import bpy
import os

PROPS_BLEND_DIR = "/Users/sakaiss/dev/starstone-rpg/blender/props"
MODELS_EXPORT_DIR = "/Users/sakaiss/dev/starstone-rpg/game/assets/models"

os.makedirs(PROPS_BLEND_DIR, exist_ok=True)
os.makedirs(MODELS_EXPORT_DIR, exist_ok=True)

def create_material(name, base_color, roughness=0.7, metallic=0.0):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if bsdf:
        bsdf.inputs['Base Color'].default_value = base_color
        bsdf.inputs['Roughness'].default_value = roughness
        bsdf.inputs['Metallic'].default_value = metallic
    return mat

def save_and_export(name):
    blend_file = os.path.join(PROPS_BLEND_DIR, f"{name}.blend")
    glb_file = os.path.join(MODELS_EXPORT_DIR, f"{name}.glb")
    
    bpy.ops.wm.save_as_mainfile(filepath=blend_file)
    bpy.ops.export_scene.gltf(
        filepath=glb_file,
        export_format='GLB',
        export_apply=True,
        export_yup=True
    )
    print(f"[GENERATED] {name} -> Blend: {blend_file}, GLB: {glb_file}")

# 1. Diorama Tree
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_wood = create_material("M_TrunkWood", (0.42, 0.28, 0.16, 1.0), roughness=0.85)
mat_leaves = create_material("M_TreeLeaves", (0.24, 0.48, 0.26, 1.0), roughness=0.75)

bpy.ops.mesh.primitive_cylinder_add(radius=0.3, depth=1.8, location=(0, 0, 0.9))
trunk = bpy.context.active_object
trunk.name = "Trunk"
trunk.data.materials.append(mat_wood)

# Tier 1 leaves
bpy.ops.mesh.primitive_cone_add(radius1=1.4, depth=1.5, location=(0, 0, 2.2))
leaves1 = bpy.context.active_object
leaves1.name = "Leaves_Bottom"
leaves1.data.materials.append(mat_leaves)

# Tier 2 leaves
bpy.ops.mesh.primitive_cone_add(radius1=1.0, depth=1.4, location=(0, 0, 3.1))
leaves2 = bpy.context.active_object
leaves2.name = "Leaves_Top"
leaves2.data.materials.append(mat_leaves)

# Bevel modifier for rounded miniature feel
for obj in [trunk, leaves1, leaves2]:
    bev = obj.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.04
    bev.segments = 2
save_and_export("diorama_tree")

# 2. Diorama Rock
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_rock = create_material("M_RockStone", (0.48, 0.50, 0.45, 1.0), roughness=0.8)
bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=1.0, location=(0, 0, 0.5))
rock = bpy.context.active_object
rock.name = "DioramaRock"
rock.scale = (1.2, 0.9, 0.6)
bpy.ops.object.transform_apply(scale=True)
rock.data.materials.append(mat_rock)
bev = rock.modifiers.new(name="Bevel", type='BEVEL')
bev.width = 0.08
bev.segments = 2
save_and_export("diorama_rock")

# 3. Wooden Fence
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_fence = create_material("M_FenceWood", (0.52, 0.36, 0.22, 1.0), roughness=0.8)
# Post 1
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(-1.0, 0, 0.5))
p1 = bpy.context.active_object
p1.scale = (0.15, 0.15, 1.0)
# Post 2
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(1.0, 0, 0.5))
p2 = bpy.context.active_object
p2.scale = (0.15, 0.15, 1.0)
# Rail Top
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.75))
r1 = bpy.context.active_object
r1.scale = (2.1, 0.08, 0.12)
# Rail Bottom
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.35))
r2 = bpy.context.active_object
r2.scale = (2.1, 0.08, 0.12)
for o in [p1, p2, r1, r2]:
    o.data.materials.append(mat_fence)
    bev = o.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.02
    bev.segments = 2
save_and_export("wooden_fence")

# 4. Village Lantern
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_iron = create_material("M_LanternIron", (0.18, 0.16, 0.15, 1.0), roughness=0.5, metallic=0.7)
mat_glass = create_material("M_LanternGlass", (0.95, 0.88, 0.65, 1.0), roughness=0.2)

# Post
bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=2.4, location=(0, 0, 1.2))
post = bpy.context.active_object
post.data.materials.append(mat_iron)
# Lantern Cap
bpy.ops.mesh.primitive_cone_add(radius1=0.3, depth=0.2, location=(0, 0, 2.5))
cap = bpy.context.active_object
cap.data.materials.append(mat_iron)
# Lantern Body (Glass)
bpy.ops.mesh.primitive_cylinder_add(radius=0.2, depth=0.35, location=(0, 0, 2.25))
glass = bpy.context.active_object
glass.data.materials.append(mat_glass)
save_and_export("village_lantern")

# 5. Ancient Shrine
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_shrine_stone = create_material("M_ShrineStone", (0.55, 0.56, 0.52, 1.0), roughness=0.75)
# Pedestal Step 1
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.15))
s1 = bpy.context.active_object
s1.scale = (4.0, 4.0, 0.3)
# Pedestal Step 2
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.45))
s2 = bpy.context.active_object
s2.scale = (3.2, 3.2, 0.3)
# Pillar Left
bpy.ops.mesh.primitive_cylinder_add(radius=0.28, depth=2.4, location=(-1.2, 0, 1.65))
pil1 = bpy.context.active_object
# Pillar Right
bpy.ops.mesh.primitive_cylinder_add(radius=0.28, depth=2.4, location=(1.2, 0, 1.65))
pil2 = bpy.context.active_object
# Arch Top
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 2.9))
arch = bpy.context.active_object
arch.scale = (3.2, 0.7, 0.3)
for obj in [s1, s2, pil1, pil2, arch]:
    obj.data.materials.append(mat_shrine_stone)
    bev = obj.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.04
    bev.segments = 2
save_and_export("ancient_shrine")

# 6. Starstone Chest
bpy.ops.wm.read_factory_settings(use_empty=True)
mat_cwood = create_material("M_ChestWood", (0.45, 0.28, 0.14, 1.0), roughness=0.75)
mat_cgold = create_material("M_ChestBrass", (0.85, 0.72, 0.25, 1.0), roughness=0.35, metallic=0.85)

# Chest Body
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0, 0.25))
cbody = bpy.context.active_object
cbody.name = "ChestBody"
cbody.scale = (1.0, 0.65, 0.5)
cbody.data.materials.append(mat_cwood)

# Chest Lid
bpy.ops.mesh.primitive_cylinder_add(radius=0.325, depth=1.0, location=(0, 0, 0.5))
clid = bpy.context.active_object
clid.name = "ChestLid"
clid.rotation_euler = (0, 1.5708, 0)
clid.scale = (0.6, 1.0, 1.0)
clid.data.materials.append(mat_cwood)

# Brass Lock Plate
bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0, 0.33, 0.32))
clock = bpy.context.active_object
clock.name = "ChestLock"
clock.scale = (0.15, 0.04, 0.18)
clock.data.materials.append(mat_cgold)

for o in [cbody, clid, clock]:
    bev = o.modifiers.new(name="Bevel", type='BEVEL')
    bev.width = 0.02
    bev.segments = 2
save_and_export("starstone_chest")

print("--- All Props Generated Successfully! ---")
