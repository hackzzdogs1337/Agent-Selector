# Agent-Selector
A script that returns a list of agents or agent depending upon the selection mode

# Run the script
**python agentselector.py**

# Test cases
### All available mode
All the available agents who can resolve the issue will be returned
```
PS E:\anirudh\Assignment> python .\agentselector.py
Enter the no of agents:6
Format (eg:kumar True 25 spanish,sales,support)
kumar True 46 spanish,support
Balu False 21 sales,support
bala True 55 support,sales
anirudh True 43 marketing,sales
arun False 13 spanish,sales
govind True 31 spanish,support
Enter the selection mode:all available
Enter the issue to be resolved:support
[Agent(kumar), Agent(bala), Agent(govind)]
```
### Random mode
A random agent who can solve the issue will be returned
```
PS E:\anirudh\Assignment> python .\agentselector.py
Enter the no of agents:6
Format (eg:kumar True 25 spanish,sales,support)
kumar True 46 spanish,support
Balu False 21 sales,support
bala True 55 support,sales
anirudh True 43 marketing,sales
arun False 13 spanish,sales
govind True 31 spanish,support
Enter the selection mode:random
Enter the issue to be resolved:support
Agent(bala)
```
### Least busy
The agent who is available_time is the highest and who can resolve the issue will be returned
```
PS E:\anirudh\Assignment> python .\agentselector.py
Enter the no of agents:6
Format (eg:kumar True 25 spanish,sales,support)
kumar True 46 spanish,support
Balu False 21 sales,support
bala True 55 support,sales
anirudh True 43 marketing,sales
arun False 13 spanish,sales
govind True 31 spanish,support
Enter the selection mode:least busy
Enter the issue to be resolved:support
Agent(bala)

```
