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

```txt
The main themes in documents summarizing environmental policies, practices, and challenges can be broadly categorized as follows:

1. **Climate Change and Emissions**:
   - **Mitigation and Adaptation**: Strategies to reduce greenhouse gas emissions and adapt to changing climate conditions.
   - **Carbon Pricing Mechanisms**: Use of economic tools like carbon taxes and cap-and-trade to manage emissions.
   - **Scientific Research and Monitoring**: Data collection and studies on climate impacts and mitigation efficacy.
   - **Resilience and Adaptation**: Building capacity to withstand and recover from climatic impacts.

2. **Biodiversity and Conservation**:
   - **Conservation Policies**: Measures to protect wildlife, habitats, and natural ecosystems.
   - **Biodiversity Loss**: Addressing the decline in species variety and ecosystem services.
   - **Protected Areas**: Strategies and legal frameworks for conserving biodiversity.

3. **Sustainable Development and Resource Management**:
   - **Natural Resources**: Management and sustainable use of water, soil, and forests.
   - **Land Use and Urban Planning**: Policies for sustainable land use and urban development.
   - **Agriculture**: Issues related to crop yields, irrigation, and the impact of climate change on food production.
   - **Water Management**: Efficient usage, distribution, and conservation of water resources.

4. **Energy and Renewable Resources**:
   - **Renewable Energy**: Transition to solar, wind, hydro, and other renewable sources.
   - **Energy Efficiency**: Improving efficiency in energy use and production.
   - **Technological Innovations**: Advances in energy storage, grid integration, and renewable energy technologies.

5. **Pollution and Environmental Impact**:
   - **Air and Water Quality**: Measures to control air and water pollution and improve environmental health.
   - **Waste Management**: Strategies for reducing waste, recycling, and sustainable disposal practices.

6. **Health and Human Impact**:
   - **Public Health**: Effects of environmental changes on human health, such as air quality and extreme heat.
   - **Social and Economic Dimensions**: Balancing economic growth with environmental and social sustainability.

7. **Policy and Legislation**:
   - **Environmental Regulations**: Legal frameworks to enforce environmental protection.
   - **International Agreements**: Collaborative efforts to address global environmental issues.
   - **Funding and Economic Policies**: Financial mechanisms to support environmental initiatives.

8. **Community and Stakeholder Involvement**:
   - **Public Awareness and Education**: Educating the public and stakeholders on environmental issues and sustainable practices.
   - **Local Communities**: Role of local governance and community engagement in environmental conservation.

These themes provide a comprehensive understanding of the various dimensions involved in addressing environmental challenges and advancing sustainability.
```

_Note that the example uses a multiple albeit small documents for simplicity. In a real-world scenario, you would need to process multiple large documents and answer multiple queries. Expect the script to run for several minutes and cost around $3-5 in OpenAI credits using the GPT-4o model for all of the NLP tasks._
