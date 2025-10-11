import os
##testing taking of env var from runner for github actions
yay = os.environ.get('my_var')
print(yay)