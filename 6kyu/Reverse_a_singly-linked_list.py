def reverse_list(node):
    ans=None
    while node!=None:
        ans,node=Node(node.value,ans),node.next
    return ans