import bpy

for scene in bpy.data.scenes:
    for object in scene.objects:
        for modifier in object.modifiers:
            if modifier.type == 'PARTICLE_SYSTEM':
                print("Baking particles:", object.name, ":", modifier.name)
                override = {'scene': scene, 'active_object': object,
                            'point_cache': modifier.particle_system.point_cache}
                bpy.ops.ptcache.free_bake(override)
                bpy.ops.ptcache.bake(override, bake=True)

bpy.ops.wm.save_mainfile()
