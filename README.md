# CoinBase Tools

**CoinBase Tools** is a set of tools developed to gather and manage CoinBase information from their resources.

## Installation

`$ git clone https://github.com/alejandrocora/cb_tools`  
`$ cd cb_tools`  
`$ pip3 install .`  

## nawa

**nawa** (**N**ew **A**sset **Wa**rning) checks if a new asset has been added to the CoinBase store, and sends a message via Telegram.

A Telegram bot should be configured before running. Do `$ telegramd-send --configure`, `$ telegram-send --configure-group` or `$ telegram-send --configure-channel` and follow the instructions.

### Running

To run **nawa** use the command `nawa`. To change the path for the file nawa uses to store the last added asset, use the parameter `--file` or `-f`. To change the delay for nawa checkings, use `--delay` or `-d` followed by the time in seconds. I.e `nawa --file ~/.config/nawa.log --delay 600`, nawa will save the file in `~/.config/nawa.log` and run every 10 minutes.
