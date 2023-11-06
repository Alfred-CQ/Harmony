#!/bin/bash

PROJECT_DIR=$(pwd)

source hm_bash_utils.sh

error_log_file="../logs/Primary_Node_errors.log"

print_title "Initializing Primary Node Setup for Harmony"

install_package "Git Version Control" \
                "sudo yum install -y git" \
                $error_log_file

install_package "Nginx HTTP and reverse proxy server" \
                "sudo yum install -y nginx"
                $error_log_file

install_package "Python 3 virtual environment support" \
                "sudo yum install -y python3 python3-virtualenv" \
                $error_log_file

print_title "Creating a Python 3 virtual environment..."
python3 -m venv .venv

print_title "Activating the virtual environment..."
source ./.venv/bin/activate

install_package "Installing Harmony Web Browser Requirements" \
                "pip3 install -r requirements.txt" \
                $error_log_file

print_title "Setup Harmony service daemon"
sed -i "s|WorkingDirectory=.*|WorkingDirectory=$PROJECT_DIR|" scripts/Harmony.service
sed -i "s|ExecStart=.*|ExecStart=$PROJECT_DIR/.venv/bin/gunicorn -b localhost:8000 harmony:app|" scripts/Harmony.service

sudo cp scripts/Harmony.service /etc/systemd/system/Harmony.service
sudo systemctl daemon-reload
sudo systemctl restart Harmony.service
sudo systemctl enable Harmony

sudo systemctl status Harmony

print_title "Setup Harmony Nginx"

sudo systemctl start nginx
sudo systemctl enable nginx

sudo cp scripts/HarmonyWeb.conf /etc/nginx/conf.d/

sudo systemctl restart nginx

print_finish "Setup process finished"

print_title "Primary Node Setup Completed, check $error_log_file for any errors"
