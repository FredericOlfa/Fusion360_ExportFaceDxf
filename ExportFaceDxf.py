#Author-FredThx
#Description-Export la face sélectionnée en dxf\t

import adsk.core, adsk.fusion, adsk.cam, traceback
import os

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent
        sketches = rootComp.sketches
        faces = []
        for seln in ui.activeSelections:
            if isinstance(seln.entity, adsk.fusion.BRepFace):
                faces.append(seln.entity)
        if faces:
            folderdlg = ui.createFolderDialog()
            folderdlg.title = 'Please select a folder to save dxf files:'
            res = folderdlg.showDialog()
            if res == adsk.core.DialogResults.DialogOK:
                folder = folderdlg.folder
                for face in faces:
                    dxf_sketch = sketches.add(face)
                    fullpath = os.path.join(folder, face.body.name)
                    dxf_sketch.saveAsDXF(fullpath + '.dxf')
                    dxf_sketch.deleteMe()
        else:
            ui.messageBox("No valid face selected.")
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
