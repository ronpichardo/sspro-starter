# Boilerplate for 4-Series

## Usage
This is intended as a starting point for a Crestron 4-series Control System.
The idea is to clone/fork this repo and write up the code and connect it to a CI/CD Tool like Jenkins

## TODO
1. Add a jenkinsfile to build the Crestron Sandbox nuget packages
2. Create a postbuild process that copies and versions the cpz output file used to load to a processor
3. Create a postbuild script that deploys to a processor or VC4 Server
