#!/bin/bash


function help(){

	echo "---Debe incluir tres parametros---"
}

if ! [ $# -eq 3 ]; then
	help
	exit 1
fi

if [ $# -eq 3 ]; then
	echo "Corriendo Programa"
fi