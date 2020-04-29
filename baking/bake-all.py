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
            elif modifier.type == 'FLUID_SIMULATION':
                if modifier.settings.type == 'DOMAIN':
                    print("Baking Fluid Simulation:", sobj.name)
                    override = {'scene': scene, 'active_object': sobj}
                    bpy.ops.fluid.bake(override)
            elif modifier.type == 'CLOTH':
                print("Baking Cloth", sobj.name)
                override = {'scene': scene, 'active_object': object, 'point_cache': modifier.point_cache}
                bpy.ops.ptcache.free_bake(override)
                bpy.ops.ptcache.bake(override, bake=True)
            elif modifier.type == 'SOFT_BODY':
                print("Baking Softbody:", sobj.name)
                override = {'scene': scene, 'active_object': sobj, 'point_cache': modifier.point_cache}
                bpy.ops.ptcache.free_bake(override)
                bpy.ops.ptcache.bake(override, bake=True)
            elif modifier.type == 'DYNAMIC_PAINT':
                print("Baking Dynamic Paint:", sobj.name)
                if modifier.canvas_settings:
                    for canvas_surface in modifier.canvas_settings.canvas_surfaces:
                        print("Baking Dynamic Paint Canvas: " + canvas_surface.name)
                        override = {'scene': scene, 'active_object': sobj, 'point_cache': canvas_surface.point_cache}
                        bpy.ops.ptcache.free_bake(override)
                        bpy.ops.ptcache.bake(override, bake=True)
            elif modifier.type == 'PARTICLE_SYSTEM':
                print("Baking particles")
                override = {'scene': scene, 'active_object': sobj,
                            'point_cache': modifier.particle_system.point_cache}
                bpy.ops.ptcache.free_bake(override)
                bpy.ops.ptcache.bake(override, bake=True)

bpy.ops.wm.save_mainfile()
