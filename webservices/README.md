# Webservices
This folder is for essential webservices. Same basic architecture as emergency_webservices (i.e. microservice docker containers) but different in that it will contain things pertaining to network billing, management, topping up, etc. If you want to deploy a commercial/production network, use this. Otherwise (home router? local testing?) you can leave it out.

## Running Locally

### Setup/Configure
- Use `npm install` to install the dependencies
- Make sure the EPC database (oai_db) is installed (i.e. make sure you've setup/installed the epc)
- Create a .env file for environment variables. If you're just following the standard install scripts, the best way to do this is to just copy "production.env" to ".env" and make sure the DB_USER and DB_PASSWORD variables are set correctly. If you're just playing around on your local machine, copy "local_dev.env" to ".env" and look it over.
- `npm start` to run the app. It should be running on [localhost:3000](http://localhost:3000/) unless you've changed the PORT number in the .env file.