#!/bin/bash

pass=0

read -p "Introduce un numero: " input

function CheckValue(){
	if [ $input -eq 0 ]; then
        pass=1
        exit 1
    elif [ $input -eq 1 ]; then
        pass=1
        exit 1
    else
        echo "Intentalo de nuevo"
    fi
}
    while [ $pass -eq 0 ]
    do
      CheckValue
      read -p "Introduce un numero: " input
    done
