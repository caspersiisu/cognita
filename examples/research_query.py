"""
Advanced Research Workflow Example for Cognita SDK

This example walks through a complete scientific research workflow using the Cognita Agent.
It demonstrates how to handle multiple research queries and process their results.
"""

import logging
from cognita import CognitaAgent, Config

def main():
    # Setup logging for detailed debugging information
    logging.basicConfig(level=logging.DEBUG)
    
    # Load configuration from environment variables
    config = Config()
    
    # Create an instance of the Cognita Agent
    agent = CognitaAgent(config)
    
    # Define a list of research queries covering various topics
    research_topics = [
        "Investigate the impact of renewable energy on global markets.",
        "Examine the role of artificial intelligence in healthcare innovation.",
        "Assess the effects of microplastics on marine ecosystems."
    ]
    
    aggregated_results = {}
    
    # Execute each research query and store the results
    for topic in research_topics:
        print(f"Executing query: {topic}")
        try:
            result = agent.execute_query(topic)
            aggregated_results[topic] = result
            print("Query completed successfully.")
        except Exception as e:
            print(f"Error executing query '{topic}': {e}")
    
    # Process aggregated results (e.g., summarizing or comparing responses)
    print("\nAggregated Research Results:")
    for topic, result in aggregated_results.items():
        print(f"\nTopic: {topic}")
        print(result)

if __name__ == '__main__':
    main()
