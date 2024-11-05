# Craigslist Bike Monitor

This code will search Craigslist for bikes and send an email with the results.

## Setup:

1. Clone this repo
2. Install pyyaml package

```
pip install pyyaml 
```

OR

```
 sudo apt install python3-yaml
```

3. In config.yaml, provide your email and an smtp password. If you have a gmail account, follow this guide to create an app password, and use that as the smtp password (https://support.google.com/accounts/answer/185833?hl=en)
4. Fill in the other config.yaml parameters, such as location, distance, brand, and price settings

5. Run the code. It should send you an email with the results, or print to terminal, based on your config parameters.

```
python3 main.py 
```


### OPTIONAL: Setup run on startup

1. Modify the service file bike_monitor.service so that ExecStart points to main.py, and WorkingDirectory points to the directory main.py is in
2. Place the service file

```
sudo cp bike_monitor.service /etc/systemd/system/
```

3. Enable the service

```
sudo systemctl daemon-reload
```

```
sudo systemctl enable bike_monitor.service
```

4. Now whenever your computer restarts, main.py will run, and send an email. Optionally test the service:

```
sudo systemctl start bike_monitor.service
```

5. If you're getting spammed with emails and wanna disable the service, run

```
sudo systemctl disable bike_monitor.service
```
