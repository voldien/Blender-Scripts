import bpy

for scene in bpy.data.scenes:
    for object in scene.objects:
        for modifier in object.modifiers:
            if modifier.type == 'FLUID_SIMULATION':
                if modifier.settings.type == 'DOMAIN':
                    print("Baking Fluid Simulation:", object.name)
                    override = {'scene': scene, 'active_object': object}
                    bpy.ops.fluid.bake(override)

bpy.ops.wm.save_mainfile()
