import torch
import torch.nn as nn
import torch.nn.functional as F

class Model(nn.Module):

	def __init__(self):

		# Call the parent method
		super(Model, self).__init__()

		# Define the model here

    # Forward pass
	def forward(self, x):

		# Apply forward pass, and return digit (c) and box coordinates (r)

		c = None
		r = None

		return c, r