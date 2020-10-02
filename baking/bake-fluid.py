import bpy


screen = bpy.context.screen
data = bpy.data
area = bpy.context.area
blend_data = bpy.context.blend_data
screen = bpy.context.screen
window = bpy.context.window
object = bpy.context.object
region = bpy.context.region

for scene in bpy.data.scenes:
    for sobj in scene.objects:
        for modifier in sobj.modifiers:
            if modifier.type == 'FLUID_SIMULATION':
                if modifier.settings.type == 'DOMAIN':
                    print("Baking Fluid Simulation:", sobj.name)
                    override = {'scene': scene, 'active_object': sobj, 'screen': screen, 'area' : area, 'blend_data' : blend_data, 'window' : window, 'object':sobj, 'region':region}
                    bpy.ops.fluid.bake(override)

bpy.ops.wm.save_mainfile()
