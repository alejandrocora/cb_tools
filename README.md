# CoinBase Tools

**CoinBase Tools** is a set of tools developed to gather and manage CoinBase information from their resources.


## Installation

`$ git clone https://github.com/alejandrocora/cb_tools`  
`$ cd cb_tools`  
`$ pip3 install .`  


### NAWA

**NAWA** (**N**ew **A**sset **Wa**rning) checks if a new asset has been added to the CoinBase store, and sends a message via Telegram.

A Telegram bot should be configured before running. Do `$ telegramd-send --configure`, `$ telegram-send --configure-group` or `$ telegram-send --configure-channel` and follow the instructions.
