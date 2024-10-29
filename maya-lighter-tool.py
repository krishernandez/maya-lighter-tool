#!/usr/bin/env python
#SETMODE 777

#----------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------ HEADER --#

"""
:author:
    Kris Hernandez

:synopsis:
    This module creates functions that affect a spotlight in a Maya scene.

:description:
    This module is focused on controlling the spotlight in a Maya scene by creating a
    Python module. It requires the user to implement a list of functions with specific
    uses and argument checks such as size, color and intensity.

:applications:
    Maya

:see_also:
    N/A
"""

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- IMPORTS --#

# Default Python Imports

import maya.cmds as cmds

# Imports That You Wrote

#----------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------- FUNCTIONS --#

def affect_light(light_name, colors=None, intensity=None, cone_angle=None):
    """
        This function updates properties of a given light node.

        :param light_name: Name of light node taking effect.
        :type: str

        :param colors: RGB color values
        :type: list

        :param intensity: Light intensity value
        :type: int, float

        :param cone_angle: Angle of the spotlight
        :type: int, float

        :return: The success of the operation. True.
        :type: bool
        """

    if not light_name:
        cmds.warning("Light node name must be given.")
        return None

    if not cmds.objExists(light_name):
        cmds.warning(f"Light node '{light_name}' does not exist in the scene.")
        return None

    if colors is not None:
        update_light_color(light_name, colors)
    if intensity is not None:
        update_light_intensity(light_name, intensity)
    if cone_angle is not None:
        update_light_cone_angle(light_name, cone_angle)

    return True

def update_light_color(light_name, colors):
    """
        This function updates the color of the light.

        :param light_name: Name of light node taking effect.
        :type: str

        :param colors: RGB color values
        :type: int, float

        :return: The success of the operation. True.
        :type: bool
        """
    if not isinstance(colors, list) or len(colors) != 3:
        cmds.warning("Color values has to be a list of three number values.")
        return None
    if not all(isinstance(value, (int, float)) for value in colors):
        cmds.warning("Each color value needs be a number.")
        return None

    if cmds.objExists(f"{light_name}.color"):
        cmds.setAttr(f"{light_name}.color", colors[0], colors[1], colors[2],
                     type="double3")
    else:
        cmds.warning(f"'{light_name}' does not have a color attribute.")
        return None

    return True

def update_light_intensity(light_name, intensity):
    """
           This function updates the intensity of the light.

           :param light_name: Name of the light node taking effect.
           :type: str

           :param intensity: Intensity of the light.
           :type: int, float

           :return: The success of the operation. True.
           :type: bool

           """
    if not isinstance(intensity, (int, float)):
        cmds.warning("Intensity needs to have a number value.")
        return None

    if cmds.objExists(f"{light_name}.intensity"):
        cmds.setAttr(f"{light_name}.intensity", intensity)
    else:
        cmds.warning(f"'{light_name}' does not have an intensity attribute.")
        return None

    return True

def update_light_cone_angle(light_name, cone_angle):
    """
           This function updates the cone angle of the light.

           :param light_name: Name of the light node taking effect.
           :type: str

           :param cone_angle: Angle of the light.
           :type: int, float

           :return: The success of the operation. True
           :type: bool
           """
    if not isinstance(cone_angle, (int, float)):
        cmds.warning("Cone angle needs to have a number value.")
        return None

    if cmds.objectType(light_name) in ['spotLight', 'spotLightShape']:
        cmds.setAttr(f"{light_name}.coneAngle", cone_angle)
    else:
        cmds.warning(f"'{light_name}' is not a spotlight.")
        return None

    return True 

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- CLASSES --#