import flet as ft
from flet.core.types import TextAlign


def checkInt(e):  # Self explanatory, checks to make sure that the text field IS an int.
    if e.control.value.isdigit():
        e.control.error_text = None
    else:
        e.control.value = 10
    e.control.update()


vertical_border = ft.Container(
    width=1,  # Border width
    height=50,  # Adjust height to fit content
    bgcolor="white",  # Border color
)


def main(page: ft.Page):
    # Anything Major section that needs to start with a ft.Row is its own area. Columns are usually kept together
    # This is probably the worst coding i've done in awhile, but it does what it needs to and looks presentable.
    page.title = "Star's Star's Stars Character Creator"
    page.scroll = "adaptive"

    def navigate_to(route):
        page.go(route)

    def mainView():
        return ft.View(
            route="/main",
            controls=[
                ft.Column(
                    controls=[
                        sectionOne,
                        ft.Divider(),
                        navigationBar,
                        ft.Divider(),
                        sectionTwo,
                        ft.Divider(),
                        sectionThree,
                    ],
                ),
            ],
        )

    def inventoryView():
        return ft.View(
            route="/inventory",
            controls=[
                ft.Column(
                    controls=[
                        sectionOne,
                        ft.Divider(),
                        navigationBar,
                        ft.Divider(),
                        ft.Text("INVENTORY PAGE: TO BE COMPLETED", weight=ft.FontWeight.BOLD, size=30)
                    ],
                ),
            ],
        )

    def actionsView():
        return ft.View(
            route="/actions",
            controls=[
                ft.Column(
                    controls=[
                        sectionOne,
                        ft.Divider(),
                        navigationBar,
                        ft.Divider(),
                        ft.Text("ACTIONS PAGE: TO BE COMPLETED", weight=ft.FontWeight.BOLD, size=30)
                    ],
                ),
            ],
        )

    def classSelectionView():
        return ft.View(
            route="/class-selection",
            controls=[
                ft.Column(
                    controls=[
                        sectionOne,
                        ft.Divider(),
                        navigationBar,
                        ft.Divider(),
                        ft.Text("CLASS SELECTION PAGE: TO BE COMPLETED", weight=ft.FontWeight.BOLD, size=30)
                    ],
                ),
            ],
        )

    def featuresTalentsView():
        return ft.View(
            route="/features-talents",
            controls=[
                ft.Column(
                    controls=[
                        sectionOne,
                        ft.Divider(),
                        navigationBar,
                        ft.Divider(),
                        ft.Text("FEATURES AND TALENTS PAGE: TO BE COMPLETED", weight=ft.FontWeight.BOLD, size=30)
                    ],
                ),
            ],
        )

    def characterCreatorView():
        return ft.View(
            route="/character-creator",
            controls=[
                ft.Column(
                    controls=[
                        sectionOne,
                        ft.Divider(),
                        navigationBar,
                        ft.Divider(),
                        ft.Text("CHARACTER CREATOR PAGE: TO BE COMPLETED", weight=ft.FontWeight.BOLD, size=30)
                    ],
                ),
            ],
        )

    def route_change(route):
        route = route.data.strip()
        page.views.clear()
        if route == "/main":
            page.views.append(mainView())
        elif route == "/actions":
            page.views.append(actionsView())
        elif route == "/inventory":
            page.views.append(inventoryView())
        elif route == "/class-selection":
            page.views.append(classSelectionView())
        elif route == "/features-talents":
            page.views.append(featuresTalentsView())
        elif route == "/character-creator":
            page.views.append(characterCreatorView())
        else:
            page.views.append(mainView())
        page.update()

    def navigation_bar_change(event):
        selected_index = event.control.selected_index
        if selected_index == 0:
            navigate_to("/actions")
        elif selected_index == 1:
            navigate_to("/main")
        elif selected_index == 2:
            navigate_to("/inventory")
        elif selected_index == 3:
            navigate_to("/class-selection")
        elif selected_index == 4:
            navigate_to("/features-talents")
        elif selected_index == 5:
            navigate_to("/character-creator")

    def view_pop(view):
        page.views.pop()
        if len(page.views) == 0:
            page.window_close()

    sectionOne = ft.Column(
        controls=[
            ft.Row(
                spacing=775,
                # Trying to have it be that the Base Class is ALWAYS at the far right of the window. I could accomplish
                # something similiar by having a lot of blank texts with large widths, but I dont want to do that for
                # clutter. It's already bad enough
                controls=[
                    ft.TextField(width=200, label="Character Name"),
                    ft.TextField(width=200, label="Base Class 1"),
                ],
            ),
            ft.Row(
                spacing=775,
                controls=[
                    ft.TextField(width=200, label="Job"),
                    ft.TextField(width=200, label="Base Class 2"),
                    # Replace this later with a thing that fetches the class from another page
                ],
            ),

        ],
    )
    sectionTwo = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.Container(
                        padding=10,
                        border=ft.border.all(1, "White"),
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                            controls=[
                                ft.Text("HP", size=18),

                                ft.Row(
                                    controls=[
                                        ft.TextField(width=80, label="Current", text_size=20,
                                                     text_align=TextAlign.CENTER),
                                        ft.Text("/", size=24, weight=ft.FontWeight.BOLD),
                                        ft.TextField(width=80, label="Max", text_size=20,
                                                     text_align=TextAlign.CENTER),
                                    ],
                                ),
                            ],

                        ),

                    ),
                    ft.Container(
                        padding=10,
                        border=ft.border.all(1, "White"),
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text("ML", size=18),

                                ft.Row(
                                    controls=[
                                        ft.TextField(width=80, label="Current", text_size=20,
                                                     text_align=TextAlign.CENTER),
                                        ft.Text("/", size=24, weight=ft.FontWeight.BOLD),
                                        ft.TextField(width=80, label="Max", text_size=20,
                                                     text_align=TextAlign.CENTER),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        padding=10,
                        border=ft.border.all(1, "White"),
                        content=ft.Column(
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Text("SL", size=18),

                                ft.Row(
                                    controls=[
                                        ft.TextField(width=80, label="Current", text_size=20,
                                                     text_align=TextAlign.CENTER),
                                        ft.Text("/", size=24, weight=ft.FontWeight.BOLD),
                                        ft.TextField(width=80, label="Max", text_size=20,
                                                     text_align=TextAlign.CENTER),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            # Stupid solution but it's gonna be what im working with
                            # until i care to find out how to do a better one
                            ft.Row(
                                controls=[
                                    ft.Container(
                                        padding=10,
                                        border=ft.border.all(1, "White"),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text("AC", size=18),
                                                ft.TextField(width=80, label="AC", text_size=20),
                                            ],
                                        ),
                                    ),
                                    ft.Container(
                                        padding=10,
                                        border=ft.border.all(1, "White"),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text("Initiative", size=18),
                                                ft.TextField(width=80, label="Initiative", text_size=20),
                                            ],
                                        ),
                                    ),
                                    ft.Container(
                                        padding=10,
                                        border=ft.border.all(1, "White"),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text("Speed", size=18),
                                                ft.TextField(width=80, label="Speed", text_size=20)
                                            ],
                                        ),
                                    ),
                                    ft.Container(
                                        padding=10,
                                        border=ft.border.all(1, "White"),
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            controls=[
                                                ft.Text("Stress", size=18),
                                                ft.Row(
                                                    controls=[
                                                        ft.TextField(width=80, label="Current", text_size=20,
                                                                     text_align=TextAlign.CENTER),
                                                        ft.Text("/", size=24, weight=ft.FontWeight.BOLD),
                                                        ft.Text(value="100", size=20),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ]

            ),
        ],
    )
    sectionThree = ft.Column(
        controls=[

            ft.Row(
                controls=[
                    ft.Container(
                        padding=10,
                        border=ft.border.all(1, "White"),
                        content=ft.Column(
                            controls=[
                                ft.Text("Ability Scores", size=16),
                                ft.Row(
                                    controls=[
                                        ft.TextField(label="Str", on_change=checkInt, width=60),
                                        ft.TextField(label="Mod", disabled=True, width=60),
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.TextField(label="Dex", on_change=checkInt, width=60),
                                        ft.TextField(label="Mod", disabled=True, width=60),
                                    ],
                                ),
                                ft.Row(
                                    controls=[

                                        ft.TextField(label="Con", on_change=checkInt, width=60),
                                        ft.TextField(label="Mod", disabled=True, width=60),
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.TextField(label="Int", on_change=checkInt, width=60),
                                        ft.TextField(label="Mod", disabled=True, width=60),
                                    ],
                                ),
                                ft.Row(

                                    controls=[
                                        ft.TextField(label="Wis", on_change=checkInt, width=60),
                                        ft.TextField(label="Mod", disabled=True, width=60),
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.TextField(label="Cha", on_change=checkInt, width=60),
                                        ft.TextField(label="Mod", disabled=True, width=60),
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.TextField(label="Luck", on_change=checkInt, width=130,
                                                     text_align=TextAlign.CENTER, text_size=24),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    ft.Container(
                        padding=10,
                        border=ft.border.all(1, "White"),
                        content=ft.Column(
                            spacing=3.5,
                            controls=[
                                ft.Row(
                                    # Probably could store all this data in an array, and have it run through to deploy
                                    # all of them to save code space, but thats not worth my time right now.
                                    # I'll change it to an array when my biggest concern isnt "I need to get this done on time."
                                    # Right now, modifiers dont do anything, but they will in a later version.
                                    controls=[
                                        ft.Checkbox(label="Acrobatics (Dex)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Animal Handling (Wis)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Arcana (Int)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Athletics (Str)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Deception (Cha)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Engineering (Int)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="History (Int)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Insight (Wis)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Intimidation (Cha)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Investigation (Int)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Medicine (Wis)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Nature (Int)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Perception (Wis)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Performance (Cha)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Persuasion (Cha)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Religion (Int)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Sleight of Hand (Dex)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Stealth (Dex)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Checkbox(label="Survival (Wis)", height=20),
                                        ft.TextField(label="Mod", disabled=True, width=40, height=20)
                                    ],
                                ),
                            ],

                        ),

                    ),
                    # Note to self: Add to pdf to have it be denoted that anything in bold is expertise, or smtn similiar

                    ft.Container(
                        padding=10,
                        border=ft.border.all(1, "White"),
                        content=ft.Column(  # The goal here is have the entire right column be self automating.
                            controls=[
                                ft.Column(
                                    controls=[
                                        # Formatting is a bit weird, but works.
                                        ft.Text("Psychoses", weight=ft.FontWeight.BOLD, size=16),
                                        ft.TextField(width=300),
                                        ft.Text("Damage Resistances", weight=ft.FontWeight.BOLD, size=16),
                                        ft.TextField(width=300),
                                        ft.Text("Damage Protections", weight=ft.FontWeight.BOLD, size=16),
                                        ft.TextField(width=300),
                                        # Damage Immunity isnt really a thing for players, so not on the sheet.
                                        # to make it more stylized. "Later" being after everything important is done.
                                        ft.Text("Armor Proficiencies", weight=ft.FontWeight.BOLD, size=16),
                                        ft.TextField(width=300),
                                        ft.Text("Tool Proficiencies", weight=ft.FontWeight.BOLD, size=16),
                                        ft.TextField(width=300),
                                        # Ideally, by the end of this project, the entire right
                                        # side of the program should be self-automated.
                                    ],
                                ),
                                #   ft.Container(width=800,border=ft.border.all(1,"white")),  SAVE THIS!
                            ],
                        ),
                    ),
                ],
            ),

        ],
    )
    navigationBar = ft.NavigationBar(
        selected_index=1,
        on_change=navigation_bar_change,
        destinations=[
            ft.NavigationBarDestination(label="Actions"),
            ft.NavigationBarDestination(label="Main"),
            ft.NavigationBarDestination(label="Inventory"),
            ft.NavigationBarDestination(label="Class Selection"),
            ft.NavigationBarDestination(label="Features and Talents"),
            ft.NavigationBarDestination(label="Character Creator"),
        ]

    )
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/main") # THIS IS NECESSARY! DONT TOUCH
ft.app(main)
