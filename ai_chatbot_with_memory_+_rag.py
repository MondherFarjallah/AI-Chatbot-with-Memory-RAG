!rm -rf venv
!python3 -m venv --without-pip venv
!curl -sSL https://bootstrap.pypa.io/get-pip.py -o get-pip.py
!/content/venv/bin/python get-pip.py
!rm get-pip.py
!source venv/bin/activate

pip install google-genai python-dotenv numpy

GEMINI_API_KEY='AIzaSyDG05GZ7RhFO-XO3CW_WYt8SbOZQM8Ayxo'
