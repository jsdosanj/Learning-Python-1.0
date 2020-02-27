#!/bin/bash

a=1 # Global Variable

function f1()
{
 # local a=1
 a=1000  # Overwriting the value of a (global variable)
 echo $a
}

function f2()
{
 echo $a
}

f1
f1
