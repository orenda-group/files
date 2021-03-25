curl http://35.229.113.99/api/models/laststamps?key=orenda1234 -o laststamps.zip
yes | unzip laststamps.zip 
rm -f laststamps.zip 
ls time_stamps
cat time_stamps/last_trained_5min.json
cat time_stamps/last_trained_hour24.json