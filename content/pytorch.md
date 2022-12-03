---
Title: Pytorch Introduction
Summary: General overview of Pytorch and its usage
Date: 2022-10-26 08:15
Category: Introduction
Status: published
---

Pytorch is python bindings for the Torch library from Lua, which is a machine learning framework based on using GPUs as the compute platform.

## Install
	:::bash
    python -m pip install --upgrade pip
    python -m pip install pytorch

## Check if GPU is being used
	:::python
	import torch
	torch.cuda.is_available()
	torch.cuda.device_count()
	torch.cuda.current_device()
	torch.cuda.device(0)
	torch.cuda.get_device_name(0)

This should show something like 'GeForce GTX 940M', or whatever your GPU name is.
