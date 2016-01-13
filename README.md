# quickstart-mturk
Welcome to the easiest way to start developing with Amazon Mechanical Turk (mturk), using Flask and boto. boto3 is currently in development, but mturk has not been ported over, so this is the simplest and most up-to-date way.  
# Purpose
To easily start developing crowdsourcing tasks without going from blogpost to blogpost. Note that the entire assignment is yours to create via HTML/CSS/JS, so the possibilities are endless.  
# General flow 
* Register on mturk.com and https://requester.mturk.com/developer/sandbox
* Create your HIT in page.html
* Deploy to heroku (or your choice of hosting service)
* Edit and execute post_hits.py
* Amazon Mechanical Turk will post your HIT, and IFrame your url in when a user accepts it.
* After completion, head to Mechanical to see collected data and accept work. Note that there are programmatic ways to do this (will add to this repository, time permitting) 

# To deploy
Download the heroku toolbelt, login, run 'heroku create' in the directory, and push the code to the heroku repository created via 'git push heroku master'. 
# To make HITs
Update the url variable in post_hits.py to correctly point to your application and then execute post_hits.py
