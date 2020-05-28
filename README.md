# AC-Rec-service

## System Description
The purpose of AC-Rec-service system is to provide a personalized recommendation service. The data set used in this system is the real data on the ResearchGate platform, so it is mainly a recommendation service for the researchers on the ResearchGate platform to find potential academic researchers with the same or similar interests.

The architecture of the AC-Rec recommendation service system is as follows.

<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/bs.png" width="500"/>

The system adopts B/S structure, which is divided into three functional modules: system interface display, business logic processing and user data access. The system interface display is mainly constructed by HTML, CSS and JavaScript. Business logic processing includes the connection of the front-end to the back-end database masql, and the implementation of the algorithm is recommended. User data access mainly deals with the existing data of users.

## System screenshots
### Home page
The home page of the system gives a brief introduction to the system. For new users, click the registration button to register; for non new users, you can log in directly.
<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/home.png" width="600"/>
### Recommendation page
Here we can recommend top-5, top-10, top-15, top-20, top-25, top-30 most similar potential academic collaborators using our AC-Rec recommendation service, respectively.
<img src="https://github.com/QXL4515/AC-Rec-service/blob/master/img/service.png" width="600"/>











