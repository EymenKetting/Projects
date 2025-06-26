#!/usr/bin/env python3
import tcod


def main() -> None:
    # Stel de variabelen in voor de algemene schermgrootte
    screen_width = 80
    screen_height = 50
# Defineer welke fonts worden gebruikt
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )
#  Maak een nieuwe terminal met de opgegeven schermgrootte en tileset
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        # Titel van het venster
        title="Eymen's Roguelike Project",
        #vsync ja of nee
        vsync=True,
    ) as context:
        # Stel het array in voor de root console om op basis van x en y te tekenen in plaats van y en x
        root_console = tcod.Console(screen_width, screen_height, order="F")
        # Game loop, blijft draaien totdat het spel wordt afgesloten
        while True:
            # Startpositie van @, op basis van x en y positie
            root_console.print(x=1, y=1, string="@")
            # Teken de root console op het scherm
            context.present(root_console)
            # Laat het scherm sluiten door op het kruisje te klikken of door de escape toets in te drukken
            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == "__main__":
    main()