import random

def world_model_learning():
    print("Initializing Reinforcement World Learning demo...")
    # Simulated environment state
    state = 0
    for i in range(10):
        action = random.choice([0, 1])
        next_state = state + action
        print(f"Step {i}: State {state} -> Action {action} -> Next State {next_state}")
        state = next_state
    print("World model updated.")

if __name__ == "__main__":
    world_model_learning()
