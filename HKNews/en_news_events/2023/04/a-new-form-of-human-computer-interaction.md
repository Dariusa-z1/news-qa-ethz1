# a-new-form-of-human-computer-interaction

**Source:** en_news_events/2023/04/a-new-form-of-human-computer-interaction.html

**Date processed:** 2025-05-01

## Abstract

• ETH researchers developed a new programming language called LMQL (Language Model Query Language).
• The combination of natural and programming languages enables users to interact more systematically with large language models like ChatGPT.
• The new programming language allows users to express safety constraints to avoid undesirable results as much as possible.
The language model ChatGPT is widely known by people in the tech community and the general public. Through a chatbot, one can interact with these language models directly without needing any programming skills. Instead of using code, the user can input commands and questions with natural language.

Sometimes this interaction works well, and the desired result appears on-screen. However, at other times the language model does not understand the command, and the generated output can turn out unexpectedly or even unsatisfactory. What people usually do as a response is that they follow up with another query. ChatGPT will then try to correct its mistakes and adapt its answer. This way of using a language model is messy and random, and it can take quite some time to get the preferred outcome.

To solve this problem, ETH researchers now developed a new programming language and open-source platform called LMQL (Language Model Query Language). Utilizing LMQL allows a user to interact with large language models like ChatGPT in a more elevated and controlled way. This programming language enables a novel way of programming and is a new form of computer-human interaction because the user can directly talk to and instruct the computer.

LMQL is the first language that combines natural and programming languages’ power to interact with these large language models. For simple queries, it is sufficient to guide ChatGPT using natural language. However, for more complex and specific tasks, such as creating a database or analyzing data, it is essential to instruct the language model precisely. Therefore, the formalism of programming languages is needed to guide the language model with formal constructs to ensure the user gets the desired output. Martin Vechev, Professor of Computer Science and one of the creators, clarifies: “Essentially, it is a much more concise way to get what you want. Decreasing the necessary exchanges with the language model also reduces the costs of interacting with the model, which can be quite expensive. Using LMQL increases the chances of getting the desired output. It sometimes even makes it possible to get a result you would have never gotten otherwise because you can formulate your query more accurately.”

## A key advantage

The datasets that large language models are trained with and based on are so massive that the user cannot control and comprehend what happens internally within the model. Because of that, these models can sometimes produce unexpected or controversial outputs. According to the researchers, one of the substantial problems for people using these large language models is that they cannot understand why a certain result was produced and how to prevent it.

LMQL allows its user to express safety constraints which can help guide the model in the right direction and try to steer it away from unwanted or unexpected outputs. “Using LMQL, you can restrict your language model to strictly follow a specific framework you designed. This allows you to better control how the language model behaves. Of course, full guaranteed prevention of bad behaviour is still very hard to achieve, but LMQL is one step in this direction”, explains Luca Beurer-Kellner, one of the researchers. For example, LMQL allows the user to exclude specific words or prevents the model from going in certain directions of reasoning.

Many companies develop their large language models behind closed doors. Due to that, the large language models become intransparent, and their reasoning behind a particular output is incomprehensible to the user. According to the researchers, to counterbalance this, academia must produce open-source tools like LMQL that are transparent, accessible, and adaptable for people. Marc Fischer, who also developed the new programming language, further declares: “I think for both a technical and non-technical crowd, it is crucial to have this open-source to see what is going on rather than LMQL being a magical black box. Especially since the research on language models is moving at an insane pace, it is crucial that LMQL simultaneously offers transparency and enables fast development.”

LMQL is a declarative, SQL-like language from a syntactic point of view. Therefore, it is a very accessible language requiring less expertise to achieve the desired results. The new programming language can also function as an innovative tool for researchers of various disciplines. “If you are not too invested in coding or may not have the time to code because it is not a core part of your work, then LMQL makes it much more accessible to interact with large language models in a precise, yet easy way”, explains Beurer-Kellner.

Additionally, it can function as a helpful base for advanced users and an expert community because you can add different programming constructs to the natural language query. Technical programmer users can use LMQL as a building block and build their own programs on top to interact with large language models.

A vast interest and interdisciplinary community is already beginning to form around the new programming language. The researchers declare LMQL a long-term project and plan several follow-ups and papers. They were also accepted to present their work in June at the ACM PLDI, one of the top international conferences on programming language design and implementation.

## Try it out!

Interested readers, who would like to learn more about LMQL and test the programming language themselves can access a demo version on the corresponding website. This can run directly in the web browser.

Further information: http://lmql.ai

## About

Luca Beurer-Kellner and Marc Fischer are doctoral students at the Department of Computer Science. Martin Vechev is a professor of Computer Science.

The three ETH researchers developed the LMQL programming language together.

