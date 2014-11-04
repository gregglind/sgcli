#!/usr/bin/env python

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
import sys
from collections import defaultdict
import pydoc

from decorator import decorator
from clint.textui import puts, indent, colored


from surveygizmo import SurveyGizmo

"""
sg = SurveyGizmo(api_version='v3', response_type='json')
sg.config.auth_method = "user:pass"
sg.config.username = "username"
sg.config.password = "password"


sg.api.survey.list()
sg.api.survey.get('39501')
sg.api.survey.copy('39501', '39501 Copy')
sg.api.surveyresponse.list('39501')
"""

# decorators

@decorator
def action(fn, *args, **kwargs):
  print "action, calling with %s with args %s, %s" % (f.func_name, args, kw)
  return fn(*args, **kwargs)

@decorator
def web_action(fn, *args, **kwargs):
  """ supports --web interface """
  # basically, if --web is passed, do something useful with it.
  print "action, calling with %s with args %s, %s" % (f.func_name, args, kw)
  return fn(*args, **kwargs)



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


@action
def bug(surveyid):
  """ does this bug sg, or bug people about sg-cli """
  pass


@action
def nullaction():
  """ this action doesn't exist."""
  pass

@action
def _help():
  """ should this be sg help, or client help? """
  pass

@action
def listall():
  """ list all known actions with help"""
  pass

# yes, this is gross.
all_actions = defaultdict(lambda:nullaction)
all_actions.update({
  "adduser": adduser,
  "users": users,
  "help": _help,
  "bug": bug,
  "web": web,
  "edit": edit,
  "download": download,
  "search": search,
  "adminreport":  adminreport,
  "my": my,
  "list": listall
})


def fmt(name, fn):
  [puts(x, False) for x in [
    colored.blue('action'),
    " ",
    colored.red(name)
  ]]
  puts("")
  with indent(4):
    puts(pydoc.render_doc(fn, "%s"))

if __name__ == "__main__":
  # get user, pass
  # setup sg
  # run action
  # dump
  # exit
  import sys
  myaction = (sys.argv[1] if len(sys.argv) > 1 else 'my').lower()
  # same as 'help' but printable
  if myaction == "list":
    for k,v in sorted(all_actions.iteritems()):
      fmt(k,v)

  else:
    fmt(myaction, all_actions[myaction])
  sys.exit(0)




