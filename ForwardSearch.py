from State import State
# from queue import PriorityQueue
import collections

import heapdict

def forward_search(goal_state, initial_state, actions):
    # fringe=PriorityQueue()
    fringe =heapdict.heapdict()
    fringe[initial_state]=0
    in_fringe = [initial_state.hash()]
    explored = []

    while fringe:
        current_state = fringe.popitem()[0]
        in_fringe.pop(0)
        explored.append(current_state.hash())
        successors = get_successors(current_state, actions)

        for successor in successors:
            if goal_test(successor, goal_state):
                print_solution(successor)
                return
            else:
                if successor.hash() not in in_fringe and successor.hash() not in explored:
                    fringe[successor]= ignorePreconditions(actions,successor,goal_state)
                    # fringe.append(successor)
                    in_fringe.append(successor.hash())


def get_successors(state, actions):
    result = []
    for action in actions:
        if action.is_relevantForward(state):
            successor=State(state,action,state.positive_literals,state.negative_literals)
            action.progress(successor)
            result.append(successor)      
    return result


def goal_test(state, goal_state):
    for positive_literal in state.positive_literals:
        if positive_literal not in goal_state.positive_literals:
            return False

    for negative_literal in state.negative_literals:
        if negative_literal in goal_state.positive_literals:
            return False
    return True


def print_solution(state):
    if state.action == None or state.parent == None:
        return
    print_solution(state.parent)
    print(state.action.to_string())
    
def ignoreDeleteList(state):
    for neg in state.negative_literals:
        for dell in state.action.delete_list:
            if(neg==dell):
                state.action.delete_list.remove(dell)
                
                
def ignorePreconditions(actions,state,goal):
    st = state
    cost =0 
    # while True:
        #temp = cost
        # for act in actions:
        #     for posact in act.add_list:
        #         if (posact in actions.goal_state.positive_literals & posact not in goals):
        #             goals.append(posact)
        #             cost+=1
        #             for negact in act.delete_list:
        #                 if(negact in goals):
        #                    goals.remove(negact)
        # if(temp==cost):
        #     return cost
    for act in actions:
        for poseffect in act.add_list:  
            if(( poseffect not in st.positive_literals) & (poseffect in goal.positive_literals)):
                st.positive_literals.append(poseffect)
                cost+=1
                for negeff in act.delete_list:
                    if(negeff in st.positive_literals):
                        st.positive_literals.remove(negeff)           
                    
                    
    if (compareList(goal.positive_literals,st.positive_literals)):
        print("here ", cost)
        return cost 
        
        
#This method tests for the equality of the lists by comparing frequency of each element
# in first list with the second list. This method also does not take 
# into account the order of the elements of the list.        
def compareList(l1,l2):
   if(collections.Counter(l1)==collections.Counter(l2)):
      return True
   else:
      return True
            
    
                
        