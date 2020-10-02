import bpy

for scene in bpy.data.scenes:
    print(scene.rigidbody_world.solver_iterations, scene.rigidbody_world.steps_per_second)
    override = {'scene': scene, 'point_cache': scene.rigidbody_world.point_cache}
    bpy.ops.ptcache.free_bake_all()
    bpy.ops.ptcache.bake_all(override, bake=True)
bpy.ops.wm.save_mainfile()
