#!/bin/bash
#Mkae this shell script an executable 
#chmod +x setup_project.sh

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

pip install python-dotenv

# Run the main program
python Main.py

# Deactivate the virtual environment
deactivate

echo "Setup and program execution complete."

