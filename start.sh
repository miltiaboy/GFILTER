if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/miltiaboy/Gfilter.git /Gfilter
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Gfilter
fi
cd /Gfilter
pip3 install -U -r requirements.txt
echo "Gfilter Bot V3 🎗️"
python3 bot.py
