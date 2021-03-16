from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import *

class TestApp(ShowBase):

	def __init__(self):
		ShowBase.__init__(self)

		# Disable the camera trackball controls.
		#self.disableMouse()

		# Load the environment model.
		self.lander = self.loader.loadModel("lunar_lander.obj")
		# Reparent the model to render.
		self.lander.reparentTo(self.render)
		# Apply scale and position transforms on the model.
		self.lander.setScale(0.1, 0.1, 0.1)
		#self.lander.setPos(-8, 42, 0)

		# Add the spinCameraTask procedure to the task manager.
		#self.taskMgr.add(self.myTask, "myTask")

	def myTask(self, task):
		# things
		return Task.cont


app = TestApp()
app.run()
