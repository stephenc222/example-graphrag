# Example Graph RAG

## Overview

This repository provides an example implementation of the Graph RAG (Graph-based RAG) pipeline described in the [paper](https://arxiv.org/abs/2404.16130) "From Local to Global: A Graph RAG Approach to Query-Focused Summarization" by Darren Edge et al. The implementation is written in Python and demonstrates how to process documents, build a graph, detect communities, and generate a final answer to a query.

## Prerequisites

Create a `.env` file in the root of the project with the following variables:

```bash
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

- Python 3.12 or later
  - After installing Python, use pip to install the following packages:
    - `pip install openai networkx leidenalg cdlib python-igraph python-dotenv`

## Implementation

The following steps are implemented in the `app.py` file, in accordance with the paper's description:

### 1. Source Documents → Text Chunks

- **Paper:** Describes splitting input texts into chunks for processing.
- **Code:** `split_documents_into_chunks` function splits the documents into chunks of a specified size with overlap.

### 2. Text Chunks → Element Instances

- **Paper:** Describes extracting entities and relationships using an LLM.
- **Code:** `extract_elements_from_chunks` function uses OpenAI's GPT-4 to extract entities and relationships from each chunk of text.

### 3. Element Instances → Element Summaries

- **Paper:** Describes summarizing extracted elements into meaningful summaries.
- **Code:** `summarize_elements` function uses GPT-4 to summarize the entities and relationships.

### 4. Element Summaries → Graph Communities

- **Paper:** Describes building a graph from element summaries and using community detection algorithms.
- **Code:** `build_graph_from_summaries` function creates a graph with nodes and edges based on the summaries. `detect_communities` function uses the Leiden algorithm to detect communities in the graph.

### 5. Graph Communities → Community Summaries

- **Paper:** Describes summarizing each detected community.
- **Code:** `summarize_communities` function concatenates the elements of each community into a summary.

### 6. Community Summaries → Community Answers → Global Answer

- **Paper:** Describes generating answers from community summaries and combining them into a final answer.
- **Code:** `generate_answers_from_communities` function generates intermediate answers based on community summaries and combines them into a final answer using GPT-4.

### Putting It All Together

- **Paper:** Describes a full pipeline that processes the documents, builds a graph, detects communities, and generates a final answer to a query.
- **Code:** `graph_rag_pipeline` function implements the full pipeline as described.

### Example Usage

- **Code:** The provided example demonstrates how to use the pipeline to process documents and generate an answer to a query, which aligns with the paper's goal of answering global questions over a text corpus.

To run the example once the dependencies have been installed, use the following command:

```bash
python app.py
```

Example query:

```txt
What are the main themes in these documents?
```

Example Graph RAG output:

````txt
The main themes in the provided documents include:

1. **Environmental Policies**: Emphasis on how these policies aim to protect natural ecosystems, promote sustainability, and address environmental challenges.
2. **Sustainability Practices**: Focus on maintaining ecological balance and health.
3. **Environmental Challenges**: Addressing issues like pollution, climate change, deforestation, and their broader impacts on wildlife, human health, and the economy.
4. **Governmental Responsibility**: The role of governments and international organizations in enforcing and implementing environmental policies.
5. **Stakeholder Cooperation**: The critical role of various stakeholders, including local authorities and communities, in upholding and promoting environmental policies.
6. **Adaptation and Mitigation Strategies**: Strategies for mitigating the effects of climate change, including renewable energy adoption, efficient water use, and sustainable agriculture.
7. **Interconnectedness of Environmental Issues**: Exploring how different environmental issues are interconnected, such as deforestation leading to pollution and climate change.
8. **Impact on Specific Sectors**: Effects on sectors like agriculture (e.g., reduced yields, food security) and their relationships to environmental factors.

These themes reflect a comprehensive approach to understanding and addressing complex environmental issues through policy, cooperation, and sustainable practices.
```

_Note that the example uses a multiple albeit small documents for simplicity. In a real-world scenario, you would need to process multiple large documents and answer multiple queries. Expect the script to run for several minutes and cost around $3-5 in OpenAI credits using the GPT-4o model for all of the NLP tasks._
````
