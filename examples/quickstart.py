"""
Quickstart Example for Cognita SDK

This minimal example demonstrates how to initialize the Cognita agent,
configure the API, and execute a basic research query.
"""

from cognita import CognitaAgent, Config

def main():
    # Initialize configuration from environment variables
    config = Config()
    
    # Create an instance of the Cognita Agent
    agent = CognitaAgent(config)
    
    # Define a research query (ensure the query meets the minimum requirements)
    query = "What are the recent advancements in quantum computing?"
    
    try:
        # Execute the research query and obtain results
        results = agent.execute_query(query)
        print("Research Results:")
        print(results)
    except Exception as e:
        print(f"An error occurred while executing the query: {e}")

if __name__ == '__main__':
    main()
