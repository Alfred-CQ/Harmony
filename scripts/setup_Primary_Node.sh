#!/bin/bash

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
                "sudo yum install -y python3-venv"
                $error_log_file

print_title "Creating a Python 3 virtual environment..."
python3 -m venv .venv

print_title "Activating the virtual environment..."
source .venv/bin/activate


print_finish "Installation process finished"

print_title "Primary Node Setup Completed, check $error_log_file for any errors"
