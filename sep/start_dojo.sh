#!/bin/bash

# Monitora os testes

while [ 1 == 1 ]
do
    python -m unittest -v tests
    sleep 5
    clear
done

