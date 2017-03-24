1. Clone repo
2. At the top of the directory run the following commands:
### Ensure machine is up
vagrant up

### ssh to the machine
vagrant ssh

### cd to the directory with the scripts
cd /vagrant/tournament

3. Clean up the database with the following command
psql tournament < tournament.sql

4. Run the test
python tournament_test.py