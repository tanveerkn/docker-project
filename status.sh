#!/bin/bash
if (($(curl -I http://130.230.19.200:5000/v2/ | grep OK | wc -l) > 0))
then
  echo "Docker Registry is Working Fine"
else
  exit (1)
fi
