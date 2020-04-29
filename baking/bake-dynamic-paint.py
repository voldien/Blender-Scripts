import bpy

for scene in bpy.data.scenes:
    for sobj in scene.objects:
        for modifier in sobj.modifiers:
            if modifier.type == 'DYNAMIC_PAINT':
                print("Baking Dynamic Paint:", sobj.name)
                if modifier.canvas_settings:
                    for canvas_surface in modifier.canvas_settings.canvas_surfaces:
                        print("Baking Dynamic Paint Canvas: " + canvas_surface.name)
                        override = {'scene': scene, 'active_object': sobj, 'point_cache': canvas_surface.point_cache}
                        bpy.ops.ptcache.free_bake(override)
                        bpy.ops.ptcache.bake(override, bake=True)

bpy.ops.wm.save_mainfile()
