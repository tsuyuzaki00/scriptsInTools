import maya.cmds as cmds
import json
import pprint

file_pass = 'D:/GMR/MgearGuide/mgear_guide/jic_rig/dict/addjoint.json'

def get_parent_joint(sel):
    joint_check = cmds.listRelatives(sel, p = True)
    if cmds.objectType(joint_check[0], isType = "joint"):
        if "blend_" in joint_check[0]:
            part = joint_check[0].split("_")
            append_part = part[1],part[2],part[3],part[4]
            normal_joint = "_".join(append_part)
            parent_joint = normal_joint
        else:
            parent_joint = joint_check[0]
    else:
        second_joint = cmds.listRelatives(joint_check[0], p = True)
        parent_joint = second_joint[0]
    return parent_joint

def get_space_joint(sel):
    if cmds.objectType(sel, isType = "joint"):
        space_joint = sel
    else:
        joint_check = cmds.listRelatives(sel, typ = "joint")
        space_joint = joint_check[0]
    return space_joint

def get_translate_attr(sel):
    joint_check = cmds.listRelatives(sel, p = True)
    if cmds.objectType(joint_check[0], isType = "joint"):
        trs_attr = cmds.getAttr(sel + ".translate")
    else:
        space = cmds.listRelatives(sel, p = True)
        trs_attr = cmds.getAttr(space[0] + ".translate")
    return trs_attr

def get_rotate_attr(sel):
    joint_check = cmds.listRelatives(sel, p = True)
    if cmds.objectType(joint_check[0], isType = "joint"):
        rot_attr = cmds.getAttr(sel + ".rotate")
    else:
        space = cmds.listRelatives(sel, p = True)
        rot_attr = cmds.getAttr(space[0] + ".rotate")
    return rot_attr

def get_radius_attr(sel):
    if cmds.objectType(sel, isType = "joint"):
        radius_attr = cmds.getAttr(sel + ".radius")
    else:
        joint_check = cmds.listRelatives(sel, typ = "joint")
        radius_attr = cmds.getAttr(joint_check[0] + ".radius")
    return radius_attr

def export_dict(sel):
    if cmds.objectType(sel, isType = "joint"):
        trs_list = list(get_translate_attr(sel)[0])
        rot_list = list(get_rotate_attr(sel)[0])
        export_string = "[" + '"' + get_parent_joint(sel) + '","' + get_space_joint(sel) + '",' + str(get_radius_attr(sel)) + "," + str(trs_list) + "," + str(rot_list) + "],"
        return export_string
    else :
        cmds.error("Please select joint")

def reverse_param(sel):
    trs_list = list(get_translate_attr(sel))
    rot_list = list(get_rotate_attr(sel))
    trs_list[0] = trs_list[0] * -1
    trs_list[1] = trs_list[1] * -1
    trs_list[2] = trs_list[2] * -1
    rot_list[0] = rot_list[0] * -1
    rot_list[1] = rot_list[1] * -1
    rot_list[2] = rot_list[2] * -1
    reverse_string = "[" + '"' + get_parent_joint(sel) + '","' + get_space_joint(sel) + '",' + str(get_radius_attr(sel)) + "," + str(trs_list) + "," + str(rot_list) + "]"
    return reverse_string

def write_dict(dict_name):
    sels = cmds.ls(sl = True)
    mylist = []
    for sel in sels:
        text = export_dict(sel)
        #text = reverse_param(sel)
        mylist.append(text)
    d = {dict_name : mylist}
    return d

#########################################################################

def read_json(file_pass):
    with open(file_pass, 'r') as f:
        roots = json.load(f)
        return roots

def update_dict_json(new_dict,file_pass):
    dict = read_json(file_pass)
    update_json = new_dict
    dict.update(update_json)
    with open(file_pass, 'w') as f:
        json.dump(dict, f, indent = 4, ensure_ascii =False)