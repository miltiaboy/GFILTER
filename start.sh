if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/afluaflu123/Nancy-V3.git /Nancy
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Nancy
fi
cd /Nancy
pip3 install -U -r requirements.txt
echo "Nancy Bot V3 🎗️"
python3 bot.py
