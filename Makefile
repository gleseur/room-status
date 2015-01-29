run_detector:
	sudo python detector/daemon.py

infinite_run:
	bin/run_detector.sh

setup_detector:
	sudo pip install -r detector/requirements.txt
