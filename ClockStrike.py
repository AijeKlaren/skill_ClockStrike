from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


Class ClockStrike(AliceSkill):

def __init__(self):
	super().__init__()

    self.say("starting ringing the bell here")

	@IntentHandler('ClockStrikeIntent')

	def onFullMinute(self)
		self.say('The clock strikes {}'.format(time.time())


