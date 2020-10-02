#!/usr/bin/env python
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
bl_info = {
    "name": "Render Viewport Preview",
    "author": "Valdemar Lindberg",
    "version": (0, 1, 0),
    "blender": (2, 79, 0),
    "location": "Properties > Render",
    "description": "A seperate rendering configuration from the main for creating fast render preview without having "
                   "to alter the rendering settings for the final target.",
    "wiki_url": "",
    "category": "Render",
}

if "bpy" in locals():
    import importlib
else:
    pass

import bpy
from bpy.types import Operator,Panel
from bpy.types import RenderSettings
from bpy.props import (
    BoolProperty,
    CollectionProperty,
    PointerProperty,
    StringProperty,
    IntProperty
)
#
# # Configure the settings:
# bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
# bpy.context.scene.render.ffmpeg.format = 'MPEG4'
# bpy.context.scene.render.ffmpeg.codec = 'H264'
# bpy.context.scene.render.ffmpeg.constant_rate_factor = 'PERC_LOSSLESS'
# bpy.context.scene.render.use_file_extension = True
#
# # Read the optional output.
# bpy.context.scene.render.filepath = "preview"
#
# #
# bpy.ops.render.opengl(animation=True, view_context=False)
# bpy.ops.wm.quit_blender()

class RENDER_UL_camera_settings(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        # assert(isinstance(item, (bpy.types.RenderCopySettingsScene, bpy.types.RenderCopySettingsDataSetting)))
        print(active_propname)
        print(index)
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            print(item)
            if isinstance(item, bpy.types.RenderCameraData):
                layout.prop(item, "camera", text=item.camera.name, icon_value=icon, toggle=item.enabled)
                layout.prop(item, "enabled")

            #layout.prop(item.filepath, "copy", text="")
            else:  # elif isinstance(item, bpy.types.RenderCopySettingsDataScene):
                layout.prop(item, "allowed", text=item.name, toggle=item.enabled)
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            if isinstance(item, bpy.types.RenderCameraData):
                layout.label(item.name, icon_value=icon)
                layout.prop(item, "copy", text="")
            else:  # elif isinstance(item, bpy.types.RenderCopySettingsDataScene):
                layout.prop(item, "allowed", text=item.name, toggle=True)


class RenderPreviewPanel(Panel):
    bl_label = "Render Preview "
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "render"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def draw(self, context):
        layout = self.layout
        camera_sett = context.scene.render_preview_settings

        # split = layout.split(1.0)
        # split.template_list("RENDER_UL_camera_settings", "settings", camera_sett, "cameras",
        #                     camera_sett, "affected_settings_idx", rows=6)
        #
        # #		split.prop(context.scene.render_camera_set_settings, "cameras", text="Camera Set")
        # #split.prop(self.dummy_object2, "active", text="Object2")
        #
        # #
        # layout.enabled = len(camera_sett.cameras) > 0
        # layout.operator("scene.render_camera_set", text="Camera Render Set")
        # layout.enabled = True
        # col = layout.split(0.5)
        # col.operator("scene.render_camera_select", text="Add Camera")
        # col.operator("scene.render_camera_select", text="Remove Camera")
        #
        # #
        # layout.separator()
        # layout.enabled = len(camera_sett.cameras) > 0
        # layout.label("Output Settings")
        # split = layout.split(0.9)
        # if len(camera_sett.cameras) > 0:
        #     split.prop(camera_sett.cameras[camera_sett.affected_settings_idx], property="filepath", text="")
        #     bpy.ops.buttons.file_browse()
        # #bpy.ops.buttons.file_browse()
        # layout.enabled = True
        # #			split.prop
        #
        #
        # #		split.prop(camera_sett, )
        #
        # #
        # col = layout.row()
        # col.prop(camera_sett, "pattern")
        # col.prop(camera_sett, "render")

    # all_set = {sett.strid for sett in cp_sett.affected_settings if sett.copy}
    # for p in preset.presets:
    # 	label = ""
    # 	if p.elements & all_set == p.elements:
    # 		label = "Clear {}".format(p.ui_name)
    # 	else:
    # 		label = "Set {}".format(p.ui_name)
    # 	col.operator("scene.render_camera_option", text=label).presets = {p.rna_enum[0]}

    # layout.prop(cp_sett, "filter_scene")
    # if len(cp_sett.allowed_scenes):
    # 	layout.label("Camera Scenes:")
    # 	layout.template_list("RENDER_UL_camera_settings", "scenes", cp_sett, "allowed_scenes",
    # 	                     #                                 cp_sett, "allowed_scenes_idx", rows=6, type='GRID')
    # 	                     cp_sett, "allowed_scenes_idx", rows=6)  # XXX Grid is not nice currently...
    # else:
    # 	layout.label(text="No Affectable Scenes!", icon="ERROR")



# settings = scene.render.image_settings
# old_ff_settings = {}
# for attr in dir(scene.render.ffmpeg):
#     if attr not in ['__doc__', '__module__', '__slots__', 'bl_rna', 'rna_type']:
#         old_ff_settings[attr] = getattr(scene.render.ffmpeg, attr)
#
# old_format = settings.file_format
# old_quality = settings.quality
# settings.file_format = 'JPEG'
# settings.quality = 90
#
# filepath = "/tmp/Temp.jpg"
#
# print(bpy.ops.render.render())
#
# img = bpy.data.images['Render Result']
# img.save_render(filepath, scene=scene)
#
# settings.file_format = old_format
# settings.quality = old_quality
#
# for key in old_ff_settings:
#     setattr(scene.render.ffmpeg, key, old_ff_settings[key])

class RenderPreview(Operator):
    bl_idname = "scene.render_preview"
    bl_label = "Render Preview"
    bl_description = "Render Preview from a separated rendering configuration from the main rendering configuration"
    bl_options = {'REGISTER', 'UNDO'}

    old_image_settings = None

    @classmethod
    def poll(cls, context):
        return context.scene is not None

    def execute(self, context):
        override = {'animation': True, 'view_context': False}

        # Get all properties once only.
        properties = [p.identifier for p in context.scene.render.image_settings.bl_rna.properties
                      if not p.is_readonly]
        print(properties)

        print(dir(bpy.context.scene.render))
        print(dir(bpy.context.scene.render.image_settings))
        bpy.ops.render.opengl(override)
#        bpy.ops.render.opengl(animation=True, view_context=True)
        return {'FINISHED'}

    def invoke(self, context, event):
        bpy.ops.render.view_show()
        return self.execute(context)

    def cancel(self, context):
        # TOOD make sure it restore to its original state.
        pass

    # def draw(self, context):
    #     layout = self.layout
    #     col = layout.column()
    #     col.label(text="Custom Interface!")
    #
    #     row = col.row()
    #     row.prop(self, "scene.render_preview_set_settings")

class RenderCameraData(bpy.types.PropertyGroup):
    #
    camera = PointerProperty(name="camera", type=bpy.types.Object, description="")#,
    #update=scene..classes.CameraRenderQueueSet.draw)
    filepath = StringProperty(name="filepath", description="")
    enabled = BoolProperty(name="enabled", default=True, description="")
    affected_settings_idx = IntProperty()

class RenderViewportPreviewSettings(bpy.types.PropertyGroup):
    #
    #preview_render_settings = PointerProperty(type=bpy.types.FFmpegSettings, name="preview_render_settings")
    preview_image_settings = bpy.types.ImageFormatSettings()#PointerProperty(type=bpy.types.ImageFormatSettings, name="preview_image_settings")
    preview_video_setting = bpy.types.FFmpegSettings()#PointerProperty(type=bpy.types.FFmpegSettings, name="preview_video_setting")
    # TODO rename
    pattern = BoolProperty(name="pattern", description="", default=False)
    render = BoolProperty(name="render", description="", default=False)

classes = (
    RenderViewportPreviewSettings,
    RenderPreview,
    RenderPreviewPanel
)
addon_keymaps = []

def menu_func_render_preview(self, context):
    self.layout.operator("scene.render_preview", text="Render Preview", icon='RENDER_ANIMATION')

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    if bpy.app.version >= (2, 80, 0):
        bpy.types.TOPBAR_MT_render.append(menu_func_render_preview)
    else:
        bpy.types.INFO_MT_render.append(menu_func_render_preview)

    bpy.types.Scene.render_preview_settings = PointerProperty(type=RenderViewportPreviewSettings)

    bpy.types.RENDER_PT_render.append(menu_func_render_preview)

    # add keymap default entries
    kcfg = bpy.context.window_manager.keyconfigs.addon
    if kcfg:
        km = kcfg.keymaps.new(name='Screen', space_type='EMPTY')
        kmi = km.keymap_items.new("scene.render_preview", 'P', 'PRESS', shift=True, ctrl=True, alt=True)
        addon_keymaps.append((km, kmi))

def unregister():

    # remove keymap entries
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.types.TOPBAR_MT_render.remove(menu_func_render_preview)

    # unregister the class.
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
