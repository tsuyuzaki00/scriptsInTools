from maya import cmds

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

riggings = [

]


def main_menu_item(title,grps):
    cmds.menuItem(divider=True,dividerLabel=title)
    for grp in grps:
        cmds.menuItem(label=grp[0],i=grp[3],c=grp[1]+" as ps; reload(ps); ps."+grp[2])

def sub_menu_item(title,grps):
    cmds.menuItem(subMenu=True,label=title,to=True)
    for grp in grps:
        cmds.menuItem(label=grp[0],i=grp[3],c=grp[1]+" as ps; reload(ps); ps."+grp[2])
    cmds.setParent( '..', menu=True)

def main():
    cmds.menu(l = "scriptsInTools", p ="MayaWindow", to = True)
    sub_menu_item(title="ExternalScript",grps=external_script)
    
    main_menu_item(title="Modeling",grps=modeling)

    sub_menu_item(title="CreateObjects",grps=create_object)
    sub_menu_item(title="ModelingEdit",grps=modeling_edit)

    cmds.menuItem( divider = True, dividerLabel = "Rigging")
    
    cmds.menuItem( subMenu=True, label="setCurves", to = True)
    cmds.menuItem( label="Antenna", c = "from scriptsInTools.MayaExecute import setCurves_antenna as ps; reload(ps); ps.main()" )
    cmds.menuItem( label="Arrow1", c = "from scriptsInTools.MayaExecute import setCurves_arrow1 as ps; reload(ps); ps.main()" )
    cmds.menuItem( label="Arrow2", c = "from scriptsInTools.MayaExecute import setCurves_arrow2 as ps; reload(ps); ps.main()" )
    cmds.menuItem( label="Arrow4", c = "from scriptsInTools.MayaExecute import setCurves_arrow4 as ps; reload(ps); ps.main()" )
    cmds.menuItem( label="Circle", c = "from scriptsInTools.MayaExecute import setCurves_circle as ps; reload(ps); ps.main()" )
    cmds.menuItem( label="Cube", c = "from scriptsInTools.MayaExecute import setCurves_cube as ps; reload(ps); ps.main()" )
    cmds.menuItem( label="Hexagon", c = "from scriptsInTools.MayaExecute import setCurves_hexagon as ps; reload(ps); ps.main()" )
    cmds.menuItem( label="Pyramid", c = "from scriptsInTools.MayaExecute import setCurves_pyramid as ps; reload(ps); ps.main()" )
    cmds.menuItem( label="Square", c = "from scriptsInTools.MayaExecute import setCurves_square as ps; reload(ps); ps.main()" )
    cmds.menuItem( label="Twist", c = "from scriptsInTools.MayaExecute import setCurves_twist as ps; reload(ps); ps.main()" )
    cmds.menuItem( label="VectorIK", c = "from scriptsInTools.MayaExecute import setCurves_vectorIK as ps; reload(ps); ps.main()" )
    cmds.setParent( "..", menu=True )

    cmds.menuItem( subMenu=True, label="CurveEdit", to = True)
    cmds.menuItem( label="CurveInSelects", c = "from scriptsInTools.singleRun import curveInSelect as ps; reload(ps); ps.main()")
    cmds.setParent( "..", menu=True )

    cmds.menuItem( subMenu=True, label="ColorChenge", to = True)
    cmds.menuItem( label="CtrlColorChange", c = "from scriptsInTools.singleRun import ctrlColorChenge as ps; reload(ps); ps.main()")
    cmds.menuItem( label="CtrlColorFreeChange", c = "from scriptsInTools.singleRun import ctrlColorFreeChenge as ps; reload(ps); ps.main()")
    cmds.setParent( "..", menu=True )

    cmds.menuItem( subMenu=True, label="Skin", to = True)
    cmds.menuItem( label="SkinPaintValue", i = "skinPaintValue.png", c = "from scriptsInTools.singleRun import skinPaintValue as ps; reload(ps); ps.main()" )
    cmds.setParent( "..", menu=True )

    cmds.menuItem( divider = True, dividerLabel = "Other")
    cmds.menuItem( subMenu=True, label="SelectsEdit", to = True )
    cmds.menuItem( label="JointRadiusEdit", c = "from scriptsInTools.singleRun import jointRadius as ps; reload(ps); ps.main()")
    cmds.menuItem( optionBox=True, c = "from scriptsInTools.singleRun import jointRadius as ps; reload(ps); ps.option()")
    cmds.setParent( "..", menu=True )

    cmds.menuItem( subMenu=True, label="Inquiry", to = True)
    cmds.menuItem( label="LookNodeType", c = "from scriptsInTools.singleRun import lookNodeType as ps; reload(ps); ps.main()")
    cmds.menuItem( label="LookSelectList", c = "from scriptsInTools.singleRun import lookSelectList as ps; reload(ps); ps.main()")
    cmds.menuItem( label="LookSelectKeyAttr", c = "from scriptsInTools.singleRun import lookSelectKeyAttr as ps; reload(ps); ps.main()")
    cmds.menuItem( label="LookBindJoints", c = "from scriptsInTools.singleRun import lookBindJoints as ps; reload(ps); ps.main()")
    cmds.menuItem( label="LookShapeColor", c = "from scriptsInTools.singleRun import lookShapeColor as ps; reload(ps); ps.main()")
    cmds.menuItem( label="LookMatrix", c = "from scriptsInTools.singleRun import lookMatrix as ps; reload(ps); ps.main()")
    cmds.setParent( "..", menu=True )
