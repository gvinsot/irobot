
#check we are in current path
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR
#

sudo apt-get update
sudo apt-get install -y python3-venv python3-pip

cd ../app

sudo python3 -m venv venv
source venv/bin/activate
sudo pip3 install -r requirements.txt

sudo echo '
    wifis:
        wlan0:
            optional: true
            dhcp4: true
            access-points:
                "VINSOT":
                    password: "replace password"' | sudo tee -a /etc/netplan/50-cloud-init.yaml
                    
sudo netplan generate
sudo netplan apply

cd -

sudo cp ./iRobot.service /etc/systemd/system/iRobot.service
sudo systemctl enable iRobot
sudo systemctl start iRobot
