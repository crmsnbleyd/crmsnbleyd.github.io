---
Title: Pre-training
Summary: What pre-training is and how it is done.
Date: 2022-12-04 09:33
Category: Terminology
Status: published
Slug:pre-training
---
Pre-training in AI refers to training a model with one task to help it form parameters that can be used in other tasks.

The language models we will be dealing with are trained in a specific way to solve an artificial task (for example, guessing blanks in sentences for [BERT]({filename}/Models/bert.md)), and that knowledge is used in order to solve other tasks.

BERT and [ELECTRA]({filename}/Models/electra.md) are two pre-training techniques used for the same structure of nodes, and both of them use _unstructured data_, that is, data we do not have to label ourselves, in the form of a large corpus of text that we can obtain from the internet.

Pre-training involves setting the number of parameters and layers required, pointing the training code to the text used to train, and letting it run and refine the network for a while. This can take days.

The training code for many popular models like ELECTRA are available online on [Hugging Face](https://huggingface.co), and only need to be modified slighty, easing our task considerably.
