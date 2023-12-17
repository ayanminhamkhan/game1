#!/venv1/bin/env python
import tcod

# from actions import EscapeAction,MovementAction
from input_handler import EventsHandler
from entity import Entity
from engine import Engine
from game_map import GameMap




def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45
    

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventsHandler()


    player = Entity(int(screen_width/2),int(screen_height/2),"@")
    npc = Entity(int(screen_width/2-10),int(screen_height/2),"n",[255,255,0])
    entities = {player,npc}

    game_map = GameMap(map_width,map_height)
    engine = Engine(entities=entities,event_handler=event_handler,game_map=game_map,player=player)



    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Roguelike1",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
       
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()
            engine.handle_events(events)

                


if __name__ == "__main__":
    main()