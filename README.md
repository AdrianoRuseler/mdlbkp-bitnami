# mdlbkp-bitnami

## Moodle Update
```bash
export MDLBRANCH="MOODLE_403_STABLE"
export MDLREPO="https://github.com/moodle/moodle.git"
export PLGBRANCH="main"
export PLGREPO="https://github.com/AdrianoRuseler/moodle403-plugins.git"
export MDLCORE="mdlcore" # Temp folder for moodle core
export MDLPLGS="mdlplugins" # Temp folder for moodle plugins
# Moodle software (For example, everything in server/htdocs/moodle)
export MDLHOME="/opt/bitnami/moodle" # TODO!

cd /tmp
git clone --depth=1 --branch=$MDLBRANCH $MDLREPO $MDLCORE
git clone --depth=1 --recursive --branch=$PLGBRANCH $PLGREPO $MDLPLGS
rsync -a /tmp/$MDLPLGS/moodle/* /tmp/$MDLCORE/
	
echo "Moving old files ..."
mv $MDLHOME $MDLHOME.tmpbkp
mkdir $MDLHOME

echo "moving new files..."
mv /tmp/$MDLCORE/* $MDLHOME

echo "Copying config file ..."
cp $MDLHOME.tmpbkp/config.php $MDLHOME

echo "Remove tmp files..."
rm -rf /tmp/$MDLPLGS
rm -rf /tmp/$MDLCORE
```

## Docker build
```bash

docker compose build --no-cache
docker compose up -d
```