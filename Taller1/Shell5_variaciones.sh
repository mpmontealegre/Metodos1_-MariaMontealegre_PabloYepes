#!/bin/bash

FACT=1
FACT2=1
NUM=20
NUM2=17
for i in $(seq 1 1 $NUM)
do
    FACT=$((FACT*i))
done
for i in $(seq 1 1 $NUM2)
do
    FACT2=$((FACT2*i))
done
let NUM3=FACT/FACT2
echo "El numero de posibles variaciones es $NUM3"