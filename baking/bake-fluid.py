import bpy

for scene in bpy.data.scenes:
    for sobj in scene.objects:
        for modifier in sobj.modifiers:
            if modifier.type == 'FLUID_SIMULATION':
                if modifier.settings.type == 'DOMAIN':
                    print("Baking Fluid Simulation:", sobj.name)
                    override = {'scene': scene, 'active_object': sobj}
                    bpy.ops.fluid.bake(override)

bpy.ops.wm.save_mainfile()
