import GabesPythonToolBox.Utility.Collor as GTB
from GabesPythonToolBox.Utility.Debug import Debug

Debug.add_group("Showcase", True)

Debug.log("Color Showcase", "Header", group="Showcase")


fg_colors = [
    (GTB.FG_Black, "Black"),
    (GTB.FG_Red, "Red"),
    (GTB.FG_Green, "Green"),
    (GTB.FG_Yellow, "Yellow"),
    (GTB.FG_Blue, "Blue"),
    (GTB.FG_Magenta, "Magenta"),
    (GTB.FG_Cyan, "Cyan"),
    (GTB.FG_White, "White"),
    (GTB.FG_B_Black, "B_Black"),
    (GTB.FG_B_Red, "B_Red"),
    (GTB.FG_B_Green, "B_Green"),
    (GTB.FG_B_Yellow, "B_Yellow"),
    (GTB.FG_B_Blue, "B_Blue"),
    (GTB.FG_B_Magenta, "B_Magenta"),
    (GTB.FG_B_Cyan, "B_Cyan"),
    (GTB.FG_B_White, "B_White"),
]

bg_colors = [
    (GTB.BG_Black, "Black"),
    (GTB.BG_Red, "Red"),
    (GTB.BG_Green, "Green"),
    (GTB.BG_Yellow, "Yellow"),
    (GTB.BG_Blue, "Blue"),
    (GTB.BG_Magenta, "Magenta"),
    (GTB.BG_Cyan, "Cyan"),
    (GTB.BG_White, "White"),
    (GTB.BG_B_Black, "B_Black"),
    (GTB.BG_B_Red, "B_Red"),
    (GTB.BG_B_Green, "B_Green"),
    (GTB.BG_B_Yellow, "B_Yellow"),
    (GTB.BG_B_Blue, "B_Blue"),
    (GTB.BG_B_Magenta, "B_Magenta"),
    (GTB.BG_B_Cyan, "B_Cyan"),
    (GTB.BG_B_White, "B_White"),
]


# Sorted by text color
Debug.log("Sorted by Text Color", "Header", group="Showcase")
for fg, fg_name in fg_colors:
    Debug.log(f"{fg}Printed just in GTB.FG_{fg_name}{GTB.R}", "None", group="Showcase")
    for bg, bg_name in bg_colors:
        Debug.log(
            f"{fg}{bg}Printed in GTB.FG_{fg_name} and GTB.BG_{bg_name}{GTB.R}",
            "None",
            group="Showcase",
        )
Debug.log("End of Text Color Showcase", "End", group="Showcase")

# Sorted by background color
Debug.log("Sorted by Background Color", "Header", group="Showcase")
for bg, bg_name in bg_colors:
    Debug.log(f"{bg}Printed just in GTB.BG_{bg_name}{GTB.R}", "None", group="Showcase")
    for fg, fg_name in fg_colors:
        Debug.log(
            f"{fg}{bg}Printed in GTB.FG_{fg_name} and GTB.BG_{bg_name}{GTB.R}",
            "None",
            group="Showcase",
        )
Debug.log("End of Background Color Showcase", "End", group="Showcase")

Debug.log("Color Showcase Complete", "End", group="Showcase")
