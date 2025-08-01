from nicegui import ui

with ui.grid(columns=16).classes('w-full h-full gap-0'):
    with ui.column().classes('col-span-3 h-full border p-1'):
        with ui.row().classes('w-full h-full'):
            with ui.column().classes('w-full h-full border'):
                ui.label('1')
        ui.separator()
        with ui.row().classes('w-full h-full'):
            with ui.column().classes('w-full h-full border'):
                ui.label('2')
    with ui.column().classes('col-span-10 h-full border p-1'):
        ui.editor().classes('w-full')
    with ui.column().classes('col-span-3 h-full border p-1'):
        pass
        

ui.run()