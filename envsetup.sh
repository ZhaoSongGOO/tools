#!/bin/sh

#get project root dir
#script relative to execute
mypath=$(dirname $0)
#execute path
current_path=`pwd` 
ROOT_PATH=${current_path}/${mypath}

export PYTHONPATH=${ROOT_PATH}:$PYTHONPATH
#path of code - format
PATH_CODE_CHECK=${ROOT_PATH} 
export PATH=${PATH}:${PATH_CODE_CHECK}

alias tools="tool_main.py"
