#Author-FredThx
#Description-Export la face sélectionnée en dxf\t

import adsk.core, adsk.fusion, adsk.cam, traceback
import os

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct # Active Design
        rootComp = design.rootComponent #Root component
        sketches = rootComp.sketches #Sketches collection

        #create list of selected faces
        faces = []
        for seln in ui.activeSelections:
            if isinstance(seln.entity, adsk.fusion.BRepFace):
                faces.append(seln.entity)
        if faces:
            #Ask for a path to export dxf files
            folderdlg = ui.createFolderDialog()
            folderdlg.title = 'Please select a folder to save dxf files:'
            reponse = folderdlg.showDialog()
            if reponse == adsk.core.DialogResults.DialogOK:
                folder = folderdlg.folder
                #create one sketch by face, export it in dxf and delete it
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
