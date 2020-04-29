import bpy

for scene in bpy.data.scenes:
    for sobj in scene.objects:
        for modifier in sobj.modifiers:
            if modifier.type == 'SMOKE':
                if modifier.smoke_type == 'DOMAIN':
                    print("Baking smoke:", sobj.name)
                    override = {'scene': scene, 'active_object': sobj,
                                'point_cache': modifier.domain_settings.point_cache}
                    bpy.ops.ptcache.free_bake(override)
                    bpy.ops.ptcache.bake(override, bake=True)
bpy.ops.wm.save_mainfile()
