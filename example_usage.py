from client import HierarchicalMultiAgentWorkflowGraphOrchestratorClient

def main():
    client = HierarchicalMultiAgentWorkflowGraphOrchestratorClient()
    res = client.orchestrate_agent_team("Design and deploy a microservice backend for user auth", 4)
    print(f"Consensus Result: {res['consensus_result']}")
    print("Executed Sub-Tasks:")
    for t in res["executed_sub_tasks"]:
        print(f"  - {t}")

if __name__ == "__main__":
    main()
