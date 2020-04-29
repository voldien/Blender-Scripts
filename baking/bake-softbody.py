import bpy

for scene in bpy.data.scenes:
    for sobj in scene.objects:
        for modifier in sobj.modifiers:
            if modifier.type == 'SOFT_BODY':
                print("Baking Softbody:", sobj.name)
                override = {'scene': scene, 'active_object': sobj, 'point_cache': modifier.point_cache}
                bpy.ops.ptcache.free_bake(override)
                bpy.ops.ptcache.bake(override, bake=True)

bpy.ops.wm.save_mainfile()
