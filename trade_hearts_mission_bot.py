import pyautogui as pg
import cv2 as cv

from autorun import AutoRun
from autorun_routes_service import RoutesService
from complete_routes import complete_routes, city_routes
from tele_bot import TelegramBot
from trade_hearts_ui_controller import TradeHeartsUIController
from window_capture import WindowCapture

if __name__ == '__main__':
    pg.countdown(3)

    print("Finding window...", end='')
    albion_window = WindowCapture()
    # albion_window.init_region('Albion Online Client')
    print(' +')

    routes_service = RoutesService()
    ui = TradeHeartsUIController(albion_window)
    tb = TelegramBot(default_region={'top': 25, 'left': 0, 'width': 2925, 'height': 1110})
    autorun = AutoRun(window=albion_window, tb=tb)

    autorun.init_keybinding()

    repeat = 11

    for i in range(repeat):
        # put award hearts and take another hearts
        ui.open_bank()
        tb.send_message(msg=f'Trade mission {i+1} is starting...')
        ui.open_inventory()
        ui.put_hearts_to_bank()
        ui.take_hearts_to_inventory()
        ui.close_bank_window()

        # start from bank
        bank__yara = [
            city_routes.bank_of_bridgewatch__bank_chest__bridgewatch__r,
            city_routes.bridgewatch__bank_of_bridgewatch__yara_sunblaze_heart_mission__r,
        ]
        autorun.start(curr_routes=bank__yara)

        # take mission
        tb.send_screenshot()
        ui.open_trade_mission_window()
        ui.open_trade_mission_tab()
        ui.open_lymhurst_mission()
        ui.open_major_mission_dialog()
        ui.click_contract_accept_btn()

        # go to shady
        yara__shady = [
            city_routes.bridgewatch__yara_sunblaze_heart_mission__lazygrass_plain__r,
            *complete_routes.bridgewatch__hornbeam_wood__treeheart_mission,
        ]
        autorun.start(curr_routes=yara__shady)

        # give items to shady
        pg.moveTo(*ui.get_screen_point((950, 675), {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}), duration=0.15)
        tb.send_screenshot()

        ui.open_major_mission_dialog()
        ui.click_contract_give_items_btn()
        ui.close_trade_mission_window()

        # go to yara
        shady__yara = [
            *complete_routes.hornbeam_wood__bridgewatch__treeheart_mission,
            city_routes.bridgewatch__lazygrass_plain__yara_sunblaze_heart_mission,
        ]
        autorun.start(curr_routes=shady__yara)

        # finish mission and give items to yara
        tb.send_screenshot()

        ui.open_major_mission_dialog()
        ui.click_contract_give_items_btn()
        ui.close_trade_mission_window()

        # go to bank
        yara__bank = [
            city_routes.bridgewatch__yara_sunblaze_heart_mission__bank_of_bridgewatch,
            city_routes.bank_of_bridgewatch__bridgewatch__bank_chest,
        ]
        autorun.start(curr_routes=yara__bank)

        tb.send_screenshot(msg=f'Trade mission {i+1} has finished +')

    pg.press('esc')
    tb.stop_polling()
    cv.destroyAllWindows()