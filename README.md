# Baby AGI

Baby AGI is a project that integrates two AI techniques within a unified framework using the Hyperon framework. The project demonstrates how these AI techniques can work together as agents to perform specific AI tasks.

## The Agents

### Sentiment analyzer Agent
- **Purpose**: Analyzes the sentiment of a given text.
- **Functionality**: Simulates sentiment analysis by assigning a sentiment score based on the presence of positive or negative words in the text.

### CNN Agent
- **Purpose**: Generates a simple response based on the sentiment analysis.
- **Functionality**: Simulates response generation by returning a positive or negative reply based on the sentiment score provided by the Sentiment Analyzer Agent.

### MeTTa Agent
- **Purpose**: Acts as the symbolic reasoner agent.
- **Functionality**: Calls the sntmnt and rspgen agents, stores and reads their outputs, and reasons over them using symbolic reasoning.

## SetUp Guide

Clone the repo
```bash
git clone https://github.com/Basliel-Amsalu/baby_agi_2.git
```

Cd to the repo
```bash
cd baby_agi_2
```

Install the requirements
```bash
pip install -r requirements.txt
```

Download vader lexicon
```bash
import nltk
nltk.download('vader_lexicon')
```

Run the metta file
```bash
metta run-baby-agi.metta
```