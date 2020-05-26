# AC-Rec-service
AC-Rec: a personalized academic collaborator recommendation service framework which aims to provide a recommendation service for academic collaborator on ResearchGate.

## System Description
This is a multi-feature-based service framework, named AC-Rec (Academic Collaborator Recommendation). This framework aims to provisioning a personalized academic collaborator recommendation service on ResearchGate. This service is able to recommend Top-N academic collaborators for each researcher based on multi-layer perception.

AC-Rec measures the correlation between researchers by aggregating three factors, namely, the textual similarity between researchers’ published papers, the social relevance between researchers and the self-activity of researchers on ResearchGate. The textual similarity of published papers is calculated by the Doc2Vec text depth representation model. The social relevance is calculated by the graph-based random walk algorithm.

We ran our experiments on the win10 platform, which with Intel (R) Core(TM) i7-8750H CPU @2.20 GHz 2.21 GHz, 8.00 GB RAM.

The flow chart of AC-Rec for personalized academic collaborator recommendation service framework as follows. The framework is divided into three main steps: data collection and processing, model training and optimization, and model prediction and recommendation.

<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/AC-Rec.png" width="500"/>

## Related Codes
* program1: It mainly includes data processing, training text vector model and calculating textual similarity.
* program2: It mainly includes calculating social relevance.
* program3: It mainly includes calculating self-activity, training recommendation model and recommendation service.
### The textual similarity
We use the Doc2Vec model to calculate the similarity of published papers between researchers, and construct a textual similarity Matrix: Textual-Similarity Matrix. The relevant code is as follows.
<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/textual.png" width="500"/>
### The social relevance
We use the graph-based random walk algorithm to calculate the social relevance between two researchers. A Social Relevance Matrix will be constructed as the output of this step.The relevant code is as follows.
<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/social.png" width="500"/>
### The academic collaborator recommendation service
We use multi-layer perceptron to build our recommendation service. Our MLP model contains two hidden layers. Each hidden layer includes 10 neurons. There are three neurons on the input layer and one neuron on the output layer.
<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/recommend.png" width="500"/>
## Experimental screenshot
Here we recommend 30 most similar potential academic collaborators using our AC-Rec recommendation service.
<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/top30.png" width="500"/>











