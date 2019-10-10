#!/bin/bash

if [ $# -eq 0 ]
then
  git grep TODO
else
  git grep TODO $1
fi
