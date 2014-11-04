"""

Usage:

Brainstorm

sg recent  # default, recent activity, status changes, whatever gregg finds useful
sg search x  # name, word in surveygizmo
sg results ID  # attempt to get all results
sg users


sg 'admin' # <- admin report... # default, recent activity, status changes, whatever gregg finds useful
sg adduser # otherwise so tedious!

sg open id  # <- in browser / web?

07:28 < ilana> mm, okay
07:28 < ilana> 1. all my active surveys
07:29 < ilana> 2. number of responses in each one
07:31 < ilana> 3. if there's an alert, which active surveys have 0 responses

7:31 < gregglind> is 'read only' okay, or do you expect to be able to do actions?
07:31 < ilana> 4. maybe quick stats per question, though i;m not sure that's necessary
07:31 < ilana> gregglind: maybe "deploy" and "stop"
07:32 < ilana> though i'm not sure those need to be exposed via cli
07:32 < ilana> maybe just "stop"
07:32 < gregglind> deploy -> testing -> live.
07:32 < gregglind> what is stop?
07:32 < gregglind> (for you)
07:33 < ilana> either put it back in testing mode or remove the survey completely

"""

from surveygizmo import SurveyGizmo

sg = SurveyGizmo(api_version='v3', response_type='json')
sg.config.auth_method = "user:pass"
sg.config.username = "username"
sg.config.password = "password"


sg.api.survey.list()
sg.api.survey.get('39501')
sg.api.survey.copy('39501', '39501 Copy')
sg.api.surveyresponse.list('39501')

# thing to support

def action(fn):
  def inner(*args,**kwargs):
    return fn(*args, **kwargs)

  return inner

## actions

@action
def adduser(blob):
  """ add a user to the db"""
  ## todo, how to param this?  valid json?  email, quoted name?
  pass

@action
def users():
  """ user report """
  pass

@action
def search(string):
  """ search users, survey names, otherstuff?"""
  pass

@action
def adminreport():
  """ recent surveys, new users, etc """
  pass


@action
def my():
  """ my stuff, surveys. status, responses """
  pass

@action
def download(surveyid):
  """ results of a survey """
  pass


@action
def edit(surveyid):
  """ opens in edit mode in browser """
  pass

@action
def web(surveyid):
  """ opens survey in browser """
  pass

if __name__ == "main":
  # get user, pass
  # setup sg
  # run action
  # dump
  # exit
  pass


