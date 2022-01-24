# Custom clipboard for CLI application
A personal key-value store.

Add path to scripts as aliases to your CLI application profile and execute commands to store and retrieve data from unlimited clipboard.
```commandline
# Store something (and sync it to the network)
set kitty meow

# Fetch something (from the local cache)
get kitty

# What’s in the store?
list

# Spaces are fine
set "kitty litter" "smells great"
```

## Installation
Add path to each script into profiles of your CLI user application
```commandline
# custom clipboard
alias set='python3 <path_to_repo>/custom_clipboard/commands/set.
py'

alias get='python3 <path_to_repo>/custom_clipboard/commands/get.
py'

alias list='python3 <path_to_repo>/custom_clipboard/commands/lis
t.py'

alias clear='python3 <path_to_repo>/custom_clipboard/commands/cl
ear.py'

alias clear_all='python3 <path_to_repo>/custom_clipboard/command
s/clear_all.py'
```

### License
[MIT](LICENSE)