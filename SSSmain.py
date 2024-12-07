from enum import global_str

import flet as ft
from flet.core.types import TextAlign
import random


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

globalStr = None
globalDex = None
globalCon = None
globalInt = None
globalWis = None
globalCha = None
chosenStats = []
statSelectionConfirm = []


def main(page: ft.Page):
    # Anything Major section that needs to start with a ft.Row is its own area. Columns are usually kept together
    # This is probably the worst coding i've done in awhile, but it does what it needs to and looks presentable.
    page.title = "Star's Star's Stars Character Creator"

    statSelection1 = []
    statSelection2 = []
    statSelection3 = []
    statSelectionHolder = [statSelection1, statSelection2,
                           statSelection3]  # Theres a better way of doing this, but not in the mood

    def generateStats():
        for x in statSelectionHolder:  # Yeah our runtime is gonna be pretty bad, but i can fix this up later
            badNumber = 0
            y = 0
            while y < 6:
                y += 1
                tempStat = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
                tempStat.remove(min(tempStat))
                x.append(sum(tempStat))
                if sum(tempStat) <= 10:
                    badNumber += 1
                if y == 6:
                    if sum(x) <= 65 or badNumber >= 3:
                        y = 0
                        badNumber = 0
                        x.clear()

    def confirmStats(e):
        global chosenStats
        isChecked = e.control.value
        statConfirm1.disabled = isChecked
        statConfirm2.disabled = isChecked
        statConfirm3.disabled = isChecked
        for x in range(3):
            if statConfirmHolder[x].value == isChecked:
                statConfirmHolder[x].disabled = False
                if isChecked == True:
                    chosenStats = statSelectionHolder[x].copy()
                    for dd in statDropHolder:
                        dd.options = [
                            ft.dropdown.Option("None"),
                            ft.dropdown.Option(chosenStats[0]),
                            ft.dropdown.Option(chosenStats[1]),
                            ft.dropdown.Option(chosenStats[2]),
                            ft.dropdown.Option(chosenStats[3]),
                            ft.dropdown.Option(chosenStats[4]),
                            ft.dropdown.Option(chosenStats[5]),
                        ]
                        dd.update()
                else:
                    for dd in statDropHolder:
                        dd.options = []
                        dd.value = None
                        dd.update()

        statConfirm1.update()
        statConfirm2.update()
        statConfirm3.update()

    def statConfirm(
            e):  # This is probably one of the worst coding jobs I've ever done in my entire life. I'll need to fix this later.
        global globalStr
        global globalDex
        global globalCon
        global globalInt
        global globalWis
        global globalCha
        global statSelectionConfirm
        global chosenStats

        dupeCheck = False
        dupeCheck2 = False

        stat = e.control.label
        if e.data == "None":
            if stat == "Strength" and globalStr != None:
                if (globalStr != None):
                    for dd in statDropHolder:
                        if dd.label != "Strength":
                            dd.options.append(ft.dropdown.Option(globalStr))
                    chosenStats.append(globalStr)
                    statSelectionConfirm.remove(globalStr)
                globalStr = None
            elif stat == "Dexterity" and globalDex != None:
                for dd in statDropHolder:
                    if dd.label != "Dexterity":
                        dd.options.append(ft.dropdown.Option(globalDex))
                chosenStats.append(globalDex)
                statSelectionConfirm.remove(globalDex)
                globalDex = None
            elif stat == "Constitution" and globalCon != None:
                for dd in statDropHolder:
                    if dd.label != "Constitution":
                        dd.options.append(ft.dropdown.Option(globalCon))
                chosenStats.append(globalCon)
                statSelectionConfirm.remove(globalCon)
                globalCon = None
            elif stat == "Intelligence" and globalInt != None:
                for dd in statDropHolder:
                    if dd.label != "Intelligence":
                        dd.options.append(ft.dropdown.Option(globalInt))
                chosenStats.append(globalInt)
                statSelectionConfirm.remove(globalInt)
                globalInt = None
            elif stat == "Wisdom" and globalWis != None:
                for dd in statDropHolder:
                    if dd.label != "Wisdom":
                        dd.options.append(ft.dropdown.Option(globalWis))
                chosenStats.append(globalWis)
                statSelectionConfirm.remove(globalWis)
                globalWis = None
            elif stat == "Charisma" and globalCha != None:
                if (globalCha != None):
                    for dd in statDropHolder:
                        if dd.label != "Charisma":
                            dd.options.append(ft.dropdown.Option(globalCha))
                chosenStats.append(globalCha)
                statSelectionConfirm.remove(globalCha)
                globalCha = None
            page.update()
            return
        score = int(e.data)
        if statSelectionConfirm.__contains__(score):
            dupeCheck = True
        if chosenStats.__contains__(score):
            dupeCheck2 = True

        if dupeCheck and not dupeCheck2:
            return
        # Could do a for or while loop here, but I dont think its necessary for values which never change. Might change that later though for saving space.
        if stat == "Strength":
            strength.value = score
            strMod.value = score // 2 - 5
            if (globalStr != None):
                for dd in statDropHolder:
                    if dd.label != "Strength":
                        dd.options.append(ft.dropdown.Option(globalStr))
                chosenStats.append(globalStr)
                statSelectionConfirm.remove(globalStr)
            globalStr = score

        elif stat == "Dexterity":
            dexterity.value = score
            dexMod.value = score // 2 - 5
            if (globalDex != None):
                for dd in statDropHolder:
                    if dd.label != "Dexterity":
                        dd.options.append(ft.dropdown.Option(globalDex))
                chosenStats.append(globalDex)
                statSelectionConfirm.remove(globalDex)
            globalDex = score

        elif stat == "Constitution":
            constitution.value = score
            conMod.value = score // 2 - 5
            if (globalCon != None):
                for dd in statDropHolder:
                    if dd.label != "Constitution":
                        dd.options.append(ft.dropdown.Option(globalCon))
                chosenStats.append(globalCon)
                statSelectionConfirm.remove(globalCon)
            globalCon = score

        elif stat == "Intelligence":
            intelligence.value = score
            intMod.value = score // 2 - 5
            if (globalInt != None):
                for dd in statDropHolder:
                    if dd.label != "Intelligence":
                        dd.options.append(ft.dropdown.Option(globalInt))
                chosenStats.append(globalInt)
                statSelectionConfirm.remove(globalInt)
            globalInt = score

        elif stat == "Wisdom":
            wisdom.value = score
            wisMod.value = score // 2 - 5
            if (globalWis != None):
                for dd in statDropHolder:
                    if dd.label != "Wisdom":
                        dd.options.append(ft.dropdown.Option(globalWis))
                chosenStats.append(globalWis)
                statSelectionConfirm.remove(globalWis)
            globalWis = score

        elif stat == "Charisma":
            charisma.value = score
            chaMod.value = score // 2 - 5
            if (globalCha != None):
                for dd in statDropHolder:
                    if dd.label != "Charmisa":
                        dd.options.append(ft.dropdown.Option(globalCha))
                chosenStats.append(globalCha)
                statSelectionConfirm.remove(globalCha)
            globalCha = score

        scoreCycle(score)

    def scoreCycle(score):
        global statSelectionConfirm
        statSelectionConfirm.append(score)
        for dd in statDropHolder:
            if str(dd.value) != str(score):
                for o in dd.options:
                    if o.key == score:
                        dd.options.remove(o)
                        break

        chosenStats.remove(score)
        page.update()

    strengthDrop = ft.Dropdown(
        label="Strength",
        on_change=statConfirm,
        width=200,
    )
    dexterityDrop = ft.Dropdown(
        label="Dexterity",
        on_change=statConfirm,
        width=200,
    )
    constitutionDrop = ft.Dropdown(
        label="Constituion",
        on_change=statConfirm,
        width=200,
    )
    intelligenceDrop = ft.Dropdown(
        label="Intelligence",
        on_change=statConfirm,
        width=200,
    )
    wisdomDrop = ft.Dropdown(
        label="Wisdom",
        on_change=statConfirm,
        width=200,
    )
    charismaDrop = ft.Dropdown(
        label="Charisma",
        on_change=statConfirm,
        width=200,
    )
    statDropHolder = [strengthDrop, dexterityDrop, constitutionDrop, intelligenceDrop, wisdomDrop,
                      charismaDrop]  # This will be important later

    statConfirm1 = ft.Checkbox(value=False, on_change=confirmStats)
    statConfirm2 = ft.Checkbox(value=False, on_change=confirmStats)
    statConfirm3 = ft.Checkbox(value=False, on_change=confirmStats)
    statConfirmHolder = [statConfirm1, statConfirm2, statConfirm3]  # Really dumb way of doing this

    def navigate_to(route):
        page.go(route)

    def mainView():
        return ft.View(

            route="/main",
            scroll=ft.ScrollMode.ADAPTIVE,
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
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[
                ft.Column(
                    expand=True,
                    controls=[
                        sectionOne,
                        ft.Divider(),
                        navigationBar,
                        ft.Divider(),
                        characterCreator,
                    ],
                ),
            ],
        )

    def routeChange(route):
        route = route.data.strip()
        page.views.clear()
        if route == "/main":
            page.views.append(mainView())
        elif route == "/actions":
            page.views.append(actionsView())
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
            navigate_to("/class-selection")
        elif selected_index == 3:
            navigate_to("/features-talents")
        elif selected_index == 4:
            navigate_to("/character-creator")

    def viewPop(view):
        page.views.pop()
        if len(page.views) == 0:
            page.window_close()

    sectionOne = ft.Column(
        controls=[
            ft.Row(
                # Trying to have it be that the Base Class is ALWAYS at the far right of the window. I could accomplish
                # something similiar by having a lot of blank texts with large widths, but I dont want to do that for
                # clutter. It's already bad enough
                controls=[
                    ft.TextField(width=200, label="Character Name"),
                    ft.Row(
                        expand=1,
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.TextField(width=200, label="Base Class 1"),
                        ],
                    ),
                ],
            ),
            ft.Row(
                controls=[
                    ft.TextField(width=200, label="Job"),
                    ft.Row(
                        expand=1,
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.TextField(width=200, label="Base Class 1"),
                        ],
                    ),
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
    strength = ft.TextField(label="Str", on_change=checkInt, width=60)
    strMod = ft.TextField(label="Mod", disabled=True, width=60)
    dexterity = ft.TextField(label="Dex", on_change=checkInt, width=60)
    dexMod = ft.TextField(label="Mod", disabled=True, width=60)
    constitution = ft.TextField(label="Con", on_change=checkInt, width=60)
    conMod = ft.TextField(label="Mod", disabled=True, width=60)
    intelligence = ft.TextField(label="Int", on_change=checkInt, width=60)
    intMod = ft.TextField(label="Mod", disabled=True, width=60)
    wisdom = ft.TextField(label="Wis", on_change=checkInt, width=60)
    wisMod = ft.TextField(label="Mod", disabled=True, width=60)
    charisma = ft.TextField(label="Cha", on_change=checkInt, width=60)
    chaMod = ft.TextField(label="Mod", disabled=True, width=60)
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
                                        strength,
                                        strMod,
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        dexterity,
                                        dexMod,
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        constitution,
                                        conMod,
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        intelligence,
                                        intMod,
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        wisdom,
                                        wisMod,
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        charisma,
                                        chaMod,
                                    ],
                                ),
                                ft.Row(
                                    controls=[
                                        ft.TextField(label="Luck", value=random.randint(1, 100), on_change=checkInt,
                                                     width=130,
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

    generateStats()
    characterCreator = (
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Choose a stat selection. Your luck has already been automatically generated.", size=18),
                ft.Container(
                    padding=10,
                    border=ft.border.all(1, "White"),
                    content=
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Stat Choice 1", size=18),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.TextField(label="Stat 1", value=statSelection1[0], disabled=True, width=120),
                                    ft.TextField(label="Stat 2", value=statSelection1[1], disabled=True, width=120),
                                    ft.TextField(label="Stat 3", value=statSelection1[2], disabled=True, width=120),
                                    ft.TextField(label="Stat 4", value=statSelection1[3], disabled=True, width=120),
                                    ft.TextField(label="Stat 5", value=statSelection1[4], disabled=True, width=120),
                                    ft.TextField(label="Stat 6", value=statSelection1[5], disabled=True, width=120),
                                    statConfirm1

                                ],
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    padding=10,
                    border=ft.border.all(1, "White"),
                    content=
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Stat Choice 2", size=18),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.TextField(label="Stat 1", value=statSelection2[0], disabled=True, width=120),
                                    ft.TextField(label="Stat 2", value=statSelection2[1], disabled=True, width=120),
                                    ft.TextField(label="Stat 3", value=statSelection2[2], disabled=True, width=120),
                                    ft.TextField(label="Stat 4", value=statSelection2[3], disabled=True, width=120),
                                    ft.TextField(label="Stat 5", value=statSelection2[4], disabled=True, width=120),
                                    ft.TextField(label="Stat 6", value=statSelection2[5], disabled=True, width=120),
                                    statConfirm2

                                ],
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    padding=10,
                    border=ft.border.all(1, "White"),
                    content=
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Stat Choice 3", size=18),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.TextField(label="Stat 1", value=statSelection3[0], disabled=True, width=120),
                                    ft.TextField(label="Stat 2", value=statSelection3[1], disabled=True, width=120),
                                    ft.TextField(label="Stat 3", value=statSelection3[2], disabled=True, width=120),
                                    ft.TextField(label="Stat 4", value=statSelection3[3], disabled=True, width=120),
                                    ft.TextField(label="Stat 5", value=statSelection3[4], disabled=True, width=120),
                                    ft.TextField(label="Stat 6", value=statSelection3[5], disabled=True, width=120),
                                    statConfirm3
                                ],
                            ),
                        ],
                    ),
                ),
                ft.Container(
                    padding=10,
                    border=ft.border.all(1, "White"),
                    content=
                    ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Confirm stat choices", size=18),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    strengthDrop,
                                    dexterityDrop,
                                    constitutionDrop,
                                    intelligenceDrop,
                                    wisdomDrop,
                                    charismaDrop,

                                ],
                            ),
                        ],
                    ),
                ),
            ],
        )
    )

    navigationBar = ft.NavigationBar(
        selected_index=1,
        on_change=navigation_bar_change,
        destinations=[
            ft.NavigationBarDestination(label="Actions"),
            ft.NavigationBarDestination(label="Main"),
            ft.NavigationBarDestination(label="Class Selection"),
            ft.NavigationBarDestination(label="Features and Talents"),
            # Despite what you may assume, this place only keeps track of what Features and Talents you HAVE
            ft.NavigationBarDestination(label="Character Creator"),
        ]

    )
    page.on_route_change = routeChange
    page.on_view_pop = viewPop
    page.go("/main")  # THIS IS NECESSARY! DONT TOUCH


ft.app(main)
