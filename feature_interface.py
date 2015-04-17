class FeatureInterface(object):
	def __init__(self):
		self.share = "???"
	
	def render(self, context):
		raise NotImplemented
	
	def get_date(self):
		raise NotImplemented
	
	def call(self):
		return self.render(self.gat_date())
