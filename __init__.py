# MIT LICENSE
# Mycroft Skill: Application Launcher, opens/closes Linux desktop applications
# Copyright © 2019 Philip Mayer philip.mayer@shadowsith.de

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import subprocess
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

# Each skill is contained within its own class, which inherits base methods
# from the MycroftSkill class.  You extend this class as shown below.
# TODO: Change "Template" to a unique name for your skill


class AppLauncherSkill(MycroftSkill):
    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(AppLauncherSkill, self).__init__(name="AppLauncherSkill")
        # Initialize working variables used within the skill.
        self.user = ""  # change this to your default desktop user
        self.app = ""

    def getUser(self):
        who = subprocess.Popen("who -u", stdout=subprocess.PIPE,
                               shell=True).stdout.read()
        usr = who.decode("utf-8").split(" ")[0]
        self.user = usr

    @intent_handler(IntentBuilder("").require("Open"))
    def handle_open_intent(self, message):
        try:
            self.getUser()
            msg = message.data.get('utterance')
            self.app = str(msg).split(" ")[1]
            exists = subprocess.Popen("command -v {}".format(self.app),
                                      stdout=subprocess.PIPE,
                                      shell=True).stdout.read()
            exists = exists.decode("utf-8")
            if(exists != ''):
                subprocess.call("su {} -c {} &".format(self.user, self.app),
                                shell=True)
                self.speak_dialog("app.open", data={"app": self.app})
            else:
                self.speak_dialog("app.not.exists", data={"app": self.app})
        except Exception as e:
            LOG.exception("open command failed")
            self.speak_dialog(e.message)

    @intent_handler(IntentBuilder("").require("Close"))
    def handle_close_intent(self, message):
        try:
            msg = message.data.get('utterance')
            self.app = str(msg).split(" ")[1]
            subprocess.call("killall {}".format(self.app), shell=True)
            self.speak_dialog("app.close", data={"app": self.app})
        except Exception as e:
            LOG.exception("close command failed")
            self.speak_dialog(e.message)


def create_skill():
    return AppLauncherSkill()
