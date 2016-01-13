import os
from flask import Flask, render_template, url_for, request, make_response
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import ExternalQuestion
from boto.mturk.qualification import Qualifications, PercentAssignmentsApprovedRequirement, NumberHitsApprovedRequirement
from boto.mturk.price import Price


#Start Configuration Variables
AWS_ACCESS_KEY_ID = "XXX"
AWS_SECRET_ACCESS_KEY = "XXX"
DEV_ENVIROMENT_BOOLEAN = True
DEBUG = True
#End Configuration Variables

#This allows us to specify whether we are pushing to the sandbox or live site.
if DEV_ENVIROMENT_BOOLEAN:
    AMAZON_HOST = "https://workersandbox.mturk.com/mturk/externalSubmit"
else:
    AMAZON_HOST = "https://www.mturk.com/mturk/externalSubmit"

app = Flask(__name__, static_url_path='')



@app.route('/', methods=['GET', 'POST'])
def main():

#The following code segment can be used to check if the turker has accepted the task yet
    if request.args.get("assignmentId") == "ASSIGNMENT_ID_NOT_AVAILABLE":
        #Our worker hasn't accepted the HIT (task) yet
        pass
    else:
        #Our worker accepted the task
        pass


    '''
    We're creating a dict with which we'll render our template page.html
    Note we are grabbing GET Parameters
    In this case, I'm using someInfoToPass as a sample parameter to pass information
    '''
    render_data = {
        "worker_id": request.args.get("workerId"),
        "assignment_id": request.args.get("assignmentId"),
        "amazon_host": AMAZON_HOST,
        "hit_id": request.args.get("hitId"),
        "some_info_to_pass": request.args.get("someInfoToPass")
    }


    resp = make_response(render_template("page.html", name = render_data))
    
    #This is particularly nasty gotcha.
    #Without this header, your iFrame will not render in Amazon
    resp.headers['x-frame-options'] = 'this_can_be_anything'
    return resp


if __name__ == "__main__":
    app.debug = DEBUG
    app.run() 
