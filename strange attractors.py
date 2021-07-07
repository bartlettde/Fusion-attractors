#Author-Daniel Bartlett
#Description-Plots a Lorenz Attractor

import adsk.core, adsk.fusion, adsk.cam, traceback
import time, math
from . import equations as equ

handlers = []

def calc_attractor(num_steps, xs, ys, zs, attractor_selected):
    """
    Given:
        num_steps: Number of points being plotted
        dt: Scaling factor
        xs, ys, zs: Empty lists to hold values for the points to be plotted
        attractor_selected: Defines the attractor equations used
    Return:
        xs, ys, zs: The list filled with points
    """

    if attractor_selected == 'Lorenz':
        xs, ys, zs = equ.lorenz(num_steps, xs, ys, zs)

    elif attractor_selected == 'Thomas':
        xs, ys, zs = equ.thomas(num_steps, xs, ys, zs)

    elif attractor_selected == 'Aizawa':
        xs, ys, zs = equ.aizawa(num_steps, xs, ys, zs)

    elif attractor_selected == 'Dadras':
        xs, ys, zs = equ.dadras(num_steps, xs, ys, zs)

    elif attractor_selected == 'Chen':
        xs, ys, zs = equ.chen(num_steps, xs, ys, zs)

    elif attractor_selected == 'Lorenz84':
        xs, ys, zs = equ.lorenz84(num_steps, xs, ys, zs)

    elif attractor_selected == 'Rössler':
        xs, ys, zs = equ.rossler(num_steps, xs, ys, zs)

    elif attractor_selected == 'Halvorsen':
        xs, ys, zs = equ.halvorsen(num_steps, xs, ys, zs)

    elif attractor_selected == 'Rabinovich-Fabrikant':
        xs, ys, zs = equ.rf(num_steps, xs, ys, zs)       

    elif attractor_selected == 'Three-Scroll Unified Chaotic System':
        xs, ys, zs = equ.three_scroll(num_steps, xs, ys, zs) 

    elif attractor_selected == 'Sprott':
        xs, ys, zs = equ.sprott(num_steps, xs, ys, zs) 

    elif attractor_selected == 'Four-Wing':
        xs, ys, zs = equ.four_wing(num_steps, xs, ys, zs) 

    return xs, ys, zs


def calc_list(num_steps, xs, ys, zs):
    """
    Given:
        num_steps: Number of points being plotted
        xs, ys, zs: Lists of values for the points to be plotted
    Return:
        points_list: list of points in order for custom graphic line
    """
    # Create the list for 
    points_list = []

    for j in range(num_steps):
        # print(str(j) + '/' + str(num_steps))
        points_list.append(xs[j])
        points_list.append(ys[j])
        points_list.append(zs[j])
    
    return points_list

def plot_all(index, LinecgGroup, points_list, orange_color):
    """
    Given:
        index: Empty list needed for the add lines
        LinecgGroup: Custom Graphics group which lines will be added to
        points_list: List of points which will be used to create the lines
        orange_color: Colour of the line
    Return:
        attractor: Custom graphic line
    """

    coordinates = adsk.fusion.CustomGraphicsCoordinates.create(points_list)
    attractor = LinecgGroup.addLines(coordinates, index, True)
    attractor.color = orange_color
    attractor.isSelectable = False

    return attractor
    

class ButtonPressedEventHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        # setup
        app = adsk.core.Application.get()
        ui = app.userInterface
        cmd = args.command
        inputs = cmd.commandInputs

        try:

            # Set initial size of the ui window
            cmd.setDialogInitialSize(400,250)
            cmd.isOKButtonVisible = False

            colour_dropdown = inputs.addDropDownCommandInput('colour_dropdown', 'Select colour',
                                                                       adsk.core.DropDownStyles.TextListDropDownStyle);
            colour_options = colour_dropdown.listItems
            colour_options.add('Orange', True, '')
            colour_options.add('Yellow', False, '')
            colour_options.add('Green', False, '')
            colour_options.add('Blue', False, '')
            colour_options.add('Violet', False, '')
            colour_options.add('Red', False, '')

            product_dropdown = inputs.addDropDownCommandInput('attractor_dropdown', 'Select atrractor equation',
                                                                       adsk.core.DropDownStyles.TextListDropDownStyle);
            options = product_dropdown.listItems
            options.add('Lorenz', True, '')
            options.add('Thomas', False, '')
            options.add('Aizawa', False, '')
            options.add('Dadras', False, '')
            options.add('Chen', False, '')
            options.add('Lorenz84', False, '')
            options.add('Rössler', False, '')
            options.add('Halvorsen', False, '')
            options.add('Rabinovich-Fabrikant', False, '')
            #options.add('Three-Scroll Unified Chaotic System', False, '')
            options.add('Sprott', False, '')
            options.add('Four-Wing', False, '')

            # Preview button
            # Create bool value input with button style that can be clicked.
            inspect_button = inputs.addBoolValueInput('generate', '  Generate  ', True)


            # Connect up to command related events.
            onExecute = inspectDialogCloseEventHandler()
            cmd.execute.add(onExecute)
            handlers.append(onExecute)

            onExecutePreview = GenerateHandler()
            cmd.executePreview.add(onExecutePreview)
            handlers.append(onExecutePreview)

        except:
            if ui:
                ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


class GenerateHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()

        
    def notify(self, args):
        ui = None
        try:
            # Setup stuff
            app = adsk.core.Application.get()
            ui = app.userInterface
            cmd = args.firingEvent.sender
            product = app.activeProduct
            design = adsk.fusion.Design.cast(product)
            root = design.rootComponent
            eventArgs = adsk.core.CommandEventArgs.cast(args)
            inputs = eventArgs.command.commandInputs

            gen_button = inputs.itemById('generate').value

            colour_dropdown = cmd.commandInputs.itemById('colour_dropdown')
            colour_selected = str(colour_dropdown.selectedItem.name)

            attractor_dropdown = cmd.commandInputs.itemById('attractor_dropdown')
            attractor_selected = str(attractor_dropdown.selectedItem.name)


            if gen_button == True:
                # Define the custom graphic stuff
                cgGroups = design.rootComponent.customGraphicsGroups
                LinecgGroup = adsk.fusion.CustomGraphicsGroup.cast(cgGroups.add())

                colour = equ.colour_selector(colour_selected)

                index = []
                num_steps = 50000

                xs = []
                ys = []
                zs = []

                xs, ys, zs = calc_attractor(num_steps, xs, ys, zs, attractor_selected)

                points_list = calc_list(num_steps, xs, ys, zs)

                attractor = plot_all(index, LinecgGroup, points_list, colour)
                attractor.setOpacity(0.25, True)

                camera_ = app.activeViewport.camera
                camera_.isFitView = True
                app.activeViewport.camera = camera_

        except:
            if ui:
                ui.messageBox('Input Changed Class Failed:\n{}'.format(traceback.format_exc()))


class inspectDialogCloseEventHandler(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        ui = None

        try:
            pass

        except:
            if ui:
                ui.messageBox('command executed failed:\n{}'.format(traceback.format_exc()))


def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        command_definitions = ui.commandDefinitions
        addins_toolbar_panel = ui.allToolbarPanels.itemById('SolidScriptsAddinsPanel')

        button_definition = command_definitions.addButtonDefinition('lorenz_attractor',
                                                                            'Lorenz Attractor',
                                                                            'Plot a Lorenz System',
                                                                            'resources')

        button_control = addins_toolbar_panel.controls.addCommand(button_definition,
                                                                          'button_control')

        button_control.isPromotedByDefault = True
        button_control.isPromoted = True

        button_pressed = ButtonPressedEventHandler()
        button_definition.commandCreated.add(button_pressed)
        handlers.append(button_pressed)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


def stop(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        addin_panel = ui.allToolbarPanels.itemById('SolidScriptsAddinsPanel')
        control = addin_panel.controls.itemById('lorenz_attractor')
        if control:
            control.deleteMe()

        # Delete the command definition.
        _def = ui.commandDefinitions.itemById('lorenz_attractor')
        if _def:
            _def.deleteMe()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
