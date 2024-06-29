import pyautogui


# a alert displays with a ok button
# on it
pyautogui.alert(text='', title='', button='OK')

# a confirm dialog box appears with ok 
# and cancel buttons on it
pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])

# a prompt displays that lets you to 
# write something
pyautogui.prompt(text='', title='' , default='')

# a password field appears with entry box 
# to fill a password 
pyautogui.password(text='', title='', default='', mask='*')
