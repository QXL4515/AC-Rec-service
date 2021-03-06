# AC-Rec service

## System Description
The purpose of AC-Rec service system is to provide a personalized recommendation service. The data set used in this system is the real data on the ResearchGate platform, so it is mainly a recommendation service for the researchers on the ResearchGate platform to find potential academic researchers with the same or similar interests. Due to the limited conditions, we can not directly expand on the ResearchGate platform, so we have made an offline recommendation service. 

The architecture of the AC-Rec recommendation service system is as follows.

<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/bs.png" width="500"/>

The system adopts B/S structure, which is divided into three functional modules: system interface display, business logic processing and user data access. The system interface display is mainly constructed by HTML, CSS and JavaScript. Business logic processing includes the connection of the front-end to the back-end database masql, and the implementation of the algorithm is recommended. User data access mainly deals with the existing data of users.
## Core code
Program1 mainly cleans our text data, trains the text vector model and calculates the textual similarity between researchers. Program2 mainly calculates the social relevance between researchers. Program3 mainly includes the calculation of the self-activity of researchers, the training of our recommendation model and the implementation of the recommendation service system. Process_wiki.py is a program to process Wikipedia datasets into txt files.

## Core system screenshots
### Recommend page
Here we can recommend top-5, top-10, top-15, top-20, top-25, top-30 most similar potential academic collaborators using our AC-Rec recommendation service for a given researcher, respectively.
<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/service.png" width="600"/>
### Profile page
#### paper page
The paper page shows the researcher's published papers.
<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/paper.png" width="600"/>
#### follow page
The paper page shows the researcher's following information.
<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/follow.png" width="600"/>
#### other page
The other page displays other relevant information of users, including behavior data and topic description of themselves.
<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/other.png" width="600"/>












