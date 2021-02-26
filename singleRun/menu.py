from maya import cmds

# ("labal=string or optionbox=True","path_import=string","run_function=string","icon=string")

external_script = [
    ("ModelChecker",   "from externalScript.modelChecker.src import modelChecker","main()",""),
    ("ErrorCheckingTool","from externalScript.errorCheckingTool import ErrorCheckingTool","StartUI()",""),
    ("SkinningTool","from externalScript.skinningTool import SkinningToolsUI","startUI()",""),
]

modeling = [
    ("autoRename","from scriptsInTools.MayaExecute import getNameSplits_autoRename","main()",""),
    ("GeometryReset","from scriptsInTools.singleRun import freezeResetHisDel","main()",""),
]

create_object = [
    ("Cube","from scriptsInTools.MayaExecute import createNodes_polyCube","main()","polyCube.png"),
    ("Ball","from scriptsInTools.MayaExecute import createNodes_polyBall","main()","polySphere.png"),
    ("Cylinder","from scriptsInTools.MayaExecute import createNodes_polyCylinder","main()","polyCylinder.png"),
    ("Plean","from scriptsInTools.MayaExecute import createNodes_polyPlane","main()","polyMesh.png"),
    ("ImagePlean","from scriptsInTools.MayaExecute import createNodes_imagePlane","main()","ImagePlane.png"),
    ("Camera","from scriptsInTools.MayaExecute import createNodes_camera","main()" ,"view.png"),
    ("AmbientLight","from scriptsInTools.MayaExecute import createNodes_ambientLight","main()","ambientlight.png"),
    ("DirectionalLight","from scriptsInTools.MayaExecute import createNodes_directionalLight","main()","directionallight.png"),
    ("PointLight","from scriptsInTools.MayaExecute import createNodes_pointLight","main()","pointlight.png"),
    ("SpotLight","from scriptsInTools.MayaExecute import createNodes_spotLight","main()","spotlight.png"),
]

modeling_edit = [
    ("CornerEdge","from scriptsInTools.singleRun import cornerEdgeSelect","main()","cornerEdge.png"),
    ("Combine","from scriptsInTools.singleRun import combineMesh","main()","polyUnite.png"),
    ("Extract" ,"from scriptsInTools.singleRun import extractComponent","main()","polyChipOff.png"),
    ("HardEdge","from scriptsInTools.singleRun import hardEdge","main()","polyHardEdge.png"),
    ("SoftEdge","from scriptsInTools.singleRun import softEdge","main()","polySoftEdge.png"),
    ("CamImageOffConnect","from scriptsInTools.singleRun import camImageOffsetConnection" ,"ps.main()",""),
]

rigging = [
]

set_curves = [
    ("Antenna","from scriptsInTools.MayaExecute import setCurves_antenna","main()",""),
    ("Arrow1","from scriptsInTools.MayaExecute import setCurves_arrow1","main()",""),
    ("Arrow2","from scriptsInTools.MayaExecute import setCurves_arrow2","main()",""),
    ("Arrow4","from scriptsInTools.MayaExecute import setCurves_arrow4","main()",""),
    ("Circle","from scriptsInTools.MayaExecute import setCurves_circle","main()",""),
    ("Cube","from scriptsInTools.MayaExecute import setCurves_cube","main()",""),
    ("Hexagon","from scriptsInTools.MayaExecute import setCurves_hexagon","main()",""),
    ("Pyramid","from scriptsInTools.MayaExecute import setCurves_pyramid","main()",""),
    ("Square","from scriptsInTools.MayaExecute import setCurves_square","main()",""),
    ("Twist","from scriptsInTools.MayaExecute import setCurves_twist","main()",""),
    ("VectorIK","from scriptsInTools.MayaExecute import setCurves_vectorIK","main()",""),
]

curve_edit = [
    ("CurveInSelects","from scriptsInTools.singleRun import curveInSelect","main()",""),
]

color_chenge = [
    ("CtrlColorChange","from scriptsInTools.singleRun import ctrlColorChenge","main()",""),
    ("CtrlColorFreeChange","from scriptsInTools.singleRun import ctrlColorFreeChenge","main()",""),
]

skin = [
    ("SkinPaintValue","from scriptsInTools.singleRun import skinPaintValue","main()","skinPaintValue.png"),
]

other = [
]

selects_edit = [
    ("JointRadiusEdit","from scriptsInTools.singleRun import jointRadius","main()",""),
    (True,"from scriptsInTools.singleRun import jointRadius","option()",""),
]

inquiry = [
    ("LookNodeType","from scriptsInTools.singleRun import lookNodeType","main()",""),
    ("LookSelectList","from scriptsInTools.singleRun import lookSelectList","main()",""),
    ("LookSelectKeyAttr","from scriptsInTools.singleRun import lookSelectKeyAttr","main()",""),
    ("LookBindJoints","from scriptsInTools.singleRun import lookBindJoints","main()",""),
    ("LookShapeColor","from scriptsInTools.singleRun import lookShapeColor","main()",""),
    ("LookMatrix","from scriptsInTools.singleRun import lookMatrix","main()",""),
]

def main_menu_item(title,grps):
    cmds.menuItem(divider=True,dividerLabel=title)
    for grp in grps:
        if grp[0] == True:
            cmds.menuItem(optionBox=grp[0], c = grp[1]+" as ps; reload(ps); ps."+grp[2])
        else:
            cmds.menuItem(label=grp[0],i=grp[3],c=grp[1]+" as ps; reload(ps); ps."+grp[2])

def sub_menu_item(title,grps):
    cmds.menuItem(subMenu=True,label=title,to = True)
    for grp in grps:
        if grp[0] == True:
            cmds.menuItem(optionBox=grp[0], c = grp[1]+" as ps; reload(ps); ps."+grp[2])
        else:
            cmds.menuItem(label=grp[0],i=grp[3],c=grp[1]+" as ps; reload(ps); ps."+grp[2])        
    cmds.setParent("..",menu=True)

def main():
    cmds.menu(l = "scriptsInTools", p ="MayaWindow", to = True)
    sub_menu_item(title="ExternalScript",grps=external_script)
    main_menu_item(title="Modeling",grps=modeling)
    sub_menu_item(title="CreateObjects",grps=create_object)
    sub_menu_item(title="ModelingEdit",grps=modeling_edit)
    main_menu_item(title="Rigging",grps=rigging)
    sub_menu_item(title="SetCurves",grps=set_curves)
    sub_menu_item(title="CurveEdit",grps=curve_edit)
    sub_menu_item(title="ColorChenge",grps=color_chenge)
    sub_menu_item(title="Skin",grps=skin)
    main_menu_item(title="Other",grps=other)
    sub_menu_item(title="SelectsEdit",grps=selects_edit)
    sub_menu_item(title="Inquiry",grps=inquiry)
