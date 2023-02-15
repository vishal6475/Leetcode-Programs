class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.comp = val
        self.next = []

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        nodes = []
        for i in range(numCourses):
            t = TreeNode(i)
            nodes.append(t)
            
        comps = [[i] for i in range(numCourses)]
            
        def checkForCycles(node, previous, nxt):
            
            visited = [0 for _ in range(numCourses)]
            to_check = []
            to_check.extend(node.next)            
            visited[nxt] = 1
            
            while len(to_check) > 0:
                curr = to_check.pop(0)
                if curr == previous: return True
                if visited[curr] == 0:
                    to_check.extend(nodes[curr].next)
                    visited[curr] = 1
            
            return False
        
        for req in prerequisites:
            c_from = req[1]
            c_to = req[0]
            if c_from == c_to: return False
            
            if nodes[c_from].comp != nodes[c_to].comp:
                nodes[c_from].next.append(c_to)
                
                oldComp = nodes[c_to].comp
                newComp = nodes[c_from].comp
                comps[newComp].extend(comps[oldComp])
                for n in comps[oldComp]:
                    nodes[n].comp = newComp    
                comps[oldComp] = []
                
            else:
                nodes[c_from].next.append(c_to)
                
                if checkForCycles(nodes[c_to], c_from, c_to):
                    return False
            
        return True
        
sol = Solution()

print(sol.canFinish(2,[[1,0]]))