import random


class Agent:
    def __init__(self,name,is_available,available_time,roles):
        self.name=name
        self.is_available=is_available
        self.available_time=available_time
        self.roles=roles
    def __repr__(self):
        return f'Agent({self.name})'
    #Function that returns a list of agents that resolves the issue
    @staticmethod
    def correct_agents(agent_list,issue):
        return [agent  for agent in agent_list if agent.is_available=='True' and issue in agent.roles]

    #Function that returns a agent or a list of agents depending upon the selection mode
    @staticmethod
    def agents_available(agent_list,mode):
        if mode=='all available':
            return agent_list
        elif mode=='least busy':
            for i in range(0,len(agent_list)):
                for j in range(i+1,len(agent_list)):
                    if(agent_list[i].available_time>agent_list[j].available_time):
                        max=agent_list[i]
                    else:
                        max=agent_list[j]
            return max
        elif mode=='random':
            return random.choice(agent_list)
        else:
            print('Enter a valid mode eg:random,least busy,all available')

n=int(input('Enter the no of agents:'))
agent_list=[]
print('Enter the agents:\nFormat (eg:kumar True 25 spanish,sales,support)')

for i in range(0,n):
    agent=input()
    name,is_available,available_time,roles=agent.split(' ')
    agent_list.append(Agent(name=name,is_available=is_available,available_time=int(available_time),roles=roles.split(',')))

mode=input('Enter the selection mode:')
issue=input('Enter the issue to be resolved:')
#Select the agents that can resolve the issues

agents_rightful=Agent.correct_agents(agent_list,issue)
#The List of agents returned depending upon the selection mode

print(Agent.agents_available(agents_rightful,mode))

