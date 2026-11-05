# Steam Player Count Tracker Architecture

## Context Diagram
This diagram shows the interaction between the user, the Steam Player Count Tracker system, and the external Steam API.
```mermaid
flowchart TD
    User[User]
    System[System]
    SteamAPI[Steam API]

    User --> System
    System <--> SteamAPI
```

## Container Diagram
This diagram shows the deployment structure of the application. The system consists of three separate Docker containers for the frontend, backend, and database.
```mermaid
flowchart TD
    User[User]
    SteamAPI[Steam API]

    subgraph Container
        subgraph Docker Frontend
            Frontend["Frontend"]   
        end
        
        subgraph Docker Backend
            Backend["Backend"]
        end
        
        subgraph Docker Database
            Database["Database"]
        end
    end

    User --> Frontend
    Frontend <--> Backend
    Backend <--> Database
    Backend --> SteamAPI
```

## Component Diagram
This diagram shows the internal structure of the backend container and how the different components communicate with each other and external services.
```mermaid
flowchart TD
    Frontend[Frontend]

    subgraph Backend Container
        API[API]
        Manager[Manager]
        DBClient[DB Client]
        SteamClient[Steam Client]
    end

    Database[(Database)]
    SteamAPI[Steam API]

    Frontend --> API
    API --> Manager

    Manager --> API
    Manager --> DBClient
    Manager --> SteamClient

    DBClient --> Database
    SteamClient --> SteamAPI
```