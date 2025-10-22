# Social Network Graph Analysis
A Python based tool to ingest, model, and analyze social network data from raw text files, identify community structures, and compute key network metrics.

**The Challenge**

The objective of this project was to design and implement a program to solve a series of network related problems. The core task involved extracting data from multiple disparate files (.csv and .txt) representing user profiles and their connections on different social platforms.

The challenge was to build a complete data pipeline to ingest, clean, normalize, and structure this raw data into a queryable, in memory social graph. Using this graph, custom algorithms were required to analyze network properties, such as identifying "triangle friendships" a common form of community detection in graph theory.

**Key Features & Skills Demonstrated**

**Data Ingestion Pipeline:** Engineered a robust data pipeline in Python to process and parse social network data from varied sources, handling potential file errors and inconsistent formats.

**Data Normalization:** Implemented a critical data transformation process to seamlessly unify ID based records (from one data source) with name-based records (from another), ensuring data integrity and creating a consistent schema for analysis.

**Graph Modeling:** Structured the transformed data into a queryable social graph using nested dictionaries and sets. This allowed for efficient, in memory analysis and direct lookups of user profiles and their connections.

**Algorithm Development:** Applied graph theory by developing custom traversal and clique detection algorithms from scratch in Python for social network analysis (SNA), successfully quantifying community structures ('triangle friendships').

Metric Calculation: Developed multiple functions to compute key network analytics, including the intersection of friend groups across platforms and the percentage of users with overlapping connections.

**Core Skills:** Python, Data Structures (Dictionaries, Sets), Algorithms, Data Normalization.

