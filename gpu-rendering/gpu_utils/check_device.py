import bpy


def check_and_print_cycles_devices():
    supported_compute_api = ('CUDA', 'OPENCL')

    # Version based.
    print("Blender version", bpy.app.version_string)

    print("All Cycle devices:")
    for type in get_cycles_devices():
        for device in type:
            print(device.name, "; type:", device.type, ";")

    print("Cycle supported GPUs:")
    for type in get_cycles_devices():
        for device in type:
            if device.type in supported_compute_api:
                print(device.name, "; type:", device.type, ";")


def get_cycles_devices():
    """
    Get the cycle device based on the app version.
    :return:
    """
    if (2, 79, 0) < bpy.app.version:
        cycle_pref = bpy.context.preferences.addons['cycles']
    else:
        cycle_pref = bpy.context.user_preferences.addons['cycles']

    return cycle_pref.preferences.get_devices()


if __name__ == '__main__':
    check_and_print_cycles_devices()
