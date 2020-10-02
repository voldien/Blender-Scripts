import argparse
import sys

import bpy


def create_cycle_gpu_parser(arguments=None):
    """
    Creater argument options parser
    :param arguments: valid list of words.
    :return: parsed parser object.
    """

    # Search for end of command options for the parser.
    if "--" in sys.argv:
        arguments = sys.argv[sys.argv.index("--") + 1:]
    else:
        arguments = ""

    parser = argparse.ArgumentParser(description='GPU Rendering.')
    parser.add_argument('--indices', metavar='N', type=int, nargs='+',
                        help='indices for GPU assignment for performing the rendering.')
    parser.add_argument('--tile', metavar='T', type=tuple, default=(256, 256),
                        help='Override the default tile settings.')
    parser.add_argument('--verbose', metavar='V', type=bool,
                        default=True, help='Set verbose mode.')

    return parser, parser.parse_args(arguments)


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


def rendering_cycle_gpu(tile=(256, 256), indices=None, verbose=True):
    supprted_compute_api = ('CUDA', 'OPENCL')
    if verbose:
        print("Script develop for Blender 2.79 (sub 0)", bpy.app.version_string)
    if (2, 79, 0) < bpy.app.version:
        print("You're Blender version is too old!")

    # Load the tile size.
    if tile is None:
        print("Tile set to default tile size by the blender file.")
    else:
        tile_x, tile_y = tile

    #
    if (2, 79, 0) < bpy.app.version:
        cycle_pref = bpy.context.preferences.addons['cycles']
    else:
        cycle_pref = bpy.context.user_preferences.addons['cycles']

    # Get all cycle devices.
    cycle_devices = get_cycles_devices()

    # Set default if not specified.
    if indices is None:
        indices = []
        for i, type in enumerate(cycle_devices):
            for device in type:
                if device.type in supprted_compute_api:
                    indices.append(i)
    else:
        print("indices", indices)

    # Print information of all devices.
    if verbose:
        for type in cycle_devices:
            for device in type:
                print(device.name, "type", device.type)

    computeLayer = None
    deviceSelected = []
    GPUIndex = 0
    for i, type in enumerate(cycle_devices):
        for device in type:
            if device.type in supprted_compute_api:
                if i in indices:
                    device.use = True
                    computeLayer = device.type
                    deviceSelected.append(device)
                else:
                    device.use = False
                GPUIndex += 1

    #
    for device in deviceSelected:
        if device.type != computeLayer:
            raise RuntimeError("All GPU devices are not using the same compute type")

    # Assert the state of the selected gpu
    if computeLayer and len(deviceSelected) > 0:
        print("Auto Selected compute", computeLayer)
        print("Selected GPU")
        for d in deviceSelected:
            print(d.name)

        # Set GPU API.
        print(cycle_pref.preferences.compute_device_type)
        cycle_pref.preferences.compute_device_type = computeLayer

        # Set Enable GPU rendering.
        bpy.context.scene.cycles.device = 'GPU'

        # Set the tile to the most common optimal tile size.
        bpy.context.scene.render.tile_x = tile_x
        bpy.context.scene.render.tile_y = tile_y

    else:
        print("No supported GPU compute.")
        exit(1)


if __name__ == '__main__':

    # Create parser object.
    parser, args = create_cycle_gpu_parser()
    # Perform rendering.
    rendering_cycle_gpu(indices=args.indices, verbose=args.verbose)
