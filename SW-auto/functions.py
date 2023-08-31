import pyautogui
import pygetwindow
import time
import cv2

def check_screenshots():
    counter = 0

    #targets active NoxPlayer window(if any). Change "NoxPlayer" to whatever emulator you are using (case sensitive)
    nox_window = pygetwindow.getWindowsWithTitle("NoxPlayer")[0]

    #assigns window dimensions so autogui can take ss of application
    left, top, width, height = nox_window.left, nox_window.top, nox_window.width, nox_window.height

    #top left corner of emulator window passed to functions.
    flag = process_screencap(left, top)

    if flag == 1:
        #restart farming.
        print("flag 1 returned")
        restartBattle()
    else: #flag = 0
        print("flag 2 returned")
        return
        # #refresh energy function call. 10 consecutive energy refreshes triggers bot check (mana quiz!)
        # refreshEnergy()
        # counter += 1

        # if counter == 9:
        #     #relaunch game. call function that reloads game and restarts farm.
    

def process_screencap(left, top):


    #capture trigger elements (indicators for restarting repeat battle or refilling energy)
    #x10 restart triggers
    endTrigger = pyautogui.locateOnScreen("images/repeat_battle_results-element.JPG", grayscale=False, confidence=0.3)
    print(endTrigger.left, endTrigger.top)
    pyautogui.moveTo(left, top)
    # triggerThree_selectDung = pyautogui.locateOnScreen("images/selectDung_replay-element.JPG", grayscale=True, confidence=0.3)
    # print(triggerTwo_repeatBattleResults, triggerThree_selectDung, screenshot) #test element capture

    #energy refill trigger


    #scenario determination
    if endTrigger is not None:
        #all three elements are found
        print("all elements found.")
        return 1
    else:
        print("elements not found")
        return 0
    
def restartBattle():
    return 1
    #sell runes (this tool will only autosell)
    # pyautogui.click(pyautogui.locateCenterOnScreen("images/new_sell_selected.JPG", grayscale=True, confidence=0.5))
    # time.sleep(0.1) #waits for game animation

    # #confirm
    # x, y = pyautogui.locateCenterOnScreen("images/target_sell_confirm-element.JPG", grayscale=False, confidence=0.9)
    # pyautogui.moveTo(x, y)
#     #"sell all for x mana stones?" prompt
#     pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("images/yes-element.JPG", grayscale=True, confidence=0.3)))

# #     #confirm yes if legendary rune selected
#     if pyautogui.locateOnScreen("images/selling-leg-rune.PNG") is not None:
#         pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("images/yes-element.JPG", grayscale=True, confidence=0.3)))
#     replayBattle()

# #     #"you didn't select item(s) to sell" prompt
#     if pyautogui.locateOnScreen("images/no_rune_selected-element.JPG") is not None:
# #         #okay then cancel button
#         pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("images/ok-element.JPG", grayscale=True, confidence=0.3)))
#         pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("images/cancel-element.JPG", grayscale=True, confidence=0.3)))
#         replayBattle()
#         return    
#     return
   
# def replayBattle():
#     pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("images/target_replay-element.JPG", grayscale=True, confidence=0.3)))
#     pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("images/repeat-battle.JPG", grayscale=True, confidence=0.3)))
#     pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("images/shop.png", grayscale=True, confidence=0.3)))
#     pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("images/60_crystal_recharge.PNG", grayscale=True, confidence=0.3)))
#     pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("images/yes-element.JPG", grayscale=True, confidence=0.3)))
#     pyautogui.click(pyautogui.center(pyautogui.locateOnScreen("images/target_replay-element.JPG", grayscale=True, confidence=0.3)))



