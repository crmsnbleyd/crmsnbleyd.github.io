---
Title: An introduction to transformers
Date: 2022-10-03 23:35
Category: General
---

This README is a primer on all the terms that one needs to be aware of and the knowledge one would need to gain in order to confidently work on an academic paper implementing a transformer language model.

This paper is about implementing an ELECTRA language model for a specific Indian language, which is possibly going to be Punjabi, using training code that is available on the internet and running it on some sort of cloud or on-premises environment which has the GPU power required to do this task as well as the availability in terms of time. The current expectation is that such a task takes days on a single GPU.

The language model needs to be trained on an unstructured corpus of data in the language of choice using a tokenizer, both of which are made available online by multiple organizations, the most prominent of which is [Huggingface](https://huggingface.co) (often represented by 🤗).
