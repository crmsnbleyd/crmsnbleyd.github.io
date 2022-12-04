---
Title: Artificial Neural Network
Summary: A discussion of artificial neural networks.
Date: 2022-12-04 09:30
Status: published
Slug:ann
---
An artificial neural network is an interconnected group of _nodes_, inspired by a simplification of neurons in a brain. Here, each circular node represents an artificial neuron and an arrow represents a connection from the output of one artificial neuron to the input of another.

![NeuralNetworkNodes](https://upload.wikimedia.org/wikipedia/commons/e/e4/Artificial_neural_network.svg)

Neural networks learn (or are trained) by processing examples, each of which contains a known "input" and "result," forming probability-weighted associations between the two, which are stored within the data structure of the net itself. The training of a neural network from a given example is usually conducted by determining the difference between the processed output of the network (often a prediction) and a target output. This difference is the error. The network then adjusts its weighted associations according to a learning rule and using this error value.

The neurons are typically organized into multiple _layers_, especially in deep learning. Neurons of one layer connect only to neurons of the immediately preceding and immediately following layers. The layer that receives external data is the _input layer_. The layer that produces the ultimate result is the _output layer_. In between them are zero or more _hidden layers_. Single layer and unlayered networks are also used. Between two layers, multiple connection patterns are possible. They can be _fully connected_, with every neuron in one layer connecting to every neuron in the next layer. They can be _pooling_, where a group of neurons in one layer connect to a single neuron in the next layer, thereby reducing the number of neurons in that layer.

