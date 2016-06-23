#!/bin/bash
set -e

# read the options
TEMP=`getopt vd $*`
eval set -- "$TEMP"

PIPARGS=-q
DEV=false

# extract options and their arguments into variables.
while true ; do
    case "$1" in
        -v) PIPARGS= ; shift ;;
        -d) DEV=true ; shift ;;
        --) shift ; break ;;
        *) echo "Internal error!" ; exit 1 ;;
    esac
done

# Go to repo root
cd $(git rev-parse --show-toplevel)

# Install root level python env
rm -rf env
virtualenv env
. env/bin/activate
pip $PIPARGS install pip-accel
pip-accel $PIPARGS install -r dev-requirements.txt
python setup.py develop
deactivate

# Install each component's python dependencies into ./vendored
for func in $(find * -name requirements.txt)
do
  lambda_folder=$(dirname $func)
  cd $lambda_folder
  comp=$(echo $lambda_folder|sed -e 's@/@-@')
  VENV=/tmp/$comp
  rm -rf vendored $VENV
  echo Install modules required by component $comp
  virtualenv $VENV
  . /tmp/$comp/bin/activate
  pip $PIPARGS install pip-accel
  pip-accel $PIPARGS $PIPARGS install -r requirements.txt
  deactivate
  mv $VENV/lib/python2.7/site-packages vendored
  touch vendored/__init__.py
  rm -rf $VENV
  if [ "$DEV" == true ] && [ -e 'dev-requirements.txt' ]
  then
    . ../env/bin/activate
    pip-accel $PIPARGS install -r dev-requirements.txt
    deactivate
  fi
  cd -
done
