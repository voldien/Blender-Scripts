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
    "name": "Copy Softbody Attributes",
    "author": "Valdemar Lindberg",
    "version": (0, 1, 0),
    "blender": (2, 79, 0),
    "location": "Object > Make Links... > Copy Softbody Attributes",
    "description": "A simple operator for easily copy soft-body attributes from one target to multiple other targets",
    "warning": "",
    "wiki_url": "",
    "category": "Object",
}

import bpy
from bpy.types import Operator


class CopySoftBodyAttribute(Operator):
    bl_idname = "scene.copy_softbody_attributes"
    bl_label = "Copy SoftBody Attributes"
    bl_description = ""
    bl_option = {'REGISTER', 'UNDO'}

    parent_object = None

    @classmethod
    def poll(cls, context):
        # Make sure an active object is selected.
        active_object = bpy.context.active_object
        if active_object is None:
            return False
        has_multiple_objects = len(context.selected_objects) > 1
        # The active selected must have a softbody modifier.
        return has_multiple_objects and active_object.modifiers.find('Softbody') >= 0

    def execute(self, context):
        self.parent_object = bpy.context.active_object
        active_softbody_object = self.parent_object.modifiers['Softbody'].settings

        # Get all properties once only.
        properties = [p.identifier for p in active_softbody_object.bl_rna.properties
                      if not p.is_readonly]

        # Iterate through all other object and copy from the main selected object.
        for c in context.selected_objects[:-1]:
            if c.modifiers.find('Softbody') >= 0:
                c_softbody_settings = c.modifiers['Softbody'].settings

                for k in properties:
                    target_attr_value = getattr(active_softbody_object, k)
                    setattr(c_softbody_settings, k, target_attr_value)
            print("Copied SoftBody attributes from {} -> {}".format(self.parent_object.name, c.name))

        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


classes = (
    CopySoftBodyAttribute,
)
addon_keymaps = []


def menu_func_link(self, context):
    self.layout.operator(CopySoftBodyAttribute.bl_idname, text="Copy Softbody Attributes")


menu_func_list = [menu_func_link]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_MT_make_links.append(menu_func_link)

    # add keymap default entries
    kcfg = bpy.context.window_manager.keyconfigs.addon
    if kcfg:
        km = kcfg.keymaps.new(name='User Interface', space_type='EMPTY')
        kmi = km.keymap_items.new("scene.copy_softbody_attributes", 'S', 'PRESS', ctrl=True, alt=True)
        addon_keymaps.append((km, kmi))


def unregister():
    # remove keymap entries
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    bpy.types.VIEW3D_MT_make_links.remove(menu_func_link)

    # unregister the class.
    for cls in classes:
        bpy.utils.unregister_class(cls)
